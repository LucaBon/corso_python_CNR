# %% [markdown]
# # Giorno 2, pomeriggio: pulizia, raggruppamenti, unioni e il progetto
#
# Obiettivo: dal file grezzo alla tabella pulita e aggregata, con un breve report di
# quanti dati sono stati scartati e perché. È quello che fate ogni volta che vi arriva
# un export dallo strumento, ma questa volta scritto, ripetibile e verificabile.
#
# ## 0. Cella di avvio

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def trova_dati():
    for cand in [Path("../dati"), Path("dati"), Path("corso_python_CNR/dati")]:
        if cand.exists():
            return cand
    for radice in [Path(".."), Path("."), Path("corso_python_CNR")]:
        if (radice / "genera_dati.py").exists():
            sys.path.insert(0, str(radice.resolve()))
            from genera_dati import genera_tutto
            return genera_tutto(radice / "dati")
    raise FileNotFoundError("Cartella 'dati' non trovata: carica la cartella del corso.")

DATI = trova_dati()
pd.set_option("display.width", 120)

# Ripartiamo dal punto in cui eravamo stamattina (una funzione, così è riusabile)
def carica_misure(percorso):
    df = pd.read_csv(percorso, sep=";", decimal=",", encoding="latin-1",
                     comment="#", na_values=["n.d."])
    df = df.rename(columns={"concentrazione (µg/L)": "conc_ug_L", "T (°C)": "T_C"})
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    df["operatore"] = df["operatore"].str.upper().str.replace(".", "", regex=False)
    return df

df = carica_misure(DATI / "misure_sporche.csv")
print(df.shape)
df.head(3)

# %% [markdown]
# ---
# ## 1. Valori mancanti: individuare, contare, decidere
#
# Tre passi, sempre nello stesso ordine:
# 1. Individuare: `isna()` restituisce una maschera; `.sum()` conta per colonna.
# 2. Capire perché mancano: sono a caso? Sono concentrati in un operatore, in un giorno, in
#    un analita? Da questo dipende il passo 3, e nessuna funzione lo decide per voi.
# 3. Decidere: scartare le righe (`dropna`), riempire (`fillna`), o tenerli e usare
#    funzioni che li ignorano (la media di pandas li ignora già).
#
# **Non riempite mai un mancante con 0**: 0 è una misura, "mancante" no.

# %%
print(df.isna().sum())
print(f"\nrighe con almeno un mancante: {df.isna().any(axis=1).sum()}")

# %%
# Dove mancano? Guardare prima di decidere
df[df["conc_ug_L"].isna()][["data", "campione", "analita", "operatore"]]

# %%
# Decisione: la concentrazione è la variabile di interesse -> senza, la riga non serve.
# La temperatura è accessoria -> la teniamo anche se manca.
n_prima = len(df)
df = df.dropna(subset=["conc_ug_L"])
print(f"scartate {n_prima - len(df)} righe senza concentrazione; restano {len(df)}")

# %%
# Per la temperatura scegliamo di riempire i mancanti con la mediana (scelta da dichiarare nel report):
df["T_C"] = df["T_C"].fillna(df["T_C"].median())
print(df["T_C"].isna().sum(), "mancanti in T_C dopo il riempimento")

# %% [markdown]
# ---
# ## 2. Duplicati e valori anomali
#
# **Duplicati**: righe identiche, tipiche di export ripetuti o copia-incolla. `duplicated()` le
# marca (tutte tranne la prima occorrenza), `drop_duplicates()` le toglie. Con `subset=` si
# definisce cosa vuol dire "uguale" (es. stesso campione, analita e replica).

# %%
print("righe identiche duplicate:", df.duplicated().sum())
print("stesso campione+analita+replica:", df.duplicated(subset=["campione", "analita", "replica"]).sum())
df[df.duplicated(keep=False)].sort_values(["campione", "analita"]).head(6)

# %%
n_prima = len(df)
df = df.drop_duplicates()
print(f"rimossi {n_prima - len(df)} duplicati; restano {len(df)}")

# %% [markdown]
# **Anomali**: qui non esiste una regola automatica buona per tutti. Alcune tecniche di
# individuazione, dalla più cieca alla più informata:
# - `describe()` e un box plot per vedere se ci sono code assurde;
# - regola dell'intervallo interquartile (IQR): anomalo se fuori da $[Q_1 - 1.5\,\text{IQR},\ Q_3 + 1.5\,\text{IQR}]$;
# - buon senso sul dato: un valore 20 volte la mediana del suo gruppo quasi certamente
#   non è una misura ma un errore (di unità, di diluizione, di trascrizione).
#
# Va fatto **per gruppo** (per analita, per matrice): un valore normale per il rame è
# assurdo per il cadmio. Qualunque criterio usiate, scrivetelo nel report.
#
# Le concentrazioni hanno una coda a destra (distribuzione lognormale: si vede dal box plot,
# che leggiamo in scala log). Su dati così la regola IQR si applica **ai logaritmi**: in scala
# lineare marcherebbe come anomali anche valori alti del tutto normali.
#
# La funzione `anomali_iqr` qui sotto è **già pronta: per ora usatela così com'è**. Le righe
# `groupby(...).transform(...)` le capiremo nella sezione 3; per adesso basta sapere che
# calcolano Q1 e Q3 separatamente per ogni combinazione analita × matrice.

