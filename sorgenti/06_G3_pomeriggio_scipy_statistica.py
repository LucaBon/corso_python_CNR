# %% [markdown]
# # Giorno 3, pomeriggio: SciPy e statistica per il laboratorio
#
# Obiettivo: una retta di taratura fatta come si deve, con le incertezze sui parametri e gli
# intervalli di confidenza e di predizione, e un fit non lineare di cui sapete dire quanto
# fidarvi. Poi t-test, ANOVA e cosa significa davvero un p-value.
#
# È la parte più vicina al vostro lavoro quotidiano. Queste cose le conoscete già: oggi
# imparate a scriverle in Python, e a non fidarvi di un R² da solo.
#
# ## 0. Cella di avvio

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

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
mpl.rcParams.update({"figure.dpi": 100, "axes.spines.top": False, "axes.spines.right": False})
tar = pd.read_csv(DATI / "taratura.csv")
print(tar.groupby("conc_uM")["i_uA"].agg(["mean", "std"]).round(3))

# %% [markdown]
# ---
# ## 1. Regressione lineare: pendenza, intercetta e le loro incertezze
#
# `np.polyfit` dà i coefficienti; `scipy.stats.linregress` dà anche gli **errori standard**,
# che sono quello che serve in un articolo. La regressione si fa sui punti singoli (18 misure),
# non sulle medie per livello: le repliche portano informazione sulla dispersione.

# %%
x = tar["conc_uM"].to_numpy()
y = tar["i_uA"].to_numpy()
n = len(x)

reg = stats.linregress(x, y)
print(f"pendenza   m = {reg.slope:.4f} ± {reg.stderr:.4f} µA/µM")
print(f"intercetta q = {reg.intercept:.4f} ± {reg.intercept_stderr:.4f} µA")
print(f"R² = {reg.rvalue**2:.5f}")

# %% [markdown]
# L'errore standard è "± una deviazione standard" sul parametro. Per un intervallo di
# confidenza al 95 % si moltiplica per il quantile della t di Student con $n-2$ gradi di
# libertà (≈ 2.1 con 16 gradi; tende a 1.96 per $n$ grande).

# %%
gdl = n - 2
t95 = stats.t.ppf(0.975, gdl)
print(f"t(0.975, {gdl}) = {t95:.3f}")
print(f"m = {reg.slope:.4f}  IC95 % [{reg.slope - t95*reg.stderr:.4f}, {reg.slope + t95*reg.stderr:.4f}]")
print(f"q = {reg.intercept:.4f}  IC95 % [{reg.intercept - t95*reg.intercept_stderr:.4f}, {reg.intercept + t95*reg.intercept_stderr:.4f}]")
print("l'intercetta è compatibile con zero?", "no" if abs(reg.intercept) > t95 * reg.intercept_stderr else "sì")

# %% [markdown]
# ### R² e cosa non dice
#
# R² misura quanta varianza di $y$ è spiegata dalla retta. Non dice se la retta è il modello
# giusto. Quattro insiemi di dati con la stessa retta e lo stesso R² = 0.67 (il quartetto di
# Anscombe, 1973):

