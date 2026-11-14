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