# %%
fig, ax = plt.subplots(figsize=(6, 3))
df.boxplot(column="conc_ug_L", by="analita", ax=ax)
ax.set_yscale("log")
ax.set_ylabel("µg/L (scala log)")
fig.suptitle("")
plt.show()

# %%
def anomali_iqr(df, col="conc_ug_L", per=("analita", "matrice"), k=1.5, log=True):
    """Maschera booleana: True = anomalo secondo la regola IQR, calcolata ENTRO ogni gruppo.
    Con log=True la regola si applica a log10(valore): adatta a dati con coda a destra."""
    valori = np.log10(df[col]) if log else df[col]
    g = valori.groupby([df[c] for c in per])
    q1 = g.transform(lambda s: s.quantile(0.25))
    q3 = g.transform(lambda s: s.quantile(0.75))
    iqr = q3 - q1
    return (valori < q1 - k * iqr) | (valori > q3 + k * iqr)

df["anomalo"] = anomali_iqr(df)
print(df["anomalo"].sum(), "anomali secondo IQR (per analita x matrice)")
df[df["anomalo"]].sort_values("conc_ug_L", ascending=False)[["campione", "matrice", "analita", "conc_ug_L"]].head(8)

# %% [markdown]
# Guardate la lista: oltre ai valori assurdi (centinaia di µg/L), la regola a 1.5 IQR marca anche
# tutte le repliche di uno stesso campione. Quello è un campione davvero più alto degli altri,
# non un errore di misura. E c'è anche un valore *basso* (C033, Cu nella foglia): la regola IQR
# guarda entrambe le code, non solo i valori troppo alti. La decisione: scartiamo solo quelli oltre 3 IQR (grossolani) e
# teniamo gli altri, segnalandoli nel report.

# %%
df["grossolano"] = anomali_iqr(df, k=3.0)
print(df["grossolano"].sum(), "anomali grossolani")
n_prima = len(df)
df = df[~df["grossolano"]].drop(columns=["grossolano"])
print(f"scartati {n_prima - len(df)}; restano {len(df)}")

# %% [markdown]
# ### Esercizio 4.1: diagnosi dei mancanti (livello 2)
#
# Prima di scartare, avremmo dovuto chiederci se i mancanti sono a caso. Ripartite dal file
# grezzo (`carica_misure`) e contate i mancanti di `conc_ug_L` per operatore e per analita.
# C'è un operatore o un analita che ne ha molti più degli altri?
#
# Bastano due strumenti di stamattina: un filtro con maschera booleana e `value_counts()`.
# Lavorate su `grezzo`, non su `df`: a questo punto `df` è già senza mancanti (li abbiamo
# scartati con `dropna` sopra), quindi non trovereste nulla.

# %%
# ESERCIZIO 4.1 (livello 2)
grezzo = carica_misure(DATI / "misure_sporche.csv")
# 1. tenete solo le righe di grezzo in cui conc_ug_L manca (maschera con isna())
# 2. value_counts() sulla colonna operatore di queste righe
# 3. value_counts() sulla colonna analita
# --- SOLUZIONE ---
mancanti = grezzo[grezzo["conc_ug_L"].isna()]
print(mancanti["operatore"].value_counts())
print(mancanti["analita"].value_counts())

# %% [markdown]
# Due cose da notare:
# - **LB non compare**: non ha mancanti, quindi nessuna sua riga passa il filtro. Un conteggio
#   che non mostra gli zeri può far dimenticare un gruppo. Con `groupby` (fra poco) LB compare con 0.
# - **Contate anche il totale**: gli operatori non hanno lo stesso numero di misure
#   (`grezzo["operatore"].value_counts()`). 9 mancanti su 146 non è come 9 su 30.

# %% [markdown]
# ---
# ## 3. `groupby`: dividi, applica, ricombina
#
# Fa quello che fa la tabella pivot di Excel, ma in modo esplicito e ripetibile. Tre fasi:
#
# ![groupby](../img/groupby.png)
#
# La sintassi si legge da sinistra a destra: *"raggruppa per matrice, prendi la colonna
# concentrazione, calcola la media"*. Prima filtriamo un solo analita: una media che mescola
# Cu, Pb e Cd (scale diverse di un fattore 20) sarebbe un numero senza significato.

# %%
df[df["analita"] == "Cu"].groupby("matrice")["conc_ug_L"].mean()

# %% [markdown]
# Torniamo alla diagnosi dell'esercizio 4.1. Con `groupby` si fa in un colpo solo, e con il
# totale accanto: `size` conta le righe del gruppo, `count` solo i valori presenti, quindi la
# differenza sono i mancanti. E questa volta LB compare, con 0.

# %%
diagnosi = grezzo.groupby("operatore")["conc_ug_L"].agg(["size", "count"])
diagnosi["mancanti"] = diagnosi["size"] - diagnosi["count"]
diagnosi

