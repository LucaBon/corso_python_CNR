"""
nb_tools.py: catena di produzione dei notebook del corso.

Un solo sorgente per notebook (sorgenti/NN_*.py, formato "percent"):

    # %% [markdown]
    # ## Titolo
    # testo...

    # %%
    codice python

    # %% tags=["raises-exception"]
    codice che DEVE dare errore (es. per mostrare un traceback vero): il build non si ferma

    # %% tags=["solo-docente"]          (anche: # %% [markdown] tags=["solo-docente"])
    cella che compare SOLO nella versione docente (es. soluzioni delle estensioni facoltative)

Convenzioni per gli ESERCIZI (dentro una cella di codice):

    # ESERCIZIO 1.3 (livello 2)
    # 1. carica il file          <- commento normale: resta uguale in entrambe le versioni
    #> media = np.____(valori)   <- riga "per lo studente": nella versione studenti
    #>                              viene scommentata (con i ____ da riempire)
    # --- SOLUZIONE ---           <- da qui in poi: solo nella versione docente
    media = np.mean(valori)
    # --- FINE SOLUZIONE ---      <- (facoltativo) da qui in poi: di nuovo in ENTRAMBE le versioni

Il marcatore può anche essere indentato (es. dentro una funzione): in quel caso il segnaposto
"# scrivi qui il tuo codice" viene indentato allo stesso livello, e con FINE SOLUZIONE si
restituiscono allo studente le righe finali (return, chiamate di prova...).

Versione docente  = tutto (le righe #> restano commenti, la soluzione viene eseguita).
Versione studenti = scaffold (righe #> scommentate) + cella Markdown "Output atteso"
                    con l'output REALE ottenuto eseguendo la versione docente.
Le immagini (../img/*.png e i grafici attesi) sono INCORPORATE nei notebook come allegati:
i notebook sono autosufficienti (funzionano anche aperti da soli, es. su Google Colab).

Comandi:
    python strumenti/nb_tools.py build            # sorgenti -> docente/*.ipynb (eseguiti) -> studenti/*.ipynb
    python strumenti/nb_tools.py build 03         # solo il notebook che inizia per 03
    python strumenti/nb_tools.py build --no-exec  # senza eseguire (niente output atteso)
    python strumenti/nb_tools.py pacchetto        # dist/: zip partecipanti (senza soluzioni), zip docente, zip solo installazione
"""
import base64
import re
import sys
import zipfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient

RADICE = Path(__file__).resolve().parent.parent
SORGENTI = RADICE / "sorgenti"
DOCENTE = RADICE / "docente"
STUDENTI = RADICE / "studenti"
DIST = RADICE / "dist"
MARK_SOL = "# --- SOLUZIONE ---"
MARK_FINE = "# --- FINE SOLUZIONE ---"
RE_TAGS = re.compile(r"tags\s*=\s*\[([^\]]*)\]")
RE_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+\.png)\)")


# ----------------------------------------------------------------- parsing
def py_to_cells(testo):
    """Restituisce una lista di (tipo, sorgente, tags)."""
    celle = []
    tipo, buf, tags = None, [], []

    def chiudi():
        if tipo is None:
            return
        src = "\n".join(buf).strip("\n")
        if tipo == "markdown":
            righe = []
            for r in src.splitlines():
                if r.startswith("# "):
                    righe.append(r[2:])
                elif r.strip() == "#":
                    righe.append("")
                else:
                    righe.append(r)
            src = "\n".join(righe)
        if src.strip():
            celle.append((tipo, src, tags))

    for riga in testo.splitlines():
        if riga.startswith("# %%"):
            chiudi()
            tipo = "markdown" if "[markdown]" in riga else "code"
            m = RE_TAGS.search(riga)
            tags = [t.strip().strip("'\"") for t in m.group(1).split(",") if t.strip()] if m else []
            buf = []
        else:
            buf.append(riga)
    chiudi()
    return celle


def incorpora_immagini(src, cartella_nb):
    """Sostituisce ![..](percorso.png) con un allegato del notebook. Restituisce (src, allegati)."""
    allegati = {}

    def sostituisci(m):
        percorso = (cartella_nb / m.group(2)).resolve()
        if not percorso.exists():
            return m.group(0)          # immagine mancante: lascio il link com'è
        nome = percorso.name
        allegati[nome] = {"image/png": base64.b64encode(percorso.read_bytes()).decode("ascii")}
        return f"![{m.group(1)}](attachment:{nome})"

    return RE_IMG.sub(sostituisci, src), allegati


