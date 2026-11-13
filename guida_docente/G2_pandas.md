## Giorno 2 — Pandas: dal file grezzo alla tabella pulita, aggregata e documentata

Notebook: `studenti/03_G2_mattina_pandas_essenziale.ipynb` (mattina), `studenti/04_G2_pomeriggio_pandas_avanzato_progetto.ipynb` (pomeriggio). Tu proietti la versione **studenti** e tieni aperta la `docente/` solo sul tuo schermo.

### Apertura del giorno (5')
- **Ieri**: tipi, liste, dizionari, cicli; poi funzioni, traceback, `pathlib`, lettura dei file DPV, array NumPy con maschere e NaN, e il ciclo sulla cartella che ha scritto `riassunto_dpv.csv` "a mano", riga per riga.
- **Oggi**: lo stesso lavoro con pandas in una riga, e poi tutto il resto: leggere un CSV "italiano" sporco, filtrare, creare colonne, pulire, raggruppare, unire tabelle.
- **Obiettivo di fine giornata**: una cella che parte dal file grezzo e produce tabella pulita, riassunto e un report di cosa è stato scartato e perché. Scritto, ripetibile, verificabile.

---

## MATTINA — `03_G2_mattina_pandas_essenziale` (9:00–12:30)

Il notebook non indica tempi per sezione: la scaletta qui sotto è una proposta.

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 9:00–9:10 | Apertura + §0 cella di avvio (tutti vedono `pandas 3.x`?) | spiego | 10 |
| 9:10–9:20 | §1 DataFrame e Series | demo live | 10 |
| 9:20–9:25 | §2 leggere il file di ieri | demo live | 5 |
| 9:25–9:50 | §3 `read_csv` sul CSV sporco (errore vero → parametri) | demo live | 25 |
| 9:50–10:10 | §4 ispezione (shape/info/describe/value_counts), rename, date | demo live | 20 |
| 10:10–10:20 | §5 `read_excel` e scrittura | demo live | 10 |
| 10:20–10:45 | §6 selezione: `[]`, `loc`/`iloc`, filtri booleani | spiego + demo live | 25 |
| 10:45–11:00 | Esercizio 3.1 | esercizio | 15 |
| 11:00–11:15 | Pausa | | 15 |
| 11:15–11:40 | §7 colonne derivate, `map`, `.str`, `.dt`, `apply`/`pd.cut`/`np.where` | demo live | 25 |
| 11:40–12:00 | Esercizio 3.2 | esercizio | 20 |
| 12:00–12:20 | Esercizio 3.3 (livello 3, da zero) | esercizio | 20 |
| 12:20–12:30 | Grafico di controllo + riepilogo + trappole per chi viene da R | spiego | 10 |

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

**Grafico di controllo + riepilogo (12:20)**
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

Il notebook indica due tempi: **API UniProt circa 30', facoltativo** e **Progetto 60'**. Con 165' utili il pomeriggio è il più denso del corso. La scaletta qui sotto contiene l'API in versione compressa (25'). **Se alle 15:15 sei già in ritardo di più di 10', salta l'API.**

### 1. Scaletta

| orario | sezione | modalità | min |
|---|---|---|---|
| 14:00–14:05 | §0 cella di avvio (`carica_misure`: la mattina in una funzione) | spiego | 5 |
| 14:05–14:15 | §1 mancanti: individuare, capire, decidere | demo live | 10 |
| 14:15–14:30 | §2 duplicati e anomali (IQR per gruppo, sui log) | demo live | 15 |
| 14:30–14:40 | Esercizio 4.1 | esercizio | 10 |
| 14:40–14:55 | §3 `groupby` / `agg` / `transform` | spiego + demo live | 15 |
| 14:55–15:05 | Esercizio 4.2 | esercizio | 10 |
| 15:05–15:15 | §4 `merge` con i metadati | demo live | 10 |
| 15:15–15:30 | Pausa | | 15 |
| 15:30–15:55 | API UniProt → JSON → merge + Esercizio 4.3 (**facoltativo**) | demo live + esercizio | 25 |
| 15:55–16:00 | §5 pivot / melt | demo live | 5 |
| 16:00–17:00 | §6 Progetto wrangling (incluso 10' di chiusura) | progetto | 60 |

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

### 3. Progetto data wrangling (60', 16:00–17:00)

**Lancio (primi 2 minuti, da dire così)**
- "Avete tutti i pezzi: ora li mettete in fila, in **una cella**, partendo dal file grezzo. Da soli o in coppia, come preferite."
- "Tre prodotti: `misure_pulite.csv`, `riassunto.csv` per sito × matrice × analita, e il report stampato a video."
- "La configurazione è in alto: `FILE`, `COL_VALORE`, i gruppi, i limiti. Per un altro export basterà cambiare quelle righe."
- "C'è una traccia con i `____`. Chi vuole la sfida cancella la traccia e scrive da zero. Il controllo finale è il report: **311 / 10 / 6 / 4 / 25 / 291**." (Scrivi questi numeri alla lavagna.)

**Girare fra i banchi**
- Primo giro (16:02–16:10): solo per verificare che tutti abbiano **eseguito la cella di avvio e quella di `anomali_iqr`** (sono necessarie; chi ha riavviato il kernel dopo la pausa non ha `carica_misure` né `anomali_iqr` → `NameError`).
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

**Checkpoint a 20' (16:20)**
- Ad alta voce: "A che punto siete? Dovreste avere almeno i passi 1-4: righe lette, senza valore, duplicati, anomali. Se il report dice 311, 10, 6, 4, siete in linea."
- Chi è indietro: mostra sul proiettore solo i passi 1-3 della traccia compilati (non la soluzione intera).

**Checkpoint a 40' (16:40)**
- "Ora dovreste avere il merge (25 senza sito) e `misure_pulite.csv` salvato. Chi ha finito passa alle estensioni, nell'ordine: mediana e CV, Excel con un foglio per analita, funzione `pulisci`, grafico."
- Chi è ancora fermo al merge: "Fate il riassunto anche senza `pct_fuori_limite`, poi lo aggiungete."

**Chiusura (16:50–17:00)**
- 16:50: chiedi a **un volontario** (meglio uno che ha usato la traccia, non il più veloce) di proiettare il suo report. Confronto con 311/10/6/4/25/291. Se qualcuno ha numeri diversi, è materiale prezioso: "Quale scelta avete fatto diversamente?"
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