# %%
# Più chiavi, più statistiche: agg con una lista
df.groupby(["analita", "matrice"])["conc_ug_L"].agg(["count", "mean", "std", "min", "max"]).round(2)

# %%
# Nomi personalizzati per le colonne risultanti, e statistiche diverse per colonne diverse
tab = df.groupby(["analita", "matrice"]).agg(
    n=("conc_ug_L", "size"),
    media=("conc_ug_L", "mean"),
    sd=("conc_ug_L", "std"),
    T_media=("T_C", "mean"),
).round(2)
tab

# %% [markdown]
# Il risultato ha un indice a più livelli (`MultiIndex`): comodo da leggere, scomodo da
# usare. `reset_index()` lo riporta a colonne normali. Conviene farlo quasi sempre prima di salvare.

# %%
tab = tab.reset_index()
tab

# %% [markdown]
# ### `transform`: un valore per gruppo, riportato su ogni riga
#
# Quando la statistica di gruppo serve riga per riga (per normalizzare rispetto alla media
# del gruppo, per calcolare uno scarto), `transform` restituisce una colonna lunga quanto il
# DataFrame originale.
#
# È esattamente quello che fa `anomali_iqr` della sezione 2: `transform` riporta Q1 e Q3 del
# gruppo su ogni riga, così ogni valore si confronta con i quartili del *suo* gruppo.

# %%
df["media_gruppo"] = df.groupby(["analita", "matrice"])["conc_ug_L"].transform("mean")
df["scarto_rel"] = (df["conc_ug_L"] - df["media_gruppo"]) / df["media_gruppo"]
df[["campione", "analita", "matrice", "conc_ug_L", "media_gruppo", "scarto_rel"]].head()

# %% [markdown]
# ### Esercizio 4.2: aggregazioni (livello 1)
#
# 1. Media e deviazione standard di `conc_ug_L` per operatore e analita.
# 2. Numero di campioni distinti analizzati per matrice (`"nunique"` sulla colonna `campione`).
# 3. Per ogni campione e analita: media delle repliche e quante repliche (`size`). Ordinate per
#    media decrescente e mostrate le prime 5.

# %%
# ESERCIZIO 4.2 (livello 1)
#> print(df.groupby(["operatore", ____])["conc_ug_L"].agg(["mean", "std"]).round(2))
#> print(df.groupby("matrice")["campione"].____())
#> per_campione = df.groupby(["campione", "analita"])["conc_ug_L"].agg(media="mean", n=____)
#> per_campione.sort_values(____, ascending=False).head()
# --- SOLUZIONE ---
print(df.groupby(["operatore", "analita"])["conc_ug_L"].agg(["mean", "std"]).round(2))
print(df.groupby("matrice")["campione"].nunique())
per_campione = df.groupby(["campione", "analita"])["conc_ug_L"].agg(media="mean", n="size")
per_campione.sort_values("media", ascending=False).head()

# %% [markdown]
# ---
# ## 4. `merge`: unire una tabella di dati a una di metadati
#
# Fa il lavoro del `CERCA.VERT`, senza le sue trappole: si dichiara la **colonna chiave** e
# pandas allinea le righe. Il parametro `how` decide cosa fare delle chiavi che non trovano
# corrispondenza.
#
# ![merge](../img/merge.png)
#
# Dopo ogni merge controllate il **numero di righe**. Se aumenta, la chiave non era
# univoca in una delle due tabelle e avete duplicato dati senza accorgervene.

# %%
meta = pd.read_excel(DATI / "metadati_campioni.xlsx")
print(meta.shape, "campioni nei metadati;", df["campione"].nunique(), "campioni nelle misure")
print("chiave univoca nei metadati?", meta["campione"].is_unique)

# %%
n_prima = len(df)
unito = pd.merge(df, meta, on="campione", how="left")
print(f"righe prima {n_prima}, dopo {len(unito)}")      # deve restare uguale con how='left' e chiave univoca
print("misure senza metadati:", unito["sito"].isna().sum())
unito.head(3)

# %%
# Quali campioni non hanno metadati?
sorted(unito.loc[unito["sito"].isna(), "campione"].unique())

# %%
# how='inner' tiene solo chi ha corrispondenza in entrambe
stretto = pd.merge(df, meta, on="campione", how="inner")
print(len(stretto), "righe con inner")

# `join` è la stessa cosa, ma allinea sugli INDICI invece che su una colonna: utile quando la
# tabella dei metadati ha il campione come indice. Nella pratica, merge(on=...) copre quasi tutti i casi.
stesso = df.join(meta.set_index("campione"), on="campione")
print(len(stesso), "righe con join (equivale a merge how='left')")

# %% [markdown]
# ### Scaricare dati da un'API e unirli ai propri
#
# > *Facoltativo: si può saltare se si è in ritardo (circa 30').*
#
# Molte banche dati (UniProt, Ensembl, NCBI…) si interrogano con un indirizzo web: si chiede un URL
# con dei parametri e si riceve una risposta, quasi sempre in **JSON**, cioè dizionari e liste uno
# dentro l'altro (quelli del giorno 1). Lo schema è sempre lo stesso:
#
# 1. la vostra tabella, con una colonna chiave (qui il nome del gene);
# 2. la chiamata all'API, con `requests`;
# 3. dal JSON a una tabella;
# 4. `merge`, e i controlli di sempre: quante righe prima e dopo, chi non ha trovato corrispondenza.
#
# L'esempio: 10 geni umani con un valore misurato (inventato), a cui aggiungiamo da UniProt il nome
# della proteina e la sua lunghezza.

