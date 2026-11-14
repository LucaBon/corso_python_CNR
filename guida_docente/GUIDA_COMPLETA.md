# Guida del docente: Python e Analisi Dati per Ricercatori CNR

4 giorni × 6 ore · 20 partecipanti · settimana del 16/11/2026

Come usare questa guida: la **Parte A** si legge una volta questa settimana. Le **Parti G1-G4** si
stampano e si tengono sul leggio, una per giorno. Gli orari sono quelli del corso (10:00-13:00
e 14:00-17:00, con 15' di pausa per mezza giornata: 165' netti). Dalle 9:00 alle 10:00 prepari l'aula.

---

# Parte A: preparazione e conduzione dell'aula

## A1. Checklist della settimana prima

**Materiali**
- [ ] **Rigenera gli zip.** I notebook 01, 02, 05, 07 e 08 sono stati ricompilati il 14/11, quindi gli zip in
      `dist/` sono vecchi:
      `uv run python strumenti/nb_tools.py pacchetto`. Poi apri lo zip dei partecipanti e controlla
      che **non** contenga `docente/` né `sorgenti/`.
- [ ] Copia `corso_python_CNR_partecipanti.zip` su una **chiavetta USB** (meglio due) e su un link
      di download (Drive o simili) da scrivere alla lavagna il primo giorno.
- [ ] Hai raccolto l'output di `verifica_ambiente.py` di tutti e 20? Fai una lista di chi **non** ha
      risposto o ha avuto errori, e il giorno 1 parti da loro.
- [ ] Prova **Colab** (piano C) con lo zip dei partecipanti, almeno sul notebook 01 e sullo 04.
      Sono i due che più spesso si rompono per i percorsi.

**Prova generale (la cosa più utile in assoluto)**
- [ ] Fai ogni notebook della cartella `studenti/` **come se fossi uno studente**: riempi i `____`
      senza guardare la soluzione e cronometrati. In aula ci vorrà circa **2,5-3 volte** il tuo tempo.
      Se un blocco ti richiede più di 10', in aula ne richiederà 30: segnalo come candidato al taglio.
- [ ] Per ogni giorno scegli **prima** cosa tagliare se sei in ritardo (vedi le sezioni
      "Se sei in ritardo" di ogni giorno). Le decisioni in aula, sotto pressione, sono peggiori.
- [ ] Leggi le sezioni "Da verificare prima del corso" di ogni giorno e risolvi quello che serve.
- [ ] Giorno 4: parla **in privato e prima** con la persona che ha fornito il dataset del progetto
      finale (vedi la Parte G4).

**Postazione**
- [ ] Proiettore: JupyterLab con zoom al **150-175%** (`Ctrl +`), tema chiaro (il tema scuro si
      legge male proiettato). Verifica dall'ultima fila che si legga il codice.
- [ ] Nascondi la barra laterale di JupyterLab (`Ctrl+B`) mentre proietti.
- [ ] Due finestre: proietti il notebook **studenti** (vuoto, lo riempi dal vivo), sul tuo schermo
      tieni il notebook **docente** con le soluzioni. **Non proiettare mai `docente/`.**
      Se non hai un secondo schermo: soluzioni stampate o su tablet.
- [ ] Un notebook "lavagna" vuoto, per rispondere alle domande al volo senza sporcare quello del giorno.
- [ ] Lavagna o flipchart: ci scrivi il link allo zip, l'esercizio in corso e l'ora in cui si riprende.

## A2. Il ritmo di una lezione di programmazione

Ogni blocco di 20-40 minuti segue lo stesso ciclo:

