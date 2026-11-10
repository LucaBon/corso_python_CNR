"""
genera_dati.py: genera tutti i dataset sintetici del corso nella cartella `dati/`.

Uso:   python genera_dati.py            (dalla radice del corso)
oppure, da un notebook:  from genera_dati import genera_tutto; genera_tutto()

Tutti i dati sono generati con seme fisso (42): rilanciando lo script si
ottengono ESATTAMENTE gli stessi file, quindi gli "output attesi" nei notebook
restano validi.

Tema: sensori elettrochimici e matrici biologiche (foglie, frutti, suoli).
Quando arriveranno i dataset del gruppo, basta salvarli in `dati/` e cambiare
il nome del file nella cella di ingresso dei progetti (giorno 2 e giorno 4).
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEME = 42


def _cartella(base):
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    return base


# --------------------------------------------------------------------------
# 1. Cartella di file "da strumento": 12 voltammogrammi DPV con header
#    (giorno 1 pomeriggio: parsing, ciclo su cartella, tabella riassuntiva)
# --------------------------------------------------------------------------
def genera_strumento(base):
    rng = np.random.default_rng(SEME)
    cart = _cartella(Path(base) / "strumento")
    E = np.round(np.linspace(-0.6, 0.2, 161), 3)
    conc = [0.5, 1, 2, 5, 10, 20, 50, 100, 5, 10, 20, 50]
    matrici = ["tampone"] * 8 + ["estratto foglia"] * 4
    date = ["12/03/2026"] * 8 + ["13/03/2026"] * 4
    for k, (c, m, d) in enumerate(zip(conc, matrici, date), start=1):
        fondo = 0.8 + 0.4 * (E + 0.6) + (0.3 if m != "tampone" else 0)
        picco = (0.42 * c + 0.15) * np.exp(-((E + 0.22) / 0.06) ** 2)
        i = fondo + picco + rng.normal(0, 0.03 + 0.002 * c, E.size)
        righe = [
            "# Strumento: PalmSens4 (DPV)",
            f"# Campione: S{k:02d}",
            f"# Data: {d}",
            f"# Matrice: {m}",
            f"# Concentrazione nominale (uM): {c}",
            "# Scan rate (mV/s): 50",
            "# Elettrodo: SPCE",
            "",
            "E(V)\ti(uA)",
        ]
        righe += [f"{e:.3f}\t{v:.4f}" for e, v in zip(E, i)]
        (cart / f"DPV_S{k:02d}.txt").write_text("\n".join(righe) + "\n", encoding="utf-8")
    # un file "rotto" per l'estensione facoltativa: riga mancante e virgola decimale
    testo = (cart / "DPV_S03.txt").read_text(encoding="utf-8")
    rotto = testo.replace("# Scan rate (mV/s): 50\n", "").replace(".", ",", 40)
    (cart / "DPV_S13_malformato.txt").write_text(rotto, encoding="utf-8")
    return cart


# --------------------------------------------------------------------------
# 2. CSV "sporco" in formato italiano (giorno 2)
# --------------------------------------------------------------------------
def genera_misure_sporche(base):
    """Disegno realistico: ogni CAMPIONE ha una matrice fissa, una data di campionamento e
    un sito; ogni campione viene analizzato per i 3 analiti, in 2-3 repliche, qualche giorno
    DOPO il campionamento. Le repliche dello stesso campione si somigliano (effetto campione)."""
    rng = np.random.default_rng(SEME)
    n_camp = 40
    campioni = [f"C{k:03d}" for k in range(1, n_camp + 1)]
    fattore_matrice = {"foglia": 3.0, "frutto": 1.6, "suolo": 5.5}
    analiti = {"Cu": 25, "Pb": 8, "Cd": 1.5}
    operatori = ["MR", "LB", "GF", "gf", "M.R."]   # nomi non uniformi: da pulire
    # --- metadati per campione (sito, quota, data di campionamento)
    matrice_camp = rng.choice(list(fattore_matrice), size=n_camp)
    sito_camp = rng.choice(["Cascine", "Vallombrosa", "Maremma", "Chianti"], size=n_camp)
    quota_camp = rng.integers(20, 950, size=n_camp)
    data_camp = pd.to_datetime("2026-01-05") + pd.to_timedelta(rng.integers(0, 20, n_camp), unit="D")
    righe = []
    for k, camp in enumerate(campioni):
        mat = matrice_camp[k]
        data_analisi = data_camp[k] + pd.Timedelta(days=int(rng.integers(3, 40)))
        op = rng.choice(operatori)
        for an, base_an in analiti.items():
            livello = base_an * fattore_matrice[mat] / 3 * rng.lognormal(0, 0.30)   # effetto campione
            for rep in range(1, int(rng.integers(2, 4)) + 1):
                conc = livello * rng.lognormal(0, 0.08)                              # ripetibilità
                righe.append([data_analisi.strftime("%d/%m/%Y"), camp, mat, rep, an,
                              conc, rng.normal(22.5, 1.2), op])
    df = pd.DataFrame(righe, columns=["data", "campione", "matrice", "replica",
                                       "analita", "conc_ug_L", "temperatura_C", "operatore"])
    n = len(df)
    # sporcizia controllata
    idx = rng.choice(np.arange(1, n), 18, replace=False)
    df.loc[idx[:10], "conc_ug_L"] = np.nan          # 10 mancanti
    df.loc[idx[10:14], "temperatura_C"] = np.nan    # 4 mancanti
    df.loc[idx[14:18], "conc_ug_L"] *= 20           # 4 anomali grossolani (errore di unita')
    df["conc_ug_L"] = df["conc_ug_L"].round(2)
    df["temperatura_C"] = df["temperatura_C"].round(1)
    dup = rng.choice(np.setdiff1d(np.arange(n), idx), 6, replace=False)
    df = pd.concat([df, df.iloc[dup]], ignore_index=True)  # 6 duplicati esatti
    df = df.sample(frac=1, random_state=SEME).reset_index(drop=True)
    # la prima riga di dati deve essere completa: il nb 03 commenta l'errore "Expected 1 fields in line 5, saw 3"
    assert df.loc[0, ["conc_ug_L", "temperatura_C"]].notna().all()
    conc_txt = df["conc_ug_L"].map(lambda v: "n.d." if pd.isna(v) else f"{v:.2f}".replace(".", ","))
    temp_txt = df["temperatura_C"].map(lambda v: "" if pd.isna(v) else f"{v:.1f}".replace(".", ","))
    out = df.copy()
    out["conc_ug_L"] = conc_txt
    out["temperatura_C"] = temp_txt
    out = out.rename(columns={"conc_ug_L": "concentrazione (µg/L)", "temperatura_C": "T (°C)"})
    intest = ("# Laboratorio sensori - export misure\n"
              "# Metodo: DPV su SPCE modificato; taratura del 10/01/2026\n"
              "# Valori 'n.d.' = non determinato\n")
    path = Path(base) / "misure_sporche.csv"
    with open(path, "w", encoding="latin-1", newline="") as f:
        f.write(intest)
        out.to_csv(f, sep=";", index=False)
    # metadati dei campioni, in Excel
    meta = pd.DataFrame({"campione": campioni, "sito": sito_camp, "quota_m": quota_camp,
                         "data_campionamento": data_camp})
    meta = meta.iloc[:37]   # 3 campioni SENZA metadati -> merge con NaN
    meta.to_excel(Path(base) / "metadati_campioni.xlsx", index=False)
    return path


# --------------------------------------------------------------------------
# 3. Serie temporale da sensore (giorno 2, resample)
# --------------------------------------------------------------------------
def genera_serie(base):
    rng = np.random.default_rng(SEME)
    t = pd.date_range("2026-03-02 00:00", "2026-03-08 23:50", freq="10min")
    ore = (t.hour + t.minute / 60).to_numpy()
    temp = 18 + 6 * np.sin((ore - 9) / 24 * 2 * np.pi) + rng.normal(0, 0.4, t.size)
    segnale = np.asarray(2.0 + 0.05 * temp + 0.3 * np.sin(np.arange(t.size) / 90) + rng.normal(0, 0.08, t.size))
    segnale[900:915] = np.nan   # buco di acquisizione
    df = pd.DataFrame({"timestamp": t, "temperatura_C": temp.round(2), "segnale_uA": segnale.round(3)})
    df.to_csv(Path(base) / "sensore_serie.csv", index=False)


# --------------------------------------------------------------------------
# 4. Taratura, dose-risposta, cinetica, confronto fra gruppi (giorno 3)
# --------------------------------------------------------------------------
def genera_statistica(base):
    rng = np.random.default_rng(SEME)
    base = Path(base)
    # taratura: 6 livelli x 3 repliche
    conc = np.repeat([1, 2, 5, 10, 20, 50], 3)
    i = 0.42 * conc + 0.15 + rng.normal(0, 0.18, conc.size)
    tar = pd.DataFrame({"conc_uM": conc, "replica": np.tile([1, 2, 3], 6), "i_uA": i.round(3)})
    tar.to_csv(base / "taratura.csv", index=False)
    rng.normal(0, 0.18, 10)   # ex "bianchi" (non più usati): estrazione mantenuta per non cambiare i dati seguenti
    # dose-risposta (Hill): risposta = top * d^n / (k^n + d^n)
    d = np.array([0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000])
    risp = 95 * d ** 1.3 / (12 ** 1.3 + d ** 1.3) + 4 + rng.normal(0, 3, d.size)
    pd.DataFrame({"dose_uM": d, "risposta_%": risp.round(2)}).to_csv(base / "dose_risposta.csv", index=False)
    # cinetica di degradazione (esponenziale con plateau)
    t = np.arange(0, 121, 5)
    c = 80 * np.exp(-t / 35) + 12 + rng.normal(0, 1.8, t.size)
    pd.DataFrame({"t_min": t, "conc_residua_%": c.round(2)}).to_csv(base / "cinetica.csv", index=False)
    # confronto fra 3 trattamenti, 8 repliche
    tratt = np.repeat(["controllo", "trattamento_A", "trattamento_B"], 8)
    medie = {"controllo": 14.0, "trattamento_A": 14.6, "trattamento_B": 17.8}
    val = [rng.normal(medie[g], 1.9) for g in tratt]
    pd.DataFrame({"trattamento": tratt, "risposta": np.round(val, 2)}).to_csv(base / "confronto_gruppi.csv", index=False)


# --------------------------------------------------------------------------
# 5. Matrice campioni x variabili per PCA / classificazione (giorno 4)
# --------------------------------------------------------------------------
def genera_matrice_ml(base):
    rng = np.random.default_rng(SEME)
    n_per = 20
    classi = ["Cascine", "Vallombrosa", "Maremma"]
    potenziali = np.round(np.linspace(-0.5, 0.2, 15), 2) + 0.0
    potenziali[np.abs(potenziali) < 1e-9] = 0.0
    colonne = [f"i_{p:+.2f}V" for p in potenziali] + ["pH", "conducibilita_uS", "umidita_%", "clorofilla", "fenoli_tot"]
    blocchi = []
    for k, cl in enumerate(classi):
        centro = np.zeros(len(colonne))
        # le prime 15 variabili (correnti) hanno struttura: un picco la cui posizione
        # cambia con la classe; le ultime 5 sono chimico-fisiche
        pos = [-0.25, -0.18, -0.10][k]
        centro[:15] = 1.0 + 3.0 * np.exp(-((potenziali - pos) / 0.08) ** 2)
        centro[15:] = [6.2 + 0.25 * k, 350 + 70 * k, 55 - 3.5 * k, 30 + 2.5 * k, 12 + 2 * k]
        scala = np.r_[np.full(15, 0.6), [0.4, 70, 5, 4, 3]]
        X = centro + rng.normal(0, 1, (n_per, len(colonne))) * scala
        # rumore correlato comune a tutte le correnti (deriva dello strumento)
        X[:, :15] += rng.normal(0, 0.6, (n_per, 1))
        blocchi.append(pd.DataFrame(X, columns=colonne).assign(classe=cl))
    df = pd.concat(blocchi, ignore_index=True)
    df.insert(0, "campione", [f"M{k:03d}" for k in range(1, len(df) + 1)])
    df = df.sample(frac=1, random_state=SEME).reset_index(drop=True)
    df.iloc[:, 1:-1] = df.iloc[:, 1:-1].round(3)
    # qualche mancante
    for r, c in [(4, "pH"), (17, "fenoli_tot"), (33, "i_-0.20V")]:
        df.loc[r, c] = np.nan
    df.to_csv(Path(base) / "sensori_matrice.csv", index=False)
    # dataset "solo rumore" per la dimostrazione dell'overfitting
    rng_r = np.random.default_rng(1)
    Xr = rng_r.normal(size=(30, 200))
    yr = np.repeat([0, 1], 15)
    rum = pd.DataFrame(Xr, columns=[f"v{k}" for k in range(200)]).assign(classe=yr)
    rum.to_csv(Path(base) / "rumore_puro.csv", index=False)


def genera_tutto(base="dati"):
    base = _cartella(base)
    genera_strumento(base)
    genera_misure_sporche(base)
    genera_serie(base)
    genera_statistica(base)
    genera_matrice_ml(base)
    print(f"Dati generati in: {base.resolve()}")
    return base


if __name__ == "__main__":
    genera_tutto()