# %%
misurati = pd.DataFrame({
    "gene": ["TP53", "BRCA1", "EGFR", "MYC", "Gapdh", "ACTB", "INS", "ALB", "CFTR", "HBB"],
    "log2FC": [1.8, -0.6, 2.3, 1.1, 0.1, -0.2, -1.5, 0.4, -2.1, 0.7],      # valori inventati
})
misurati

# %% [markdown]
# La chiamata. I parametri dicono a UniProt cosa cercare (`query`), quali campi restituire
# (`fields`) e in che formato. Tre buone abitudini:
# - `timeout`: se il server non risponde, dopo 30 secondi ci si arrende invece di restare bloccati;
# - `raise_for_status()`: trasforma una risposta di errore (404, 500…) in un errore Python, invece di
#   continuare con una risposta vuota;
# - **salvare la risposta** in un file: l'analisi diventa ripetibile anche quando la banca dati cambia
#   (e nel metodo si scrive la data di accesso).
#
# Qui `USA_RETE = False` usa una copia salvata nella cartella dei dati, così la cella funziona anche
# senza Internet o dietro il proxy dell'ente. Mettete `True` per fare la chiamata vera.

# %%
import json

URL = "https://rest.uniprot.org/uniprotkb/search"
query = "(" + " OR ".join(f"gene_exact:{g}" for g in misurati["gene"]) + ") AND organism_id:9606 AND reviewed:true"
parametri = {"query": query,
             "fields": "accession,gene_primary,organism_name,length,protein_name",
             "format": "json", "size": 50}
print(query)

USA_RETE = False          # True = chiamata vera; False = copia salvata in dati/
if USA_RETE:
    import requests       # serve solo per la chiamata vera
    try:
        r = requests.get(URL, params=parametri, timeout=30)
        r.raise_for_status()
        Path("uniprot_risposta.json").write_text(r.text, encoding="utf-8")    # la risposta, salvata
        risposta = r.json()
    except requests.RequestException as errore:
        print("Chiamata non riuscita:", errore, "-> uso la copia salvata")
        USA_RETE = False
if not USA_RETE:
    copia = DATI / "uniprot_esempio.json"
    if not copia.exists():
        raise FileNotFoundError("Copia salvata non trovata: mettete USA_RETE = True")
    risposta = json.loads(copia.read_text(encoding="utf-8"))

print(type(risposta), list(risposta.keys()))
print(len(risposta["results"]), "risultati per", len(misurati), "geni")

# %% [markdown]
# 11 risultati per 10 geni: teniamolo a mente. Ogni risultato è un dizionario annidato: si scende
# chiave per chiave, con `[0]` quando si incontra una lista.

# %%
primo = risposta["results"][0]
print(list(primo.keys()))
print(primo["primaryAccession"])
print(primo["genes"][0]["geneName"]["value"])
print(primo["sequence"]["length"])
print(primo["proteinDescription"]["recommendedName"]["fullName"]["value"])

# %% [markdown]
# `pd.json_normalize` appiattisce da solo i dizionari annidati (le chiavi diventano colonne con il
# punto, `sequence.length`), ma non le liste: la colonna `genes` resta una lista di dizionari.
# Quando la struttura è così, conviene scrivere una piccola funzione che estrae solo quello che serve.

# %%
pd.json_normalize(risposta["results"]).columns.tolist()

# %% [markdown]
# La funzione qui sotto è **già pronta**: leggetela riga per riga e confrontatela con la cella di
# prima, è la stessa discesa chiave per chiave. Una lista di dizionari "piatti" diventa direttamente
# un DataFrame.

# %%
def estrai(rec):
    """Da un risultato di UniProt a un dizionario con accession, gene, proteina, lunghezza."""
    return {
        "accession": rec["primaryAccession"],
        "gene": rec["genes"][0]["geneName"]["value"],
        "proteina": rec["proteinDescription"]["recommendedName"]["fullName"]["value"],
        "lunghezza_aa": rec["sequence"]["length"],
    }

uniprot = pd.DataFrame([estrai(r) for r in risposta["results"]])
uniprot

# %% [markdown]
# ### Esercizio 4.3: unire e controllare (livello 2)
#
# Ora la parte che conta: unire `misurati` e `uniprot` sulla colonna `gene` **senza perdere niente
# per strada**.
#
# 1. Fate un merge con `how="outer"` e `indicator=True`. `indicator=True` aggiunge la colonna `_merge`,
#    che per ogni riga dice dove stava la chiave: `both` (in entrambe), `left_only` (solo in
#    `misurati`), `right_only` (solo in `uniprot`). Contate i valori di `_merge`.
# 2. Stampate le righe che non sono `both`. Quali geni sono? Guardateli bene e scrivete in un
#    commento **perché** non hanno trovato corrispondenza (sono due motivi diversi).
# 3. Correggete il problema che dipende da voi: normalizzate la chiave di `misurati` (metodi `.str`
#    di stamattina) e rifate il merge con `how="left"` e `validate="one_to_one"`. Stampate le righe
#    prima e dopo e quanti geni sono rimasti senza dati UniProt (dovrebbero essere 0).