1. **Perché** (1-2'): che problema reale risolve quello che stiamo per vedere. ("Avete 12 file
   dallo strumento e volete una tabella: oggi lo facciamo in 15 righe.")
2. **Dimostrazione dal vivo** (5-15'): scrivi il codice, non incollarlo (vedi A3).
3. **Esercizio** (10-25'): lo lanci, giri tra i banchi, lo chiudi.
4. **Correzione** (3-5'): mostri la soluzione dal vivo e commenti 1-2 errori che hai visto girando.
5. **Una frase di sintesi**: "Quindi: `groupby` = dividi, applica, ricombina."

Regola pratica: **non parlare più di 15-20 minuti di fila** senza far toccare la tastiera.

## A3. Scrivere codice dal vivo

- **Scrivi, non incollare.** Scrivere rallenta il tuo ritmo fino a quello che la sala riesce a
  seguire, e mostra che anche tu sbagli e correggi.
- **Racconta mentre scrivi**: "Creo una variabile… apro le parentesi quadre perché voglio una lista…"
- **Sbaglia apposta** almeno una volta per blocco (una parentesi mancante, un nome scritto male) e
  **leggi l'errore ad alta voce, dal basso**: "Ultima riga: NameError, name 'concentrazone' is not
  defined. Ah, ho scritto male." È la competenza più utile del corso.
- **Prima la previsione, poi l'esecuzione**: "Secondo voi cosa stampa?" Aspetta 5 secondi
  di silenzio, anche se sembrano lunghi. Poi esegui.
- Dopo ogni cella importante **fermati e indica** sullo schermo cosa guardare (la forma della tabella,
  il tipo della colonna, il numero di righe).
- Se qualcosa si rompe davvero in diretta: niente panico, è materiale didattico. "Vediamo insieme
  cosa ci dice Python." Se non lo risolvi in 2 minuti: "Ci torno nella pausa", e passi alla soluzione.

## A4. Gestire gli esercizi con 20 persone

**Lanciare** (30 secondi, sempre uguali):
- "Esercizio 2.3. Obiettivo: … Avete **15 minuti**, si riprende alle **10:40**." Scrivi l'ora alla lavagna.
- "Sotto c'è l'output atteso: se il vostro coincide, avete finito. Chi finisce fa l'estensione."

**Girare tra i banchi**
- Fai un primo giro rapido nei primi 3-4 minuti, per scovare chi non è nemmeno partito (kernel
  sbagliato, cella di avvio non eseguita, file non trovato). Sono i blocchi più frequenti, non la logica.
- Con chi è bloccato: **fai domande, non prendere la tastiera**. "Cosa dice l'ultima riga
  dell'errore?" "Cosa contiene questa variabile? Stampala."
- Se vedi lo **stesso errore 3 volte**, fermati e spiegalo a tutta la sala.
- Tieni d'occhio chi non chiede mai aiuto: spesso è chi è più indietro.

**Chiudere**
- Chiudi quando circa **due terzi** hanno finito, non quando hanno finito tutti: aspettare l'ultimo
  annoia gli altri 19. "Chi non ha finito: tranquilli, ora lo facciamo insieme."
- Annuncia la fine 2 minuti prima: "Ancora due minuti."

## A5. Un'aula eterogenea

Il pubblico va dai principianti assoluti agli utenti esperti di R.

- **Esperti di R e chi ha già usato Python**: dagli le estensioni facoltative e gli esercizi per
  casa. Chiedi loro in aula "Come si fa in R?": li coinvolge e fa da ponte per gli altri. Se però
  cominciano a dominare la discussione: "Ottima domanda, ne parliamo in pausa."
- **Principianti**: il primo giorno è decisivo. Se a pranzo del G1 qualcuno è completamente perso,
  parlaci in pausa e indicagli gli esercizi di livello 1 (quelli con i `____`) come obiettivo
  minimo. Dire "è normale non finire tutto" (è nelle regole d'aula) serve davvero.
- Chi conosce Perl/PHP capisce subito la sintassi, ma non pandas e NumPy: le sue difficoltà
  arrivano dal giorno 2.
- Chi lavora in genetica con dataset molto grandi: farà domande sulle prestazioni e sulla memoria.
  Risposta onesta: "Le idee sono le stesse. Per dati molto grandi esistono strumenti dedicati
  (formati colonnari, librerie apposite), ma non sono l'argomento di questo corso."

## A6. Domande difficili e domande di dominio

Il corso usa dati di chimica e biologia, ma **tu sei qui come esperto di Python e di analisi dei
dati, non di elettrochimica**. È una posizione legittima: dichiarala il primo giorno.

- Frase da usare: *"Sulla chimica di questo esempio voi ne sapete più di me. Io vi mostro come si fa
  in Python; se l'interpretazione non vi torna, ditemelo, che mi interessa."*
- "Non lo so" va benissimo, purché sia seguito da **"verifico e vi rispondo domani"**. Tieni una
  lista delle domande in sospeso e aprici la mattina successiva: dà molta credibilità.
- Domande fuori tema (deep learning, il loro dataset specifico, Git…): "Lo segno, se resta tempo ne
  parliamo alla fine o in pausa." La tabella "Cosa NON faremo" nel notebook 01 ti protegge: rimanda a quella.

## A7. Energia e tempi

- **Pause puntuali**, anche nel mezzo di un argomento. Dopo pranzo l'attenzione crolla: il primo
  blocco del pomeriggio deve essere pratico (esercizio o demo), non teoria.
- Ogni 20-25 minuti **cambia modalità** (spiegazione → demo → esercizio).
- Fine di ogni mezza giornata (5'): "Tre cose da ricordare di stamattina", scritte alla lavagna.
- Fine giornata: distribuisci i notebook `docente/` **del giorno appena concluso** (non di quelli
  dopo) e indica gli *Esercizi per casa* in fondo al notebook.
- La tua voce: parla più lentamente di quanto ti sembri naturale. Bevi. Siediti quando fai la demo.

## A8. Se qualcosa va storto

| Problema | Cosa fare |
|---|---|
| Installazione rotta su un portatile | Non sistemarla in aula a lezione iniziata: subito Colab (piano C del README), sistemi in pausa |
| `FileNotFoundError` sui dati | Ha aperto il notebook fuori da `studenti/` o non ha eseguito la cella di avvio. Controlla il percorso |
| Risultati strani o variabili "fantasma" | `Kernel → Restart Kernel and Run All Cells`. Ricorda la regola: conta l'ordine di esecuzione |
| Il notebook non risponde più | Ciclo infinito o cella lunga: pulsante ■ (interrompi), poi restart |
| Rete assente | La sezione API (G2) ha `USA_RETE = False` di default con la copia offline: nessun problema |
| Sei in ritardo di 30' o più | Applica la lista "Se sei in ritardo" del giorno, senza esitare. Gli esercizi per casa esistono apposta |
| Il proiettore non va | Fai fare ai partecipanti l'esercizio successivo mentre sistemi: ognuno ha il notebook |

## A9. Da sistemare prima di lunedì (aggiornato il 14/11)

**Già corretto nei sorgenti il 14/11** (notebook 01, 02, 05, 07, 08 ricompilati)
- Il risultato del progetto finale non è più nel `README.md`; la conclusione d'esempio è solo nella versione docente. Restano gli "Output attesi" del progetto nel notebook studenti del giorno 4.
- Es. 5.3: il testo chiede `verifica_figura(fig, larghezza_max=7.5)`.
- Suggerimento di C7.1 allineato alla soluzione.
- Segno meno tipografico nelle soglie del notebook 02 sostituito con `-`.
- Esercizio 1.3 spostato dopo le prime tre celle su `for` e `if`.
- "domani" → "oggi pomeriggio" nel notebook 05.
- Leave-one-out nel notebook 08: ora rimanda alla k-fold ripetuta.

**Ancora da fare**
1. **Rigenera gli zip** (`uv run python strumenti/nb_tools.py pacchetto`) dopo queste correzioni, e controlla che lo zip dei partecipanti non contenga `docente/` né `sorgenti/`.
2. Formulazioni statistiche del nb 06 da limare a voce: la banda di confidenza descritta come "probabilità
   95 %" (`:103-104`), dove è frequentista e punto per punto; il tempo di dimezzamento τ·ln2 (`:242`),
   che vale solo per la parte sopra il plateau; l'ANOVA presentata come obbligatoria prima di Tukey
   (`:418-419`).
3. Tempi di calcolo del giorno 4: su una macchina a 2 core il test di permutazione della §4 richiede circa 30 s e il punto 5 del progetto circa 1,5 minuti. Sui portatili dei partecipanti saranno simili o inferiori; il punto 5 resta comunque solo proiettato.
4. `requests` (sezione API, solo con `USA_RETE = True`) non è dichiarato in `environment.yml`:
   controllalo sull'ambiente Miniforge.
5. Windows, "Estrai tutto": lo zip dei partecipanti può finire in una cartella annidata invece di
   unirsi a quella dell'installazione. Prevedilo nelle istruzioni del giorno 1.
6. Costrutti usati senza spiegazione, da dire a voce: `elif` e `continue` (in `leggi_dpv`, giorno 1), la somma senza parentesi quadre in `dev_std` (giorno 1), `lambda` in `anomali_iqr` (giorno 2).
7. Gli output dei notebook `docente/` mostrano il percorso della cartella in cui sono stati compilati: se ti dà fastidio, ricompila dalla tua cartella definitiva prima di distribuirli.


---

# Guida del docente

## Giorno 1 — Python essenziale; funzioni, errori, file e NumPy

Notebook: `studenti/01_G1_mattina_python_essenziale.ipynb` (mattina), `studenti/02_G1_pomeriggio_funzioni_file_numpy.ipynb` (pomeriggio).
Sorgenti con le soluzioni: `sorgenti/01_G1_...py`, `sorgenti/02_G1_...py`. Proietta solo i notebook di `studenti/`, mai quelli di `docente/`.
I notebook non danno orari, a parte "Prova tu (2')" nel §1 della mattina: gli orari qui sotto sono costruiti sull'orario del corso, 10:00–13:00 e 14:00–17:00 (165' netti per mezza giornata, con 15' di pausa).

Obiettivo da ripetere a fine giornata: *"Oggi avete scritto uno script che apre 12 file di uno strumento, estrae un numero da ciascuno e salva una tabella. Domani la apriamo con pandas in una riga."*

---

## Primi 20 minuti del corso (10:00–10:20)

Chi non ha mandato l'output di `verifica_ambiente.py` può arrivare alle 9:30: sei già in aula per la preparazione.

**Prima che entrino**: JupyterLab aperto sul tuo portatile in `studenti/`, font grande (Ctrl/Cmd +), tema chiaro. Il notebook 01 già aperto, kernel pulito. La chiavetta USB con lo zip pronta.

1. **Presentazione (3')**
   - "Sono un ingegnere di machine learning, non un chimico né un biologo. Gli esempi usano dati di sensori elettrochimici e matrici biologiche, ma di solito sono solo curve e tabelle. Se mi fate una domanda sul dominio vi dico onestamente se non so rispondere, e chi di voi lo sa ci darà una mano."
   - Chiedi per alzata di mano: chi ha mai scritto codice? chi usa R? chi ha già usato Python? Ti serve per calibrare il ritmo e sapere a chi chiedere un parere su R.
2. **Aspettative (3'). Leggi dal notebook la sezione "Benvenuti"**
   - L'arco dei 4 giorni: script su file di strumento, poi pandas al posto di Excel, poi figura da rivista e taratura, infine PCA e un modello predittivo, "e soprattutto quando *non* fidarci del risultato".
   - Il messaggio chiave, da dire con parole tue: "Non dovete imparare a ragionare sui dati, lo fate da anni. Dovete imparare una lingua nuova. Vi capiterà di sapere cosa volete e di non riuscire a scriverlo: è normale."
3. **Regole d'aula (1'). Sono quelle del notebook, non aggiungerne altre**
   - Si lavora da soli o in coppia, come si preferisce.
   - È normale non finire tutti gli esercizi; in fondo a ogni esercizio c'è un'estensione facoltativa per chi finisce presto.
   - Sotto ogni esercizio c'è l'"Output atteso": se il vostro coincide, avete finito.
4. **Controllo dell'ambiente (8')**
   - Tutti aprono un terminale nella cartella `corso_python_CNR` ed eseguono `uv run python verifica_ambiente.py` (con Miniforge: `conda activate corso-cnr`, poi `python verifica_ambiente.py`). L'ultima riga deve essere `tutto ok`.
   - Poi `uv run jupyter lab`, aprire `studenti/01_G1_mattina_python_essenziale.ipynb` ed eseguire la cella di avvio (§0). Deve stampare `Cartella dati: .../corso_python_CNR/dati` e `Python: 3.12.x`.
   - **Prima trappola, lo zip dei materiali**: lo zip dei partecipanti contiene una cartella `corso_python_CNR/` e va scompattato **nello stesso posto** della cartella di installazione. Su Windows "Estrai tutto" crea di solito `corso_python_CNR_partecipanti\corso_python_CNR\`. Lì manca `.venv/` e `uv run` ricrea l'ambiente; con la cache di uv di solito è veloce, ma serve la rete. Soluzione: spostare `studenti/` e `dati/` nella cartella di installazione, oppure lanciare `uv sync` nella cartella nuova.
   - `uv` non riconosciuto: il terminale è stato aperto prima di installare uv. Va chiuso e riaperto.
   - `No pyproject.toml found`: il terminale non è nella cartella giusta. Bisogna aprirlo dentro `corso_python_CNR`.
   - **Se l'installazione non va entro 5 minuti, non fermare l'aula.** Passa al piano C del README, Google Colab: caricare lo zip, `!unzip corso_python_CNR.zip`, poi *File → Carica notebook* da `studenti/` (Colab non apre direttamente i `.ipynb` scompattati). La cella di avvio trova `corso_python_CNR/dati`. Sistemi la sua installazione durante la pausa.
   - Su Colab `verifica_ambiente.py` segnala pandas 2.x: per oggi non conta (pandas si usa da domani, e cambia solo `object` al posto di `str`).

---

# MATTINA (10:00–13:00): Python essenziale

## 1. Scaletta

| orario | sezione del notebook | modalità | min |
|---|---|---|---|
| 10:00 | Primi 20 minuti (vedi sopra) | spiego | 20 |
| 10:20 | Benvenuti: "Cosa NON faremo", "Python o R?" (due frasi ciascuno) | spiego | 8 |
| 10:28 | §0 Cella di avvio + §1 JupyterLab (+ "Prova tu" 2') | demo live | 15 |
| 10:43 | §2 Variabili e tipi, conversioni, f-string | demo live | 20 |
| 11:03 | Esercizio 1.1 | esercizio | 10 |
| 11:13 | §3 Liste, slicing (tuple: una frase) | demo live | 12 |
| 11:25 | Pausa | | 15 |
| 11:40 | Esercizio 1.2 | esercizio | 15 |
| 11:55 | §4 Dizionari | demo live | 8 |
| 12:03 | §5 prime tre celle (`for`, `for` + `if`, filtro con `append`) + accumulatore dal vivo | demo live | 10 |
| 12:13 | Esercizio 1.3 | esercizio | 8 |
| 12:21 | §5 Confronti, `range` / `enumerate` / `zip` | demo live | 12 |
| 12:33 | Esercizio 1.4 | esercizio | 17 |
| 12:50 | §6 List comprehension: solo demo, l'esercizio 1.5 lo fai tu dal vivo | demo live | 5 |
| 12:55 | Riepilogo: i tre errori della settimana | spiego | 5 |

Note:
- L'esercizio 1.3 ora sta nel §5, dopo le prime tre celle su `for` e `if` (spostato nei sorgenti il 14/11).
- Prima dell'esercizio 1.4 mostra dal vivo lo schema dell'accumulatore, che nessuna demo contiene: `n = 0`, poi `for c in correnti:` / `if c > soglia:` / `n = n + 1`. L'esercizio 1.4 chiede lo stesso schema per la somma.
- Il notebook 01 non ha estensioni facoltative: chi finisce presto (utenti R, Perl/PHP) fa C1.1 e C1.2 in fondo al notebook.
- Rispetto alla versione su 9:00–12:30 sono compressi: Benvenuti, tuple, comprehension (l'esercizio 1.5 diventa demo) e riepilogo.

## 2. Sezioni

### Benvenuti: Cosa NON faremo / Python o R?
**Cosa dire**
- "Niente deep learning: con 30 campioni è pericoloso, e in 4 giorni non si insegna onestamente."
- "Niente bioinformatica specifica (FASTA, VCF, scanpy): ogni formato ha la sua libreria, ma sotto ci sono sempre pandas e NumPy, che vedremo."
- R: "Non vi chiedo di abbandonare R. Python è più comodo per procurarsi e pulire i dati, per l'automazione e l'ML; R resta più comodo per `lm`/`lme4`, Bioconductor e ggplot2. Si passano CSV senza problemi."
- "Il test migliore: rifate in Python un'analisi che fate già in R e confrontate."

### §0 Cella di avvio e §1 JupyterLab
**Cosa dire**
- "Prima cosa di ogni notebook: la cella di avvio, con Shift+Invio. Trova i dati, e se non ci sono li rigenera."
- "Conta l'ordine in cui eseguite le celle, non l'ordine sulla pagina. Il numero `[7]` a sinistra ve lo dice."
- "Prima di salvare un lavoro: Kernel → Restart Kernel and Run All Cells. Se arriva in fondo senza errori, è riproducibile." (Per chi usa R è come lanciare `source()` su un ambiente pulito.)

**Demo live**
- Esegui `2 + 3`, poi la cella con `print`: fai notare che si vede solo l'**ultima** espressione (`42`) più i `print`.
- Variabile fantasma: scrivi `x = 5` in una cella nuova, eseguila, cancella la cella, poi scrivi `print(x)` e funziona. Ora *Kernel → Restart* e `print(x)` dà `NameError`. È il primo traceback della settimana: indica solo l'ultima riga, i dettagli sono per oggi pomeriggio.
- "Prova tu" (2'): i tasti `B` e `M` funzionano solo in **modalità comando** (bordo blu, prima si preme `Esc`). In modalità modifica scrivono la lettera nella cella: è il primo intoppo di molti.

### §2 Variabili e tipi, f-string
**Cosa dire**
- "Una variabile è un nome attaccato a un valore. Come la cella B3 di Excel, ma il nome lo scegliete voi."
- "Il decimale si scrive con il punto: `25.4`, non `25,4`." (Con `25,4` Python crea una tupla e non dà errore. Mostralo.)
- "Gran parte degli errori di oggi è un problema di tipo: un numero che in realtà è testo."
- R: `conc = 25.4` è il `conc <- 25.4` di R. `type()` è il `class()` di R.

**Demo live**
- `print(conc_testo * 2)` dà `25.425.4`: nessun errore, ma un risultato sbagliato. È il caso più subdolo.
- Aggiungi una riga: `"25.4" + 2` dà `TypeError: can only concatenate str (not "int") to str`. Leggi solo l'ultima riga.
- `int(3.99)` dà `3`: tronca, non arrotonda.
- f-string: cambia `.3f` in `.1f` e poi in `.3g` dal vivo e fai vedere come cambia il risultato.

**Esercizi**
- **1.1** (livello 1). Output atteso: `Cu: 25.4 µg/L = 399.7 nmol/L`.
  - Errore tipico: formato `{conc_nM:.1}` (senza `f`) che stampa `4e+02`. Suggerimento: "Il formato per i decimali ha una lettera dopo il numero: guardate la cella sopra."
  - Errore tipico: `/ 63.55` scritto a mano invece della variabile. Funziona, ma chiedi di usare `massa_molare_Cu`.
  - Errore tipico: `* 1000` dimenticato, che dà `0.4`. Suggerimento: "Rileggete la frase sulle unità sopra la cella."
  - Il simbolo `µ` è difficile da digitare: non serve, la stringa è già scritta.

### §3 Liste e tuple
**Cosa dire**
- "Si conta da 0. `misure[0]` è il primo, `misure[-1]` l'ultimo."
- R: "`[1:4]` prende gli indici 1, 2, 3, cioè **tre** elementi. In R `v[1:4]` ne prende quattro. E attenzione: in R `v[-1]` **toglie** il primo, in Python **prende l'ultimo**."
- "`sorted(misure)` fa una copia ordinata; `misure.sort()` ordina la lista sul posto e restituisce `None`."

**Demo live**
- Indica lo schema `indici_lista.png`, poi esegui la cella degli slice riga per riga.
- Errore voluto: `misure[10]` dà `IndexError: list index out of range`.
- Media: "Python base non ha una funzione media: `sum()/len()`. Oggi pomeriggio arriva NumPy."

**Esercizi**
- **1.2** (livello 2, senza `#>`: si parte da zero). Output: `n = 8, media = 4.079 µA`, poi la lista ordinata di 7 valori, poi `media senza anomalo = 3.261 µA`.
  - Errore tipico: `correnti.sort()[:7]` dà `TypeError: 'NoneType' object is not subscriptable`. Suggerimento: "Cosa restituisce `.sort()`? Provate `print(correnti.sort())`."
  - Errore tipico: `[:6]` oppure `[1:8]` (si toglie il più piccolo invece del più grande). Suggerimento: "Stampate la lista ordinata: l'anomalo è all'inizio o alla fine?"
  - Errore tipico: `correnti.remove(9.80)` funziona, ma modifica la lista originale; se la cella viene eseguita due volte dà `ValueError: list.remove(x): x not in list`. È un buon esempio del tranello dell'ordine di esecuzione.

### §4 Dizionari
**Cosa dire**
- "Chiave → valore. Come i metadati in testa a un file di strumento: oggi pomeriggio ne leggiamo uno vero."
- R: "Un dizionario somiglia a `list(a = 1, b = 2)` di R."
- "Una chiave che non esiste dà `KeyError`; `.get(chiave, riserva)` evita l'errore."

**Demo live**: esegui `metadati["temperatura"]` per mostrare `KeyError: 'temperatura'`, poi la versione con `.get`.

### §5 `for` e `if` (prime tre celle), poi Esercizio 1.3
**Cosa dire**
- "Il `for` di Python è il `for` di R senza parentesi graffe: il blocco lo decide il rientro di 4 spazi, e la riga finisce con i due punti. Per chi viene da Excel, è il trascinare una formula."
- "In Python l'indentazione **è** la sintassi: decide cosa sta dentro il ciclo." Per chi usa R e per chi conosce Perl/PHP: "Niente graffe."

**Demo live**: togli i `:` dal `for` e leggi il `SyntaxError: expected ':'`. Poi togli l'indentazione da `print(c)` e leggi l'`IndentationError: expected an indented block after 'for' statement on line ...`.

**Esercizi**
- **1.3** (livello 1). Output: `{'foglia': 3, 'suolo': 2, 'frutto': 1}`.
  - Errore tipico: riempire con `m` invece di `1`, che dà `TypeError: can only concatenate str (not "int") to str` oppure conteggi strani. Suggerimento: "Cosa state contando? Di quanto cresce il contatore ogni volta?"
  - Errore tipico: eseguire la cella due volte non raddoppia, perché `conteggi = {}` è nella stessa cella. Se qualcuno sposta `conteggi = {}` in un'altra cella, al secondo run i conteggi raddoppiano: è il tranello dell'ordine di esecuzione.
  - Frase da dire: "Domani questo sarà `value_counts()`. Oggi lo fate a mano una volta, così domani sapete cosa fa."

### §5 Confronti, `range`, `enumerate`, `zip`
**Cosa dire**
- "`=` assegna, `==` confronta. È l'errore più comune in assoluto."
- "`20 < T < 25` è legale in Python."
- "`zip` scorre due liste in parallelo, per esempio concentrazione e segnale."

**Demo live**: `if analita = "Cu":` dà `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`. Fai notare che Python 3.12 suggerisce la correzione.

**Esercizi**
- **1.4** (livello 2, senza scaffold). Output: `media = 3.261 ± 0.069 µA`.
  - Errore tipico: `somma = 0` dentro il ciclo (si azzera a ogni giro). Suggerimento: "Stampate `somma` a ogni giro del ciclo."
  - Errore tipico: dividere per `n` invece che per `n-1`, che dà `0.064`. Suggerimento: "Rileggete la formula: sotto c'è *n−1*."
  - **Trappola seria**: chiamare una variabile `sum = 0`. Poi `sum(...)` dà `TypeError: 'int' object is not callable`, anche nelle celle successive. Rimedio: `del sum` oppure Kernel → Restart. Il messaggio: "non usate come nomi le funzioni di Python: `sum`, `max`, `list`, `type`."
  - `math.sqrt` senza `import math` dà `NameError: name 'math' is not defined`. Suggerimento: "Il testo sopra la cella dice due modi per fare la radice."

### §6 List comprehension ed Esercizio 1.5
**Cosa dire**
- "Non è obbligatoria. Serve a leggere codice scritto da altri. Le due forme fanno la stessa cosa."
- R: "Somiglia a `sapply(v, function(x) x^2)`, o semplicemente a `v^2` in R. Ma in Python base le liste non sono vettorizzate: `[1,2,3] * 2` **ripete** la lista. Oggi pomeriggio NumPy risolve."

**Esercizi**
- **1.5** (livello 1). Output: `[500.0, 1000.0, 2000.0, 5000.0, 10000.0]`.
  - Errore tipico: `[conc_uM * 1000 for c in conc_uM]` stampa una lista enorme (la lista ripetuta 1000 volte, per 5 volte). Suggerimento: "Dentro le parentesi, quale nome indica *un* valore alla volta?"

### Riepilogo della mattina
- Scorri la tabella Excel / R / Python e leggi le quattro "Trappole per chi viene da R". La più importante da dimostrare: `b = a`, poi `b.append(99)`, poi `print(a)`: anche `a` è cambiata. Per una copia: `b = a.copy()`.
- I tre errori della settimana: `=` invece di `==`, `:` o indentazione mancanti, numero che in realtà è stringa.

## 3. Se sei in ritardo (mattina)
Nel notebook della mattina non ci sono blocchi marcati *Facoltativo*. Gli esercizi C1.1 e C1.2 sono già "per casa". Taglia in quest'ordine:
1. Esercizio 1.5: fallo tu dal vivo in 1 minuto.
2. Tuple (§3): basta una frase, "le rivedete oggi pomeriggio con `mu, s, n = statistiche(...)`".
3. Esercizio 1.3: fallo insieme a voce.
4. Esercizio 1.4: dai 10 minuti invece di 20 e mostra la soluzione. Nel pomeriggio `dev_std` e `np.std(ddof=1)` riprendono lo stesso concetto.
5. Non tagliare: §1 (ordine di esecuzione) e §2 (tipi). Il pomeriggio li dà per scontati.

## 4. Domande probabili (mattina)
- **"Perché da 0?"** "È una convenzione di molti linguaggi: l'indice è la distanza dall'inizio. Ci si abitua in un giorno, e per una settimana sbaglierete tutti."
- **"Posso usare R e Python insieme?"** "Sì: con CSV, oppure `reticulate` da R e `rpy2` da Python. Nel corso non sono installati: l'ambiente è uguale per tutti."
- **"Perché `round(2.5)` dà 2?"** "Arrotonda al pari (banker's rounding), come fa anche R."
- **"Jupyter o RStudio?"** "JupyterLab è il nostro RStudio per questi 4 giorni. Esistono altri editor, ma restiamo qui."
- **(Perl/PHP) "Niente `$`, niente `;`?"** "No. I blocchi li decide l'indentazione; il dizionario è l'hash di Perl / l'array associativo di PHP."
- **(Genetica, grandi dati) "Python è lento con milioni di righe?"** "I cicli `for` sì. NumPy e pandas, che vediamo da oggi pomeriggio, lavorano in C sotto il cofano. La bioinformatica specifica è fuori scope, ma poggia su queste basi."
- **"E gli assistenti AI?"** Rispondi come dice la tabella "Cosa NON faremo": "Prima bisogna saper leggere e verificare il codice; ne riparliamo alla fine."
- **Dominio: "Che massa molare uso per il piombo?" / "Cos'è un recupero?"** I valori sono nel notebook (Pb 207.2, Cd 112.4 nel pomeriggio). Per il recupero (C1.1): "Si aggiunge una quantità nota e si vede quanto se ne ritrova. Per la chimica analitica fidatevi più dei colleghi in aula che di me."

## 5. Punti delicati (mattina)
- `B`/`M` in modalità modifica (vedi §1).
- Il simbolo `µ` sulle tastiere: non va digitato, è già nelle stringhe.
- `25,4` con la virgola non dà errore (crea una tupla): se uno studente ha un risultato strano, controlla questo.
- Variabili ridefinite: `correnti` viene definita nell'esercizio 1.2 e ridefinita all'inizio del §5. Se qualcuno salta celle, gli output non coincidono. Rimedio: "Restart and Run All".

---

# POMERIGGIO (14:00–17:00): Funzioni, errori, file e NumPy

## 1. Scaletta

| orario | sezione del notebook | modalità | min |
|---|---|---|---|
| 14:00 | §0 Cella di avvio + §1 Funzioni (default, più valori di ritorno) | demo live | 20 |
| 14:20 | Esercizio 2.1 | esercizio | 10 |
| 14:30 | §2 Import e librerie | demo live | 8 |
| 14:38 | §3 Traceback, i 6 errori, `try`/`except` | demo live | 15 |
| 14:53 | Esercizio 2.2 Caccia al bug | esercizio | 20 |
| 15:13 | §4 `pathlib`, `read_text`, metodi delle stringhe | demo live | 15 |
| 15:28 | Pausa | | 15 |
| 15:43 | `leggi_dpv`: spieghi tu la versione pronta (Esercizio 2.3 per casa) | demo live | 7 |
| 15:50 | §5 NumPy: array, `loadtxt`, primo grafico, maschere, NaN | demo live | 25 |
| 16:15 | §6 Picco netto | demo live | 8 |
| 16:23 | Esercizio 2.4 | esercizio | 22 |
| 16:45 | Grafico di controllo sulla tabella + Riepilogo del giorno 1 | demo live | 10 |
| 16:55 | Margine | | 5 |

## 2. Sezioni

### §1 Funzioni
**Cosa dire**
- "Stamattina avete scritto la media con un ciclo. Se vi serve dieci volte, la chiudete in una funzione."
- "Senza `return`, la funzione restituisce `None`: è l'errore numero uno con le funzioni."
- R: "`def media(valori):` è il `media <- function(valori) {...}` di R. Una differenza: in R l'ultima espressione viene restituita da sola, in Python serve `return`."
- "Una docstring e un piccolo test (`media([1, 2, 3])` deve dare `2.0`) rendono il codice verificabile, anche quando l'ha scritto qualcun altro."

**Demo live**
- Togli il `return` da `media` e riesegui: `print(media([1,2,3]))` stampa `None`, e la cella `dev_std` fallisce con `TypeError: unsupported operand type(s) for -: 'float' and 'NoneType'`. Rimetti il `return`.
- `ug_L_a_nM(massa_molare=112.4, conc_ug_L=1.5)`: argomenti per nome in qualsiasi ordine, come in R.

**Esercizi**
- **2.1** (livello 2: lo studente trova solo i commenti, lo scheletro va scritto). Output: `96.4`.
  - Errore tipico: `print` dentro la funzione invece di `return`. Stampa `96.4` e poi `None`. Suggerimento: "Cosa vedete se scrivete `x = recupero_percentuale(48.2, 50)` e poi `print(x)`?"
  - Errore tipico: argomenti invertiti, che danno `103.73...`. Suggerimento: "Rileggete la definizione: chi sta sopra la frazione?"
  - Errore tipico: dimenticare i `:` dopo `def ...)`, che dà `SyntaxError: expected ':'`.

### §2 Import e librerie
**Cosa dire**
- "`import numpy as np`: gli alias `np`, `pd`, `plt` li usano tutti, non cambiateli. È il `library()` di R, ma in Python si scrive il prefisso: `np.mean`, non solo `mean`."
- "Per sapere cosa fa una funzione: `np.mean?` oppure Shift+Tab. Non serve memorizzare."
- R: "`np.std` divide per *n*; `sd()` di R divide per *n−1*. Per avere lo stesso risultato di R serve `ddof=1`. Ve lo ritroverete."

**Demo live**: `np.mean?`. Poi confronta `np.std(correnti)` con `np.std(correnti, ddof=1)` e fai vedere che i due numeri sono diversi.

### §3 Traceback e `try`/`except`
**Cosa dire**
- "Saper leggere un errore è ciò che vi rende autonomi. Si legge **dal basso**: tipo di errore, messaggio, poi la riga con la freccia."
- Indica lo schema `traceback.png` e la tabella dei 6 errori.
- "`try`/`except` solo per errori che sapete spiegare, e sempre con il tipo preciso (`ValueError`). Un `except:` generico nasconde i bug veri."

**Demo live**
- Esegui la cella `valori[0] + 1` (cella marcata raises-exception). Leggi ad alta voce: `TypeError: can only concatenate str (not "int") to str`. Poi la freccia, poi la domanda: "Che tipo ha davvero `valori[0]`?"
- Cella `try`: fai notare che `"4,1"` (virgola decimale) **non** è un numero per Python. È il gancio per il CSV "italiano" di domani.

**Esercizi**
- **2.2** (5 bug). Insisti: "**Prima** leggete l'ultima riga dell'errore, **poi** guardate il codice."
  - BUG 1: `SyntaxError: expected ':'`. L'output corretto contiene `295.84999999999997`: prepara la risposta (vedi Domande).
  - BUG 2: `TypeError: can't multiply sequence by non-int of type 'float'`. Suggerimento: "Che tipo ha `conc`?" Va bene sia `float("12.5")` sia `12.5` scritto senza virgolette.
  - BUG 3: `IndexError: list index out of range`. Suggerimento: "Quanti elementi ha la lista, e da dove si comincia a contare?"
  - BUG 4: `NameError: name 'media_lsta' is not defined` (a seconda della versione di IPython può comparire anche `Did you mean: 'media_lista'?`). Suggerimento: "Confrontate lettera per lettera il nome definito e quello chiamato."
  - BUG 5: `KeyError: 'Campione'`. Le chiavi distinguono maiuscole e minuscole.
  - Chi finisce presto: "Rompete voi una cella che funziona e fate indovinare l'errore al vicino."

### §4 `pathlib` e lettura di file
**Cosa dire**
- "`FileNotFoundError` quasi sempre vuol dire che state cercando **nel posto sbagliato**, non che il file manchi. `Path.cwd()` vi dice dove siete."
- "I percorsi si compongono con `/`, che funziona uguale su Windows e Mac." R: è il `file.path()` di R.
- "Un file di strumento ha un header di metadati, una riga vuota, un'intestazione di colonna e i dati separati da tabulazione."
- Spiega il dominio in una frase, come fa il notebook: "Ogni file è una curva x-y: corrente in funzione del potenziale, con un picco sopra un fondo. Il picco cresce con la concentrazione. È lo stesso schema di uno spettro o di un cromatogramma."

**Demo live**
- `Path.cwd()`: da JupyterLab locale è la cartella `studenti/`; su Colab è `/content`. Fallo vedere, perché è la ragione per cui i percorsi "funzionano da me e non da te".
- Nella cella `repr(r)` indica `\t` nelle righe dei dati e la riga vuota `''`.
- Errore voluto: `Path("DPV_S01.txt").read_text()` dà `FileNotFoundError`, perché il file sta in `DATI / "strumento"`.
- Box "E `with open`?": leggilo in 30 secondi. "Lo incontrerete nel codice degli altri; noi usiamo `read_text`."

### Esercizio 2.3 (facoltativo): `leggi_dpv`
- **Nella scaletta 10–13/14–17 è per casa**: mostra tu la versione pronta (la cella prima dell'esercizio 2.4) e spiegala in 7 minuti. Di' una frase su `elif` ("altrimenti, se") e `continue` ("salta al giro successivo"): compaiono qui per la prima volta. Quanto segue vale se decidi di farlo fare in aula (conta 25', non 15').
- Livello 2. Lo studente trova lo scheletro della funzione con i commenti-guida. Chi lo salta ha la versione pronta prima di 2.4. Output: il dizionario dei metadati, `161 punti; primo: -0.6 0.8094 ; ultimo: 0.2 1.0901`, `corrente massima: 1.3289`.
- Errori tipici:
  - Non saltare `E(V)\ti(uA)` dà `ValueError: could not convert string to float: 'E(V)'`.
  - Non saltare la riga vuota dà `ValueError: not enough values to unpack (expected 2, got 1)`.
  - **Usare `i` come contatore** (`for i, riga in enumerate(...)`) sovrascrive la lista delle correnti `i`, e poi arriva `AttributeError: 'int' object has no attribute 'append'`. Suggerimento: "Quante cose diverse si chiamano `i` nella vostra funzione?"
  - Chiamare `leggi_dpv("DPV_S01.txt")` con una stringa dà `AttributeError: 'str' object has no attribute 'read_text'`. Bisogna passare un `Path` (`file`).
  - Codice scritto fuori dal corpo (non indentato) dopo i commenti: `return` restituisce liste vuote e compare il messaggio "E è vuota".
- Suggerimento generale: "Prima fate solo il `for` con `print(repr(riga))`, poi aggiungete un ramo alla volta."

### §5 NumPy
**Cosa dire**
- "Una lista può contenere di tutto, quindi è scomoda per la matematica: `[1,2,3]*2` ripete la lista. Un array contiene numeri dello stesso tipo e le operazioni valgono per tutti gli elementi insieme."
- R: "Un array NumPy è il vettore numerico di R: `a * 2` funziona come in R. `NaN` è il vostro `NA`; `np.nanmean` è `mean(x, na.rm = TRUE)`."
- "Prima di qualsiasi calcolo si guarda il dato." È il messaggio chiave del primo grafico.
- `fig, ax = plt.subplots()`, poi si disegna su `ax`: "È la forma che useremo sempre; il giorno 3 la portiamo a livello rivista."

**Demo live**
- **Cella `np.loadtxt(..., skiprows=9)`: dì ad alta voce "eseguitela tutti, anche chi ha fatto 2.3".** Altrimenti `E` e `i` restano liste e `i.min()` dà `AttributeError: 'list' object has no attribute 'min'`.
- Primo grafico: indica la gobba vicino a −0.2 V e il fondo che **sale** verso destra. Ti serve per il box del §6.
- Maschere: fai l'errore che faranno gli utenti R/Excel, `(E > -0.35) and (E < -0.10)`, che dà `ValueError: The truth value of an array with more than one element is ambiguous...`. Correzione: `&`. Poi togli le parentesi, `E > -0.35 & E < -0.10`, ed esce `TypeError: ufunc 'bitwise_and' not supported...` (`&` ha la precedenza sul confronto). Messaggio: "Con gli array: `&`, `|`, `~`, e sempre le parentesi attorno a ogni confronto."
- NaN: `v.mean()` dà `nan`, `np.nanmean(v)` dà il numero.
- "Creare array" (`arange`/`linspace`): basta eseguirla, senza commento.

### §6 Picco netto ed Esercizio 2.4
**Cosa dire**
- "Picco netto = massimo meno fondo. Il fondo è la media della corrente lontano dal picco, per E < −0.45 V: una maschera e una media."
- Box sulla semplificazione: "Il fondo sale, quindi questo metodo sovrastima ogni picco di circa 0.12–0.13 µA. È un errore costante: pesa sui picchi piccoli e finisce nell'intercetta della retta di taratura, non nella pendenza. Chi vuole fa il metodo con la retta nell'estensione 3."
- "Dodici file, un ciclo, una tabella. In R lo fareste con `list.files()` e `lapply()`: qui vediamo come si scrive in Python."

**Esercizi**
- **2.4** (livello 2, con `____`). Prima di partire: "Chi ha saltato 2.3 esegua la cella con `leggi_dpv` pronta (eseguirla non fa danni a nessuno)." Output: 12 righe da `S01,tampone,0.5,-0.225,0.499` a `S12,estratto foglia,50,-0.225,21.147`.
  - Eseguire con i `____` ancora dentro dà `NameError: name '____' is not defined`: è un nome valido per Python. Dillo prima.
  - Glob `"DPV_S*.txt"` invece di `"DPV_S??.txt"`: entra il file malformato e arriva `ValueError: could not convert string to float: '-0,600'`. Suggerimento: "Da quale file viene l'errore? Stampate `f` all'inizio del ciclo." È un buon momento per rileggere il traceback.
  - Copiare `−0.45` dal testo markdown dà `SyntaxError: invalid character '−' (U+2212)`, perché il testo usa il segno meno tipografico. Suggerimento: "Riscrivete il meno a mano."
  - Ultimo blank: usare `i_picco` (variabile della cella sopra, calcolata su S01) dà **tutte le righe a 0.499**. Nessun errore, risultato sbagliato. Suggerimento: "Il numero cambia da un campione all'altro? Cosa avete dentro `k` e `fondo`?" La risposta attesa è `i[k] - fondo`.
  - Convertire la concentrazione con `float(...)` dà `TypeError: sequence item 2: expected str instance, float found` nel `join`.
  - Se la `leggi_dpv` dello studente (2.3) è incompleta, le liste sono vuote: `RuntimeWarning: Mean of empty slice` e poi `ValueError: attempt to get argmax of an empty sequence`. Rimedio: eseguire la cella con la versione pronta.
- Estensioni per chi finisce presto, in ordine di difficoltà: 2 (grafico sovrapposto con legenda), 1 (file malformato), 3 (fondo con una retta; controllo: S01 0.380, S08 42.118). Sull'estensione 1: il file malformato dichiara `Campione: S03`, quindi S03 compare due volte. È voluto: è il gancio per i duplicati di domani.

### Grafico di controllo e Riepilogo
**Cosa dire**
- "La risposta è lineare? Il grafico lo dice in un secondo." I punti dell'estratto di foglia stanno sulla stessa retta del tampone.
- "Domani apriamo `riassunto_dpv.csv` con pandas in una riga." Se qualcuno non ha il file, il notebook 03 lo ricostruisce da solo: rassicurali.
- Riepilogo: funzione, traceback dal basso, `Path` + `glob` + `read_text`, array e maschere, `fig, ax`.
- Ricorda: "Stasera fate Restart and Run All sui due notebook: se arrivano in fondo, sono riproducibili."

## 3. Se sei in ritardo (pomeriggio)
Taglia in quest'ordine:
1. **Esercizio 2.3**: è marcato *Facoltativo: si può saltare se si è in ritardo*. Fai eseguire la cella con `leggi_dpv` pronta prima di 2.4, e mostra tu la funzione spiegandola in 2 minuti.
2. Box "E `with open`?" e cella "Creare array": una frase ciascuno.
3. Cella NaN: una frase ("domani pandas lo gestisce meglio").
4. Caccia al bug: fai fare BUG 1, 2 e 4 e mostra tu 3 e 5.
5. Grafico di controllo finale: lo esegui tu.
- **Non tagliare**: la cella `np.loadtxt` (le celle seguenti ne hanno bisogno), la cella `leggi_dpv` pronta e l'esercizio 2.4 (è l'obiettivo dichiarato del giorno). Se il tempo manca davvero, fai 2.4 insieme riempiendo i blank dal vivo.

## 4. Domande probabili (pomeriggio)
- **"Perché `295.84999999999997`?"** (BUG 1) "I decimali in binario non sono esatti, succede in tutti i linguaggi, R compreso. Si risolve nella stampa con `:.2f`."
- **"Che differenza c'è tra lista e array?"** "La lista può contenere di tutto, l'array solo numeri dello stesso tipo, e su un array la matematica si applica a tutti gli elementi."
- **"Perché `np.std` dà un numero diverso da R?"** "`ddof`: NumPy divide per *n*, R per *n−1*."
- **"Perché `skiprows=9`?"** "Sono le 7 righe di header, la riga vuota e l'intestazione. Contatele nell'output `repr`."
- **"Come leggo un file Excel o un CSV vero?"** "Domani, con pandas."
- **"Posso scaricare i dati da un'API/database?"** "Sì: domani pomeriggio c'è un esempio con l'API di UniProt."
- **Dominio, da gestire con onestà.** Frase pronta: *"Non sono un elettrochimico: per il corso questo file è una curva x-y con un picco sopra un fondo. Se qualcuno di voi lavora con queste tecniche, ci aiuta a capire se la semplificazione regge."*
  - "Cos'è la DPV / PalmSens4 / SPCE?" Per la lezione basta questo: voltammetria a impulsi differenziali, un potenziostato portatile, un elettrodo serigrafato. Non andare oltre.
  - "Perché il picco è a −0.22 V?" / "Perché il fondo sale?" / "Che analita è?" Non improvvisare spiegazioni fisiche. I dati sono **sintetici** (README): "sono generati per avere la forma tipica; i dettagli fisici non sono modellati."
  - "L'estratto di foglia dà un effetto matrice?" Le correnti di S09–S12 sono simili a quelle del tampone alle stesse concentrazioni (es. 20 µM: 8.648 contro 8.760). "Nei dati sintetici l'effetto è piccolo; come si valuta davvero è materia vostra."
  - "Il fondo andrebbe tolto con una retta o un polinomio?" "Sì, il notebook lo dice: è l'estensione 3. Il metodo con la media è una semplificazione dichiarata."

## 5. Punti delicati / trappole (pomeriggio)
- **Cartella di lavoro**: `riassunto_dpv.csv` viene scritto in `Path.cwd()`: `studenti/` in locale, `/content` su Colab. Il notebook 03 lo cerca nella cartella corrente e, se non lo trova, lo ricostruisce. Nessun blocco, ma qualcuno non troverà "il suo" file.
- **Colab**: il notebook va caricato con *File → Carica notebook*. Se lo zip non è stato scompattato in `/content`, la cella di avvio dà `FileNotFoundError: Cartella 'dati' non trovata`. Su Colab `pd.__version__` (§2) stampa 2.x: è normale.
- **Ordine di esecuzione**: se uno studente riesegue la cella 2.3 *dopo* `np.loadtxt`, `E` e `i` tornano liste e `i.min()` fallisce. Rimedio: rieseguire la cella `loadtxt`.
- **Nomi riusati**: `i`, `E`, `meta`, `file`, `misure`, `metadati` vengono ridefiniti più volte. Dopo il ciclo 2.4, `E` e `i` sono quelli di S12.
- **Il segno meno tipografico `−`** nel markdown del notebook 02 è stato sostituito con `-` (14/11). Se qualcuno lo copia da altre fonti: `SyntaxError: invalid character '−' (U+2212)`.
- **Windows**: `read_text`/`write_text` hanno `encoding="utf-8"` esplicito, quindi non ci sono problemi. Se qualcuno scrive il proprio codice senza encoding e mette `µ` nel CSV, su Windows può comparire testo illeggibile. Dì: "indicate sempre l'encoding".
- `np.loadtxt(file, skiprows=9)` funziona per S01–S12 (header di 7 righe). Il file S13 ha 6 righe di header (manca "Scan rate"), ma il notebook non lo legge mai con `loadtxt`.

---

## Da verificare prima del corso
1. *(Risolto il 14/11.)* L'esercizio 1.3 è stato spostato nel §5, dopo le prime tre celle su `for` e `if`.
2. *(Risolto il 14/11.)* Le soglie nel testo del notebook 02 ora usano il trattino normale `-`: copiarle nel codice non dà più `SyntaxError`.
3. **`sorgenti/02_G1_pomeriggio_funzioni_file_numpy.py:473`**: "circa 0.13 µA" come sovrastima costante. Dall'estensione 3 risulta 0.119 per S01 e 0.134 per S08. Va bene come "circa", ma se qualcuno fa il conto, ti conviene dire "0.12–0.13".
4. **Zip dei partecipanti (`dist/corso_python_CNR_partecipanti.zip`)**: contiene la cartella `corso_python_CNR/`. Le istruzioni chiedono di scompattarlo "nello stesso posto" della cartella di installazione, ma su Windows "Estrai tutto" propone una sottocartella. Prepara una frase precisa da dire o da scrivere alla lavagna (es. "estraete in Documenti, non in Documenti\corso_python_CNR_partecipanti").
5. Fai girare su Colab, almeno una volta, i due notebook `studenti/` del giorno 1 con lo zip dei partecipanti, per controllare che la cella di avvio trovi `corso_python_CNR/dati` dopo `!unzip`.


---

## Giorno 2 — Pandas: dal file grezzo alla tabella pulita, aggregata e documentata

Notebook: `studenti/03_G2_mattina_pandas_essenziale.ipynb` (mattina), `studenti/04_G2_pomeriggio_pandas_avanzato_progetto.ipynb` (pomeriggio). Tu proietti la versione **studenti** e tieni aperta la `docente/` solo sul tuo schermo.

### Apertura del giorno (5')
- **Ieri**: tipi, liste, dizionari, cicli; poi funzioni, traceback, `pathlib`, lettura dei file DPV, array NumPy con maschere e NaN, e il ciclo sulla cartella che ha scritto `riassunto_dpv.csv` "a mano", riga per riga.
- **Oggi**: lo stesso lavoro con pandas in una riga, e poi tutto il resto: leggere un CSV "italiano" sporco, filtrare, creare colonne, pulire, raggruppare, unire tabelle.
- **Obiettivo di fine giornata**: una cella che parte dal file grezzo e produce tabella pulita, riassunto e un report di cosa è stato scartato e perché. Scritto, ripetibile, verificabile.

---

## MATTINA — `03_G2_mattina_pandas_essenziale` (10:00–13:00)

Il notebook non indica tempi per sezione: la scaletta qui sotto è costruita sull'orario 10:00–13:00. Rispetto alla versione su 9:00–12:30: l'esercizio 3.3 è per casa, §5 e §7 sono accorciati, e nella lunga parte di demo iniziale ci sono due momenti in cui lavora la sala (la prova su `decimal` e la previsione su `alto.loc[0]`).

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 10:00–10:20 | Apertura + §0 cella di avvio, §1 DataFrame e Series, §2 il file di ieri | spiego + demo live | 20 |
| 10:20–10:45 | §3 `read_csv` sul CSV sporco (errore vero → parametri) + **prova loro**: togliere `decimal=","` e rifare `info()` | demo live + prova | 25 |
| 10:45–11:03 | §4 ispezione (shape/info/describe/value_counts), rename, date | demo live | 18 |
| 11:03–11:08 | §5 `read_excel` e scrittura (solo `index=False`) | demo live | 5 |
| 11:08–11:23 | §6 selezione: `[]`, filtri booleani | spiego + demo live | 15 |
| 11:23–11:38 | Pausa | | 15 |
| 11:38–11:45 | §6 `loc`/`iloc` dopo un filtro (**prevedi, poi esegui**: `alto.loc[0]`) | demo live | 7 |
| 11:45–11:58 | Esercizio 3.1 | esercizio | 13 |
| 11:58–12:18 | §7 colonne derivate, `map`, `.str`, `pd.cut`, `np.where` (senza `apply`) | demo live | 20 |
| 12:18–12:38 | Esercizio 3.2 | esercizio | 20 |
| 12:38–12:45 | Correzione + grafico di controllo | demo live | 7 |
| 12:45–12:55 | Riepilogo + trappole per chi viene da R; Esercizio 3.3 assegnato per casa | spiego | 10 |
| 12:55–13:00 | Margine | | 5 |

### 2. Sezioni

**§0 Cella di avvio**
- Cosa dire: "Eseguite la prima cella: deve stampare `pandas 3.` qualcosa. Chi è su Colab vedrà `2.`: va bene, cambiano solo alcune etichette."
- Demo: esegui e indica la riga `pandas 3.0.5`. Controlla con un giro d'occhi che nessuno abbia `FileNotFoundError` (vuol dire notebook aperto fuori dalla cartella del corso).

**§1 DataFrame e Series**
- Cosa dire:
  - "Un DataFrame è un foglio Excel fatto bene: una riga per osservazione, una colonna per variabile, e ogni colonna ha **un solo tipo**."
  - "Per chi usa R: è un `data.frame`/`tibble`. La differenza grossa è l'**index**, l'etichetta di riga: in R non c'è, qui sì, e ci tornerà fra un'ora."
  - "Una colonna è una Series: si comporta come un array NumPy di ieri."
- Demo live: `df.dtypes` → indica `str` per il testo e `float64` per i numeri. `df["conc_ug_L"] * 2`: "l'indice 0..3 è rimasto attaccato".

**§2 Il file di ieri**
- Cosa dire: "Ieri vi sono servite 15 righe per scrivere questo CSV. Oggi si rilegge con una riga sola."
- Demo: la cella usa il vostro `riassunto_dpv.csv` se è nella cartella corrente, altrimenti lo ricostruisce. Se a qualcuno esce una tabella strana (intestazione mancante, colonne sbagliate), è il suo file di ieri: cancellatelo e rieseguite.

**§3 `read_csv` su dati sporchi (il cuore della mattina)**
- Cosa dire:
  - "Regola numero uno: **prima di leggere un file, guardatelo come testo**. 30 secondi che fanno risparmiare mezz'ora."
  - "Questo file ha i difetti di un export italiano da Windows: `;`, virgola decimale, latin-1, commenti in testa, `n.d.`, date gg/mm/aaaa."
  - "Il messaggio d'errore sembra criptico, ma dice esattamente cosa è successo: leggiamolo insieme."
  - R: "È come `read.csv2()` / `readr::read_csv2()` con `locale(encoding = "latin1")`: in pandas ogni difetto ha il suo parametro."
- Demo live:
  1. Cella con `repr(r)`: indica `;`, `22,06`, le 3 righe `#`, la riga d'intestazione con `µ` e `°`.
  2. Tentativo ingenuo → `ParserError ... Expected 1 fields in line 5, saw 3`. Spiega: righe 1-4 senza virgole (1 campo), riga 5 con due virgole decimali (3 campi).
  3. Tabella problema → parametro, poi lettura corretta.
  4. **Fuori copione, molto efficace**: togli `encoding="latin-1"` dal vivo → `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5` ("0xb5 è il `µ` in latin-1"). Togli `comment="#"` → `ParserError: Expected 2 fields in line 4, saw 8`.

**§4 Ispezione, rename, date**
- Cosa dire:
  - "Quattro domande a ogni tabella: quanto è grande, che tipi e quanti mancanti, che numeri, che categorie."
  - "Una colonna numerica che compare come `str` (o `object` su Colab) è un campanello d'allarme: c'è qualcosa di sporco nel file."
  - R: "`info()` è `str()`, `describe()` è `summary()`, `value_counts()` è `table()`."
- Demo live:
  - `df.info()`: 311 righe, `concentrazione` 301 non-null (10 mancanti), `T (°C)` 307 (4 mancanti), `data` è `str`.
  - Cella `sbagliato` senza `decimal=","`: concentrazione e T diventano `str`.
  - `describe()`: indica **max 952.65** contro mediana 7.17 → "qui c'è qualcosa che non va, lo sistemiamo nel pomeriggio".
  - `value_counts()` su `operatore`: MR, GF, gf, M.R., LB → "tre persone scritte in cinque modi".
  - Dopo `to_datetime`: `data` diventa `datetime64[us]` (su Colab `[ns]`: è lo stesso).
- Consiglio pratico: per scrivere `"concentrazione (µg/L)"` nel `rename` **copiate il nome dall'output di `df.columns`**: `µ` e `°` sono scomodi da digitare, e un nome sbagliato nel `rename` **non dà errore** (la colonna semplicemente non viene rinominata; l'errore arriva dopo, come `KeyError: 'conc_ug_L'`).

**§5 `read_excel` e scrittura**
- Cosa dire: "`index=False` quasi sempre, altrimenti vi ritrovate una colonna senza nome con 0, 1, 2… Per chi riapre in Excel italiano: `sep=";", decimal=","`."
- Demo: `meta.head()`, `meta.info()`: 37 campioni (le misure ne hanno 40: lo useremo nel pomeriggio). Mostra dove sono finiti i 3 file (`Path.cwd()`).

**§6 Selezione**
- Cosa dire:
  - "Cinque modi, da tenere distinti: una colonna, più colonne (lista dentro le quadre: **doppie quadre**), `loc` per etichetta, `iloc` per posizione, maschera booleana."
  - "`loc` include l'estremo destro, `iloc` no."
  - "Finché l'indice è 0, 1, 2… `loc` e `iloc` sembrano uguali. Dopo un filtro no."
  - R/dplyr: `df[maschera]` ≈ `filter()`, `df[["a","b"]]` ≈ `select()`, `.isin()` ≈ `%in%`. "Gli operatori sono `&`, `|`, `~` (in R `&`, `|`, `!`), ma **con le parentesi attorno a ogni condizione**."
- Demo live:
  - `alto = df[df["conc_ug_L"] > 40]` → 34 righe; indica la colonna di sinistra: 1, 3, 7, 32, 45.
  - La cella `alto.iloc[0, 1]` / `alto.loc[1, "campione"]` → stessa riga (C002); `0 in alto.index` → False. Prova dal vivo `alto.loc[0]` → `KeyError: 0`.
  - Pb in suolo → 42; Pb o Cd a febbraio → 109; righe con concentrazione mancante (10).

**Esercizio 3.1 — filtri progressivi (livello 1, ~15')**
- Atteso: `99 22 5`, poi 5 righe con in cima **C010 581.31**.
- Errori tipici:
  - `"cu"` minuscolo o `"Cu "` → 0 righe, nessun errore. Suggerimento: "Guardate i valori esatti con `value_counts()`."
  - `cu[cu["matrice"] == foglia]` senza virgolette → `NameError: name 'foglia' is not defined`.
  - `sort_values(conc_ug_L)` senza virgolette → `NameError`.
- Aggancio: "C010 a 581 µg/L, quando gli altri sono a 30-40: lo teniamo a mente per il pomeriggio."

**§7 Creare e trasformare colonne**
- Cosa dire:
  - "`df["nuova"] = espressione`: è la formula trascinata di Excel, senza il rischio di fermarsi una riga prima. In dplyr è `mutate()`."
  - "`map` con un dizionario: è un `CERCA.VERT` con una tabellina, o `recode()` in R."
  - "`.str` per il testo, `.dt` per le date. `apply` funziona sempre ma è lento; `pd.cut` per le classi a intervalli, `np.where` per il `=SE()` (`ifelse` in R)."
- Demo live:
  - `masse_molari` + `conc_nM`: "da µg/L a nmol/L si divide per la massa molare (g/mol) e si moltiplica per 1000". È aritmetica, non chimica: non serve dire di più.
  - Normalizzazione operatore → MR 146, GF 133, LB 32.
  - `classe_conc` con `apply` vs `pd.cut`: stessi conteggi (130/127/44), ma `apply` dà `"mancante"`, `pd.cut` dà `NaN`.
  - `np.where` e il commento finale: **un confronto con NaN è sempre False**, quindi il NaN finisce nel ramo "falso" in silenzio.

**Esercizio 3.2 — colonne derivate (livello 2, ~20')**
- Atteso: `fuori_limite` False 190 / True 121; per analita Cd 37, Cu 39, Pb 45.
- Errori tipici:
  - `df["analita"].map(limiti)` scritto come `df["limite"].map(...)` → `KeyError: 'limite'`.
  - `df["fuori_limite"] = df["rapporto"] > "1"` → `TypeError` (confronto fra numero e testo).
  - Usano `if df["rapporto"] > 1:` → `ValueError: The truth value of a Series is ambiguous`. Suggerimento: "Il confronto su una colonna intera dà già una colonna di True/False: non serve `if`."
- **Da dire in correzione** (è nel commento della soluzione): i 10 mancanti stanno fra i 190 "False", come se fossero nel limite. In realtà non lo sappiamo: `df["rapporto"].isna().sum()` → 10.
- Il `groupby` alla domanda 4 è un anticipo: se non lo capiscono, va bene, lo rivediamo alle 14.

**Esercizio 3.3 — da zero (livello 3, ~20')**
- Atteso: `37 righe, media 30.6 nM`.
- Chi si blocca: "Copiate la cella di lettura della sezione 3 e la cella del rename, poi aggiungete un filtro alla volta, controllando `len()` dopo ogni passo."
- Errori tipici:
  - Filtro senza parentesi: `pb["analita"] == "Pb" & pb["matrice"] == "frutto"` → `TypeError: Cannot perform 'rand_' with a dtyped [...] array and scalar of type [bool]`. Suggerimento: "Che cosa calcola Python per primo, `==` o `&`?"
  - `and` al posto di `&` → `ValueError: The truth value of a Series is ambiguous`.
  - Dimenticano `.copy()` dopo il filtro: con pandas 3 nessun problema; **su Colab (pandas 2)** compare `SettingWithCopyWarning` quando aggiungono `conc_nM`. Spiega che è un avviso, e che `.copy()` lo toglie.
  - `notna()` dimenticato → **39 righe** invece di 37 (Pb in frutto ha 2 mancanti), con la stessa media perché `mean()` ignora i NaN. Suggerimento: "Il testo dice *non mancante*: quale metodo avete visto per i mancanti?"
- Chi finisce presto: estensione con i 9 file `{analita}_{matrice}.csv`.

**Grafico di controllo + riepilogo (12:38)**
- Demo: scatter Cu nel tempo → "i punti impazziti si vedono subito". `.plot()` di pandas va bene per guardare, per pubblicare c'è domani.
- Trappole per chi viene da R (leggile dalla tabella del notebook):
  - `mean()` di pandas **ignora i NaN in silenzio** (R restituisce `NA` senza `na.rm = TRUE`); NumPy invece dà `nan`, come R.
  - L'indice e l'allineamento.
  - `df[df["analita"] == "Cu"]["conc_ug_L"] = 0` **non modifica `df`**: con pandas 3 compare un avviso `ChainedAssignmentError` che suggerisce `.loc[righe, colonne] = valore`. Mostralo dal vivo: è uno dei pochi avvisi che vale la pena leggere.
- Tre abitudini: guardare il file come testo; `info()` dopo ogni lettura; `to_datetime` con `format` esplicito.

### 3. Se sei in ritardo (mattina), taglia in quest'ordine
1. **Esercizio 3.3** → lo assegni come primo esercizio per casa (è la stessa sequenza del progetto del pomeriggio, quindi non si perde nulla).
2. Estensione di 3.3 e grafico di controllo finale (2 minuti a voce).
3. `apply` vs `pd.cut`: mostra solo `pd.cut`, salta la funzione `classe_conc`.
4. §5 scrittura: esegui la cella senza commento, basta dire "`index=False`".
5. `.dt` (`mese`, `settimana`): un minuto, non serve nel pomeriggio.
- **Non tagliare**: §3 (lettura), `info()`, `loc`/`iloc` dopo il filtro, Esercizio 3.2 (limiti e `map` servono nel progetto).
- C3.1 (`skiprows=3`) è già per casa.

---

## POMERIGGIO — `04_G2_pomeriggio_pandas_avanzato_progetto` (14:00–17:00)

Il notebook indica due tempi: **API UniProt circa 30', facoltativo** e **Progetto 60'**. Con 165' utili il pomeriggio è il più denso del corso. Nella scaletta qui sotto l'API è **solo una demo di 5'**: esegui le celle per mostrare che con Python si scaricano dati da una banca dati e si uniscono ai propri; l'esercizio 4.3 resta per casa. **Se alle 15:22 sei in ritardo, salta anche la demo.** Attenzione: il grafico dopo l'esercizio 4.3 usa `unito_api` e dà `NameError` a chi non ha fatto il 4.3: di' di saltare quella cella.

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 14:00–14:15 | §0 cella di avvio (`carica_misure`) + §1 mancanti: individuare, capire, decidere | spiego + demo live | 15 |
| 14:15–14:32 | §2 duplicati e anomali (IQR per gruppo, sui log) | demo live | 17 |
| 14:32–14:42 | Esercizio 4.1 | esercizio | 10 |
| 14:42–15:00 | §3 `groupby` / `agg` / `transform` | spiego + demo live | 18 |
| 15:00–15:10 | Esercizio 4.2 | esercizio | 10 |
| 15:10–15:22 | §4 `merge` con i metadati | demo live | 12 |
| 15:22–15:27 | API UniProt: **solo demo**, esegui le celle e mostri il risultato (Esercizio 4.3 per casa) | demo live | 5 |
| 15:27–15:42 | Pausa | | 15 |
| 15:42–15:46 | §5 pivot (solo `pivot_table`) | demo live | 4 |
| 15:46–16:46 | §6 Progetto wrangling (lancio 3' + lavoro; checkpoint 16:06 e 16:26) | progetto | 60 |
| 16:46–16:58 | Report di un volontario + chiusura | spiego | 12 |
| 16:58–17:00 | Margine | | 2 |

### 2. Sezioni

**§0 Cella di avvio**
- Cosa dire: "Tutto quello che abbiamo fatto stamattina sul file ora è una funzione, `carica_misure`. È il primo esempio di codice riusabile: lo stesso schema servirà nel progetto."

**§1 Mancanti**
- Cosa dire:
  - "Tre passi, sempre in quest'ordine: contare, capire perché mancano, decidere. Nessuna funzione decide al posto vostro."
  - "**Mai riempire un mancante con 0**: 0 è una misura, mancante no."
  - R: `is.na()`, `drop_na()`, `replace_na()`.
- Demo live: `isna().sum()` → 10 in `conc_ug_L`, 4 in `T_C`, 14 righe con almeno un mancante. Tabella dei mancanti: indica che **quasi tutti sono di MR** (lo riprende 4.1). `dropna(subset=...)` → restano 301. `T_C` riempita con la mediana: "è una scelta, va scritta nel report".

**§2 Duplicati e anomali**
- Cosa dire:
  - "I duplicati esatti sono export ripetuti o copia-incolla: `duplicated()` li marca, `drop_duplicates()` li toglie."
  - "Gli anomali vanno cercati **per gruppo**: un valore normale per il rame è assurdo per il cadmio."
  - "Queste concentrazioni hanno una coda a destra: il box plot lo leggiamo in scala log e la regola IQR la applichiamo **ai logaritmi**, altrimenti marcherebbe come anomali valori alti del tutto normali."
  - "`anomali_iqr` è già pronta: usatela così com'è, la capiremo fra mezz'ora con `transform`."
- Demo live:
  - 6 duplicati (C001 Cu, C002 Pb, C004 Cu…) → restano 295.
  - Box plot in log per analita.
  - `anomali_iqr` (k=1.5) → 8: tre valori sopra 500 µg/L (C006, C008, C010), C026 Pb 73.8, **tre repliche di C038 Pb in suolo** (campione davvero più alto, non un errore) e **C033 Cu in foglia, un valore basso** (l'IQR guarda entrambe le code).
  - Decisione: con k=3 → 4 grossolani, restano 291.
- Messaggio: "La regola automatica propone, voi decidete. E scrivete il criterio nel report."

**Esercizio 4.1 — diagnosi dei mancanti (livello 2, ~10')**
- Atteso: MR 9, GF 1; Cu 4, Pb 4, Cd 2.
- Errori tipici: lavorano su `df` invece di `grezzo` → serie vuota (`Series([], ...)`). Il testo lo avvisa, ma succede lo stesso. Suggerimento: "Su quale tabella ci sono ancora i mancanti?"
- Da dire in correzione: **LB non compare** (zero mancanti, quindi nessuna riga passa il filtro), e 9 su 146 non è 9 su 30. La cella `diagnosi` della sezione 3 risolve entrambe le cose.

**§3 `groupby`**
- Cosa dire:
  - "Dividi, applica, ricombina. Si legge da sinistra a destra: raggruppa per matrice, prendi la concentrazione, fai la media."
  - R/dplyr: "`df.groupby("g")["x"].agg(...)` è `group_by(g) %>% summarise(...)`; `transform` è `group_by() %>% mutate()`. La sintassi `agg(n=("x", "size"))` è la più vicina a `summarise(n = n())`."
  - "Non fate la media di Cu, Pb e Cd insieme: scale diverse di un fattore 20, il numero non vuol dire nulla."
  - "`size` conta le righe, `count` solo i valori presenti: la differenza sono i mancanti."
- Demo live:
  - Cu per matrice (suolo 54.7, foglia 23.6, frutto 12.3).
  - `diagnosi`: LB compare con 0.
  - `agg` con lista, poi `agg` con nomi → indica il **MultiIndex** e poi `reset_index()` ("in R `summarise` restituisce già colonne normali: qui va fatto a mano").
  - `transform("mean")`: una colonna lunga quanto `df`. Torna su `anomali_iqr` e rileggi le due righe `transform`: "ora si capisce".

**Esercizio 4.2 — aggregazioni (livello 1, ~10')**
- Atteso: tabella operatore × analita; matrici foglia 10, frutto 15, suolo 15; in cima C024 Cu 79.89 (n=3).
- Errori tipici:
  - `agg(media="mean", n=size)` senza virgolette → `NameError: name 'size' is not defined`.
  - `.nunique` senza parentesi → stampa `<bound method ...>`.
  - `sort_values("mean")` invece di `"media"` → `KeyError: 'mean'`. Suggerimento: "Come si chiamano le colonne che avete creato voi?"

**§4 `merge`**
- Cosa dire:
  - "È il `CERCA.VERT` senza trappole: si dichiara la chiave, si sceglie `how`. In R: `left_join()`, `inner_join()`."
  - "**Dopo ogni merge contate le righe.** Se aumentano, la chiave non era univoca e avete duplicato dati senza accorgervene."
- Demo live: 37 campioni nei metadati contro 40 nelle misure; `is_unique` True; left → 291 prima e dopo, **25 misure senza sito** (C038, C039, C040); inner → 266. `join` = merge sugli indici, basta citarlo.
- Domanda da fare al pubblico: "25 righe senza sito: le buttiamo o le teniamo?" (risposta del notebook: tenute, sito = NaN, dichiarato nel report).

**API UniProt → JSON → merge (FACOLTATIVO, ~25')**
- Prima di iniziare: **lascia `USA_RETE = False`**. La rete in aula è inaffidabile, la copia `dati/uniprot_esempio.json` dà esattamente gli output attesi. Se vuoi mostrare la chiamata vera, fallo tu dal tuo computer **alla fine**, non durante l'esercizio.
- Cosa dire:
  - "Lo schema è sempre lo stesso, per UniProt, Ensembl o NCBI: la vostra tabella con una chiave, la chiamata, dal JSON a una tabella, merge e i soliti controlli."
  - "Il JSON è fatto dei dizionari e delle liste di ieri, uno dentro l'altro: si scende chiave per chiave, con `[0]` quando si trova una lista."
  - "Tre abitudini: `timeout`, `raise_for_status()`, **salvare la risposta** in un file e scrivere nel metodo la data di accesso."
  - R: `httr2` + `jsonlite`, poi `left_join()`.
- Demo live:
  - Stampa `query`: indica `OR`, `organism_id:9606` (umano), `reviewed:true`. "Una richiesta con dieci geni, non dieci richieste."
  - `11 risultati per 10 geni`: "teniamolo a mente".
  - La discesa su `primo`: `INS`, `P01308`, 110, `Insulin`.
  - `json_normalize`: appiattisce i dizionari ma non le liste (`genes` resta lista) → per questo c'è `estrai`.
- **Esercizio 4.3 (livello 2, ~10')**
  - Atteso: `both 9, right_only 2, left_only 1`; FBF1 e GAPDH right_only, Gapdh left_only; dopo la correzione `righe prima 10, dopo 10; senza dati UniProt: 0`.
  - I due motivi: `Gapdh` vs `GAPDH` (chiave scritta diversamente); FBF1 restituito perché "ALB" è un suo **sinonimo** ("l'API ha risposto alla domanda che le abbiamo fatto, non a quella che avevamo in mente").
  - Errori tipici: `indicator="True"` funziona male (diventa il nome della colonna `"True"` invece di `_merge` → `KeyError: '_merge'`); `.str.upper` senza parentesi → nessun errore: la colonna si riempie di "metodi" e il merge non trova più nessuna corrispondenza.
  - **Trappola della riesecuzione**: la cella modifica `misurati` sul posto. Chi la riesegue vede `both 10, right_only 1` e pensa di aver sbagliato. Suggerimento: "Rieseguite dalla cella che crea `misurati`."
  - Messaggio finale: `how="left"` fa sparire FBF1 senza avvisare; va bene solo perché l'avete visto prima con `outer`. `validate="one_to_one"` è un controllo gratuito (se fallisce: `MergeError: Merge keys are not unique...`).

**§5 Pivot / melt (5')**
- Cosa dire: "Lungo per analizzare, largo per leggere. `pivot_table` = `pivot_wider()`, `melt` = `pivot_longer()`." Aggiungi: "`margins=True` ha senso per i conteggi; una media 'All' che mescola Cd e Cu pandas la calcola lo stesso, tocca a voi non usarla."
- Demo: tabella larga matrice × analita; conteggi con totale 291.

### 3. Progetto data wrangling (60', 15:46–16:46)

**Lancio (primi 2 minuti, da dire così)**
- "Avete tutti i pezzi: ora li mettete in fila, in **una cella**, partendo dal file grezzo. Da soli o in coppia, come preferite."
- "Tre prodotti: `misure_pulite.csv`, `riassunto.csv` per sito × matrice × analita, e il report stampato a video."
- "La configurazione è in alto: `FILE`, `COL_VALORE`, i gruppi, i limiti. Per un altro export basterà cambiare quelle righe."
- "C'è una traccia con i `____`. Chi vuole la sfida cancella la traccia e scrive da zero. Il controllo finale è il report: **311 / 10 / 6 / 4 / 25 / 291**." (Scrivi questi numeri alla lavagna.)

**Girare fra i banchi**
- Primo giro (15:48–15:56): solo per verificare che tutti abbiano **eseguito la cella di avvio e quella di `anomali_iqr`** (sono necessarie; chi ha riavviato il kernel dopo la pausa non ha `carica_misure` né `anomali_iqr` → `NameError`).
- Poi rispondi a chi alza la mano; dai priorità a chi non ha mai programmato. Con chi viene da R chiedi: "Come lo scriveresti in dplyr?" e traduci passo per passo.
- Domanda da fare a chi è bloccato: "Quante righe hai adesso? Quante te ne aspetti?" (stampare `len(d)` dopo ogni passo).

**Errori tipici nel progetto**
- `d = d[not anom]` → `ValueError: The truth value of a Series is ambiguous` (serve `~anom`).
- `on=campione` senza virgolette → `NameError`; `how=left` → `NameError`.
- `d["sito"].isna.sum()` → `AttributeError: 'function' object has no attribute 'sum'`.
- `d["fuori_limite"] = d[COL_VALORE] > d["LIMITI"]` → `KeyError` (la colonna si chiama `limite`).
- Report con 8 anomali invece di 4: hanno lasciato `k` al default 1.5 invece di `k=3.0`. Numeri leggermente diversi: hanno cambiato l'ordine dei passi (anomali prima di togliere duplicati). L'ordine conta: è un buon punto da discutere.
- `riassunto` senza le righe con sito NaN: hanno tolto `dropna=False` dal `groupby` (le 25 misure spariscono dal riassunto senza avviso).
- `{v:5d}` con un valore float → `ValueError: Unknown format code 'd' for object of type 'float'` (succede se qualcuno salva una percentuale nel report).

**Checkpoint a 20' (16:06)**
- Ad alta voce: "A che punto siete? Dovreste avere almeno i passi 1-4: righe lette, senza valore, duplicati, anomali. Se il report dice 311, 10, 6, 4, siete in linea."
- Chi è indietro: mostra sul proiettore solo i passi 1-3 della traccia compilati (non la soluzione intera).

**Checkpoint a 40' (16:26)**
- "Ora dovreste avere il merge (25 senza sito) e `misure_pulite.csv` salvato. Chi ha finito passa alle estensioni, nell'ordine: mediana e CV, Excel con un foglio per analita, funzione `pulisci`, grafico."
- Chi è ancora fermo al merge: "Fate il riassunto anche senza `pct_fuori_limite`, poi lo aggiungete."

**Chiusura (16:46–16:58)**
- 16:46: chiedi a **un volontario** (meglio uno che ha usato la traccia, non il più veloce) di proiettare il suo report. Confronto con 311/10/6/4/25/291. Se qualcuno ha numeri diversi, è materiale prezioso: "Quale scelta avete fatto diversamente?"
- Se qualcuno ha fatto l'estensione 3 (`pulisci`), fagliela mostrare in 1 minuto: è il messaggio del giorno ("domani lo applicate al prossimo export").
- Debrief (5'):
  - "Ogni scelta di pulizia è scritta nel codice e nel report: fra sei mesi la rifate identica."
  - Tabella di riepilogo pandas ↔ dplyr del notebook: leggila a voce, una riga per ciascuna.
  - "La catena `%>%` ha un equivalente: i metodi si concatenano con il punto, anche su più righe dentro parentesi tonde."
  - Per casa: C3.1, C4.1, serie temporali con `resample` (approfondimento). Domani: figure per la pubblicazione.
- Annuncia che le soluzioni (`docente/`) le distribuisci a fine giornata.

### 4. Se sei in ritardo (pomeriggio), taglia in quest'ordine
1. **API UniProt + Esercizio 4.3** (marcata *Facoltativo*, circa 30'): dì "è nel notebook, funziona senza rete, provatela a casa; è lo schema per unire dati da qualunque banca dati". Recupera ~25'.
2. **§5 pivot/melt**: mostra solo `pivot_table` con la media (1 minuto), salta margins e melt.
3. Esercizio 4.2: fallo in plenaria, tu digiti e loro dettano (5' invece di 10').
4. `transform` in §3: mostralo, ma senza tornare su `anomali_iqr`.
5. Il progetto **non scende sotto i 45'**: piuttosto chiudi il debrief in 3'. Se proprio serve, togli dal progetto il passo 8 (riassunto) e chiedi solo report + `misure_pulite.csv`.
- Già fuori dal flusso: C4.1 e serie temporali/`resample` (per casa).

---

## Domande probabili

- **"Perché Python e non R?"** — "Per questo tipo di lavoro sono equivalenti: dplyr e pandas fanno le stesse cose. Python conviene quando nello stesso script servono anche altro: chiamate a API, machine learning (giorno 4), automazione di file. Se il vostro gruppo lavora in R, restate in R: i concetti di oggi sono gli stessi."
- **"Esiste un equivalente di `%>%`?"** — Concatenazione di metodi con il punto, su più righe dentro `( … )`. Per `mutate` dentro una catena esiste `.assign(nuova=...)`.
- **"Esiste un `tidyverse` di Python?"** — Ci sono librerie alternative (per esempio polars, più veloce su dati grandi), ma non sono nell'ambiente del corso: pandas è lo standard.
- **"I miei file genomici hanno milioni di righe: pandas regge?"** — "Fino a qualche milione di righe in memoria sì. `read_csv` ha `usecols=` e `dtype=` per leggere solo quello che serve, e `chunksize=` per leggere a pezzi. Oltre, si usano altri strumenti, fuori dallo scope del corso."
- **"Perché `df.mean()` non mi dà NaN come R?"** — pandas usa `skipna=True` di default. `df["x"].mean(skipna=False)` si comporta come R senza `na.rm`.
- **"Differenza fra `loc` e `iloc`?"** — Etichetta contro posizione. `loc` include l'estremo, `iloc` no.
- **"Perché `[[ ]]` per più colonne?"** — La parte esterna è la selezione, quella interna è una lista Python di nomi.
- **"Come leggo un file con più fogli Excel?"** — `pd.read_excel(file, sheet_name="nome")`, oppure `sheet_name=None` per averli tutti in un dizionario.
- **"`to_datetime` senza `format` funziona lo stesso?"** — A volte, con un avviso; ma su `03/02/2026` sceglie **3 febbraio o 2 marzo a seconda del caso**: per questo il `format` esplicito (vedi trappole).
- **"Perché IQR sui logaritmi?"** — Le concentrazioni hanno una coda a destra (distribuzione circa lognormale): in scala lineare valori alti ma veri sembrerebbero anomali.
- **"Perché 1.5 e 3?"** — Convenzioni (1.5 = "baffi" del box plot; 3 = anomali "estremi"). Non sono leggi: conta dichiararle.
- **"`fillna` con la mediana è corretto?"** — Per una variabile accessoria come la temperatura è una scelta difendibile; per la variabile di interesse no. L'importante è scriverlo.
- **"Il merge è come `left_join`?"** — Sì: `how="left"` ↔ `left_join`, `"inner"` ↔ `inner_join`, `"outer"` ↔ `full_join`. `indicator=True` non ha un equivalente diretto in dplyr (si usa `anti_join` per vedere chi manca).
- **"Posso usare la chiamata vera all'API?"** — Sì, `USA_RETE = True`; i risultati però possono differire dall'output atteso perché la banca dati cambia nel tempo. Il motivo per cui si salva la risposta.
- **"Ensembl, NCBI, altri servizi?"** — Stesso schema: URL + parametri + JSON + funzione che estrae + merge. Cambiano solo l'indirizzo e i nomi delle chiavi (vanno letti nella documentazione dell'API).

### Domande di dominio (chimica/biologia): risposte oneste

Non sono il tuo campo: rispondi su ciò che è dati e codice, e rimanda il resto. Frase pronta: **"Questo è un dataset sintetico costruito per esercitarsi sul codice; la domanda chimica/biologica è giusta, ma non sono la persona giusta per rispondere: chi di voi lavora su questo?"** (con un pubblico di ricercatori, girare la domanda alla sala funziona quasi sempre).

- **Cu, Pb, Cd, µg/L, "limiti di legge"**: i limiti sono **dichiaratamente inventati** (il notebook lo scrive). Se qualcuno chiede dei limiti normativi reali: "Non li conosco a memoria e dipendono dalla matrice e dalla normativa; qui servono solo per l'esercizio."
- **"Perché µg/L per un suolo o una foglia?"**: "Nel dataset è la concentrazione misurata nella soluzione analizzata; come si passa dal campione solido alla soluzione è un passaggio di laboratorio che il dataset non descrive."
- **DPV, SPCE (righe di commento del file)**: tecniche e sensori elettrochimici; per il codice contano solo come righe da saltare.
- **Masse molari**: la conversione µg/L → nM è solo aritmetica (dividere per g/mol e moltiplicare per 1000).
- **Geni, UniProt, log2FC**: i valori di log2FC sono **inventati** (scritto nel codice). `reviewed:true` = voci curate a mano (Swiss-Prot); `organism_id:9606` = uomo. Su FBF1/ALB: "UniProt cerca anche fra i sinonimi del gene, per questo esce un risultato in più".
- **Attenzione con i genetisti**: `Gapdh` (prima maiuscola) è la convenzione dei **simboli di topo/ratto**, quelli umani sono tutti maiuscoli. Qualcuno potrebbe osservare che mettere in maiuscolo non basta per passare da topo a uomo (servirebbero gli ortologhi). Risposta: "Giusto: qui `Gapdh` è un errore di battitura in una tabella di geni umani. Su dati di specie diverse la normalizzazione della chiave è un problema biologico, non di pandas."

---

## Punti delicati / trappole

- **Codifica latin-1**: senza `encoding` → `UnicodeDecodeError ... byte 0xb5` (il `µ`). Con la codifica sbagliata ma senza errore (es. `encoding_errors="replace"`) i nomi di colonna diventano `concentrazione (�g/L)` e il `rename` poi non trova nulla. `cp1252` è un'alternativa equivalente per i file Windows.
- **Virgola decimale**: dimenticare `decimal=","` non dà errore: concentrazione e temperatura diventano testo (`str`/`object`). Lo si vede solo con `info()`.
- **`n.d.`**: senza `na_values` la colonna concentrazione diventa testo (10 celle `"n.d."`), anche se `decimal` è giusto.
- **`rename` silenzioso**: una chiave scritta male non dà errore. L'errore arriva dopo (`KeyError: 'conc_ug_L'`). Copiare i nomi da `df.columns`.
- **Date**: `pd.to_datetime` **senza `format`** sul file intero funziona con un `UserWarning`, ma su una data isolata come `03/02/2026` la interpreta come **2 marzo** (mese prima). Con un `format` sbagliato (`"%d-%m-%Y"`) → `ValueError: time data "25/01/2026" doesn't match format`. Usare sempre `format="%d/%m/%Y"`.
- **Filtri**: parentesi obbligatorie attorno a ogni condizione con `&`/`|` (altrimenti `TypeError ... 'rand_'`); `and`/`or`/`not` → `ValueError: The truth value of a Series is ambiguous`.
- **NaN nei confronti**: `NaN > 1` è False → i mancanti finiscono "nel limite" (Es. 3.2) e nel ramo falso di `np.where`. Contarli a parte.
- **`mean()` ignora i NaN in silenzio** (diverso da R).
- **Assegnazione concatenata / copy-on-write (pandas 3)**: `df[maschera]["col"] = valore` non modifica `df` → avviso `ChainedAssignmentError`. Corretto: `df.loc[maschera, "col"] = valore`. **Su Colab (pandas 2.x)** l'avviso è `SettingWithCopyWarning`, e compare anche quando si aggiunge una colonna a un sottoinsieme filtrato senza `.copy()` (es. Esercizio 3.3 senza `.copy()`). Con pandas 3 quel caso non dà avviso.
- **Colab (pandas 2.x)**: testo come `object` invece di `str`, date `datetime64[ns]` invece di `[us]`, `type(df)` stampa `pandas.core.frame.DataFrame`. Avvisalo all'inizio: gli "output attesi" differiscono solo in queste etichette.
- **Indice dopo un filtro**: le etichette restano quelle originali → `alto.loc[0]` dà `KeyError: 0`.
- **Merge**: contare sempre le righe prima e dopo. Con metadati univoci e `how="left"` 291 → 291; 25 righe con `sito` NaN; `inner` → 266. Una chiave non univoca moltiplica le righe in silenzio (→ `validate=`).
- **`groupby` scarta le chiavi NaN**: nel riassunto del progetto le 25 misure senza sito spariscono se manca `dropna=False`.
- **`value_counts` non mostra gli zeri** (LB nell'Es. 4.1); `groupby(...).agg(["size","count"])` sì.
- **Ordine dei passi di pulizia**: anomali calcolati prima o dopo la rimozione dei duplicati/mancanti cambiano i quartili. Il notebook fa: mancanti → duplicati → anomali → merge.
- **Stato del kernel**: il pomeriggio dipende da `carica_misure` e `anomali_iqr` definite nelle prime celle; dopo un riavvio vanno rieseguite. L'Es. 4.3 modifica `misurati` sul posto: rieseguirlo cambia i conteggi di `_merge`.
- **File scritti nella cartella corrente**: `misure_pulite_v0*.csv/xlsx`, `pb_frutto.csv`, `misure_pulite.csv`, `riassunto.csv` finiscono accanto al notebook (`studenti/`, o `/content` su Colab). Se qualcuno "non trova il file", fagli stampare `Path.cwd()`.

---

## Da verificare prima del corso

1. **`requests` non è dichiarato** in `pyproject.toml` né in `environment.yml`, e `verifica_ambiente.py:7` non lo controlla. Con uv arriva come dipendenza indiretta di JupyterLab (`uv.lock:757`, `uv.lock:1236`), quindi oggi funziona; verificalo **sull'ambiente Miniforge** (`python -c "import requests"`). Serve solo con `USA_RETE = True` (`sorgenti/04_G2_pomeriggio_pandas_avanzato_progetto.py:349`), quindi il rischio è basso.
2. **Chiamata vera all'API** (`04_...:347-357`): con `USA_RETE = True` la risposta attuale di UniProt può differire dalla copia salvata (numero e ordine dei risultati, presenza di FBF1), quindi gli output attesi di 4.3 non coincidono. `estrai` (`04_...:393-400`) dà `KeyError` se una voce non ha `recommendedName`, e `validate="one_to_one"` (`04_...:440`) dà `MergeError` se UniProt restituisce due voci per lo stesso gene. Prova la chiamata vera dalla rete dell'aula prima di mostrarla.
3. **Il modello del report** (`04_...:510-518`) mostra righe con il trattino (`- senza valore:`) ed etichette leggermente diverse (`senza metadati sito:`) rispetto a quello che stampa il codice (`senza valore:`, `senza metadati sito (tenute):`). È solo estetica, ma qualcuno cercherà di riprodurlo identico: avvisa che contano i numeri, non la formattazione.
4. **Rieseguire l'Esercizio 4.3** (`04_...:439`): `misurati["gene"]` viene sovrascritto sul posto, quindi una seconda esecuzione dà `_merge` diverso dall'output atteso (both 10, right_only 1). Non è un bug ma confonde: avvisa prima dell'esercizio.


---

## Giorno 3 — Figure da rivista e statistica da laboratorio

**Apertura del giorno (3 righe da dire)**
- Ieri: dal CSV "sporco" a una tabella pulita con pandas (mancanti, duplicati, anomali sui log, `groupby`, `merge`), e il progetto di wrangling.
- Stamattina: dalla tabella a una **figura pronta per la sottomissione** (PDF vettoriale, larghezza di colonna, font e linee a norma, leggibile in b/n).
- Oggi pomeriggio: la retta di taratura **con le incertezze**, fit non lineari, residui, t-test/ANOVA fatti bene (niente pseudo-repliche, niente caccia al p < 0.05).

File: `sorgenti/05_G3_mattina_grafici_pubblicazione.py` (+ `materiali/figure_pubblicazione.py`, `materiali/personalizzazione_grafici.ipynb` = "la scheda") e `sorgenti/06_G3_pomeriggio_scipy_statistica.py`. I notebook non indicano tempi: quelli sotto sono costruiti sull'orario 10:00–13:00 e 14:00–17:00. Rispetto alla versione su 9:00–12:30: l'Es. 5.1 dura 12' (ha solo due buchi), l'Es. 5.3 è guidato, seaborn è una demo di 5'. Nel pomeriggio l'anomalo nascosto diventa un lavoro in coppia e l'Es. 6.1 parte prima della pausa, così la sala non resta 85' a guardare.

---

# MATTINA — nb 05: grafici per la pubblicazione

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 10:00 | Apertura + § 0 cella di avvio, dati di oggi | discorso + esecuzione | 8 |
| 10:08 | § 1 Anatomia (Figure/Axes, solo API a oggetti) | lezione + demo | 12 |
| 10:20 | § 2 Tipi fondamentali + box plot con punti | demo | 18 |
| 10:38 | **Es. 5.1** box plot taratura (liv. 1) | esercizio | 12 |
| 10:50 | § 3 Barre d'errore (sd vs sem), `fill_between` | demo + discussione | 13 |
| 11:03 | § 4 Personalizzazione + giro nella scheda + Okabe-Ito | demo | 15 |
| 11:18 | *pausa* | | 15 |
| 11:33 | **Es. 5.2** da grezza a pubblicabile (liv. 2) | esercizio | 30 |
| 12:03 | § 5 Pannelli multipli: solo mostrare la figura 1×3 | demo | 5 |
| 12:08 | § 6 Standard rivista: `stile_rivista`, `salva_figura`, `verifica_figura`, controllo in grigi | demo | 20 |
| 12:28 | **Es. 5.3 guidato**: il pannello (a) lo fai tu dal vivo, loro fanno (b) e il salvataggio | esercizio | 22 |
| 12:50 | § 7 Seaborn: esegui le due celle come esempio | demo | 5 |
| 12:55 | Riepilogo | discorso | 5 |

### 2. Sezioni

**§ 0 Avvio e dati**
- Cosa dire: "Oggi quattro dataset: taratura (6 livelli × 3 repliche), i voltammogrammi DPV di giorno 1, una cinetica, tre trattamenti × 8 repliche." "Il modulo `figure_pubblicazione.py` è un file Python normale: l'`import` funziona perché la cella aggiunge `materiali/` a `sys.path`."
- Demo live: eseguire la cella; far vedere che stampa la versione di matplotlib e il percorso di `materiali`.
- Se l'import fallisce (`ModuleNotFoundError: figure_pubblicazione`): il notebook non è aperto da `studenti/` (cartella spostata, o Colab con zip non scompattato in `corso_python_CNR/`).

**§ 1 Anatomia**
- Cosa dire: "`fig` è il foglio, con dimensioni fisiche in pollici; `ax` è il riquadro con i dati." "In rete trovate `plt.plot`, `plt.xlabel`: è l'interfaccia "di stato", va bene per un grafico solo. Noi scriviamo sempre `fig, ax = plt.subplots()` e poi solo `ax.`."
- Analogia R: `fig` ≈ il device (`pdf(width=, height=)`), `ax` ≈ un pannello; `ax.set_xlabel` ≈ `xlab()`/`labs(x=)` in ggplot2. Differenza: in ggplot2 si dichiara la mappatura e il grafico si compone; in matplotlib si danno comandi a un oggetto, passo per passo.
- Demo live: il grafico grezzo della taratura; mostrare `"o"` = solo marcatori.

**§ 2 Tipi + box plot con punti**
- Cosa dire: "Dati = marcatori senza linea; modello = linea senza marcatori: si legge anche senza legenda." "Con 8 repliche un box plot da solo nasconde i dati: sovrapponete sempre i punti, con un po' di *jitter*." "Il jitter è solo orizzontale e solo grafico: non tocca i valori."
- R: `geom_boxplot() + geom_jitter(width=0.1)`; `ax.hist` ≈ `hist()`/`geom_histogram()`.
- Demo live: la griglia 2×2 (`axs[0, 1]` è riga 0, colonna 1, indici da 0); poi box + punti. Sottolineare `showfliers=False` (altrimenti gli anomali appaiono due volte: come "flier" e come punto).

**Es. 5.1 (livello 1)** — box plot della corrente per livello di concentrazione.
- Buchi: il nome della colonna (`"i_uA"`) e le etichette dei tick (`livelli`).
- Errori tipici:
  - mettere `"conc_uM"` nel primo buco → sei box piatti a valore costante;
  - `tar["i_uA"]` al posto della stringa `"i_uA"` → `KeyError` (pandas cerca colonne con quei valori come nome);
  - `NameError: name 'rng' is not defined` → non hanno eseguito la cella demo precedente;
  - chi copia da internet `ax.boxplot(..., labels=...)` ottiene `TypeError: Axes.boxplot() got an unexpected keyword argument 'labels'` (in matplotlib 3.11 si chiama `tick_labels`; nell'esercizio si usa `set_xticks`).
- Suggerimento non risolutivo: "Il primo buco è *cosa* mettete sull'asse y; il secondo è *cosa scrivete* sotto le sei posizioni 0..5."
- Notare con la classe: l'asse x è categorico (posizioni equidistanti), non in scala: 1 e 2 µM sono distanti quanto 20 e 50.

**§ 3 Barre d'errore**
- Cosa dire: "Una barra d'errore senza didascalia non significa niente: scrivete sempre se è sd, sem o IC, e n." "La sd descrive la dispersione dei dati; il sem descrive l'incertezza sulla media e si restringe con √n." "Con n = 3 il sem è piccolo e rassicurante: per mostrare la variabilità delle repliche usate la sd."
- R: `geom_errorbar(aes(ymin=, ymax=))`, `geom_ribbon()` ≈ `fill_between`.
- Demo live: i due pannelli sd vs sem con `sharey=True`; poi la banda ± 0.4 µA, dicendo chiaramente che è **finta**: la banda vera la calcoliamo **oggi pomeriggio**.

**§ 4 Personalizzazione**
- Cosa dire: "Nessuno ricorda tutte queste opzioni: per questo c'è la scheda con 33 casi, ognuno con la riga che lo risolve." "La palette Okabe-Ito si imposta una volta in cima e vale per tutte le figure." "Colore + tratteggio diverso: la figura sopravvive alla stampa in b/n e a chi è daltonico (circa 1 uomo su 12)."
- R: `scale_colour_manual(values=...)` / pacchetto `ggthemes::colorblind_pal()` ≈ `axes.prop_cycle`; `linetype` ≈ `linestyle`.
- Demo live: aprire la scheda accanto e mostrare § 2.4 (log), § 2.6 (niente `1e6` sull'asse), § 3.2 (equazione nel riquadro), § 3.5 (pedici `$_p$`, `$\mu$`).

**Es. 5.2 (livello 2)** — media ± sd, retta sotto i punti, equazione e R² nel riquadro, legenda in basso a destra.
- Errori tipici:
  - `ax.text(0.04, 0.95, ...)` **senza** `transform=ax.transAxes` → il testo finisce in coordinate dati, vicino all'origine, quasi invisibile;
  - R² calcolato sulle medie (`stat`) invece che sui 18 punti → R² più alto; il commento chiede i punti singoli;
  - LaTeX dentro f-string: `f"$i_{p}$"` → `NameError: name 'p' is not defined` (o, peggio, sostituisce silenziosamente un `p` esistente). Le graffe LaTeX in f-string vanno raddoppiate: `{{p}}`;
  - retta sopra i punti: manca `zorder` (retta 1, punti 2);
  - `markerfacecolor="white"` dimenticato → marcatori pieni.
- Suggerimento: "Il riquadro è nella scheda § 3.2: copiatelo pure. Le coordinate (0.04, 0.95) sono frazioni del riquadro, non µM: cosa dice a matplotlib di interpretarle così?"
- Per chi finisce presto: rifarlo con marcatori diversi per n diversi, o aggiungere i punti singoli in grigio sotto le medie.

**§ 5 Pannelli multipli**
- Cosa dire: "`sharey=True` impone la stessa scala: usatelo quando i pannelli vanno confrontati, non quando misurano cose diverse." "`constrained_layout=True` sistema gli spazi da solo; le lettere (a)(b)(c) si mettono in ciclo con `transAxes`."
- R: `facet_wrap()`/`facet_grid()` per pannelli dello stesso tipo; `patchwork`/`cowplot::plot_grid(labels="AUTO")` per pannelli diversi: è questo il caso.
- Demo live: la figura 1×3; cambiare `-0.2` in `0` nella posizione della lettera per mostrare che le coordinate negative escono dal riquadro.

**§ 6 Standard per la pubblicazione**
- Cosa dire:
  - "La larghezza si fissa **alla creazione**: 9 cm di colonna. Se disegnate a 15 cm e l'editore riduce, il font da 8 pt diventa 5 pt."
  - "PDF vettoriale con font incorporati come TrueType (`pdf.fonttype = 42`): il testo resta testo, selezionabile e modificabile in Illustrator/Inkscape."
  - "`savefig` prima di `plt.show()`, e niente `bbox_inches="tight"`: cambia la larghezza finale."
  - "`stile_rivista()` è globale; `with stile_rivista_ctx():` vale solo dentro il blocco."
- R: `ggsave("fig.pdf", width = 90, height = 66, units = "mm")`, `theme_classic(base_size = 8)` ≈ `stile_rivista(base_font=8)`; in R il PDF usa di default font base-14 non incorporati, in matplotlib li incorporiamo noi.
- Demo live:
  1. `controlla_font("Arial")`: sul proiettore (Linux) stampa ATTENZIONE e ripiega su DejaVu Sans; su Windows/Mac dei partecipanti di solito dice "disponibile" → **l'output atteso è diverso, ed è normale**.
  2. `verifica_figura(fig)`: leggere ad alta voce le righe (dimensioni in cm, font minimo 7 pt, linee, b/n, pixel a 600 dpi).
  3. Aprire `figure/taratura_singola.pdf` e zoomare: non si sgrana. Il file è in `studenti/figure/` (cartella relativa al notebook).
  4. Controllo in grigi: tre curve tutte continue, solo colore → in b/n due si confondono. Chiedere alla sala: "quali due?".

**Es. 5.3 (livello 3)** — due pannelli, doppia colonna Elsevier (`LARGHEZZE["elsevier_doppia"]` = 7.48 in = 19 cm), altezza `7 * CM`; (a) voltammogrammi distinguibili in b/n, (b) taratura con equazione; PDF + TIF a 600 dpi.
- Errori tipici:
  - `verifica_figura(fig)` senza argomenti → **"ATTENZIONE: larghezza oltre 7.0 in"**: il default è il limite ACS; il testo dell'esercizio ora indica `larghezza_max=7.5` (corretto il 14/11);
  - `figsize=(19, 7)` → figura di 19 *pollici*: serve `7 * CM` (e `LARGHEZZE` è già in pollici: non moltiplicarlo per `CM`);
  - `NameError: r2` (o `m`, `stat`, `x`) se hanno riavviato il kernel o chiamato diversamente l'R² in 5.2 → "Run all above";
  - dopo un riavvio senza rieseguire la cella di § 6 manca `stile_rivista()` → niente `constrained_layout`, etichette che si sovrappongono, font grandi;
  - `plt.show()` prima di `salva_figura` → file bianco;
  - con curve colorate a tratto continuo `verifica_figura` segnala "coppie di curve indistinguibili in bianco e nero": è il controllo che funziona.
- Suggerimento: "Partite dalla soluzione del 5.2 e dalla figura 1×3 del § 5: cambiano solo `figsize`, numero di pannelli e il salvataggio."
- Il TIF a 600 dpi doppia colonna è 4488 × 1653 px: su alcuni PC si apre lento. È RGB senza canale alfa, compressione LZW.

**§ 7 Seaborn (facoltativo)**
- Cosa dire: "Per chi viene da ggplot2: seaborn è il parente più vicino: `data=`, `x=`, `y=`, `hue=`, formato lungo." "Si usa per esplorare; per la figura finale si passa `ax=` e si rifinisce con matplotlib."
- Attenzione: `mpl.rcdefaults()` azzera stile rivista **e** palette Okabe-Ito.
- `regplot(ci=95)` disegna una banda di **confidenza** della retta (stimata per bootstrap), non di predizione: aggancio perfetto al pomeriggio.

### 3. Se sei in ritardo (mattina) — cosa tagliare, in ordine
1. **§ 7 Seaborn** (marcato *Facoltativo*): citarlo in una frase per gli utenti R e dire che è nel notebook.
2. Le **estensioni facoltative** (inset, pannello (c) con la cinetica) e il "Confronto finale" con il vicino (opzionale per natura).
3. *(Non marcato, mia scelta)* § 5: mostrare solo l'output della figura 1×3, senza modificarla dal vivo.
4. *(Non marcato)* Es. 5.3: farlo a metà in plenaria (solo pannello (b) + salvataggio), il resto per casa. **Non tagliare § 6**: è il motivo per cui molti sono venuti.

### 4. Domande probabili (mattina)
- **"In ggplot2 faccio `facet_wrap(~gruppo)` in una riga. Qui?"** → `sns.relplot(..., col="gruppo")` / `sns.catplot`; oppure un ciclo su `plt.subplots(1, k)`. Per figure da rivista con pannelli diversi, matplotlib + lettere è l'equivalente di `patchwork`.
- **"Meglio sd o sem?"** → Dipende da cosa volete comunicare: dispersione delle misure → sd; precisione della media → sem o, meglio, IC 95 %. Sempre dichiarato in didascalia, con n.
- **"La rivista vuole Arial e io non ce l'ho (Linux)."** → Installare il font o usare Liberation Sans (metricamente identica ad Arial); dopo l'installazione può servire cancellare la cache dei font di matplotlib (`matplotlib.get_cachedir()`) e riavviare il kernel. Onestamente: sul proiettore resta DejaVu Sans.
- **"Le parti con `$...$` (pedici, µ) hanno un font diverso."** → Vero: il mathtext usa di default DejaVu. Si può mettere `mpl.rcParams["mathtext.default"] = "regular"` per usare il font del testo; oppure scrivere i pedici senza `$` quando non servono.
- **"EPS?"** → `salva_figura` lo supporta, ma l'EPS non gestisce la trasparenza (`alpha`): le bande diventano opache. Preferire PDF.
- **"La rivista chiede CMYK / TIFF a 1200 dpi per i line-art."** → `salva_figura(..., dpi=1200)`; il CMYK il modulo non lo fa: "non lo gestiamo, si converte dopo con Pillow o con il software dell'editore; verifico e vi dico".
- **"Perché non `bbox_inches='tight'`?"** → Ritaglia la figura e la larghezza finale non è più 9 cm; `constrained_layout` sistema gli spazi senza cambiare le dimensioni.
- **"Come controllo che i font siano incorporati nel PDF?"** → Acrobat: Proprietà → Font; Linux: `pdffonts file.pdf`.
- **"Posso modificare il PDF in Illustrator/Inkscape?"** → Sì, con fonttype 42 il testo è testo. Il consiglio è comunque rifare la figura dal codice: è riproducibile.

---

# POMERIGGIO — nb 06: SciPy e statistica

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 14:00 | § 0 avvio + § 1 `linregress`, errori standard, IC 95 %, Anscombe | lezione + demo | 20 |
| 14:20 | § 2 Bande di confidenza e predizione | lezione + demo | 15 |
| 14:35 | Report di regressione + anomalo nascosto: **le tre domande in coppia**, poi discussione | lavoro in coppia | 15 |
| 14:50 | § 3 `curve_fit`: solo la sigmoide a 4 parametri | demo | 12 |
| 15:02 | § 4 Residui | demo | 8 |
| 15:10 | **Es. 6.1 ridotto**: R² dei due modelli e figura dei residui | esercizio | 20 |
| 15:30 | *pausa* | | 15 |
| 15:45 | Correzione dell'Es. 6.1 | discorso | 5 |
| 15:50 | § 5 t-test Welch, p-value, ANOVA + Tukey, confronti multipli (Shapiro in una frase) | lezione + demo | 20 |
| 16:10 | **Es. 6.2** Cu nelle tre matrici, fatto bene (liv. 2) | esercizio | 30 |
| 16:40 | Correzione + riepilogo: tabella R ↔ Python | discorso | 10 |
| 16:50 | Margine | | 10 |

Il pomeriggio è pieno: parte del pubblico conosce già la statistica meglio di voi. Strategia: "La statistica la conoscete; oggi vediamo **come si scrive in Python** e **dove scipy si comporta diversamente da R**."

### 2. Sezioni

**§ 1 Regressione con incertezze**
- Cosa dire: "`np.polyfit` dà solo i coefficienti; `stats.linregress` dà anche gli errori standard." "La regressione si fa sui 18 punti, non sulle 6 medie: le repliche portano l'informazione sulla dispersione." "IC 95 % = stima ± t(0.975, n−2) × errore standard; con 16 gradi di libertà t = 2.12."
- R: `summary(lm(i_uA ~ conc_uM))` → stessi numeri (m = 0.4195 ± 0.0023, q = 0.1428 ± 0.0514); `confint()` → stessi IC.
- Demo live: output atteso → intercetta 0.14 µA, IC [0.03, 0.25] → **non** compatibile con zero. Domanda alla sala: "Cosa può voler dire in laboratorio?" (segnale del bianco, corrente di fondo, contaminazione).
- Anscombe: quattro dataset, stessa retta e R² = 0.67. "L'R² non dice se il modello è giusto. Lo dicono il grafico e i residui."
  - **Come presentarlo**: è un esempio classico, chi fa statistica lo conosce. Presentalo come promemoria, non come scoperta ("molti di voi lo conoscono, lo uso solo come promemoria"), **2 minuti**, poi avanti. Il tempo va al codice e alla dimostrazione dell'anomalo nascosto.
  - Coinvolgi chi usa R invece di spiegargli cose note: "Chi usa R, come ottenete l'intervallo di predizione?" (risposta attesa: `predict(fit, newdata, interval = "prediction")`), poi mostra l'equivalente in Python nel § 2.

**§ 2 Bande di confidenza e predizione**
- Cosa dire: "Confidenza: dove sta la *retta* (la media di y a quella x). Si stringe aumentando i punti." "Predizione: dove cadrà la *prossima singola misura*. Contiene anche il rumore della misura, quindi non scende mai sotto ±t·s(y/x)." "Entrambe sono più strette al centro dei dati (x̄) e si allargano agli estremi: estrapolare costa."
- R: `predict(fit, newdata, interval = "confidence")` e `interval = "prediction"` danno esattamente queste bande. In ggplot2, `geom_smooth(method = "lm")` disegna **solo** quella di confidenza.
- Demo live: le due formule differiscono solo per quel "1 +" sotto radice: indicarlo.
- "Le metriche del vostro settore" (LOD, LOQ, concentrazione di un incognito, x50): il notebook non dà formule di proposito. Dire: "si prendono dalla linea guida del vostro settore e si dichiara quale si usa."

**Dimostrazione: report + anomalo nascosto**
- Cosa dire: "Una sola replica a 20 µM sbagliata del 30 %: la pendenza cambia di +0.6 %, s(y/x) cresce di ~4 volte, la banda di predizione a 20 µM passa da ±0.36 a ±1.42 µA. L'R² passa da 0.9995 a 0.9928: per chiunque è ancora 'ottimo'."
- Fare le tre domande del notebook alla sala **prima** di mostrare il commento finale.
- Messaggio: "Riportate s(y/x) e guardate il grafico. L'R² da solo non vi avverte."

**§ 3 `curve_fit`**
- Cosa dire: "Scrivete il modello come funzione Python con x come primo argomento, poi `curve_fit` cerca i parametri che minimizzano la somma dei quadrati." "`popt` sono i parametri, `np.sqrt(np.diag(pcov))` i loro errori standard." "Tre cose: `p0` sensato (guardando il grafico), `bounds` fisici, aver guardato i dati."
- R: `nls(y ~ C0*exp(-t/tau) + plateau, start = list(...))`; `p0` ≈ `start=`. Per la sigmoide, chi lavora in farmacologia usa `drc::drm(..., fct = LL.4())` o GraphPad Prism.
- Decadimento: C0 = 80.3 è l'**ampiezza** della parte che decade, non il valore a t = 0 (che è C0 + plateau ≈ 90.8). Il "tempo di dimezzamento" τ·ln2 = 26 min è quello della parte sopra il plateau (vedi "Da verificare").
- Sigmoide: "x50 è la dose che dà metà della salita fra Rmin e Rmax; n è la ripidità." Risultato: x50 = 14.0 ± 1.2 µM, n = 1.30. Si fitta sulla dose originale e si **mostra** con asse x log: in scala lineare la S è schiacciata a sinistra.
- Demo live consigliata (2'): togliere `p0` e `bounds` alla sigmoide e mostrare cosa succede (senza `p0` scipy parte da tutti 1: può non convergere o dare parametri assurdi). Poi rimetterli.

**§ 4 Residui**
- Cosa dire: "Residuo = misura − modello. Se il modello è giusto, i residui sono rumore senza forma." "Qui la retta sulla cinetica ha R² alto, ma i residui fanno una U: modello sbagliato." "Forme da riconoscere: curva → modello sbagliato; ventaglio → varianza che cresce con il livello."
- R: `plot(residuals(fit))`, o `plot(fit)` (il primo dei quattro grafici diagnostici).

**Es. 6.1 (livello 2)** — sigmoide vs retta in log10(dose): R², figura dati+residui, parametri ± incertezza, scelta motivata.
- Atteso: R² sigmoide 0.9974, retta-log 0.9189; residui della retta-log con forma a S.
- Errori tipici:
  - `np.log(d)` invece di `np.log10(d)` → nessun errore, numeri diversi (la pendenza cambia di un fattore 2.3); il testo chiede log10;
  - residui della retta calcolati con `d` invece di `log10(d)` nella previsione → residui enormi;
  - curva della retta-log disegnata su `dd` senza log10 → curva assurda;
  - `sharex=True` con il pannello in alto in scala lineare e quello in basso in log: con assi condivisi basta `set_xscale("log")` su uno dei due;
  - etichetta f-string con `$x_{50}$` → `NameError`/sostituzione silenziosa (vedi mattina: graffe doppie).
- Suggerimento: "Il modello lineare in log10(dose) ha la stessa forma della retta di taratura: cambia solo cosa mettete al posto di x."
- La motivazione corretta **non** è l'R²: residui sistematici + la retta non ha plateau.
- Estensione bootstrap: avvisare che in qualche ricampionamento `curve_fit` può non convergere (`RuntimeError`) → `try/except` e si scarta quel giro.

**§ 5 Statistica di base**
- Shapiro: "Con n = 8 il test di normalità ha poca potenza: p > 0.05 non dimostra la normalità. Conta il grafico."
- t-test: "In scipy `ttest_ind` **di default assume varianze uguali** (Student). In R `t.test()` di default è Welch. Scrivete sempre `equal_var=False`." Risultati: A vs controllo diff −0.44, p = 0.50, d = −0.35; B vs controllo +2.98, p = 0.0001, d = 2.65.
- p-value: "La probabilità di vedere una differenza almeno così grande *se* non ci fosse nessuna differenza vera. Non è la probabilità che H0 sia vera, e non misura l'effetto." "A: 'non significativo' non vuol dire 'nessun effetto': con n = 8 non abbiamo abbastanza dati per vederlo."
- ANOVA + Tukey: F = 17.96, p = 2.8e−5; Tukey: A−B e controllo−B significativi, controllo−A no.
- **Segno di Tukey diverso da R**: scipy riporta `media_i − media_j` (riga meno colonna: "controllo − trattamento_A = +0.44"); `TukeyHSD()` di R riporta "livello successivo − precedente" (trattamento_A−controllo = −0.44). Stessi numeri, segno opposto.
- Confronti multipli: 20 t-test su rumore puro → 1 "significativo" (p = 0.046), 0 con Bonferroni. "È aritmetica: 20 × 0.05 = 1."
- R: `aov()`+`summary()`, `TukeyHSD()`, `kruskal.test()`, `p.adjust()`.

**Es. 6.2 (livello 2)** — Cu nelle tre matrici: log10 → media per campione → box plot → ANOVA + Tukey → rapporti con IC → Kruskal-Wallis.
- Atteso: 90 misure → 40 campioni (foglia 10, frutto 15, suolo 15); ANOVA F = 97.4, p = 1.8e−15; suolo/foglia = 2.27 [1.71, 3.02]; suolo/frutto = 4.29 [3.32, 5.54]; frutto/foglia = 0.53 [0.40, 0.70]; KW H = 32.4, p = 9.4e−8.
- Errori tipici:
  - ANOVA sulle 90 misure (pseudo-repliche) → p ancora più piccolo e falsamente preciso: è proprio la trappola da far notare;
  - `groupby("campione")` senza `"matrice"` → la colonna matrice sparisce dopo `reset_index()` e non si può più dividere per matrice;
  - media delle concentrazioni e *poi* log (invece di log e poi media) → media aritmetica, non geometrica: risultati diversi;
  - `10 ** diff` senza girare il segno e i limiti dell'IC → rapporti invertiti (foglia/suolo invece di suolo/foglia), con IC [basso, alto] scambiato;
  - box plot dei log10 su asse lineare: va bene, ma allora l'etichetta deve dire "log10(Cu)"; la soluzione ritorna a 10** e mette l'asse in log.
- Suggerimento: "Prima contate: quante righe avete prima e dopo il `groupby`? Se il numero non scende da 90 a 40, il test vede pseudo-repliche." Per i rapporti: "Una differenza di log10 è il log10 di un rapporto: come si torna indietro?"
- La conclusione va scritta con effetto e IC ("il suolo ha circa 2.3 volte il rame della foglia, IC 95 % 1.7–3.0"), non solo "p < 0.001".

### 3. Se sei in ritardo (pomeriggio) — cosa tagliare, in ordine
I soli marcati facoltativi sono le estensioni; il resto è una mia proposta.
1. Le **estensioni facoltative**: riscrivere `report_regressione` da soli; bootstrap di x50.
2. *(Non marcato)* La demo "senza `p0`" e la discussione sul decadimento: mostrare solo la sigmoide.
3. *(Non marcato)* Es. 6.1 in plenaria: fate solo i punti 1-2 (R² dei due modelli) insieme, la figura per casa.
4. *(Non marcato)* Shapiro e la cella dei 20 test casuali: raccontarli in 2 minuti con l'output già visibile.
5. **Non tagliare** la Dimostrazione dell'anomalo né il messaggio sulla pseudo-replicazione dell'Es. 6.2: se manca il tempo, fate l'Es. 6.2 in plenaria, guidandolo voi.

### 4. Domande probabili (soprattutto da chi usa R)
- **"Perché qui le repliche della taratura vanno bene nella regressione, e nell'Es. 6.2 sono pseudo-repliche?"** → Nella taratura la domanda riguarda la retta e la x è fissata dallo sperimentatore: le repliche servono a stimare il rumore. Nell'Es. 6.2 la domanda riguarda le **matrici**, e l'unità indipendente è il campione: 3 misure dello stesso campione non sono 3 campioni. Onestamente: se le 3 repliche di taratura fossero 3 iniezioni della *stessa* soluzione, anche lì si sottostimerebbe la variabilità fra preparazioni.
- **"Perché non un modello misto (`lmer(log_conc ~ matrice + (1|campione))`)?"** → Sarebbe la scelta più completa; in Python serve `statsmodels`, che non è nel nostro ambiente. Con 2-3 repliche per campione la media per campione è un'approssimazione standard e onesta. Se usate già R, per i modelli misti R resta un'ottima scelta.
- **"Dov'è la tabella ANOVA con Df, Sum Sq, Mean Sq?"** → scipy dà solo F e p; niente formule `y ~ x`. Per ANOVA a più fattori serve `statsmodels` (non installato) o R.
- **"`TukeyHSD` mi dà `diff lwr upr p adj`: è lo stesso?"** → Sì, stesso metodo (Tukey-Kramer se n diversi), stessi numeri, segno della differenza invertito (vedi sopra).
- **"Serve fare l'ANOVA prima di Tukey?"** → No: Tukey HSD controlla già da solo l'errore sull'insieme dei confronti. Fare prima l'ANOVA è una prassi diffusa, non un requisito.
- **"Bonferroni è troppo conservativo; Holm/BH?"** → Sì, Holm è sempre almeno potente quanto Bonferroni; per molti test (es. genomica) si controlla l'FDR con Benjamini-Hochberg: in scipy c'è `stats.false_discovery_control(p_vals)` (equivale a `p.adjust(method="BH")`). Holm si scrive in poche righe.
- **"Il d di Cohen con n = 8 non è distorto?"** → Sì, tende a sovrastimare: la correzione di Hedges (g) moltiplica per circa 1 − 3/(4(n1+n2)−9) ≈ 0.95 qui. Soglie convenzionali 0.2/0.5/0.8: sono indicative, non leggi.
- **"La formula del d nel notebook usa la media delle varianze: è la pooled?"** → Con gruppi di uguale numerosità (8 e 8) coincide con la sd pooled classica.
- **"`curve_fit` = `nls`?"** → Sì, minimi quadrati non lineari. Gli errori standard di default sono scalati dalla varianza dei residui come in `nls` (`absolute_sigma=False`). Se avete pesi/incertezze note per punto: `sigma=` e `absolute_sigma=True`.
- **"In `drc` la pendenza ha il segno opposto."** → `LL.4()` usa b = −n con questa parametrizzazione; x50 corrisponde a `e`. Controllate sempre la formula del pacchetto.
- **"Perché x50 ± 1.23 è simmetrico? Prism mi dà un IC asimmetrico."** → Prism fitta di solito log(EC50): l'IC è simmetrico in log e asimmetrico in scala lineare. L'errore dalla covarianza è un'approssimazione locale; il bootstrap dell'estensione dà un IC più realistico.
- **"La banda di confidenza vale per tutta la retta insieme?"** → No, è **puntuale** (per ogni x separatamente). Una banda simultanea (Working-Hotelling) è più larga. "Non la calcoliamo oggi."
- **"Kruskal-Wallis confronta le mediane?"** → Solo se le distribuzioni hanno la stessa forma; in generale verifica se un gruppo tende a dare valori più alti di un altro. Si basa sui ranghi, quindi log o non log dà lo stesso risultato.
- **"Regressione pesata?"** → Si usa quando la sd cresce con la concentrazione (Miller & Miller ne parlano); qui le sd per livello non mostrano un trend. In scipy: `curve_fit` con `sigma=`.
- **"LOD/LOQ?"** → Formule comuni: LOD ≈ 3.3·s/m, LOQ ≈ 10·s/m (ICH; s = s(y/x) o la sd del bianco), oppure y_B + 3s_B (Miller & Miller). "Dipende dalla linea guida del vostro settore: non è il mio campo, verificate quale vi chiede la rivista."

### 5. Mini-glossario statistico (per voi, nb 06)
- **Errore standard (di un parametro)**: quanto varierebbe la stima ripetendo l'esperimento; è la sd della stima, non dei dati.
- **IC 95 %**: intervallo costruito con una procedura che, ripetuta molte volte, contiene il valore vero nel 95 % dei casi. Non "95 % di probabilità che il valore sia qui" (sfumatura che gli statistici notano).
- **t di Student, gradi di libertà**: con poche misure la sd stimata è incerta, quindi si usa t (più larga di 1.96). Gdl = n − numero di parametri (n − 2 per una retta).
- **R²**: frazione della varianza di y spiegata dal modello. Alta non vuol dire modello giusto (Anscombe).
- **s(y/x)**: sd dei residui della retta, il "rumore" della misura attorno alla retta, nelle unità di y.
- **S_xx**: somma dei (x − x̄)²; quanto sono sparse le concentrazioni. Più è grande, più la pendenza è precisa.
- **Sensibilità**: la pendenza m (µA per µM).
- **Banda di confidenza**: incertezza sulla posizione della retta (la media di y a una x). **Banda di predizione**: dove cade una nuova singola misura; = confidenza + rumore della misura.
- **Intercetta ≠ 0**: segnale a concentrazione zero (bianco, fondo).
- **Minimi quadrati / `curve_fit`**: trova i parametri che rendono minima la somma dei residui al quadrato. `p0` = punto di partenza; `bounds` = limiti; `pcov` = matrice di covarianza dei parametri.
- **Decadimento con plateau**: C(t) = C0·e^(−t/τ) + plateau; τ = tempo in cui la parte che decade scende al 37 %; τ·ln2 = tempo in cui si dimezza (sempre la parte sopra il plateau).
- **Logistica a 4 parametri / curva di Hill**: curva a S fra Rmin e Rmax; x50 (in farmacologia EC50, o IC50 se la curva scende) = dose a metà salita; n = coefficiente di Hill (ripidità; n > 1 curva più ripida).
- **Residui**: misura − modello; senza forma = modello adeguato.
- **Shapiro-Wilk**: test di normalità; con n piccolo raramente rifiuta anche se i dati non sono normali.
- **t-test di Welch**: confronto di due medie senza assumere varianze uguali.
- **p-value**: probabilità, se H0 fosse vera, di ottenere un risultato almeno così estremo. Non è P(H0) e non è la dimensione dell'effetto.
- **d di Cohen**: differenza fra medie divisa per la sd; effetto in "unità di sd", indipendente da n.
- **ANOVA a una via (F)**: verifica se *almeno* una media differisce; F = variabilità fra gruppi / variabilità entro gruppi.
- **Tukey HSD**: tutti i confronti a coppie con IC e p corretti per il numero di confronti.
- **Confronti multipli**: più test fate, più falsi positivi; **Bonferroni**: soglia 0.05/k, semplice e conservativo.
- **Pseudo-replicazione**: trattare misure ripetute sullo stesso campione come campioni indipendenti; gonfia n e rimpicciolisce p.
- **Scala log / media geometrica**: per concentrazioni positive con coda a destra; la media dei log10 è il log10 della media geometrica; una differenza in log10 è un rapporto (10^Δ).
- **Kruskal-Wallis**: alternativa non parametrica all'ANOVA, sui ranghi; robusta ad anomali e asimmetria.
- **Bootstrap**: ricampionare i dati con reinserimento molte volte e rifare la stima; la dispersione delle stime dà l'incertezza.

Frase onesta quando non sapete: *"Non sono uno statistico: so dirvi cosa calcola questa funzione e come si confronta con R. Per la scelta del test nel vostro disegno sperimentale, controllo e vi rispondo domani mattina."*

---

## 6. Punti delicati / trappole

**Prima del corso (tecnica)**
- Eseguire entrambi i notebook dalla versione `studenti/` sul PC del proiettore: la mattina crea `studenti/figure/` (PDF, PNG, TIF).
- Font: `controlla_font("Arial")` su Linux → ATTENZIONE + `findfont: Font family ['Arial'] not found` in rosso (stderr): **non è un errore**. Su Windows/Mac Arial di solito c'è → output diverso dall'"Output atteso". Dirlo prima che lo chiedano.
- Il mathtext (`$i_\mathrm{p}$`, `$R^2$`) resta in DejaVu anche con Arial: font misti nella figura (vedi Domande).
- `stile_rivista()` è globale e resta attivo fino a `mpl.rcdefaults()` (§ 7) o al riavvio del kernel: chi riavvia senza rieseguire § 6 perde stile e `constrained_layout`.
- `savefig`/`salva_figura` **prima** di `plt.show()`; dopo lo show la figura inline è chiusa → file bianco.
- I file vanno in `figure/` relativa al notebook (`studenti/figure/`); su Colab nel pannello file della VM, da scaricare.
- TIF: richiede Pillow (c'è, è una dipendenza di matplotlib). File da 600 dpi grandi: qualche visualizzatore Windows è lento.
- `verifica_figura` controlla i font ≥ 4.5 pt (minimo ACS) mentre il testo del § 6 dice "≥ 6-8 pt"; non controlla lo spessore delle barre d'errore (`elinewidth`), solo le linee.
- `ax.boxplot(labels=...)` dà `TypeError` in matplotlib 3.11 (ora `tick_labels`): chi copia esempi vecchi da internet ci cade.
- f-string + LaTeX: graffe da raddoppiare (`$x_{{50}}$`). Nel nb 06 una variabile `p` esiste (dai test), quindi `f"$i_{p}$"` sostituisce silenziosamente il valore del p-value.
- `curve_fit`: senza `p0` parte da tutti 1 → per la sigmoide può dare `RuntimeError: Optimal parameters not found: Number of calls to function has reached maxfev` o parametri assurdi; `OptimizeWarning: Covariance of the parameters could not be estimated` → `pcov` pieno di `inf` → errori standard infiniti: il fit non è identificabile, non fidarsi. Con `bounds` usa un altro algoritmo (`trf`): `p0` deve stare dentro i limiti, altrimenti `ValueError: x0 is infeasible`.
- `sigmoide` con `d = 0` → divisione per zero (`inf`, avviso): nei dati la dose minima è 0.1 µM, ma chi prova a disegnare da 0 con `np.linspace(0, ...)` vede l'avviso. Usare `np.logspace` come nel notebook.
- `stats.ttest_ind` di default `equal_var=True` (Student), al contrario di R.
- Segno delle differenze di `stats.tukey_hsd` opposto a `TukeyHSD()` di R.
- Il `rng` del box plot nell'Es. 6.2 viene da una cella precedente: chi salta celle ha `NameError`.
- Unità: nell'Es. 6.2 le concentrazioni di foglia/frutto/suolo sono in µg/L. Un chimico potrebbe obiettare che per un solido si usa mg/kg: risposta onesta "sono dati sintetici; si immagina la misura sull'estratto/digerito".

### Da verificare prima del corso (non corretti, solo segnalati)
1. *(Risolto il 14/11.)* Il commento nel nb 05 ora dice "oggi pomeriggio calcoleremo la banda vera".
2. *(Risolto il 14/11.)* Il testo dell'Es. 5.3 ora chiede `verifica_figura(fig, larghezza_max=7.5)`, come la soluzione.
3. `sorgenti/05_G3_mattina_grafici_pubblicazione.py:301` vs `materiali/figure_pubblicazione.py:208` — "Font ≥ 6-8 pt" nel testo, ma `verifica_figura` segnala solo sotto 4.5 pt: un testo a 5 pt passa il controllo pur essendo fuori norma per Elsevier.
4. `sorgenti/06_G3_pomeriggio_scipy_statistica.py:242` — "tempo di dimezzamento = τ·ln2" è il dimezzamento della **parte sopra il plateau**, non il tempo in cui la concentrazione residua passa dal valore iniziale (~90.8 %) alla metà (che, con plateau 10.5 %, è più lungo). Inoltre `C0` (riga 234) è l'ampiezza, non la concentrazione iniziale. Precisarlo a voce se un chimico lo chiede.
5. `sorgenti/06_G3_pomeriggio_scipy_statistica.py:103-104` — "dove sta la retta vera … con il 95 % di probabilità": formulazione semplificata (IC frequentista, banda puntuale e non simultanea). Va bene per la classe; uno statistico può obiettare → risposta nel glossario.
6. `sorgenti/06_G3_pomeriggio_scipy_statistica.py:418-419` — "si fa un'ANOVA e, se sì, i confronti post-hoc (Tukey)": è una prassi, ma Tukey HSD non richiede un'ANOVA significativa prima. Non è un errore, solo una sfumatura da conoscere.


---

## Giorno 4 — Preprocessing, PCA, random forest e validazione onesta

Notebook: `07_G4_mattina_preprocessing_PCA` (mattina), `08_G4_pomeriggio_random_forest_validazione` (pomeriggio).
Numeri citati sotto = output reali della versione `docente/` (scikit-learn 1.9.0, seme fisso).

### Apertura del giorno (3 righe da dire)

- "Oggi impariamo a usare PCA e random forest, ma soprattutto a capire quando un risultato non vale niente: il nostro, quello di un software, quello di un articolo."
- "Stamattina niente etichette, cerchiamo struttura; oggi pomeriggio le etichette e la domanda 'quanto mi posso fidare?'."
- "Se dovete portare a casa una sola cosa dal corso, sarà la sezione 4 di oggi pomeriggio: 100 % di accuratezza su puro rumore."

---

## MATTINA — Preprocessing, PCA, clustering (nb 07)

### Scaletta con orari

Orario del corso: 10:00–13:00 e 14:00–17:00. La mattina ha un margine di 8'; il pomeriggio non ne ha.

| Orario | Sezione | Note |
|---|---|---|
| 10:00–10:15 | Apertura, cella di avvio, §1 Flusso di lavoro, dataset `sensori_matrice.csv` | controllare che tutti stampino `scikit-learn 1.x`; schema `workflow_ml.png` |
| 10:15–10:30 | §2 `X`/`y`, mancanti, `SimpleImputer` | |
| 10:30–10:42 | §3 richiamo NumPy (`axis`, broadcasting) | **prova loro**: cambiare `axis=0` in `axis=1` e prevedere la forma |
| 10:42–11:02 | §3 `StandardScaler`, `fit`/`transform`, demo senza scaling | |
| 11:02–11:17 | Pausa | |
| 11:17–11:52 | §4 PCA: varianza spiegata, scores, loadings (biplot: una frase) | il cuore della mattina |
| 11:52–12:17 | Esercizio 7.1 (PCA sulle sole correnti) | |
| 12:17–12:37 | §5 k-means: tabella incrociata e ARI | gerarchico fuori scaletta |
| 12:37–12:45 | Es. 7.2 come demo | ponte verso il progetto finale |
| 12:45–12:52 | Riepilogo | |
| 12:52–13:00 | Margine | |

### §1 Flusso di lavoro

**Cosa dire**
- "Ogni freccia di questo schema contiene una decisione: imputare o scartare, standardizzare o no, quante componenti. Ogni decisione va scritta nel notebook, come in un quaderno di laboratorio."
- "L'ultima tappa non è 'il grafico bello', è 'quanto mi fido'. Oggi ci arriviamo."
- Per gli utenti R: "Il `DataFrame` con righe = campioni e colonne = variabili è esattamente il `data.frame` che passate a `prcomp` o a `caret::train`."

**Demo live**: eseguire le celle `df.head`, `value_counts` (20/20/20), `describe`. Far notare ad alta voce le scale diverse (conducibilità centinaia, pH ~6): servirà fra 30 minuti.

### §2 Preparare `X`, valori mancanti

**Cosa dire**
- "In `X` va solo ciò che è misura. Se l'etichetta finisce in `X`, il modello 'predice' perfettamente: è come uno studente che ha la soluzione scritta sul banco."
- Sull'imputazione: "Qui imputiamo su tutto perché non c'è un test da proteggere. Oggi pomeriggio la stessa riga, scritta senza attenzione, diventa una fuga di informazione. Tenete a mente questo 'per ora'."
- Mancanti: 3 in tutto (`i_-0.20V`, `pH`, `fenoli_tot`): "Buttare 3 righe su 60 = buttare il 5 % dei campioni per 3 numeri."

**Trappola**: `fit_transform` restituisce un array NumPy, si perdono i nomi delle colonne → la riga che ricostruisce il `DataFrame` è lì per questo. Dirlo esplicitamente, sennò i principianti si chiedono perché.

### §3 Richiamo NumPy e standardizzazione

**Cosa dire**
- `axis`: "`axis=0` è la dimensione che sparisce. `M.mean(axis=0)` consuma le righe e vi lascia una media per colonna." Mostrare le forme `(4,3)` → `(3,)`.
- Broadcasting: "NumPy 'stira' la riga delle medie su tutte le righe, come applicare la stessa correzione di bianco a ogni replica."
- Standardizzazione: "Senza standardizzare la PCA vi dice solo chi ha l'unità di misura con i numeri più grandi. Cambiate da µS a mS e cambia la PCA: un'analisi che dipende dall'unità di misura non è un'analisi."
- La varianza 1.02: anticiparla, perché qualcuno la noterà. "pandas divide per n−1, lo scaler per n: 60/59 = 1.017. In R `scale()` usa n−1, come pandas."
- `fit`/`transform`: "`fit` = lo strumento si tara; `transform` = misura con quella taratura. Oggi pomeriggio la regola sarà: si tara solo sul train."

**Demo live**
- Cella con `np.allclose(z_a_mano, X_std)` → `True`: "Lo scaler non fa magie, fa la riga di NumPy che avete scritto."
- Doppio grafico SENZA/CON standardizzazione: far leggere ad alta voce l'etichetta "PC1 dominata da: conducibilita_uS" e il 99 %.

**Esercizi**: nessuno in questa sezione. Usare 2 minuti per far cambiare `axis=0` in `axis=1` nella cella di `M` e far prevedere la forma prima di eseguire.

### §4 PCA: varianza, scores, loadings

**Cosa dire**
- Ordine di lettura, da scrivere alla lavagna: **varianza spiegata → scores → loadings**. "Senza loadings la PCA è una figura decorativa."
- Analogia: "La PCA è scegliere da quale angolo fotografare una nuvola di punti 3D perché sembri più larga possibile."
- Il messaggio chiave dei loadings di questo dataset: PC1 (36 %) ha pesi positivi e simili su tutti i 15 canali (0.30–0.31) e ~0 sulle chimico-fisiche → "Uno spostamento comune a tutti i canali è quasi sempre un effetto di misura: giornata, lotto, deriva. La componente più grande non è la più interessante."
- PC2 (22 %) separa i siti: `i_-0.25V` (+0.40) contro `conducibilita_uS`, `i_-0.10V`, `fenoli_tot` (negativi).
- Per i genetisti: "È lo stesso discorso dell'effetto lotto (*batch effect*) nelle matrici di espressione: la prima PC spesso è la piastra o il giorno di corsa, non la biologia."
- Per gli utenti R: `prcomp(X, scale. = TRUE)` ≈ `StandardScaler` + `PCA`; `$x` = scores, `$rotation` = loadings (= `pca.components_.T`). Attenzione: il segno di una PC è arbitrario, può essere invertito fra R e Python (e fra versioni): non è un errore.

**Demo live**: gomito (prime 4: 36.1, 22.1, 7.6, 5.5 %), scores, barre dei loadings, biplot. Sul biplot: "Le frecce sono riscalate a mano (`scala = 6`): la lunghezza è indicativa, l'angolo conta."

**Esercizio 7.1 (livello 2, ~20')**
- Atteso: i siti si separano ancora su PC2; PC1 sale al 48 %; PC1 dominata da `i_+0.05V`, `i_+0.10V`, `i_+0.00V`; PC2 da `i_-0.25V`, `i_-0.10V`, `i_-0.30V`.
- Errori tipici: dimenticare l'imputazione (`ValueError: Input X contains NaN` dalla PCA, c'è un NaN in `i_-0.20V`); standardizzare `df[correnti]` ma fare la PCA su `X_std` (tutte le variabili); indicizzare `S_c[y == cl, 0]` con `y` di lunghezza diversa; usare `df.columns` invece di `variabili` e includere `classe`.
- Aiuti che non svelano: "Rileggete le tre righe 1-2-3 del commento: sono tre classi di scikit-learn una dentro l'altra"; "Se l'errore parla di NaN, a quale passo li avete tolti stamattina?"; "Per le top 3: `pd.Series(..., index=correnti)`, poi ordinate per valore assoluto."
- Chiusura dell'esercizio: leggere il riquadro sulla normalizzazione per campione e rimandare a C7.1 (ARI da 0.36 a 0.86: spoiler da tenere per chi chiede).

### §5 Clustering

**Cosa dire**
- "Qui le classi le conosciamo e le usiamo per smascherare il clustering. Nel vostro lavoro, quando non le conoscete, non avrete questo controllo."
- Crosstab k-means: Maremma quasi isolata (17/20), Cascine e Vallombrosa spalmate; ARI 0.36. "Il clustering segue la varianza più grande, cioè PC1, cioè l'effetto di misura."
- Gomito e silhouette: "Sono indizi, non verdetti. Il k 'giusto' secondo la silhouette non è detto che sia 3."
- R: `kmeans(x, centers = 3, nstart = 10)` ≈ `KMeans(n_clusters=3, n_init=10)`; `hclust(dist(x), method = "ward.D2")` ≈ `linkage(..., "ward")`.

**Demo live**: gomito/silhouette, crosstab, ARI. Gerarchico (facoltativo): mostrare il dendrogramma con le foglie colorate e nella scaletta 10–13 è fuori: mostrarlo solo se alle 12:30 il k-means è già finito.

### Esercizio 7.2 (facoltativo) — ponte verso il progetto

- Consiglio: farlo come **demo** proiettata, 5-7', anche se si è in ritardo sul resto (si sacrifica il gerarchico). Prepara il terreno per il pomeriggio.
- Numeri da leggere: distanza media fra repliche dello stesso campione 4.91; fra campioni diversi della stessa classe 8.89; fra classi diverse 9.18.
- **Cosa dire**: "Le repliche sono gemelle: distano la metà di qualunque altro campione. E notate che 'stessa classe' (8.89) e 'classi diverse' (9.18) sono quasi uguali: tenetelo a mente per oggi pomeriggio."
- Domanda da lasciare aperta: "Se una gemella sta nel train e l'altra nel test, il modello riconosce la classe o riconosce la gemella?"
- Errori tipici (se lo fanno da soli): `____` di `D[____ & ~stesso_camp]` riempito con `stesso_camp` (dà array vuoto → `nan`); passare `dr` intero allo scaler (colonne `campione`/`classe` di testo → `ValueError`).
- Non dire ancora da dove viene il dataset (vedi sezione dedicata).

### Riepilogo mattina (12:45–12:52)
- Far leggere i 7 punti del riepilogo; insistere sul 7: "Una PCA che separa bene non è una prova."

---

## POMERIGGIO — Random forest, validazione, progetto finale (nb 08)

### Scaletta con orari

Orario del corso: 10:00–13:00 e 14:00–17:00. La mattina ha un margine di 8'; il pomeriggio non ne ha.

| Orario | Sezione | Note |
|---|---|---|
| 14:00–14:08 | §1 Supervisionato, random forest in due paragrafi | |
| 14:08–14:26 | §2 Train/test, 10 semi | |
| 14:26–14:46 | §3 k-fold + Esercizio 8.1 (5') | |
| 14:46–15:16 | §4 **Overfitting dal vivo** su rumore puro | non tagliare mai; al passo 3 chiedi alla sala, in coppia, dov'è l'errore prima di spiegarlo |
| 15:16–15:31 | Pausa | |
| 15:31–15:39 | §5 Metriche e matrice di confusione | |
| 15:39–15:47 | §6 Pipeline + importanza per impurità (il resto è facoltativo) | |
| 15:47–16:37 | §7 **Progetto finale** (lancio 5' + lavoro 45') | checkpoint 16:07, 16:22, 16:32; punto 5 solo proiettato |
| 16:37–16:45 | Debrief del progetto | vedi sezione "Come presentare" |
| 16:45–17:00 | §8 Chiusura del corso | |

Regola della nota docente nel notebook, adattata all'orario: **se alla pausa delle 15:16 la §4 non è finita, la si chiude dopo la pausa e si va dritti al progetto** (la §5 si recupera a voce al punto 4 del progetto).

### §1 Supervisionato e random forest

**Cosa dire**
- "Stamattina: c'è struttura? Adesso: dato un campione nuovo, di che sito è?"
- Random forest: "Cento esperti mediocri che hanno visto ognuno una parte dei dati e votano. Nessuno è bravo, la maggioranza spesso sì."
- R: `randomForest::randomForest()` / `ranger`; `caret::train(method = "rf")`; tidymodels `rand_forest() |> set_engine("ranger")`.

### §2 Train e test

**Cosa dire**
- Analogia centrale della giornata, da introdurre qui: "Valutare sul train è come dare all'esame le stesse domande dell'esercitazione: lo studente che ha imparato a memoria prende 30, ma non sappiamo se ha capito."
- "Per una random forest l'accuratezza sul train è 1.000 praticamente sempre: non è un risultato, è il modo in cui è costruita."
- Con 18 campioni di test un errore = 5.6 punti percentuali.

**Demo live**
- Prima esecuzione: train 1.000 **e test 1.000** (seme 0). Anticipare: "Fortunati? Vediamo." → cella dei 10 semi: da 0.778 a 1.000, media 0.933. "Lo stesso modello, gli stessi dati: tra 78 % e 100 % a seconda di quali 18 campioni pescate. Quale dei due numeri avreste messo nell'articolo?"
- `fit` dell'imputer **solo sul train**: indicarlo col cursore. È il primo incontro esplicito con il leakage.

### §3 Validazione crociata

**Cosa dire**
- "Invece di un solo esame, cinque esami diversi: ogni campione fa da domanda d'esame una volta sola."
- "Un'accuratezza senza il metodo con cui è stata misurata non dice niente": far copiare la frase modello *0.92 ± 0.09 (CV stratificata 5 fold, n = 60)*.
- Per R: `caret::trainControl(method = "cv", number = 5)`; `rsample::vfold_cv(v = 5, strata = classe)`; `RepeatedStratifiedKFold` ≈ `method = "repeatedcv"` / `vfold_cv(repeats = 10)`.
- Già qui la `Pipeline` con imputer: "Lo spieghiamo fra mezz'ora, per ora fidatevi: serve perché l'imputer si tari dentro ogni fold."

**Esercizio 8.1 (livello 1, 5')**
- Atteso: seme 1 → 0.933 ± 0.082; 10 fold → 0.917 ± 0.201.
- Messaggio: la media si muove poco, la sd molto (6 campioni per fold di test).
- Errori tipici: passare `cv_10` ma lasciare `n_splits=5`; usare `cv` invece di `cv_1` nella seconda riga (risultato identico al 0.917 di prima → "il seme non conta!").
- Aiuto: "Se il numero è identico al precedente, controllate quale oggetto `cv` state passando."

### §4 Overfitting dal vivo (non tagliare)

Preparazione: eseguire la cella del permutation test **prima** di arrivarci se la macchina di proiezione è lenta (vedi trappole sui tempi).

**Cosa dire, passo per passo**
- Presentazione: "30 campioni, 200 variabili tirate a caso, etichette 0/1 assegnate a caso. Non c'è niente da imparare. Chi scommette su che accuratezza otteniamo?" Far fare le scommesse a voce.
- Passo 1 (train = 1.00): "Esame con le domande viste in anticipo."
- Passo 2 (CV 0.51 ± 0.16): "La CV fa il suo lavoro: una moneta."
- Passo 3 (selezione delle 10 variabili più correlate su tutto, poi CV: **0.87**): "Questo è l'errore che conta. Abbiamo scelto le 10 domande d'esame guardando le risposte di tutti gli studenti, anche di quelli che poi sosterranno l'esame. La CV è venuta dopo, ma il danno era già fatto." Pausa di silenzio, lasciare il numero sullo schermo.
- Passo 4 (selezione dentro la Pipeline: 0.61 ± 0.16): "Stessa procedura, ma la selezione si rifà dentro ogni fold guardando solo il train."
- Perché 0.61 e non 0.50? "Con 30 campioni 0.6 su rumore è normale fluttuazione. Come lo dimostro? Test di permutazione": 0.67 vero, mescolati 0.51 ± 0.11, **p = 0.11**. "Una permutazione su dieci fa altrettanto bene per caso."
- Frase di chiusura: "Qualunque passo che guarda le etichette (selezione di variabili, scelta di parametri, togliere gli 'anomali' che stanno nella classe sbagliata) va dentro la validazione. Il modo meccanico per non sbagliare è la `Pipeline`."
- Per i genetisti (p ≫ n): "Questo è esattamente il caso di 20 000 geni e 40 pazienti: la selezione dei geni 'differenziali' fatta su tutti prima della CV. È documentato in letteratura dai primi anni 2000 (selection bias nei dati di microarray, Ambroise & McLachlan, PNAS 2002) e continua a comparire negli articoli." Collegamento al giorno 3: "Scegliere le 10 migliori su 200 è un problema di confronti multipli: fra 200 correlazioni casuali, le 10 più alte sono alte per costruzione."

**Esercizi**: nessuno in aula. C8.1 per casa (con n = 1000 l'inganno scende a 0.54) da citare come "chi vuole vedere quanti campioni servono perché l'inganno smetta".

### §5 Metriche

**Cosa dire**
- "Se il 90 % dei campioni è sano, dire sempre 'sano' vale 0.90."
- precision/recall con una frase sola: "precision = quando dico Vallombrosa, quante volte ho ragione; recall = dei Vallombrosa veri, quanti ne trovo."
- Collegamento: errori fra Cascine e Vallombrosa, Maremma recall 1.00 → "è la stessa cosa che diceva la PCA di stamattina."
- `cross_val_predict`: "ogni campione viene previsto quando era nel test." Avvertenza da dire: non si calcola l'accuratezza "media" da qui come se fosse la CV (coincide in questo caso, non in generale).

### §6 Pipeline e importanza

**Cosa dire**
- "Pipeline = la ricetta scritta. Ogni fold la riesegue da zero sul proprio train."
- R: è il `recipe()` di tidymodels (`step_impute_median`, `step_normalize`) dentro un `workflow()`; in caret il `preProcess` dentro `train`.
- Importanza: "Dice *quanto* il modello usa una variabile, non *in che direzione*, e non che la variabile sia causale. Variabili correlate si spartiscono l'importanza."
- Se il tempo c'è (facoltativo): impurità vs permutazione; le prime 4 coincidono (`i_-0.10V`, `i_-0.15V`, `i_-0.25V`, `i_-0.30V`), la 5ª cambia. Box plot per la direzione.
- Se in ritardo: solo il grafico a barre dell'importanza per impurità (serve `top3` per l'esercizio C8.2 a casa).

### §7 Progetto finale (60')

**Lancio (5', proiettato)**
- "Dataset reale trasformato (vedi sezione dedicata per cosa dire della provenienza): 36 campioni, 3 repliche ciascuno, 45 variabili, 3 classi da 12."
- "Domanda: dalle variabili si riconosce la classe? E, ancora più importante: quanto possiamo fidarci?"
- Le repliche: "È la pseudoreplicazione di ieri pomeriggio vista dal lato ML. L'unità indipendente è il campione, non la provetta."
- Mostrare le due righe di `StratifiedGroupKFold` con `groups=`. R: `caret::groupKFold()`, `rsample::group_vfold_cv(group = campione)`.
- Lavoro da soli o in coppia, a scelta. Chi vuole la sfida cancella la traccia.

**Checkpoint**
- **+15' (16:07)**: tutti hanno `(108, 45)`, 0 mancanti, 12/12/12 campioni, `[3]` repliche. Giro tra i banchi: chi ha incluso `replica` o `campione` in `X`?
- **+30' (16:22)**: tutti hanno le due CV. Dire ad alta voce: "Chi ha due numeri molto diversi? Bene, è quello che deve succedere." (senza gruppi 0.645 ± 0.146; per campione 0.437 ± 0.093; caso 0.33).
- **+40' (16:32)**: stop al codice, 5' per la conclusione in Markdown (punto 6). Il punto 5 (permutazioni) solo per chi è avanti, o lo si mostra proiettato dalla versione docente.

**Errori tipici e aiuti**
- `startswith("feature")` dimenticato → in `X` entra `campione` (testo → `ValueError: could not convert string to float`) o `replica` (0/1/2, nessun errore ma variabile spuria). Aiuto: "Stampate `Xp.columns[:5]`."
- `groupby(...)[COL_ID].count()` invece di `.nunique()` → 36 invece di 12. Aiuto: "Volete contare righe o campioni diversi?"
- `groups=` dimenticato con `StratifiedGroupKFold` → `ValueError: Cannot have number of splits n_splits=5 greater than the number of groups: 1.` Messaggio criptico (senza `groups` tutto è "un gruppo solo"): tradurlo a voce, "vi manca `groups=gruppi`".
- `cross_val_predict(..., cv=cv_n, groups=gruppi)` → nessun errore, ma la matrice è quella "sbagliata" (i gruppi vengono ignorati da `StratifiedKFold`). Aiuto: "Quale delle due CV state usando per la matrice?"
- Scaler dimenticato nella PCA (`("scaler", ____)`) → PCA dominata da una feature (scale fino a migliaia). Aiuto: "Rileggete la sezione 3 di stamattina."
- Lentezza al punto 5: dire subito `n=20`.

**Debrief (16:37–16:45)**: vedi sezione successiva. Proiettare la soluzione docente con il grafico del punto 5 (due istogrammi): "La CV senza gruppi arriva a 0.62 **anche con le classi mescolate**: quel numero misura quanto si somigliano le repliche, non le classi."

---

## Come presentare il risultato del progetto finale

**Prima del giorno 4 (entro il giorno 2-3, in privato, 10 minuti)**
- Parlare con la persona che ha fornito i dati. Punti da concordare:
  - **Se e come** citare la provenienza: (a) la persona lo dice lei stessa, (b) "un dataset pilota reale, trasformato e anonimizzato, gentilmente fornito da un collega" senza nome, (c) nessuna menzione. Default se non c'è accordo: (c).
  - Mostrarle **prima** il risultato (0.44 per campione, p ≈ 0.25; 0.65 ignorando le repliche) così non lo scopre davanti a 20 persone. Nota: dal 14/11 il README e la conclusione d'esempio non contengono più questi numeri; restano negli "Output attesi" del progetto nel notebook studenti del giorno 4, che servono per controllare il codice.
  - Chiedere se vuole intervenire nel debrief (es. "quali variabili ci aspettavamo che contassero").
  - Se la sua analisi originale usava una CV per riga: "È il default di quasi tutti i tutorial e di molti software; succede a chiunque. Se ti va, dopo il corso la riguardiamo insieme." Non chiederlo in pubblico, non insistere.
  - Rassicurare: i numeri sono trasformati colonna per colonna, nomi anonimi; non esistono in aula valori riconducibili alle misure originali. Non citare mai dominio, variabili, laboratorio, né valori originali (il docente stesso non li proietta né li nomina).

**In aula: frasi da usare**
- "È un errore che facciamo tutti, me compreso, e che trovate in articoli pubblicati: la CV per righe è il default di ogni tutorial. Oggi lo abbiamo visto con i nostri occhi, ed è il motivo per cui il progetto è su questo dataset."
- "Lo 0.65 non è 'sbagliato' nel senso che il codice abbia un errore: risponde a un'altra domanda, cioè 'riconosco una replica di un campione che ho già visto?'. La domanda scientifica è 'riconosco la classe di un campione nuovo?', e la risposta onesta è 0.44."
- "Con 36 campioni, 0.44 contro 0.33 non si distingue dal caso. Non vuol dire che non ci sia niente: vuol dire che con questi numeri non possiamo ancora dirlo."
- "Questo è un dataset pilota: serve proprio a questo, a sapere quanti campioni servono e dove guardare."

**Frasi da evitare**
- "Il risultato originale era gonfiato", "l'analisi era sbagliata", "questi dati non funzionano", "chi ha fatto questa analisi…", qualunque sguardo o riferimento alla persona.

**"Quindi i dati non servono?" — risposta**
- "No. Assenza di prova non è prova di assenza. Abbiamo 36 unità indipendenti e 45 variabili: con 12 campioni per classe l'incertezza sull'accuratezza è di circa ±8 punti, e un effetto moderato può semplicemente non vedersi."
- Cosa aiuterebbe, in ordine:
  1. **Più campioni indipendenti** per classe (non più repliche: le repliche migliorano la misura del campione, non il numero di campioni).
  2. **Selezione delle variabili a priori**, sulla base della conoscenza del dominio, decisa *prima* di guardare le etichette: 5 variabili motivate valgono più di 45 a caso (meno variabili = meno occasioni di trovare rumore).
  3. Media delle repliche per campione (estensione facoltativa 1): riduce il rumore di misura e rende esplicita l'unità statistica.
  4. Un modello più semplice (estensione 3: regressione logistica con scaler, CV per gruppi).
  5. Un gruppo di campioni tenuto da parte fin dall'inizio come test finale.
- Per i genetisti: "È il classico p ≫ n in piccolo. Un test univariato per variabile con correzione FDR è un'analisi complementare legittima, ma anche lì con 12 per gruppo la potenza è bassa."
- Se chiedono "quanti campioni servirebbero?": "Dipende dall'effetto, che non conosciamo: questo pilota serve appunto per stimarlo. L'esercizio C8.1 dà un'idea di come cambia la stabilità con n."

**Se la persona interviene**: lasciarle spazio, ringraziare, chiudere con "è esattamente l'ipotesi da verificare sul prossimo lotto di campioni".

---

## Chiusura del corso (16:45–17:00)

**Cosa dire (5')**
- "In quattro giorni avete letto file di strumenti, pulito dati veri, fatto figure da rivista, rette di taratura con le incertezze, PCA e un classificatore validato onestamente."
- Messaggi da portare a casa, uno per giorno:
  - **G1**: il codice è un quaderno di laboratorio; un traceback si legge dal basso, e si legge.
  - **G2**: i dati si puliscono in uno script, non a mano in Excel; ogni passo ripetibile.
  - **G3**: una figura e un test valgono quanto le loro incertezze; l'unità indipendente è il campione, non la replica.
  - **G4**: tutto ciò che guarda le etichette va dentro la validazione; un numero senza il metodo con cui è stato misurato non vale niente.
- "La settimana prossima": i 3 punti del notebook (Restart & Run All, rifare il progetto del G2 su un proprio file, rifare una propria figura con `figure_pubblicazione.py`).

**Python e R (5', discussione)**: la domanda del notebook, a voce. Non serve arrivare a una conclusione: "convivono, il CSV è il ponte".

**Dove andare (risorse già nel README/notebook)**
- Software Carpentry, *Plotting and Programming in Python* (basi).
- Aalto Scientific Computing, *Python for Scientific Computing* (pandas, NumPy, buone pratiche).
- Scientific Python Lectures (SciPy, statistica, scikit-learn).
- Documentazione ufficiale: "10 minutes to pandas", galleria Matplotlib, *User Guide* di scikit-learn (in particolare i capitoli su cross-validation e pipeline).
- `materiali/personalizzazione_grafici.ipynb` e `figure_pubblicazione.py`.
- Tabella "errori tipici della prima settimana": proiettarla 1 minuto.

**Soluzioni e feedback (5')**
- Distribuire le soluzioni di oggi (`docente/` / zip docente come da README punto 4): annunciarlo esplicitamente ("le avete stasera").
- Raccogliere il feedback con il modulo previsto dall'ente/organizzazione: chiedere esplicitamente "cosa togliereste" e "cosa vi è servito di più".
- Sezione "Assistenti automatici" del notebook: è nel materiale; leggerla velocemente o lasciarla alla lettura individuale, senza aggiungere indicazioni.

---

## Se sei in ritardo (ordine di taglio)

Mattina:
1. Clustering gerarchico (§5, già marcato facoltativo).
2. Biplot (§4): basta dire "esiste, è nel notebook".
3. Gomito/silhouette di k-means: mostrare solo crosstab + ARI.
4. Esercizio 7.1 ridotto a 10' (solo scores, niente loadings) o fatto come demo.
5. Esercizio 7.2: da tenere come demo di 5' se possibile; tagliarlo solo se si è oltre le 12:50.

Pomeriggio:
1. §6: importanza per permutazione, box plot, "campione nuovo" (facoltativi).
2. §6 intera (solo una frase sulla Pipeline).
3. §5 metriche: recuperarla a voce al punto 4 del progetto (regola della pausa delle 15:16).
4. Esercizio 8.1 come demo (2').
5. Progetto: punto 5 (permutazioni) solo proiettato; punto 2 (PCA) facoltativo.
6. Chiusura: tagliare la discussione Python/R, mai il riepilogo e il feedback.
- **Mai tagliare**: §4 overfitting su rumore, il punto 3 del progetto (le due CV), il debrief.

---

## Domande probabili

- **"Perché non leave-one-out? Ho pochi campioni."** LOO ha bassa distorsione ma alta varianza e non si può stratificare; con pochi campioni di solito meglio k-fold ripetuta (come in §4 con n = 30). Con le repliche, LOO per riga è la fuga peggiore: serve leave-one-*group*-out (`LeaveOneGroupOut`, già in scikit-learn).
- **"E per scegliere i parametri (n_estimators, profondità)?"** Anche la scelta dei parametri guarda le etichette: va dentro la CV → CV annidata (`GridSearchCV` dentro `cross_val_score`). In R: `tune_grid` dentro `nested_cv` / `caret` con resampling esterno.
- **"Ho 20 000 geni e 50 pazienti, cosa faccio?"** Stesso schema della §4: selezione dentro la pipeline, CV per paziente se ci sono più campioni per paziente, test di permutazione. Aspettarsi accuratezze modeste e dirlo.
- **"Il p-value del test di permutazione va corretto per confronti multipli?"** Se si provano molti modelli/preprocessing e si riporta il migliore, sì in spirito: il modo pulito è decidere il protocollo prima o tenere un test set finale.
- **"Perché 0.67 su rumore e non 0.50?"** Fluttuazione con n = 30; il test di permutazione serve proprio a dire se è compatibile con il caso (p = 0.11: sì).
- **"Che differenza c'è con il t-test di ieri?"** Ieri: c'è una differenza media fra gruppi? Oggi: posso prevedere il gruppo di un singolo campione? Si può avere la prima senza la seconda.
- **"Standardizzare serve alla random forest?"** No (gli alberi usano soglie), ma non nuoce e serve ad altri modelli; per PCA, k-means, regressione logistica sì.
- **"La PCA in Python dà segni opposti a R."** Il segno di una componente è arbitrario.
- **"Posso usare la PCA prima della CV per ridurre le variabili?"** Se non usa le etichette la fuga è lieve (come imputazione/scaling), ma il principio è lo stesso: dentro la `Pipeline` e non ci si pensa più.
- **"caret/tidymodels fanno la CV per gruppi?"** Sì: `groupKFold`, `group_vfold_cv`. Il problema non è il linguaggio ma il default.
- **"Feature importance = biomarcatori?"** No: indica cosa usa il modello, è instabile fra fold, e con un modello non distinguibile dal caso (progetto) non ha senso interpretarla (estensione 2).
- **"Accuratezza o AUC?"** Con classi bilanciate l'accuratezza è leggibile; `scoring="roc_auc"` (binario) o `"balanced_accuracy"` esistono già in `cross_val_score`.

---

## Punti delicati / trappole

- **Tempi di calcolo** (misurati su una macchina a 16 core; su un portatile a 2-4 core moltiplicare per 3-8):
  - §4 passi 2, 3, 4: ~10 s ciascuno (50 fit × 300 alberi, un solo core) → ~30-60 s su portatile lento. Durante l'attesa, parlare (scommesse sul risultato).
  - §4 `permutation_test_score` (100 permutazioni, `n_jobs=-1`): ~11 s su 16 core, ~40 s su un core solo; su portatili vecchi 1-2 minuti. Su Colab (2 core) ~1 minuto. Eseguirla in anticipo sulla macchina di proiezione o lanciarla e intanto spiegare l'istogramma.
  - Progetto punto 5: 100 CV complete (2 × 50) → ~1 minuto su 16 core, **3-8 minuti** su portatile. Dire `n=20` a tutti fin dal lancio.
- **Semi casuali**: chi cambia `random_state` o omette un seme vede numeri diversi dall'"Output atteso". Dirlo prima: "Se il vostro numero differisce alla seconda cifra decimale, va bene; conta il confronto." Con Miniforge le ultime cifre possono differire (README).
- `n_jobs=-1` su Windows può dare avvisi di joblib o rallentare per l'overhead dei processi: se un portatile si blocca, `n_jobs=1`.
- Accuratezza **test = 1.000** al primo split di §2: rischio che passi il messaggio "il modello è perfetto". Arrivare subito alla cella dei 10 semi.
- Varianza 1.02 dopo lo scaler (§3): anticiparla, sembra un errore.
- Leakage "lieve" (imputer/scaler fuori pipeline) vs "grave" (selezione con le etichette): non drammatizzare il primo, sennò i principianti concludono che la mattina era tutta sbagliata. Frase: "Stamattina non c'era un test da proteggere."
- L'estensione 1 del progetto (media delle repliche + CV normale) è corretta; chi invece fa la media **dopo** aver standardizzato su tutto non sbaglia in modo grave: non fermarsi su questo.
- Il punteggio "vero" del punto 5 (0.415, 100 alberi) è diverso da quello del punto 3 (0.437, 300 alberi): il notebook lo spiega, ma qualcuno chiederà.
- Sensibilità sul dataset: non proiettare mai `dati/` con nomi di file o percorsi personali; non fare battute sul risultato ("niente da fare", "dataset inutile").
- Chi ha installato con Colab vede `object` invece di `str`: irrilevante oggi.

---

## Da verificare prima del corso

- *(Risolto il 14/11.)* Il risultato del progetto è stato tolto dal `README.md` e la conclusione d'esempio è ora solo nella versione docente. Gli "Output attesi" del progetto nel notebook studenti contengono ancora i numeri (0.44, 0.65, p): servono ai partecipanti per controllare il codice. Tenerne conto nel colloquio privato.
- *(Risolto il 14/11.)* Il suggerimento per C7.1 nel nb 07 non indica più il centering su `X_c` già standardizzato: ora dice di centrare le correnti non standardizzate, come la soluzione (ARI 0.86).
- *(Risolto il 14/11.)* Il testo sul leave-one-out nel nb 08 ora dice che con 20-30 campioni di solito conviene una k-fold ripetuta, in accordo con la §4.
- **`sorgenti/08_G4_pomeriggio_random_forest_validazione.py:241` e `:517`** (`n_jobs=-1`): verificare i tempi su un portatile tipo dei partecipanti (Windows) prima del giorno 4.


---

