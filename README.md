# Python e Analisi Dati per Ricercatori CNR: materiali del corso

4 giorni × 6 ore · 8 notebook (mattina/pomeriggio) · lezione + esercizi nello stesso file.

## Struttura

```
corso_python_CNR/
├── README.md                 questo file
├── pyproject.toml, uv.lock   ambiente con uv (installazione principale): `uv sync`
├── environment.yml           piano B con Miniforge: `conda env create -f environment.yml`
├── verifica_ambiente.py      deve stampare "tutto ok" -> da far girare ai partecipanti prima del corso
├── genera_dati.py            rigenera i dataset sintetici in dati/ (seme fisso 42)
├── genera_schemi.py          rigenera gli schemi in img/ (sostituibili con le tue slide, stesso nome .png)
├── dati/                     dataset (vedi sotto)
├── img/                      12 schemi PNG richiamati dai notebook come ../img/nome.png
├── materiali/                figure_pubblicazione.py, personalizzazione_grafici.ipynb (scheda di riferimento)
├── sorgenti/                 UNICO SORGENTE di ogni notebook (formato "percent", file .py)
├── docente/                  notebook completi, ESEGUITI, con tutte le soluzioni  (non proiettare)
├── studenti/                 notebook con i buchi + "Output atteso" reale sotto ogni esercizio
└── strumenti/nb_tools.py     build: sorgenti -> docente (esegue) -> studenti; `pacchetto` -> dist/*.zip
```