# %%
# ESERCIZIO 4.3 (livello 2): sostituisci i ____
#> controllo = pd.merge(misurati, uniprot, on="gene", how=____, indicator=____)
#> print(controllo["_merge"].value_counts())
#> print(controllo[controllo["_merge"] != ____][["gene", "log2FC", "accession", "_merge"]])
#> # Perché questi geni non hanno trovato corrispondenza?
#> # 1. ...
#> # 2. ...
#>
#> misurati["gene"] = misurati["gene"].____          # normalizzate la chiave
#> unito_api = pd.merge(misurati, uniprot, on="gene", how=____, validate="one_to_one")
#> print(f"righe prima {len(misurati)}, dopo {len(unito_api)}; senza dati UniProt: {unito_api['accession'].isna().sum()}")
# --- SOLUZIONE ---
controllo = pd.merge(misurati, uniprot, on="gene", how="outer", indicator=True)
print(controllo["_merge"].value_counts())
print(controllo[controllo["_merge"] != "both"][["gene", "log2FC", "accession", "_merge"]])
# 1. Gapdh (left_only) e GAPDH (right_only): stessa chiave scritta in modo diverso.
# 2. FBF1 (right_only): UniProt l'ha restituito per un sinonimo ("ALB"); non l'abbiamo misurato.

misurati["gene"] = misurati["gene"].str.upper()
unito_api = pd.merge(misurati, uniprot, on="gene", how="left", validate="one_to_one")
print(f"righe prima {len(misurati)}, dopo {len(unito_api)}; senza dati UniProt: {unito_api['accession'].isna().sum()}")

# %% [markdown]
# Cosa c'era da trovare, due problemi entrambi tipici:
#
# - **`Gapdh` non trova `GAPDH`**: la stessa chiave scritta in modo diverso (maiuscole, spazi, versioni
#   come `ENSG00000141510.17` contro `ENSG00000141510`). Il merge confronta i testi esattamente.
# - **Un risultato in più, FBF1**: UniProt l'ha restituito perché "ALB" è anche un suo *sinonimo*.
#   L'API ha risposto alla domanda che le abbiamo fatto, non a quella che avevamo in mente. Con
#   `how="left"` sparisce senza avvisare: va bene solo perché l'abbiamo visto prima con `outer`.
#
# La regola è quella di stamattina: dopo ogni unione si controlla chi non ha trovato corrispondenza.
# `validate="one_to_one"` aggiunge un controllo gratis: fa fallire il merge se la chiave non è
# univoca da una delle due parti.

# %%
fig, ax = plt.subplots(figsize=(6, 3.5))
ordinato = unito_api.sort_values("log2FC")
ax.barh(ordinato["gene"] + " (" + ordinato["lunghezza_aa"].astype(str) + " aa)", ordinato["log2FC"])
ax.axvline(0, color="black", lw=0.6)
ax.set_xlabel("log2 fold change (valori inventati)")
plt.show()

# %% [markdown]
# > *Estensione facoltativa*: aggiungete a `misurati` un gene a vostra scelta (es. `"KRAS"`, con un
# > valore inventato), fate la chiamata vera (`USA_RETE = True`), rifate estrazione e merge e
# > controllate con `indicator=True` che sia entrato. Quando si interrogano molti identificativi,
# > si fanno poche richieste con molti geni ciascuna (come qui, con `OR`), non una richiesta per gene
# > in un ciclo: le banche dati limitano il numero di richieste al secondo.

# %% [markdown]
# ---
# ## 5. Tabelle pivot: da "lunga" a "larga"
#
# La tabella con una riga per misura è nel formato **lungo** (*tidy*), quello giusto per
# analizzare. Quella da leggere a colpo d'occhio, con gli analiti in colonna e le matrici in
# riga, è **larga**. `pivot_table` fa la conversione (e aggrega, se ci sono più valori per cella).

# %%
larga = pd.pivot_table(df, values="conc_ug_L", index="matrice", columns="analita",
                       aggfunc="mean").round(2)
larga

# %%
# Il conteggio con i totali a margine (margins=True aggiunge riga e colonna "All")
pd.pivot_table(df, values="conc_ug_L", index="matrice", columns="analita",
               aggfunc="count", margins=True)
# I margini hanno senso per il conteggio, non per la media: una media "All" mescolerebbe
# Cd, Cu e Pb, che hanno scale diverse di un fattore 20. Pandas la calcola lo stesso: tocca a voi.

# %%
# L'operazione inversa: da larga a lunga (melt). Utile quando lo strumento esporta "largo".
larga.reset_index().melt(id_vars="matrice", var_name="analita", value_name="media_ug_L")