# %%
A = {  # il quartetto di Anscombe
    "I":   ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
fig, axs = plt.subplots(1, 4, figsize=(11, 2.8), sharey=True, constrained_layout=True)
for ax, (k, (xa, ya)) in zip(axs, A.items()):
    r = stats.linregress(xa, ya)
    xx = np.linspace(3, 20, 10)
    ax.plot(xa, ya, "o", ms=4); ax.plot(xx, r.slope * xx + r.intercept, "-", color="crimson")
    ax.set_title(f"{k}: R² = {r.rvalue**2:.2f}, m = {r.slope:.2f}", fontsize=9)
plt.show()

# %% [markdown]
# Solo il primo è una regressione lineare sensata. Il secondo è curvo, il terzo ha un
# anomalo, il quarto si regge su un solo punto. Nessuno di questi difetti si vede dall'R²:
# si vedono dal grafico e dai residui (§ 4).

# %% [markdown]
# ---
# ## 2. Retta di taratura: intervalli di confidenza e di predizione
#
# Attorno alla retta si disegnano due bande diverse, e vanno tenute distinte:
#
# - **Banda di confidenza**: dove sta la retta vera (la media di $y$ a ogni $x$) con il 95 % di
#   probabilità. Si stringe con più punti.
# - **Banda di predizione**: dove cadrà una nuova singola misura. È più larga, e non si stringe
#   sotto la dispersione delle repliche.
#
# Per una retta $\hat y = mx + q$, con $s_{y/x}$ = deviazione standard dei residui:
#
# $$\text{conf}(x_0) = t \cdot s_{y/x}\sqrt{\frac{1}{n} + \frac{(x_0-\bar x)^2}{S_{xx}}}
# \qquad
# \text{pred}(x_0) = t \cdot s_{y/x}\sqrt{1 + \frac{1}{n} + \frac{(x_0-\bar x)^2}{S_{xx}}}$$
#
# La sensibilità del metodo è la pendenza $m$: quanto segnale per unità di concentrazione.

# %%
def bande_retta(x, y, x0, alpha=0.05):
    """Retta di regressione e semi-ampiezze delle bande di confidenza e predizione in x0."""
    reg = stats.linregress(x, y)
    n = len(x)
    y_hat = reg.slope * x + reg.intercept
    s_yx = np.sqrt(np.sum((y - y_hat) ** 2) / (n - 2))       # sd dei residui
    Sxx = np.sum((x - x.mean()) ** 2)
    t = stats.t.ppf(1 - alpha / 2, n - 2)
    termine = 1 / n + (x0 - x.mean()) ** 2 / Sxx
    conf = t * s_yx * np.sqrt(termine)
    pred = t * s_yx * np.sqrt(1 + termine)
    return reg, s_yx, reg.slope * x0 + reg.intercept, conf, pred

x0 = np.linspace(0, 52, 200)
reg, s_yx, y0, conf, pred = bande_retta(x, y, x0)
print(f"s(y/x) = {s_yx:.4f} µA   sensibilità = {reg.slope:.4f} µA/µM")

fig, ax = plt.subplots(figsize=(6, 4))
ax.fill_between(x0, y0 - pred, y0 + pred, alpha=0.12, lw=0, color="#0072B2", label="predizione 95 %")
ax.fill_between(x0, y0 - conf, y0 + conf, alpha=0.3, lw=0, color="#0072B2", label="confidenza 95 %")
ax.plot(x0, y0, "-", color="#0072B2", label="regressione")
ax.plot(x, y, "o", ms=4, color="black", label="misure")
ax.set_xlabel("concentrazione / µM"); ax.set_ylabel("i$_p$ / µA"); ax.legend(loc="upper left", frameon=False)
plt.show()

# %% [markdown]
# ### E le metriche del vostro settore?
#
# Ogni disciplina ricava dalla retta (o dalla curva) le sue grandezze derivate: limite di
# rilevabilità e di quantificazione, concentrazione di un incognito, $x_{50}$ di una curva a
# sigmoide, costanti di velocità. Sono tutte funzioni dei parametri appena stimati e delle loro
# incertezze ($m$, $q$, $s_{y/x}$, errori standard). Quando sapete ottenere questi numeri con le
# incertezze, le formule specifiche si prendono dalla linea guida del vostro settore e si
# scrivono in due righe di codice, dichiarando sempre quale formula avete usato.

# %% [markdown]
# ### Dimostrazione: un report di regressione completo, e un anomalo nascosto
#
# Il codice qui sotto è già scritto: eseguitelo e leggetelo. Mette insieme tutto in una funzione
# `report_regressione(x, y, nome)`, che stampa un rapporto e restituisce un dizionario con `m`, `sm`,
# `q`, `sq` (errori standard), `ic_m`, `ic_q` (semi-ampiezze degli IC al 95 %), `r2`, `s_yx`, `n`, e una
# seconda funzione per la figura (punti, retta, bande, equazione e R² nel riquadro).
#
# La usiamo due volte: sui dati originali e su una copia `tar_err` in cui **una sola** replica a 20 µM
# è sbagliata del 30 %. Le domande, da discutere: quanto cambiano pendenza, $s_{y/x}$ e la banda di
# predizione a 20 µM? L'R² vi avverte che qualcosa non va? E il grafico?
#
# > *Estensione facoltativa*: riscrivete `report_regressione` da soli, senza guardare, e controllate
# > di ottenere gli stessi numeri.

# %%
# DIMOSTRAZIONE (codice completo, da eseguire e leggere)
tar_err = tar.copy()
k_err = tar_err.index[tar_err["conc_uM"] == 20][0]
tar_err.loc[k_err, "i_uA"] *= 1.3          # una replica sbagliata del 30 % (es. errore di trascrizione)

def report_regressione(x, y, nome="regressione", alpha=0.05):
    x, y = np.asarray(x, float), np.asarray(y, float)
    reg = stats.linregress(x, y)
    n = len(x)
    s_yx = np.sqrt(np.sum((y - (reg.slope * x + reg.intercept)) ** 2) / (n - 2))
    t = stats.t.ppf(1 - alpha / 2, n - 2)
    out = dict(m=reg.slope, sm=reg.stderr, q=reg.intercept, sq=reg.intercept_stderr,
               ic_m=t * reg.stderr, ic_q=t * reg.intercept_stderr,
               r2=reg.rvalue ** 2, s_yx=s_yx, n=n)
    print(f"[{nome}]  n = {n}")
    print(f"  m = {out['m']:.4f} ± {out['ic_m']:.4f} (IC95)   q = {out['q']:.4f} ± {out['ic_q']:.4f} (IC95)")
    print(f"  R² = {out['r2']:.5f}   s(y/x) = {s_yx:.4f}")
    return out

def figura_regressione(x, y, out, ax):
    x, y = np.asarray(x, float), np.asarray(y, float)
    xx = np.linspace(0, x.max() * 1.05, 200)
    _, _, yy, conf, pred = bande_retta(x, y, xx)
    ax.fill_between(xx, yy - pred, yy + pred, alpha=0.12, lw=0, color="#0072B2", label="predizione 95 %")
    ax.fill_between(xx, yy - conf, yy + conf, alpha=0.3, lw=0, color="#0072B2", label="confidenza 95 %")
    ax.plot(xx, yy, "-", color="#0072B2")
    ax.plot(x, y, "o", ms=4, color="black", label="misure")
    ax.text(0.04, 0.95, f"$y = {out['m']:.3f}x + {out['q']:.3f}$\n$R^2 = {out['r2']:.4f}$, $n = {out['n']}$",
            transform=ax.transAxes, va="top", fontsize=8,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="0.7", lw=0.6))
    ax.set_xlabel("concentrazione / µM"); ax.set_ylabel("i$_p$ / µA")
    ax.legend(loc="lower right", frameon=False, fontsize=7)