| # | Notebook | Contenuto |
|---|---|---|
| 01 | G1 mattina: Python essenziale | benvenuto, fuori scope, Jupyter, tipi, f-string, liste, dizionari, for/if, range/enumerate/zip, comprehension |
| 02 | G1 pomeriggio: Funzioni, errori, file, NumPy | funzioni, import, traceback vero e i 6 errori, try/except, 2.2 caccia al bug, pathlib, 2.3 parsing file strumento, array/maschere/NaN, primo grafico, picco su linea di base, 2.4 ciclo su cartella → CSV |
| 03 | G2 mattina: Pandas essenziale | DataFrame/Series, read_csv su CSV "italiano" sporco, info/describe (`str` = testo), rename, date, Excel, loc/iloc/filtri, colonne derivate |
| 04 | G2 pomeriggio: Pulizia e progetto | mancanti, duplicati, anomali IQR per gruppo (sui log), groupby/agg/transform, merge/join, **API UniProt → JSON → merge (facoltativo, copia offline)**, pivot/melt, **Progetto wrangling con report (60')**, resample (per casa) |
| 05 | G3 mattina: Grafici per la pubblicazione | API a oggetti, tipi, barre d'errore, personalizzazione, subplot, standard rivista con `figure_pubblicazione.py` (`stile_rivista` / `stile_rivista_ctx`, `verifica_figura` su font e linee), controllo in b/n, figura multipannello PDF/TIF, seaborn (facoltativo) |
| 06 | G3 pomeriggio: SciPy e statistica | linregress con incertezze, Anscombe, bande di confidenza/predizione, report di regressione con un anomalo, curve_fit (decadimento, sigmoide a 4 parametri), residui, t-test/Cohen, ANOVA/Tukey, Kruskal-Wallis, una media per campione (pseudoreplicazione) e scala log, confronti multipli |
| 07 | G4 mattina: Preprocessing e PCA | workflow, X/y, imputazione, richiamo NumPy (axis, broadcasting) → scaling (demo senza), fit/transform, PCA con loadings interpretati, k-means vs classi note, normalizzazione per campione, gerarchico (facoltativo), esercizio facoltativo sulle repliche (prepara il progetto finale) |
| 08 | G4 pomeriggio: Random forest e validazione | train/test, k-fold e scelta di k, **overfitting dal vivo su rumore** (selezione fuori/dentro la CV, `permutation_test_score`), metriche e confusione, Pipeline, importanza (impurità e permutazione), **Progetto finale** su campioni con repliche (CV per gruppi, permutazioni per campione), chiusura |

## Come si lavora sui notebook

**Modificare SOLO `sorgenti/*.py`**, poi:

```bash
uv run python strumenti/nb_tools.py build            # tutti (esegue i notebook: ~3-4 minuti)
uv run python strumenti/nb_tools.py build 06         # solo il 06
uv run python strumenti/nb_tools.py build --no-exec  # senza eseguire (niente output atteso)
```

Il build esegue la versione docente (fallisce se una cella dà errore: è voluto), poi genera la
versione studenti. Gli esercizi seguono questa convenzione dentro una cella di codice:

```python
# ESERCIZIO 1.1 (livello 1)
# commento normale: resta in entrambe le versioni
#> conc_nM = conc_ug_L / ____ * 1000     # riga "per lo studente": nella versione studenti viene
#>                                       # scommentata (con i ____ da riempire)
# --- SOLUZIONE ---                      # da qui in poi: SOLO versione docente
conc_nM = conc_ug_L / massa_molare * 1000
```

- Nessuna riga `#>` = livello 2/3: lo studente trova solo i commenti-struttura (o niente) e `# scrivi qui il tuo codice`.
- Sotto ogni cella-esercizio la versione studenti riceve una cella "Output atteso" con l'output reale
  (testo e/o PNG) prodotto eseguendo la soluzione: così sanno da soli se hanno finito.
- Ogni esercizio ha un'**estensione facoltativa** in fondo per chi finisce presto.
- Il marcatore può stare anche dentro una funzione (indentato): il segnaposto viene indentato allo
  stesso livello, e una riga `# --- FINE SOLUZIONE ---` restituisce allo studente le righe che seguono
  (es. `return` e chiamate di prova).
- Una cella che **deve** dare errore (per mostrare un traceback vero) si marca con
  `# %% tags=["raises-exception"]`: il build non si ferma su quella cella.
- Una cella marcata `# %% tags=["solo-docente"]` (o `# %% [markdown] tags=["solo-docente"]`) compare
  solo nella versione docente: si usa per le soluzioni delle estensioni facoltative.
- In fondo ai notebook, la sezione *Esercizi per casa* (numerati C1.1, C3.1, …) raccoglie gli
  esercizi tolti dal flusso dell'aula per alleggerire la giornata; i blocchi segnati
  *Facoltativo: si può saltare se si è in ritardo* si possono saltare senza rompere il seguito.
- Le immagini (schemi `../img` e grafici attesi) sono **incorporate** nei notebook come allegati.

I notebook iniziano tutti con la stessa cella di avvio (`trova_dati()`), che cerca `../dati`,
`dati` o `corso_python_CNR/dati` e, se non li trova, rigenera i dati con `genera_dati.py`:
funziona anche su **Google Colab** caricando lo zip del corso (le immagini sono incorporate nei
notebook, quindi si vedono anche lì).

## Dataset (sintetici, tema sensori elettrochimici / matrici biologiche; uno derivato da dati reali per il progetto finale)

| File | Usato in | Cosa contiene |
|---|---|---|
| `strumento/DPV_S01..S12.txt` (+ `S13_malformato`) | G1 | voltammogrammi DPV con header di metadati; picco ∝ concentrazione |
| `misure_sporche.csv` | G2, G3 | 311 righe: 40 campioni (ognuno con **una** matrice: foglia/frutto/suolo) × Cu/Pb/Cd × 2-3 repliche, analizzati 5-39 giorni dopo il campionamento; `;`, virgola decimale, latin-1, `n.d.`, date gg/mm/aaaa, 10 NaN, 6 duplicati esatti, 4 anomali ×20, operatori non uniformi. Concentrazioni lognormali, repliche dello stesso campione correlate (→ media per campione nel nb 06) |
| `metadati_campioni.xlsx` | G2 | sito/quota/data di campionamento per 37 dei 40 campioni (3 senza → NaN nel merge: 25 righe) |
| `uniprot_esempio.json` | G2 (sezione API) | risposta salvata dell'API REST di UniProt per 10 geni umani (11 risultati: FBF1 entra perché "ALB" è un suo sinonimo). **Non** è generato da `genera_dati.py`: non cancellatelo. Si usa con `USA_RETE = False` (default) |
| `sensore_serie.csv` | G2 | 1 settimana ogni 10 min, un buco di acquisizione (resample) |
| `taratura.csv` | G3 | 6 livelli × 3 repliche → retta, bande di confidenza e predizione |
| `dose_risposta.csv`, `cinetica.csv` | G3 | curva di Hill, decadimento esponenziale con plateau |
| `confronto_gruppi.csv` | G3 | 3 trattamenti × 8 repliche (t-test, ANOVA) |
| `sensori_matrice.csv` | G3, G4 | 60 campioni × (15 correnti + 5 chimico-fisiche) + sito; deriva strumentale su PC1; CV RF ≈ 0.92 ± 0.09 |
| `rumore_puro.csv` | G4 | 30 × 200 variabili casuali + etichetta 15/15 senza legame con le variabili: la demo dell'overfitting |
| `dataset_features_campioni.csv` | G4 (es. 7.2 facoltativo, progetto finale) | derivato da un dataset reale (nomi anonimizzati): 36 campioni × 3 repliche (108 righe), 45 variabili `feature_01..45`, 3 classi da 12 campioni. **Non** è generato da `genera_dati.py`: non cancellatelo. numeri trasformati colonna per colonna (non corrispondono a misure reali). |

Tutti gli altri file sono sintetici e si rigenerano con `genera_dati.py`.

## Sostituire gli schemi

Le immagini in `img/` sono generate da `genera_schemi.py` e volutamente semplici. Per usare una tua
slide: esportala in PNG **con lo stesso nome** (`groupby.png`, `kfold.png`, …) e sovrascrivi il file.
Nomi: `indici_lista, broadcasting, dataframe_anatomia, loc_iloc, groupby, merge, kfold, overfitting,
pipeline_leakage, pca_concetto, workflow_ml, anatomia_figura, traceback`.

## Installazione

**Principale: uv** (nessun permesso di amministratore, scarica da solo Python 3.12, versioni bloccate in `uv.lock`):

```bash
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

cd corso_python_CNR
uv sync                                  # crea .venv/ con tutte le librerie
uv run python verifica_ambiente.py       # -> "tutto ok"
uv run jupyter lab
```

Chi ha già installato uv apre un terminale nella cartella e usa sempre `uv run ...`: non serve
"attivare" nulla. Se il proxy dell'ente blocca `astral.sh`, uv si installa anche con `pip install uv`.

**Piano B: Miniforge** (se uv è bloccato dal proxy o dall'antivirus):

```bash
conda env create -f environment.yml
conda activate corso-cnr
python verifica_ambiente.py
jupyter lab
```

**Piano C: Google Colab**: caricare lo zip del corso, `!unzip corso_python_CNR.zip`, poi aprire il
notebook da `studenti/` con *File → Carica notebook* (Colab non apre direttamente i `.ipynb` scompattati
nella macchina virtuale). Colab ha già tutte le librerie; le immagini sono incorporate nei notebook e la
cella di avvio trova i dati in `corso_python_CNR/dati`.

I due ambienti hanno le stesse librerie e le stesse versioni minime (pandas ≥ 3), Python 3.12. Gli
"output attesi" sono prodotti con le versioni esatte di `uv.lock`; con Miniforge possono differire
nelle ultime cifre. Su Colab (pandas 2.x) i tipi delle colonne di testo appaiono come `object`
invece di `str`: `verifica_ambiente.py` lo segnala.

### Windows: dove sta Python e dove vanno i materiali

uv non installa Python "nel sistema": l'interprete sta in una cartella di uv
(`%APPDATA%\uv\python`), le librerie in `.venv\` dentro `corso_python_CNR`, e `.venv\Scripts\python.exe`
è solo un rimando all'interprete. Da qui le tre cause per cui "Python non si trova":

1. **`python` scritto senza `uv run`.** PowerShell non lo trova, o apre il Microsoft Store
   (*"Python non è stato trovato; eseguire senza argomenti per installare da Microsoft Store…"*).
   Non installate niente dallo Store: scrivete sempre `uv run python …` e `uv run jupyter lab`.
2. **Materiale scompattato in una cartella nuova.** Lo zip dei partecipanti contiene già una cartella
   `corso_python_CNR`, ma "Estrai tutto…" propone una cartella con il nome dello zip. Il risultato è:

   ```
   Documenti\corso_python_CNR\.venv                                   <- ambiente installato
   Documenti\corso_python_CNR_partecipanti\corso_python_CNR\studenti  <- notebook, senza .venv
   ```

   Come destinazione va scelta la cartella che **contiene** `corso_python_CNR` (es. `Documenti`).
   Se è già successo: spostate tutto il contenuto di `...\corso_python_CNR_partecipanti\corso_python_CNR`
   dentro `Documenti\corso_python_CNR` (i file in comune sono identici: sostituite pure), **senza**
   portarvi un eventuale `.venv` creato lì (cancellatelo), poi cancellate la cartella vuota.
   Controllo: in `Documenti\corso_python_CNR` devono esserci sia `.venv` sia `studenti` e `dati`.
3. **Cartella del corso spostata o rinominata dopo `uv sync`.** I comandi in `.venv\Scripts`
   (es. `jupyter.exe`) contengono il percorso vecchio e smettono di funzionare. Spostate i materiali
   dentro la cartella, non la cartella. Se è già successo: cancellate `.venv` e lanciate
   `uv sync --offline` (lo ricrea in pochi secondi dalla cache di uv; se dà errore, `uv sync` con la rete).

Per capire quale dei tre, in PowerShell nella cartella del corso:

```powershell
ls .venv\Scripts\python.exe                           # non esiste -> caso 2
uv run python -c "import sys; print(sys.executable)"  # funziona -> l'ambiente è a posto: caso 1
```

**VS Code** al posto di JupyterLab: *File → Apri cartella…* su `corso_python_CNR` (non il singolo
`.ipynb`), poi nel notebook *Select Kernel → Python Environments → `.venv\Scripts\python.exe`*.

## Prima del corso (dalla guida operativa)

1. `python strumenti/nb_tools.py build` e poi `python strumenti/nb_tools.py pacchetto`: crea
   `dist/corso_python_CNR_partecipanti.zip` (**senza** `docente/` e `sorgenti/`, che contengono le
   soluzioni; senza `.venv/`, cache e file prodotti eseguendo i notebook) e `dist/corso_python_CNR_docente.zip`.
   **Non distribuire la cartella così com'è**: `.venv/` pesa ~560 MB e funziona solo sul computer che l'ha creata.
2. Inviare lo zip dei partecipanti con le istruzioni di installazione qui sopra, separate per Mac e
   Windows; raccogliere gli output di `verifica_ambiente.py`.
3. Chiavetta USB con lo zip; piano B Colab.
4. Gli esercizi sono nei notebook `studenti/`; le soluzioni (`docente/`) si distribuiscono a fine giornata.

## Licenze e crediti

Materiali del corso: CC-BY 4.0. Struttura e spirito degli esercizi ispirati a
[Software Carpentry, Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder) (CC-BY 4.0),
[Aalto Scientific Computing, Python for Scientific Computing](https://aaltoscicomp.github.io/python-for-scicomp) (CC-BY 4.0),
[Scientific Python Lectures](https://lectures.scientific-python.org) (CC-BY 4.0).
Formule della taratura: Miller & Miller, *Statistics and Chemometrics for Analytical Chemistry*.