# %% [markdown]
# ---
# ## 6. Progetto: data wrangling (60')
#
# Dal file grezzo alla tabella pulita e aggregata, con report. Da soli o in coppia. Il
# risultato è una cella (o poche) che parte da `misure_sporche.csv` e produce:
#
# 1. `misure_pulite.csv`: una riga per misura, senza mancanti nella concentrazione, senza
#    duplicati, senza anomali grossolani (criterio a vostra scelta, ma dichiarato), con
#    operatore normalizzato, con i metadati del sito uniti, e la colonna `conc_nM` (masse
#    molari come stamattina);
# 2. `riassunto.csv`: per sito × matrice × analita, n, media, sd e la percentuale di misure
#    fuori limite (gli stessi limiti inventati di stamattina: Cu 30, Pb 10, Cd 2 µg/L);
# 3. un report stampato a video di questo tipo:
#
# ```
# REPORT PULIZIA misure_sporche.csv
#   righe lette:                311
#   - senza valore:              10
#   - duplicati:                  6
#   - anomali (>3 IQR, log):      4
#   - senza metadati sito:        N   (tenute, sito = NaN)
#   righe finali:               ...
# ```
#
# **Dataset del progetto: `dati/misure_sporche.csv`** (lo stesso di oggi), con i metadati in
# `dati/metadati_campioni.xlsx`.
#
# Struttura consigliata (livello 2; poi provate a riscriverla senza guardare):

# %%
# PROGETTO: data wrangling
# --- CONFIGURAZIONE: raccolta in alto, così per un altro file basta cambiare queste righe
FILE = DATI / "misure_sporche.csv"
COL_VALORE = "conc_ug_L"                  # la colonna di interesse (senza valore la riga si scarta)
GRUPPI_ANOMALI = ["analita", "matrice"]   # entro quali gruppi cercare gli anomali
GRUPPI_RIASSUNTO = ["sito", "matrice", "analita"]
METADATI = DATI / "metadati_campioni.xlsx"   # None se non ci sono metadati da unire
LIMITI = {"Cu": 30, "Pb": 10, "Cd": 2}       # None se non ci sono limiti
report = {}
# 1. carica (carica_misure) e registra le righe lette
# 2. togli i mancanti di COL_VALORE e registra quanti
# 3. togli i duplicati e registra quanti
# 4. marca e togli gli anomali >3 IQR (in log) per GRUPPI_ANOMALI, registra quanti
# 5. merge con i metadati (how='left'); registra quante righe senza sito
# 6. colonne derivate: conc_nM, limite, fuori_limite
# 7. salva misure_pulite.csv
# 8. riassunto per GRUPPI_RIASSUNTO: n, media, sd, % fuori limite -> riassunto.csv
#    (attenzione: groupby scarta i gruppi con chiave NaN, a meno di dropna=False)
# 9. stampa il report
#
# Traccia: sostituite i ____ (chi vuole una sfida cancelli la traccia e scriva da zero).
#> d = carica_misure(____)
#> report["righe lette"] = len(d)
#>
#> d = d.dropna(subset=[____])
#> report["senza valore"] = report["righe lette"] - len(d)
#>
#> n = len(d); d = d.____()
#> report["duplicati"] = n - len(d)
#>
#> anom = anomali_iqr(d, col=COL_VALORE, per=GRUPPI_ANOMALI, k=____)
#> report["anomali (>3 IQR, log)"] = int(anom.sum())
#> d = d[____anom]                                   # tenere le righe NON anomale
#>
#> d = pd.merge(d, pd.read_excel(METADATI), on=____, how=____)
#> report["senza metadati sito (tenute)"] = int(d["sito"].____().sum())
#>
#> mm = {"Cu": 63.55, "Pb": 207.2, "Cd": 112.41}
#> d["conc_nM"] = d[COL_VALORE] / d["analita"].map(____) * 1000
#> d["limite"] = d["analita"].map(LIMITI)
#> d["fuori_limite"] = d[COL_VALORE] > d[____]
#> d.to_csv("misure_pulite.csv", index=____)
#> report["righe finali"] = len(d)
#>
#> riassunto = d.groupby(GRUPPI_RIASSUNTO, dropna=False).agg(
#>     n=(COL_VALORE, "size"),
#>     media=(COL_VALORE, ____),
#>     sd=(COL_VALORE, ____),
#>     pct_fuori_limite=("fuori_limite", "mean"),      # media di True/False = frazione di True
#> ).reset_index()
#> riassunto["pct_fuori_limite"] = (100 * riassunto["pct_fuori_limite"]).round(1)
#> riassunto = riassunto.round(2)
#> riassunto.to_csv(____, index=False)
#>
#> print(f"REPORT PULIZIA {FILE.name}")
#> for k, v in report.items():
#>     print(f"  {k + ':':32s}{v:5d}")
#> print()
#> print(riassunto.head(10))
# --- SOLUZIONE ---
d = carica_misure(FILE)
report["righe lette"] = len(d)

d = d.dropna(subset=[COL_VALORE])
report["senza valore"] = report["righe lette"] - len(d)

n = len(d); d = d.drop_duplicates()
report["duplicati"] = n - len(d)

anom = anomali_iqr(d, col=COL_VALORE, per=GRUPPI_ANOMALI, k=3.0)
report["anomali (>3 IQR, log)"] = int(anom.sum())
d = d[~anom]

