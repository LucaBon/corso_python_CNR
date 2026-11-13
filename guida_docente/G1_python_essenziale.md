# Guida del docente

## Giorno 1 — Python essenziale; funzioni, errori, file e NumPy

Notebook: `studenti/01_G1_mattina_python_essenziale.ipynb` (mattina), `studenti/02_G1_pomeriggio_funzioni_file_numpy.ipynb` (pomeriggio).
Sorgenti con le soluzioni: `sorgenti/01_G1_...py`, `sorgenti/02_G1_...py`. Proietta solo i notebook di `studenti/`, mai quelli di `docente/`.
I notebook non danno orari, a parte "Prova tu (2')" nel §1 della mattina: gli orari qui sotto sono una proposta su 9:00–12:30 e 14:00–17:00.

Obiettivo da ripetere a fine giornata: *"Oggi avete scritto uno script che apre 12 file di uno strumento, estrae un numero da ciascuno e salva una tabella. Domani la apriamo con pandas in una riga."*

---

## Primi 15 minuti del corso (9:00–9:15)

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

# MATTINA (9:00–12:30): Python essenziale

## 1. Scaletta

| orario | sezione del notebook | modalità | min |
|---|---|---|---|
| 9:00 | Primi 15 minuti (vedi sopra) | spiego | 15 |
| 9:15 | Benvenuti: "Cosa NON faremo", "Python o R?" | spiego | 15 |
| 9:30 | §0 Cella di avvio + §1 JupyterLab (+ "Prova tu" 2') | demo live | 15 |
| 9:45 | §2 Variabili e tipi, conversioni, f-string | demo live | 20 |
| 10:05 | Esercizio 1.1 | esercizio | 10 |
| 10:15 | §3 Liste, slicing, tuple | demo live | 15 |
| 10:30 | Esercizio 1.2 | esercizio | 15 |
| 10:45 | Pausa | | 15 |
| 11:00 | §4 Dizionari | demo live | 10 |
| 11:10 | §5 prime tre celle (`for`, `for` + `if`, filtro con `append`) | demo live | 10 |
| 11:20 | Esercizio 1.3 (torna su al §4) | esercizio | 10 |
| 11:30 | §5 Confronti, `range` / `enumerate` / `zip` | demo live | 15 |
| 11:45 | Esercizio 1.4 | esercizio | 20 |
| 12:05 | §6 List comprehension + Esercizio 1.5 | demo + esercizio | 15 |
| 12:20 | Riepilogo + "Trappole per chi viene da R" | spiego | 10 |

Nota: l'esercizio 1.3 (nel §4) usa `for`/`if`, che il notebook introduce solo nel §5. Per questo la scaletta mostra prima le tre celle del §5 e poi torna a 1.3. In alternativa fai 1.3 insieme, alla lavagna, come anteprima del `for`.

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
| 14:30 | §2 Import e librerie | demo live | 10 |
| 14:40 | §3 Traceback, i 6 errori, `try`/`except` | demo live | 15 |
| 14:55 | Esercizio 2.2 Caccia al bug | esercizio | 20 |
| 15:15 | §4 `pathlib`, `read_text`, metodi delle stringhe | demo live | 15 |
| 15:30 | Pausa | | 15 |
| 15:45 | Esercizio 2.3 (**facoltativo**) | esercizio | 15 |
| 16:00 | §5 NumPy: array, `loadtxt`, primo grafico, maschere, NaN | demo live | 25 |
| 16:25 | §6 Picco netto + Esercizio 2.4 | demo + esercizio | 25 |
| 16:50 | Grafico di controllo sulla tabella + Riepilogo del giorno 1 | demo live | 10 |

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
- **Il segno meno tipografico `−`** nel markdown (02: righe 408, 463, 486, 557). Copiandolo nel codice: `SyntaxError: invalid character '−' (U+2212)`.
- **Windows**: `read_text`/`write_text` hanno `encoding="utf-8"` esplicito, quindi non ci sono problemi. Se qualcuno scrive il proprio codice senza encoding e mette `µ` nel CSV, su Windows può comparire testo illeggibile. Dì: "indicate sempre l'encoding".
- `np.loadtxt(file, skiprows=9)` funziona per S01–S12 (header di 7 righe). Il file S13 ha 6 righe di header (manca "Scan rate"), ma il notebook non lo legge mai con `loadtxt`.

---

## Da verificare prima del corso
1. **`sorgenti/01_G1_mattina_python_essenziale.py:296-311`**: l'esercizio 1.3 (§4) usa `for`/`if`/`else` prima che vengano introdotti nel §5 (riga 315). Lo scaffold `#>` dà la struttura, ma i principianti non l'hanno ancora vista. Decidi se cambiare l'ordine in aula (come nella scaletta sopra) o presentarlo come anteprima.
2. **`sorgenti/02_G1_pomeriggio_funzioni_file_numpy.py:463, 486, 557`**: soglie scritte con `−` (U+2212) nel testo. Non è un bug del codice, ma è una trappola di copia-incolla per l'esercizio 2.4.
3. **`sorgenti/02_G1_pomeriggio_funzioni_file_numpy.py:473`**: "circa 0.13 µA" come sovrastima costante. Dall'estensione 3 risulta 0.119 per S01 e 0.134 per S08. Va bene come "circa", ma se qualcuno fa il conto, ti conviene dire "0.12–0.13".
4. **Zip dei partecipanti (`dist/corso_python_CNR_partecipanti.zip`)**: contiene la cartella `corso_python_CNR/`. Le istruzioni chiedono di scompattarlo "nello stesso posto" della cartella di installazione, ma su Windows "Estrai tutto" propone una sottocartella. Prepara una frase precisa da dire o da scrivere alla lavagna (es. "estraete in Documenti, non in Documenti\corso_python_CNR_partecipanti").
5. Fai girare su Colab, almeno una volta, i due notebook `studenti/` del giorno 1 con lo zip dei partecipanti, per controllare che la cella di avvio trovi `corso_python_CNR/dati` dopo `!unzip`.