def nuova_markdown(src, allegati=None):
    cella = nbformat.v4.new_markdown_cell(src)
    if allegati:
        cella["attachments"] = allegati
    return cella


def cells_to_nb(celle):
    nb = nbformat.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.metadata["language_info"] = {"name": "python"}
    for tipo, src, tags in celle:
        if tipo == "markdown":
            cella = nuova_markdown(*incorpora_immagini(src, DOCENTE))
            if tags:
                cella.metadata["tags"] = tags
            nb.cells.append(cella)
        else:
            cella = nbformat.v4.new_code_cell(src)
            if tags:
                cella.metadata["tags"] = tags
            nb.cells.append(cella)
    return nb


# ----------------------------------------------------------------- esecuzione
def esegui(nb, cwd):
    # allow_errors=False: qualunque errore ferma il build, TRANNE nelle celle con tag
    # "raises-exception" (gestito da nbclient), che devono mostrare un traceback vero.
    client = NotebookClient(nb, timeout=600, kernel_name="python3",
                            resources={"metadata": {"path": str(cwd)}},
                            allow_errors=False)
    client.execute()
    return nb


# ----------------------------------------------------------------- studenti
def scaffold_studente(src):
    """Restituisce (scaffold, ha_soluzione)."""
    if MARK_SOL not in src:
        return src, False
    righe_src = src.splitlines()
    i_sol = next(k for k, r in enumerate(righe_src) if r.strip() == MARK_SOL)
    rientro = righe_src[i_sol][: len(righe_src[i_sol]) - len(righe_src[i_sol].lstrip())]
    i_fine = next((k for k, r in enumerate(righe_src) if r.strip() == MARK_FINE and k > i_sol), None)
    prima = righe_src[:i_sol]
    dopo = righe_src[i_fine + 1:] if i_fine is not None else []

    righe = []
    for r in prima:
        s = r.lstrip()
        pre = r[: len(r) - len(s)]
        if s.startswith("#> "):
            righe.append(pre + s[3:])
        elif s.rstrip() == "#>":
            righe.append("")
        else:
            righe.append(r)
    while righe and not righe[-1].strip():
        righe.pop()
    if not any(r.lstrip().startswith("#>") for r in prima):
        righe += ["", f"{rientro}# scrivi qui il tuo codice"]
    if dopo:
        righe += [""] + dopo
    return "\n".join(righe).rstrip("\n") + "\n", True


def output_atteso_md(cell):
    """Testo Markdown + allegati con l'output della cella eseguita."""
    testi, allegati = [], {}
    for out in cell.get("outputs", []):
        if out.output_type == "stream":
            testi.append(out.text)
        elif out.output_type in ("execute_result", "display_data"):
            data = out.get("data", {})
            if "image/png" in data:
                allegati[f"output_atteso_{len(allegati)}.png"] = {"image/png": data["image/png"]}
            elif "text/html" in data and "<table" in data["text/html"]:
                # tabelle pandas: uso la versione testuale
                testi.append(data.get("text/plain", ""))
            elif "text/plain" in data:
                testi.append(data["text/plain"])
    parti = ["**Output atteso**"]
    txt = "".join(testi).strip()
    if txt:
        if len(txt) > 2500:
            txt = txt[:2500] + "\n... (output abbreviato)"
        parti.append("```\n" + txt + "\n```")
    for nome in allegati:
        parti.append(f"![output atteso](attachment:{nome})")
    if len(parti) == 1:
        parti.append("*(nessun output a video: controlla che la cella giri senza errori)*")
    return "\n\n".join(parti), allegati


def versione_studenti(nb_eseguito):
    nuovo = nbformat.v4.new_notebook()
    nuovo.metadata = nb_eseguito.metadata
    for cell in nb_eseguito.cells:
        if "solo-docente" in cell.metadata.get("tags", []):
            continue                       # soluzioni delle estensioni: solo versione docente
        if cell.cell_type != "code":
            nuovo.cells.append(nuova_markdown(cell.source, cell.get("attachments")))
            continue
        scaffold, ha_sol = scaffold_studente(cell.source)
        cella = nbformat.v4.new_code_cell(scaffold)
        if cell.metadata.get("tags"):
            cella.metadata["tags"] = list(cell.metadata["tags"])
        nuovo.cells.append(cella)
        if ha_sol:
            nuovo.cells.append(nuova_markdown(*output_atteso_md(cell)))
    return nuovo