r1 = report_regressione(tar["conc_uM"], tar["i_uA"], "originale")
r2_ = report_regressione(tar_err["conc_uM"], tar_err["i_uA"], "con una replica sbagliata")
pred20 = [bande_retta(d["conc_uM"].to_numpy(float), d["i_uA"].to_numpy(float), np.array([20.0]))[4][0] for d in (tar, tar_err)]
print(f"\npendenza: {100 * (r2_['m'] / r1['m'] - 1):+.1f} %   s(y/x): x{r2_['s_yx'] / r1['s_yx']:.1f}   "
      f"banda di predizione a 20 µM: ±{pred20[0]:.2f} -> ±{pred20[1]:.2f} µA   R²: {r1['r2']:.4f} -> {r2_['r2']:.4f}")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True, constrained_layout=True)
figura_regressione(tar["conc_uM"], tar["i_uA"], r1, a1); a1.set_title("originale", fontsize=9)
figura_regressione(tar_err["conc_uM"], tar_err["i_uA"], r2_, a2); a2.set_title("con una replica sbagliata", fontsize=9)
a2.plot(tar_err.loc[k_err, "conc_uM"], tar_err.loc[k_err, "i_uA"], "o", ms=8, mfc="none", color="crimson")
plt.show()
# Commento: una sola replica sbagliata sposta la pendenza di appena +0.6 %, ma s(y/x) cresce di
# circa 4 volte e la banda di predizione a 20 µM passa da ±0.36 a ±1.42 µA. L'R² scende solo da
# 0.9995 a 0.9928, resta "ottimo" e non avverte. Se ne accorgono il grafico (punto cerchiato) e i residui (§ 4).

