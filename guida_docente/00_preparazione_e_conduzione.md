# Guida del docente: Python e Analisi Dati per Ricercatori CNR

4 giorni × 6 ore · 20 partecipanti · settimana del 16/11/2026

Come usare questa guida: la **Parte A** si legge una volta questa settimana. Le **Parti G1-G4** si
stampano e si tengono sul leggio, una per giorno. Gli orari sono indicativi (9:00-12:30 e
14:00-17:00, con 15' di pausa): adattali all'orario reale dell'aula.

---

# Parte A: preparazione e conduzione dell'aula

## A1. Checklist della settimana prima

**Materiali**
- [ ] **Rigenera gli zip.** I notebook sono stati ricompilati il 12/11 alle 17:14, mentre gli zip in
      `dist/` sono dell'11/11 alle 18:13, quindi sono vecchi:
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

## A9. Da sistemare prima di lunedì (raccolto rileggendo i notebook)

**Priorità alta**
1. **Il risultato del progetto finale è già nello zip dei partecipanti.** `README.md` (riga 92, tabella
   dataset) e la conclusione d'esempio con l'"Output atteso" del progetto in `sorgenti/08…py` (righe
   492-545) contengono 0.44 / p≈0.25 / 0.65 senza gruppi. Chi ha fornito i dati può leggerli prima
   del giorno 4. Decidi se togliere quei numeri dalla versione studenti (tag `solo-docente`) oppure
   accettarlo e parlarne con quella persona prima del corso.
2. **Rigenera gli zip** (`pacchetto`): quelli in `dist/` sono precedenti all'ultima build.
3. **Es. 5.3** (`05…py:368-369`): `verifica_figura(fig)` su una figura larga 7.48 in segnala un
   avviso a tutti, perché il limite di default è 7.0 (`figure_pubblicazione.py:208`); la soluzione
   usa `larghezza_max=7.5`. Avvisa la sala o aggiungi il parametro alla traccia.
4. **Suggerimento di C7.1 / es. 7.2** (`07…py:340`): centra per riga `X_c`, che è già standardizzato,
   mentre la soluzione (`:511-513`) centra i dati grezzi. Il risultato non coincide con l'output
   atteso (ARI ≈ 0.95 contro 0.86).

**Priorità media**
5. Segno meno tipografico "−" nelle soglie `E < −0.45 V` (`02…py:463, 486, 557`): chi lo copia nel
   codice ottiene `SyntaxError: invalid character '−'`. Dillo in aula o sostituiscilo con "-".
6. L'es. 1.3 (`01…py:296-311`) usa `for`/`if` prima del §5, dove vengono spiegati: anticipali a voce.
7. `05…py:190` dice "domani calcoleremo la banda vera", ma la banda arriva lo stesso pomeriggio (nb 06).
8. Formulazioni statistiche del nb 06 da limare: la banda di confidenza descritta come "probabilità
   95 %" (`:103-104`), dove è frequentista e punto per punto; il tempo di dimezzamento τ·ln2 (`:242`),
   che vale solo per la parte sopra il plateau; l'ANOVA presentata come obbligatoria prima di Tukey
   (`:418-419`).
9. `08…py:134-135`: il leave-one-out è descritto come "spesso l'unica scelta" con 20-30 campioni.
   È discutibile e contraddice il k-fold ripetuto usato poco dopo (`:205`).
10. Prova i tempi di `permutation_test_score` e del punto 5 del progetto su un portatile Windows
    medio: su una macchina potente ci vogliono 11 s e 1 minuto, sui portatili potrebbero volerci 3-8 minuti.
11. `requests` (sezione API, solo con `USA_RETE = True`) non è dichiarato in `environment.yml`:
    controllalo sull'ambiente Miniforge.
12. Windows, "Estrai tutto": lo zip dei partecipanti può finire in una cartella annidata invece di
    unirsi a quella dell'installazione. Prevedilo nelle istruzioni del giorno 1.