# ----------------------------------------------------------------- main
def build(filtro="", esegui_nb=True):
    DOCENTE.mkdir(exist_ok=True)
    STUDENTI.mkdir(exist_ok=True)
    sorgenti = sorted(p for p in SORGENTI.glob("*.py") if p.name.startswith(filtro))
    for src in sorgenti:
        nome = src.stem
        print(f"== {nome}")
        nb = cells_to_nb(py_to_cells(src.read_text(encoding="utf-8")))
        if esegui_nb:
            nb = esegui(nb, DOCENTE)
        nbformat.write(nb, DOCENTE / f"{nome}.ipynb")
        nbformat.write(versione_studenti(nb), STUDENTI / f"{nome}.ipynb")
        n_es = sum(MARK_SOL in c.source for c in nb.cells if c.cell_type == "code")
        print(f"   {len(nb.cells)} celle, {n_es} celle-esercizio con soluzione")


ESCLUSI_SEMPRE = {".venv", "dist", "__pycache__", ".ipynb_checkpoints", ".omc", ".git", ".claude"}


def _da_includere(rel, per_studenti):
    parti = rel.parts
    if any(p in ESCLUSI_SEMPRE for p in parti):
        return False
    if per_studenti and parti[0] in ("docente", "sorgenti", "guida_docente"):
        return False                       # soluzioni e guida del docente NON vanno ai partecipanti
    if parti[0] in ("docente", "studenti") and "-Copy" in rel.name:
        return False                       # copie di lavoro create con "Duplicate" in JupyterLab
    if parti[0] in ("docente", "studenti") and len(parti) == 2 and rel.suffix != ".ipynb":
        return False                       # file prodotti eseguendo i notebook (csv, xlsx...)
    if parti[0] in ("docente", "studenti") and len(parti) > 2:
        return False                       # sottocartelle prodotte (figure/, output_atteso/ vecchie)
    return True


def pacchetto():
    """Crea dist/corso_python_CNR_partecipanti.zip (senza soluzioni) e dist/corso_python_CNR_docente.zip."""
    DIST.mkdir(exist_ok=True)
    for nome, per_studenti in [("partecipanti", True), ("docente", False)]:
        dest = DIST / f"corso_python_CNR_{nome}.zip"
        n = 0
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(RADICE.rglob("*")):
                rel = f.relative_to(RADICE)
                if f.is_file() and _da_includere(rel, per_studenti):
                    z.write(f, Path(RADICE.name) / rel)
                    n += 1
        print(f"scritto {dest.relative_to(RADICE)}: {n} file, {dest.stat().st_size / 1e6:.1f} MB")
    # solo installazione: da mandare prima del corso, senza notebook né dati
    dest = DIST / "corso_python_CNR_installazione.zip"
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for nome in FILE_INSTALLAZIONE:
            z.write(RADICE / nome, Path(RADICE.name) / nome)
        z.writestr(str(Path(RADICE.name) / "INSTALLAZIONE.txt"), ISTRUZIONI_INSTALLAZIONE)
    print(f"scritto {dest.relative_to(RADICE)}: {len(FILE_INSTALLAZIONE) + 1} file, {dest.stat().st_size / 1e3:.0f} kB")