# %% [markdown]
# ---
# ## 3. `curve_fit`: fit non lineare
#
# Quando il modello non è una retta (saturazione, sigmoide, decadimento) si scrive
# la funzione del modello e `curve_fit` trova i parametri che minimizzano gli scarti quadrati.
# Restituisce i parametri (`popt`) e la matrice di covarianza (`pcov`): la radice della sua
# diagonale è l'errore standard di ogni parametro.
#
# Tre cose che fanno la differenza fra un fit che converge e uno che no:
# 1. `p0`: una stima iniziale ragionevole dei parametri (guardando il grafico);
# 2. `bounds`: limiti fisici (una costante di tempo non è negativa);
# 3. aver guardato i dati prima: un anomalo trascina qualsiasi fit.

# %%
cin = pd.read_csv(DATI / "cinetica.csv")
t, c = cin["t_min"].to_numpy(), cin["conc_residua_%"].to_numpy()

def decadimento(t, C0, tau, plateau):
    """Decadimento esponenziale verso un plateau."""
    return C0 * np.exp(-t / tau) + plateau

popt, pcov = curve_fit(decadimento, t, c, p0=[80, 30, 10], bounds=([0, 0, 0], [200, 500, 100]))
perr = np.sqrt(np.diag(pcov))
for nome, v, e in zip(["C0", "tau", "plateau"], popt, perr):
    print(f"{nome:8s} = {v:7.2f} ± {e:.2f}")
print(f"tempo di dimezzamento = {popt[1] * np.log(2):.1f} min")

# %%
tt = np.linspace(0, 120, 200)
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(t, c, "o", ms=4, color="black", label="misure")
ax.plot(tt, decadimento(tt, *popt), "-", label=f"fit: τ = {popt[1]:.1f} ± {perr[1]:.1f} min")
ax.set_xlabel("tempo / min"); ax.set_ylabel("concentrazione residua / %"); ax.legend(frameon=False)
plt.show()

# %% [markdown]
# ### Curva sigmoide (logistica a 4 parametri)
#
# Il modello "a S" più usato quando una risposta sale da un plateau basso a uno alto al crescere
# di una dose, una concentrazione, una temperatura…:
#
# $$R(d) = R_{min} + \frac{R_{max} - R_{min}}{1 + (x_{50}/d)^{n}}$$
#
# $x_{50}$ è il punto di metà salita (la dose che dà metà della risposta), $n$ la ripidità.
# Si fitta sulla dose in scala originale, ma si guarda con l'asse x in scala log.

# %%
dr = pd.read_csv(DATI / "dose_risposta.csv")
d, r = dr["dose_uM"].to_numpy(), dr["risposta_%"].to_numpy()

def sigmoide(d, Rmin, Rmax, x50, n):
    """Logistica a 4 parametri."""
    return Rmin + (Rmax - Rmin) / (1 + (x50 / d) ** n)

popt_s, pcov_s = curve_fit(sigmoide, d, r, p0=[0, 100, 10, 1], bounds=([-10, 50, 0.01, 0.2], [30, 150, 1000, 5]))
perr_s = np.sqrt(np.diag(pcov_s))
for nome, v, e in zip(["Rmin", "Rmax", "x50", "n"], popt_s, perr_s):
    print(f"{nome:6s} = {v:7.2f} ± {e:.2f}")

dd = np.logspace(-1.2, 3.2, 200)
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(d, r, "o", ms=4, color="black", label="misure")
ax.plot(dd, sigmoide(dd, *popt_s), "-", label=f"sigmoide: $x_{{50}}$ = {popt_s[2]:.1f} ± {perr_s[2]:.1f} µM")
ax.set_xscale("log"); ax.set_xlabel("dose / µM"); ax.set_ylabel("risposta / %"); ax.legend(frameon=False)
plt.show()

# %% [markdown]
# ---
# ## 4. Analisi dei residui: riconoscere un fit sbagliato che sembra buono
#
# **Residuo** = misura − modello. Se il modello è giusto, i residui sono rumore: sparsi attorno
# allo zero, senza struttura. Se mostrano una forma (una curva, una tendenza, un ventaglio
# che si allarga), il modello è sbagliato, anche con R² = 0.99.
#
# Esempio: fittiamo la cinetica con una retta. R² alto, fit "accettabile" a occhio. Poi
# guardate i residui.

# %%
reg_lin = stats.linregress(t, c)
res_lin = c - (reg_lin.slope * t + reg_lin.intercept)
res_exp = c - decadimento(t, *popt)