if METADATI is not None:
    d = pd.merge(d, pd.read_excel(METADATI), on="campione", how="left")
    report["senza metadati sito (tenute)"] = int(d["sito"].isna().sum())

if "analita" in d.columns:
    mm = {"Cu": 63.55, "Pb": 207.2, "Cd": 112.41}
    d["conc_nM"] = d[COL_VALORE] / d["analita"].map(mm) * 1000
if LIMITI is not None:
    d["limite"] = d["analita"].map(LIMITI)
    d["fuori_limite"] = d[COL_VALORE] > d["limite"]
d.to_csv("misure_pulite.csv", index=False)
report["righe finali"] = len(d)

statistiche = dict(n=(COL_VALORE, "size"), media=(COL_VALORE, "mean"), sd=(COL_VALORE, "std"))
if LIMITI is not None:
    statistiche["pct_fuori_limite"] = ("fuori_limite", "mean")
riassunto = d.groupby(GRUPPI_RIASSUNTO, dropna=False).agg(**statistiche).reset_index()   # dropna=False: tiene sito = NaN
if LIMITI is not None:
    riassunto["pct_fuori_limite"] = (100 * riassunto["pct_fuori_limite"]).round(1)
riassunto = riassunto.round(2)
riassunto.to_csv("riassunto.csv", index=False)

print(f"REPORT PULIZIA {FILE.name}")
for k, v in report.items():
    print(f"  {k + ':':32s}{v:5d}")
print()
print(riassunto.head(10))

# %% [markdown]
# > *Estensioni facoltative* (in ordine di difficoltà):
# > 1. Aggiungete al riassunto la colonna `mediana`, e il coefficiente di variazione `cv = sd/media`.
# > 2. Salvate il riassunto in Excel con un foglio per analita (`pd.ExcelWriter`).
# > 3. Trasformate tutto in una funzione `pulisci(percorso_file)` che restituisce `(d, riassunto, report)`,
# >    e chiamatela. Così la potrete riusare sul prossimo export.
# > 4. Fate un grafico a barre della media per sito, un pannello per analita (anticipo di domani).

# %% [markdown] tags=["solo-docente"]
# #### Soluzioni delle estensioni (solo versione docente)
#
# Partono da `d` (la tabella pulita del progetto) e usano nomi nuovi, così non toccano
# `riassunto.csv` né le variabili usate negli esercizi per casa.

# %% tags=["solo-docente"]
# ESTENSIONE 1: mediana e coefficiente di variazione
riassunto_ext = d.groupby(GRUPPI_RIASSUNTO, dropna=False).agg(
    n=(COL_VALORE, "size"),
    media=(COL_VALORE, "mean"),
    mediana=(COL_VALORE, "median"),
    sd=(COL_VALORE, "std"),
).reset_index()
riassunto_ext["cv"] = riassunto_ext["sd"] / riassunto_ext["media"]   # adimensionale; NaN se n = 1
riassunto_ext.round(2).head()

# %% tags=["solo-docente"]
# ESTENSIONE 2: un foglio Excel per analita
with pd.ExcelWriter("riassunto_per_analita.xlsx") as writer:
    for analita, blocco in riassunto_ext.groupby("analita"):
        blocco.round(2).to_excel(writer, sheet_name=analita, index=False)
print(pd.ExcelFile("riassunto_per_analita.xlsx").sheet_names)

# %% tags=["solo-docente"]
# ESTENSIONE 3: tutto il progetto in una funzione riusabile
def pulisci(percorso, metadati=METADATI, limiti=LIMITI):
    """Dal file grezzo alla tabella pulita. Restituisce (tabella, riassunto, report)."""
    rep = {}
    t = carica_misure(percorso)
    rep["righe lette"] = len(t)

    t = t.dropna(subset=[COL_VALORE])
    rep["senza valore"] = rep["righe lette"] - len(t)

    n = len(t)
    t = t.drop_duplicates()
    rep["duplicati"] = n - len(t)

    anom = anomali_iqr(t, col=COL_VALORE, per=GRUPPI_ANOMALI, k=3.0)
    rep["anomali (>3 IQR, log)"] = int(anom.sum())
    t = t[~anom]

    if metadati is not None:
        t = pd.merge(t, pd.read_excel(metadati), on="campione", how="left")
        rep["senza metadati sito (tenute)"] = int(t["sito"].isna().sum())

    stat = dict(n=(COL_VALORE, "size"), media=(COL_VALORE, "mean"), sd=(COL_VALORE, "std"))
    if limiti is not None:
        t["fuori_limite"] = t[COL_VALORE] > t["analita"].map(limiti)
        stat["pct_fuori_limite"] = ("fuori_limite", "mean")
    rias = t.groupby(GRUPPI_RIASSUNTO, dropna=False).agg(**stat).reset_index()
    if limiti is not None:
        rias["pct_fuori_limite"] = 100 * rias["pct_fuori_limite"]
    rep["righe finali"] = len(t)
    return t, rias.round(2), rep

t2, rias2, rep2 = pulisci(FILE)
print(rep2)
print("stesso report del progetto?", rep2 == report)