FILE_INSTALLAZIONE = ["pyproject.toml", "uv.lock", "environment.yml", "verifica_ambiente.py"]
ISTRUZIONI_INSTALLAZIONE = """\
Corso "Python e Analisi Dati per Ricercatori CNR" - installazione dell'ambiente
==============================================================================

Questo pacchetto contiene SOLO l'ambiente: i notebook e i dati arriveranno a inizio corso.
Tempo necessario: 10-15 minuti. Non servono permessi di amministratore.
Il passo 4 scarica circa 500 MB: usate una connessione stabile.


PASSO 1 - Scompattare lo zip
-----------------------------
Scompattate lo zip in una cartella a vostra scelta (per esempio Documenti).
Si crea la cartella  corso_python_CNR.  CONSERVATELA: il materiale del corso
andra' scompattato nello stesso posto.

  Windows: clic destro sullo zip -> "Estrai tutto...". Non lavorate "dentro" lo zip
           senza estrarlo: i comandi non funzionerebbero.
  Mac:     doppio clic sullo zip.


PASSO 2 - Installare uv (il programma che installa Python e le librerie)
-------------------------------------------------------------------------
WINDOWS
  1. Aprite il menu Start, scrivete  powershell  e aprite "Windows PowerShell"
     (una finestra blu o nera dove si scrivono comandi).
  2. Copiate questa riga, incollatela nella finestra (clic destro incolla) e premete Invio:

       powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  3. Alla fine deve comparire un messaggio simile a "everything's installed!".
  4. CHIUDETE la finestra di PowerShell (e' importante: quella finestra non "vede" ancora uv).

MAC
  1. Aprite l'app Terminale (Cmd + Spazio, scrivete  Terminale, Invio).
  2. Copiate questa riga, incollatela nella finestra (Cmd + V) e premete Invio:

       curl -LsSf https://astral.sh/uv/install.sh | sh

  3. Alla fine deve comparire un messaggio simile a "everything's installed!".
  4. CHIUDETE la finestra del Terminale (Cmd + Q) e riapritela al passo 3.


PASSO 3 - Aprire il terminale DENTRO la cartella corso_python_CNR
------------------------------------------------------------------
E' il passaggio in cui ci si blocca piu' spesso: i comandi del passo 4 funzionano
solo se il terminale e' aperto nella cartella giusta.

WINDOWS
  1. Aprite la cartella  corso_python_CNR  in Esplora file (dovete vedere dentro i file
     pyproject.toml, uv.lock, verifica_ambiente.py...).
  2. Cliccate sulla barra dell'indirizzo in alto (dove c'e' il percorso della cartella),
     cancellate il testo, scrivete  powershell  e premete Invio.
     Si apre PowerShell gia' posizionato nella cartella.
     (Su Windows 11 va bene anche: clic destro in uno spazio vuoto della cartella
      -> "Apri nel Terminale".)

MAC
  1. Aprite il Terminale.
  2. Scrivete  cd  seguito da uno SPAZIO (non premete ancora Invio).
  3. Trascinate la cartella  corso_python_CNR  dal Finder dentro la finestra del Terminale:
     compare il suo percorso. Ora premete Invio.

Controllo (Windows e Mac): scrivete  ls  e premete Invio. Nell'elenco dovete vedere
pyproject.toml e verifica_ambiente.py. Se non li vedete, siete nella cartella sbagliata:
ripetete il passo 3.


PASSO 4 - Installare l'ambiente e verificarlo
----------------------------------------------
Nella stessa finestra scrivete questi due comandi, uno alla volta, premendo Invio
dopo ciascuno:

    uv sync

(attendete la fine: scarica Python e le librerie, qualche minuto)

    uv run python verifica_ambiente.py

L'ultima riga stampata deve essere:   tutto ok


PASSO 5 - Mandare il risultato al docente
------------------------------------------
Selezionate con il mouse TUTTO il testo stampato da  verifica_ambiente.py,
copiatelo e incollatelo nella risposta all'email del docente.
  Windows: selezionate il testo e premete Invio (oppure Ctrl + C) per copiarlo.
  Mac:     selezionate il testo e premete Cmd + C.
Per favore niente foto o screenshot: serve il testo.


SE QUALCOSA NON FUNZIONA
------------------------
- "uv non e' riconosciuto come nome di cmdlet..." (Windows) oppure
  "command not found: uv" (Mac):
    non avete chiuso e riaperto il terminale dopo il passo 2. Chiudetelo e ripetete dal passo 3.

- "No pyproject.toml found" oppure "can't open file verifica_ambiente.py":
    il terminale non e' nella cartella giusta. Ripetete il passo 3.

- Il comando del passo 2 viene bloccato (antivirus, proxy dell'ente, criteri di sicurezza):
    provate da un'altra rete (per esempio da casa). Se ancora non va:
      * se avete gia' Python installato:   pip install uv   e poi ripartite dal passo 3;
      * altrimenti usate il PIANO B qui sotto.

- uv sync si interrompe con errori di rete o "timeout":
    rilanciatelo (riprende da dove era rimasto), possibilmente da una rete diversa.

In ogni caso mandate al docente il messaggio di errore COMPLETO (copia-incolla, non una foto).


PIANO B - Miniforge (solo se uv non funziona)
---------------------------------------------
1. Scaricate e installate Miniforge per il vostro sistema da:
     https://github.com/conda-forge/miniforge
   (Windows: durante l'installazione lasciate le opzioni predefinite.)
2. Windows: aprite dal menu Start "Miniforge Prompt".   Mac: aprite il Terminale.
3. Spostatevi nella cartella corso_python_CNR (passo 3; nel Miniforge Prompt scrivete
   cd  seguito da uno spazio e incollate il percorso copiato dalla barra di Esplora file).
4. Eseguite, uno alla volta:
     conda env create -f environment.yml
     conda activate corso-cnr
     python verifica_ambiente.py
5. Mandate il risultato come al passo 5.
"""


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    cmd = args[0] if args else "build"
    filtro = args[1] if len(args) > 1 else ""
    if cmd == "build":
        build(filtro, esegui_nb="--no-exec" not in sys.argv)
    elif cmd == "pacchetto":
        pacchetto()
    else:
        print(__doc__)