fig, axs = plt.subplots(2, 2, figsize=(9, 5.5), constrained_layout=True, sharex="col")
axs[0, 0].plot(t, c, "o", ms=4, color="black"); axs[0, 0].plot(tt, reg_lin.slope * tt + reg_lin.intercept, "-", color="crimson")
axs[0, 0].set_title(f"retta: R² = {reg_lin.rvalue**2:.3f}", fontsize=9); axs[0, 0].set_ylabel("conc. residua / %")
axs[0, 1].plot(t, c, "o", ms=4, color="black"); axs[0, 1].plot(tt, decadimento(tt, *popt), "-")
r2_exp = 1 - np.sum(res_exp ** 2) / np.sum((c - c.mean()) ** 2)
axs[0, 1].set_title(f"esponenziale: R² = {r2_exp:.3f}", fontsize=9)
for ax, res, col in [(axs[1, 0], res_lin, "crimson"), (axs[1, 1], res_exp, "#0072B2")]:
    ax.axhline(0, color="gray", lw=0.8)
    ax.plot(t, res, "o-", ms=4, color=col, lw=0.6)
    ax.set_xlabel("tempo / min")
axs[1, 0].set_ylabel("residuo / %")
axs[1, 0].set_title("residui con STRUTTURA: modello sbagliato", fontsize=9)
axs[1, 1].set_title("residui senza struttura", fontsize=9)
plt.show()

# %% [markdown]
# ### Esercizio 6.2 (E3.2): fit non lineare con incertezze e residui (livello 2)
#
# Sulla curva sigmoide (`dose_risposta.csv`):
# 1. fittate anche un modello sbagliato ma plausibile: la retta in `log10(dose)`
#    (`stats.linregress(np.log10(d), r)`);
# 2. calcolate R² per entrambi (sigmoide e retta-log);
# 3. figura a due pannelli: sopra dati + le due curve (asse x log); sotto i residui dei due modelli;
# 4. stampate i parametri della sigmoide come `valore ± incertezza`, e scrivete in una riga di commento
#    quale modello scegliete e perché (non per l'R²).

# %%
# ESERCIZIO 6.2 (livello 2)
# 1. reg_log = linregress su log10(d)
# 2. residui e R² dei due modelli
# 3. figura 2 righe x 1 colonna, sharex
# 4. stampa e commento
# --- SOLUZIONE ---
reg_log = stats.linregress(np.log10(d), r)
res_sig = r - sigmoide(d, *popt_s)
res_log = r - (reg_log.slope * np.log10(d) + reg_log.intercept)
sst = np.sum((r - r.mean()) ** 2)
print(f"R² sigmoide = {1 - np.sum(res_sig**2) / sst:.4f}   R² retta-log = {1 - np.sum(res_log**2) / sst:.4f}")

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6, 5.5), sharex=True, constrained_layout=True,
                             gridspec_kw={"height_ratios": [2.2, 1]})
a1.plot(d, r, "o", ms=4, color="black", label="misure")
a1.plot(dd, sigmoide(dd, *popt_s), "-", label="sigmoide")
a1.plot(dd, reg_log.slope * np.log10(dd) + reg_log.intercept, "--", color="crimson", label="retta in log(dose)")
a1.set_ylabel("risposta / %"); a1.legend(frameon=False)
a2.axhline(0, color="gray", lw=0.8)
a2.plot(d, res_sig, "o-", ms=4, lw=0.6, label="sigmoide")
a2.plot(d, res_log, "s--", ms=4, lw=0.6, color="crimson", label="retta-log")
a2.set_xscale("log"); a2.set_xlabel("dose / µM"); a2.set_ylabel("residuo / %"); a2.legend(frameon=False, fontsize=8)
plt.show()

for nome, v, e in zip(["Rmin", "Rmax", "x50", "n"], popt_s, perr_s):
    print(f"{nome:5s} = {v:7.2f} ± {e:5.2f}")
# Scelgo la sigmoide: i residui della retta-log hanno una forma a S (sistematici agli estremi),
# e il modello ha i due plateau (risposta minima e massima) che una retta non può avere.

# %% [markdown]
# > Estensione facoltativa: stimate l'incertezza di $x_{50}$ anche per bootstrap (ricampionate
# > le coppie (d, r) con reinserimento 500 volte, rifate il fit, prendete il 2.5° e 97.5°
# > percentile). Confrontate con ± dalla matrice di covarianza.

