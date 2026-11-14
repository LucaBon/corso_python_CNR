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