# %% tags=["solo-docente"]
# ESTENSIONE 4: media per sito, un pannello per analita
# (le scale sono diverse fra analiti: sharey=False, ogni pannello ha il suo asse y)
per_sito = d.groupby(["analita", "sito"])[COL_VALORE].mean()    # groupby scarta sito = NaN
analiti = sorted(d["analita"].unique())
fig, axes = plt.subplots(1, len(analiti), figsize=(10, 3))
for ax, analita in zip(axes, analiti):
    valori = per_sito.loc[analita]
    ax.bar(valori.index, valori.values)
    ax.set_title(analita)
    ax.set_ylabel("media / µg/L")
    ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## Riepilogo del giorno 2
#
# | Problema | In R (dplyr / tidyr) | In pandas |
# |---|---|---|
# | mancanti | `is.na()`, `drop_na()`, `replace_na()` | `isna().sum()` → capire perché → `dropna(subset=)` / `fillna()` |
# | duplicati | `duplicated()`, `distinct()` | `duplicated()`, `drop_duplicates(subset=)` |
# | anomali | – | box plot per gruppo, regola IQR per gruppo (sui log se la coda è a destra), e buon senso |
# | statistiche per gruppo | `group_by() %>% summarise()` | `groupby(...).agg(...)`, `reset_index()` |
# | valore di gruppo su ogni riga | `group_by() %>% mutate()` | `transform` |
# | unire tabelle | `left_join()`, `inner_join()` | `merge(on=, how=)`, e poi controllare il numero di righe |
# | dati da un'API | `httr2`, `jsonlite` | `requests.get(...).json()`, poi una funzione che estrae, poi `merge` |
# | da lungo a largo | `pivot_wider()`; inverso `pivot_longer()` | `pivot_table`; inverso `melt` |
# | tempo (per casa) | `lubridate`, `slider` | `set_index("timestamp")`, `resample("1h").mean()`, `rolling` |
#
# La catena `%>%` di R ha un equivalente: i metodi di pandas si concatenano con il punto,
# `df.dropna(subset=["x"]).groupby("g")["x"].mean()`, anche su più righe dentro parentesi tonde.
#
# Ogni scelta di pulizia (cosa avete scartato, con quale criterio, cosa avete riempito) deve
# restare **scritta nel codice e nel report**. Così fra sei mesi voi stessi, o un collega,
# potrete rifarla.
#
# Domani: figure per la pubblicazione, poi regressione con le incertezze, fit non lineari e statistica.

# %% [markdown]
# ---
# ## Esercizi per casa (facoltativi)
#
# Per chi vuole più pratica. Sotto ogni esercizio c'è l'output atteso.

# %% [markdown]
# ### Esercizio C4.1: merge e aggregazione per sito (livello 2)
#
# Con la tabella `unito`: media di ogni analita per sito, escludendo le misure senza sito.
# Poi aggiungete la colonna `giorni_da_campionamento` = `data` − `data_campionamento` in giorni
# (`.dt.days` sulla differenza) e stampatene minimo e massimo. Un minimo negativo vorrebbe dire
# un errore nelle date: controllatelo sempre.

# %%
# ESERCIZIO C4.1 (livello 2)
# 1. filtra le righe con sito non mancante
# 2. groupby sito, analita -> media (round 2)
# 3. differenza fra date -> .dt.days
# --- SOLUZIONE ---
con_sito = unito[unito["sito"].notna()].copy()
print(con_sito.groupby(["sito", "analita"])["conc_ug_L"].mean().round(2))
con_sito["giorni_da_campionamento"] = (con_sito["data"] - con_sito["data_campionamento"]).dt.days
print("ritardo analisi: min", con_sito["giorni_da_campionamento"].min(),
      "max", con_sito["giorni_da_campionamento"].max(), "giorni")

# %% [markdown]
# ---
# ## Approfondimento per casa: serie temporali, `DatetimeIndex` e `resample`
#
# Se avete un sensore che registra ogni 10 minuti, prima o poi vorrete la media oraria o
# giornaliera. Con un indice di tipo data, `resample("1h")` raggruppa per intervallo di tempo:
# in pratica è un `groupby` sul tempo.

# %%
serie = pd.read_csv(DATI / "sensore_serie.csv", parse_dates=["timestamp"])
serie = serie.set_index("timestamp")
print(serie.shape, serie.index.min(), serie.index.max())
print("mancanti:", serie["segnale_uA"].isna().sum())
serie.head(3)

# %%
oraria = serie.resample("1h").mean()
giornaliera = serie.resample("1D").agg(["mean", "min", "max"])
print(giornaliera.round(2))

# %%
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(serie.index, serie["segnale_uA"], lw=0.5, alpha=0.5, label="10 min")
ax.plot(oraria.index, oraria["segnale_uA"], lw=1.5, label="media oraria")
ax.set_ylabel("segnale / µA")
ax.legend()
plt.show()

# %%
# Media mobile, selezione per intervallo di date con .loc sull'indice temporale
serie["mobile_1h"] = serie["segnale_uA"].rolling("1h").mean()
serie.loc["2026-03-04 08:00":"2026-03-04 09:00"].head(4)