# %% [markdown]
# ---
# ## 5. Statistica di base: distribuzioni, t-test, ANOVA
#
# Il dataset: una risposta misurata su 8 repliche per tre trattamenti (controllo, A, B).
# La domanda: i trattamenti cambiano la risposta?
#
# Prima di ogni test si guardano i dati (box plot con punti), e chiedersi se le assunzioni reggono
# (normalità approssimativa entro gruppo, varianze simili). Con n = 8 i test di normalità
# hanno poca potenza: il grafico vale più dello Shapiro.

# %%
grp = pd.read_csv(DATI / "confronto_gruppi.csv")
gruppi = {g: grp.loc[grp["trattamento"] == g, "risposta"].to_numpy() for g in ["controllo", "trattamento_A", "trattamento_B"]}
print(grp.groupby("trattamento")["risposta"].agg(["count", "mean", "std"]).round(2))

for g, v in gruppi.items():
    W, p = stats.shapiro(v)
    print(f"Shapiro {g:14s}: W = {W:.3f}, p = {p:.3f}")

# %%
rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.boxplot(list(gruppi.values()), positions=range(3), widths=0.5, showfliers=False)
for k, v in enumerate(gruppi.values()):
    ax.plot(k + rng.normal(0, 0.05, v.size), v, "o", ms=4, color="crimson", alpha=0.7)
ax.set_xticks(range(3), list(gruppi)); ax.set_ylabel("risposta / u.a.")
plt.show()

# %% [markdown]
# ### t-test per due gruppi
#
# `ttest_ind` confronta due medie. Usate `equal_var=False` (t di Welch) come default: non
# richiede varianze uguali e costa pochissimo in potenza quando lo sono.

# %%
for g in ["trattamento_A", "trattamento_B"]:
    res = stats.ttest_ind(gruppi[g], gruppi["controllo"], equal_var=False)
    diff = gruppi[g].mean() - gruppi["controllo"].mean()
    d_cohen = diff / np.sqrt((gruppi[g].var(ddof=1) + gruppi["controllo"].var(ddof=1)) / 2)
    print(f"{g} vs controllo: diff = {diff:+.2f}, t = {res.statistic:.2f}, p = {res.pvalue:.4f}, d di Cohen = {d_cohen:.2f}")

# %% [markdown]
# ### Cosa significa davvero un p-value
#
# $p$ è la probabilità di osservare una differenza almeno così grande *se* i due gruppi
# venissero dalla stessa popolazione. Non è la probabilità che l'ipotesi nulla sia vera, e
# **non misura quanto è grande l'effetto**: con n enorme, un effetto irrilevante ha p minuscolo;
# con n = 8, un effetto reale può avere p = 0.15.
#
# Per questo accanto al p-value si riporta sempre la dimensione dell'effetto (la differenza
# con il suo intervallo di confidenza, o il d di Cohen). Guardate il caso di A: differenza
# di −0.4 con p ≈ 0.5. "Non significativo" non vuol dire "nessun effetto", vuol dire che non
# abbiamo abbastanza dati per vederlo.

# %% [markdown]
# ### ANOVA a una via, e poi confronti a coppie
#
# Con tre o più gruppi non si fanno tre t-test: si fa un'ANOVA (c'è *qualche* differenza?)
# e, se sì, i confronti post-hoc corretti (Tukey HSD) per dire *quali* gruppi differiscono.

# %%
F, p = stats.f_oneway(*gruppi.values())
print(f"ANOVA a una via: F = {F:.2f}, p = {p:.2g}")

tukey = stats.tukey_hsd(*gruppi.values())
nomi = list(gruppi)
print("\nTukey HSD (coppie):")
for i in range(3):
    for j in range(i + 1, 3):
        lo, hi = tukey.confidence_interval().low[i, j], tukey.confidence_interval().high[i, j]
        print(f"  {nomi[i]:14s} - {nomi[j]:14s}: diff = {tukey.statistic[i, j]:+.2f}  IC95 [{lo:+.2f}, {hi:+.2f}]  p = {tukey.pvalue[i, j]:.4f}")

# %% [markdown]
# ### Igiene statistica: confronti multipli e sovra-interpretazione
#
# Se fate 20 test su dati puramente casuali, in media uno viene "significativo" al 5 %.
# È aritmetica. Proviamo:

# %%
rng = np.random.default_rng(1)
p_vals = [stats.ttest_ind(rng.normal(size=8), rng.normal(size=8)).pvalue for _ in range(20)]
print("p-value di 20 confronti fra gruppi IDENTICI (tutti rumore):")
print(np.round(sorted(p_vals), 3))
print(f"'significativi' (p < 0.05): {sum(p < 0.05 for p in p_vals)}   con Bonferroni (p < 0.05/20): {sum(p < 0.05/20 for p in p_vals)}")

# %% [markdown]
# Regole minime:
# - Decidete prima quali confronti fare; non cercate "quello che viene significativo".
# - Con più confronti, correggete (Bonferroni è conservativo ma semplice; Tukey per le coppie dopo ANOVA).
# - Riportate effetto, intervallo di confidenza e n, non solo l'asterisco.
# - Il test non sostituisce il grafico: se dal box plot non si vede niente, con n = 8 un p < 0.05 va preso con le pinze.

# %% [markdown]
# ### Esercizio 6.3: confronto fra matrici, fatto bene (livello 2)
#
# Con `misure_pulite.csv` di ieri (o il file grezzo pulito al volo con la stessa regola del
# giorno 2): il rame ha concentrazione diversa nelle tre matrici?
#
# Due trappole da evitare prima di lanciare qualsiasi test:
#
# 1. **Pseudo-repliche.** Ogni campione è stato misurato 2-3 volte. Le repliche dello stesso
#    campione non sono osservazioni indipendenti: misurano lo stesso materiale, e si somigliano
#    fra loro più che a un altro campione. Darle tutte all'ANOVA come se fossero campioni diversi
#    gonfia $n$ e rende il p-value troppo piccolo. Prima si riduce a un valore per campione.
# 2. **Distribuzione asimmetrica.** Le concentrazioni sono positive, con coda a destra, e la loro
#    dispersione cresce con la media (lognormali): proprio le condizioni in cui l'ANOVA soffre. Si
#    lavora in log10: la media dei log è il log della *media geometrica*, e una differenza fra
#    medie in log10 è un rapporto ($10^{\Delta}$: "il suolo ha 3 volte il rame della foglia").
#
# Passi: log10 → media per campione → box plot con punti → ANOVA + Tukey sui log → differenze
# riportate come rapporti con il loro IC → Kruskal-Wallis (`stats.kruskal`, non parametrico) come
# controllo. Scrivete in un commento la conclusione in una frase, con effetto e intervallo, non solo p.

# %%
# ESERCIZIO 6.3 (livello 2)
if Path("misure_pulite.csv").exists():
    misure = pd.read_csv("misure_pulite.csv")
else:   # pulizia al volo, con la stessa regola del giorno 2 (anomali: > 3 IQR in log10, per analita x matrice)
    misure = pd.read_csv(DATI / "misure_sporche.csv", sep=";", decimal=",", encoding="latin-1",
                         comment="#", na_values=["n.d."])
    misure = misure.rename(columns={"concentrazione (µg/L)": "conc_ug_L"}).dropna(subset=["conc_ug_L"]).drop_duplicates()
    lc = np.log10(misure["conc_ug_L"])
    g = lc.groupby([misure["analita"], misure["matrice"]])
    q1, q3 = g.transform(lambda s: s.quantile(0.25)), g.transform(lambda s: s.quantile(0.75))
    misure = misure[(lc >= q1 - 3 * (q3 - q1)) & (lc <= q3 + 3 * (q3 - q1))]
cu = misure[misure["analita"] == "Cu"].copy()
cu["log_conc"] = np.log10(cu["conc_ug_L"])
# 1. un valore per campione: cu.groupby(["campione", "matrice"])["log_conc"].mean().reset_index()
# 2. dizionario matrice -> array dei valori per campione; box plot con punti (asse y in log)
# 3. ANOVA + Tukey sui log10; differenze come rapporti 10**diff, con IC
# 4. stats.kruskal come controllo
# --- SOLUZIONE ---
per_camp = cu.groupby(["campione", "matrice"])["log_conc"].mean().reset_index()
print(f"{len(cu)} misure di Cu -> {len(per_camp)} campioni indipendenti")
gm = {m: per_camp.loc[per_camp["matrice"] == m, "log_conc"].to_numpy() for m in ["foglia", "frutto", "suolo"]}
print({m: len(v) for m, v in gm.items()}, "campioni per matrice")

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.boxplot([10 ** v for v in gm.values()], positions=range(3), widths=0.5, showfliers=False)
for k, v in enumerate(gm.values()):
    ax.plot(k + rng.normal(0, 0.05, v.size), 10 ** v, "o", ms=4, color="crimson", alpha=0.7)
ax.set_xticks(range(3), list(gm)); ax.set_yscale("log")
ax.set_ylabel("Cu / µg/L (media geometrica per campione)")
plt.show()

F, p = stats.f_oneway(*gm.values())
print(f"ANOVA sui log10: F = {F:.1f}, p = {p:.2g}")
tk = stats.tukey_hsd(*gm.values())
ci = tk.confidence_interval()
nm = list(gm)
for i in range(3):
    for j in range(i + 1, 3):
        print(f"  {nm[j]} / {nm[i]}: rapporto = {10 ** -tk.statistic[i, j]:.2f}  "
              f"IC95 [{10 ** -ci.high[i, j]:.2f}, {10 ** -ci.low[i, j]:.2f}]   p = {tk.pvalue[i, j]:.2g}")
H, p_kw = stats.kruskal(*gm.values())
print(f"Kruskal-Wallis: H = {H:.1f}, p = {p_kw:.2g}")
# Conclusione: il rame dipende dalla matrice (ANOVA sui log10 delle medie di 40 campioni, p < 0.001;
# Kruskal-Wallis concorda). Il suolo ne ha ~2.3 volte la foglia (IC95 1.7-3.0) e ~4.3 volte il frutto
# (IC95 3.3-5.5); il frutto circa la metà della foglia (0.53, IC95 0.40-0.70).
# Nota: n = 40 campioni, non 90 misure. Le repliche servono a stimare meglio ogni campione.

# %% [markdown]
# ---
# ## Riepilogo del giorno 3
#
# | Serve… | In R | In Python |
# |---|---|---|
# | retta con errori sui parametri | `summary(lm(y ~ x))` | `stats.linregress` → `.slope, .stderr, .intercept, .intercept_stderr` |
# | intervallo al 95 % | `confint()` | ± `stats.t.ppf(0.975, n-2)` × errore standard |
# | bande di confidenza / predizione | `predict(..., interval = "confidence" / "prediction")` | formule con $s_{y/x}$ e $S_{xx}$ (funzione `bande_retta`) |
# | report completo di una retta | – | `report_regressione` (la dimostrazione), e guardare il grafico: l'R² non avverte |
# | fit non lineare | `nls()` | `curve_fit(f, x, y, p0=, bounds=)` → `np.sqrt(np.diag(pcov))` |
# | il fit è giusto? | `plot(residuals())` | residui senza struttura, non R² |
# | due gruppi | `t.test()` (Welch di default), `wilcox.test()` | `stats.ttest_ind(a, b, equal_var=False)` + d di Cohen; `stats.mannwhitneyu` |
# | due misure sugli stessi campioni | `t.test(paired = TRUE)` | `stats.ttest_rel(a, b)`; non parametrico `stats.wilcoxon` |
# | tre o più gruppi | `aov()`, `TukeyHSD()`, `kruskal.test()` | `stats.f_oneway` poi `stats.tukey_hsd`; controllo non parametrico `stats.kruskal` |
# | repliche dello stesso campione | idem: un valore per campione (o un modello misto, `lme4`) | un valore per campione prima del test (niente pseudo-repliche) |
# | concentrazioni (positive, asimmetriche) | idem | test in log10, effetti come rapporti |
# | tanti test | `p.adjust()` | correggere, o meglio: decidere prima |
#
# Una differenza da sapere: scipy non usa le formule (`y ~ x`) e non produce la tabella ANOVA "alla R".
# Per i modelli con formula, l'ANOVA a più fattori e i modelli misti in Python esiste `statsmodels`
# (non installato nel nostro ambiente); per quei casi, se R lo usate già, R resta una scelta ottima.
#
# Domani: PCA e un modello predittivo, e come capire quando il risultato non vale niente.
#
# ---
# *Riferimenti: Scientific Python Lectures (lectures.scientific-python.org), sezioni SciPy e
# statistica (CC-BY 4.0); J. N. Miller & J. C. Miller, "Statistics and Chemometrics for
# Analytical Chemistry" per le formule della taratura.*
