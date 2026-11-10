"""
genera_schemi.py: disegna gli schemi didattici in img/ (PNG, 200 dpi).

Sono volutamente semplici: ogni immagine è SOSTITUIBILE con una tua slide
esportata in PNG con lo stesso nome. I notebook le richiamano come ../img/nome.png
"""
from pathlib import Path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch

IMG = Path(__file__).resolve().parent / "img"
IMG.mkdir(exist_ok=True)
mpl.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
BLU, ARA, VER, ROS, GRI = "#0072B2", "#E69F00", "#009E73", "#D55E00", "#bbbbbb"


def salva(fig, nome):
    fig.savefig(IMG / f"{nome}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("img/", nome)


def box(ax, x, y, w, h, testo, colore="#eeeeee", fs=10, bordo="black"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor=colore, edgecolor=bordo, linewidth=1))
    ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=fs)


def freccia(ax, x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=15, lw=1.4))


def tela(w=8, h=4):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


# 1. indicizzazione di una lista -------------------------------------------
def indici_lista():
    fig, ax = tela(8, 2.6)
    vals = ["2.1", "3.4", "5.0", "4.7", "6.2", "3.9"]
    for k, v in enumerate(vals):
        box(ax, 1 + k, 1.0, 0.9, 0.8, v, colore="#dfe9f5", fs=12)
        ax.text(1.45 + k, 1.95, str(k), ha="center", color=BLU, fontsize=11, fontweight="bold")
        ax.text(1.45 + k, 0.7, str(k - len(vals)), ha="center", color=ROS, fontsize=11)
    ax.text(0.9, 1.95, "indice", ha="right", color=BLU)
    ax.text(0.9, 0.7, "dal fondo", ha="right", color=ROS)
    ax.text(4, 0.2, "misure[0] = 2.1     misure[-1] = 3.9     misure[1:4] = [3.4, 5.0, 4.7]   (il 4 è escluso)",
            ha="center", fontsize=10, family="monospace")
    salva(fig, "indici_lista")


# 2. broadcasting NumPy ----------------------------------------------------
def broadcasting():
    fig, ax = tela(9, 3.4)
    def griglia(x0, y0, righe, cols, testo, colore):
        for r in range(righe):
            for c in range(cols):
                ax.add_patch(Rectangle((x0 + c * 0.5, y0 + (righe - 1 - r) * 0.5), 0.5, 0.5,
                                       facecolor=colore, edgecolor="black", lw=0.8))
        ax.text(x0 + cols * 0.25, y0 - 0.35, testo, ha="center", fontsize=9)
    griglia(0.5, 1.4, 3, 4, "array (3, 4)", "#dfe9f5")
    ax.text(2.9, 2.1, "+", fontsize=18, ha="center")
    griglia(3.3, 2.4, 1, 4, "array (4,)", "#fde6c4")
    for r in range(2):
        griglia(3.3, 1.4 + r * 0.5, 1, 4, "", "#fde6c4") if False else None
    for r in range(3):
        for c in range(4):
            ax.add_patch(Rectangle((3.3 + c * 0.5, 1.4 + r * 0.5), 0.5, 0.5, facecolor="none",
                                   edgecolor=ARA, lw=0.8, linestyle="--"))
    ax.text(4.3, 1.0, "copiato\nsu ogni riga", ha="center", fontsize=8, color=ARA)
    ax.text(5.9, 2.1, "=", fontsize=18, ha="center")
    griglia(6.4, 1.4, 3, 4, "risultato (3, 4)", "#d5f0e6")
    ax.text(4.5, 3.2, "Broadcasting: NumPy allinea le forme da destra e 'stira' la dimensione mancante",
            ha="center", fontsize=10)
    salva(fig, "broadcasting")


# 3. anatomia DataFrame ----------------------------------------------------
def dataframe():
    fig, ax = tela(9, 4)
    cols = ["campione", "matrice", "conc_ug_L", "T_C"]
    dati = [["C001", "foglia", "32.3", "22.7"], ["C002", "frutto", "0.44", "21.6"], ["C003", "suolo", "18.9", "23.1"]]
    x0, y0, w, h = 2.2, 1.2, 1.4, 0.55
    for c, nome in enumerate(cols):
        box(ax, x0 + c * w, y0 + 3 * h, w - 0.05, h - 0.05, nome, colore="#fde6c4", fs=10)
    for r, riga in enumerate(dati):
        box(ax, x0 - 0.8, y0 + (2 - r) * h, 0.7, h - 0.05, str(r), colore="#dfe9f5", fs=10)
        for c, v in enumerate(riga):
            box(ax, x0 + c * w, y0 + (2 - r) * h, w - 0.05, h - 0.05, v, colore="white", fs=10)
    ax.text(1.75, 3.55, "index\n(etichetta di riga)", ha="center", fontsize=9, color=BLU)
    ax.text(5.0, 3.85, "columns (nomi di colonna)", ha="center", fontsize=9, color=ARA)
    ax.add_patch(Rectangle((x0 + 2 * w - 0.05, y0 - 0.05), w, 4 * h, facecolor="none", edgecolor=VER, lw=2))
    ax.text(x0 + 2.5 * w, 0.7, "una colonna = una Series\n(un solo dtype: float64)", ha="center", fontsize=9, color=VER)
    ax.text(0.2, 0.3, "df['conc_ug_L']  →  la colonna verde, una Series", fontsize=10, family="monospace")
    salva(fig, "dataframe_anatomia")


# 3b. loc (etichette) e iloc (posizioni) -------------------------------------
def loc_iloc():
    fig, ax = tela(10, 5.4)
    cols = ["campione", "matrice", "conc_ug_L", "T_C"]
    etichette = [3, 7, 12]                       # index dopo un filtro: NON 0, 1, 2
    dati = [["C004", "foglia", "29.1", "22.4"], ["C008", "frutto", "0.44", "21.6"], ["C013", "suolo", "18.9", "23.1"]]
    x0, y0, w, h = 3.0, 2.0, 1.4, 0.55
    ax.text(5.0, 5.15, "Dopo un filtro l'index conserva le etichette originali: etichetta ≠ posizione",
            ha="center", fontsize=10, weight="bold")
    for c, nome in enumerate(cols):
        ax.text(x0 + c * w + w / 2 - 0.03, y0 + 4 * h + 0.12, f"pos. {c}", ha="center", fontsize=8, color="0.45")
        box(ax, x0 + c * w, y0 + 3 * h, w - 0.05, h - 0.05, nome, colore="#fde6c4", fs=10)
    for r, (et, riga) in enumerate(zip(etichette, dati)):
        y = y0 + (2 - r) * h
        ax.text(x0 - 1.35, y + h / 2 - 0.03, f"pos. {r}", ha="center", va="center", fontsize=8, color="0.45")
        box(ax, x0 - 0.8, y, 0.7, h - 0.05, str(et), colore="#dfe9f5", fs=10)
        for c, v in enumerate(riga):
            box(ax, x0 + c * w, y, w - 0.05, h - 0.05, v, colore="white", fs=10)
    ax.text(x0 - 0.45, y0 + 3 * h + 0.2, "index\n(etichette)", ha="center", fontsize=8, color=BLU)
    ax.text(x0 - 1.35, y0 + 3 * h + 0.2, "posizioni", ha="center", fontsize=8, color="0.45")
    ax.add_patch(Rectangle((x0 + 2 * w - 0.06, y0 + h - 0.06), w + 0.02, h + 0.02, facecolor="none", edgecolor=ROS, lw=2.5))
    righe = [
        ("df.loc[7, 'conc_ug_L']  →  0.44", "per ETICHETTA: la riga che si chiama 7, la colonna che si chiama conc_ug_L", BLU),
        ("df.iloc[1, 2]           →  0.44", "per POSIZIONE: seconda riga, terza colonna (si conta da 0)", "0.35"),
        ("df.loc[1, 'conc_ug_L']  →  KeyError", "nessuna riga si chiama 1: è stata scartata dal filtro", ROS),
    ]
    for k, (codice, spiega, col) in enumerate(righe):
        yy = 1.35 - k * 0.5
        ax.text(0.1, yy, codice, fontsize=10, family="monospace", color=col, va="center")
        ax.text(4.75, yy, spiega, fontsize=9, color=col, va="center")
    salva(fig, "loc_iloc")


# 4. groupby split-apply-combine -------------------------------------------
def groupby():
    fig, ax = tela(10, 4.2)
    righe = [("foglia", 30), ("frutto", 1.2), ("suolo", 18), ("foglia", 34), ("suolo", 20), ("frutto", 0.9)]
    for k, (m, v) in enumerate(righe):
        col = {"foglia": "#d5f0e6", "frutto": "#fde6c4", "suolo": "#dfe9f5"}[m]
        box(ax, 0.3, 3.5 - k * 0.55, 1.0, 0.45, m, colore=col, fs=8)
        box(ax, 1.3, 3.5 - k * 0.55, 0.7, 0.45, str(v), colore=col, fs=8)
    ax.text(1.15, 4.05, "tabella", ha="center", fontsize=9)
    gruppi = {"foglia": [30, 34], "frutto": [1.2, 0.9], "suolo": [18, 20]}
    y = 3.6
    for m, vs in gruppi.items():
        col = {"foglia": "#d5f0e6", "frutto": "#fde6c4", "suolo": "#dfe9f5"}[m]
        for j, v in enumerate(vs):
            box(ax, 3.4, y - j * 0.45, 0.9, 0.4, m, colore=col, fs=8)
            box(ax, 4.3, y - j * 0.45, 0.6, 0.4, str(v), colore=col, fs=8)
        box(ax, 6.0, y - 0.3, 1.0, 0.5, f"media\n{np.mean(vs):.1f}", colore=col, fs=8)
        box(ax, 8.2, y - 0.3, 1.4, 0.5, f"{m}: {np.mean(vs):.1f}", colore=col, fs=8)
        freccia(ax, 5.0, y - 0.1, 5.9, y - 0.05)
        freccia(ax, 7.1, y - 0.05, 8.1, y - 0.05)
        y -= 1.15
    freccia(ax, 2.1, 2.2, 3.3, 2.2)
    ax.text(2.7, 2.45, "SPLIT", ha="center", fontsize=9, fontweight="bold")
    ax.text(5.45, 4.0, "APPLY", ha="center", fontsize=9, fontweight="bold")
    ax.text(7.6, 4.0, "COMBINE", ha="center", fontsize=9, fontweight="bold")
    ax.text(5, 0.25, "df.groupby('matrice')['conc'].mean()", ha="center", fontsize=11, family="monospace")
    salva(fig, "groupby")


# 5. merge ------------------------------------------------------------------
def merge():
    fig, ax = tela(10, 3.6)
    def tab(x, y, intest, righe, colori):
        for c, h in enumerate(intest):
            box(ax, x + c * 1.1, y, 1.05, 0.45, h, colore="#fde6c4", fs=8)
        for r, riga in enumerate(righe):
            for c, v in enumerate(riga):
                box(ax, x + c * 1.1, y - (r + 1) * 0.5, 1.05, 0.45, v, colore=colori[r], fs=8)
    tab(0.3, 3.0, ["campione", "conc"], [["C001", "32"], ["C002", "0.4"], ["C004", "9"]], ["#d5f0e6", "#dfe9f5", "#f5d5d5"])
    tab(3.2, 3.0, ["campione", "sito"], [["C001", "Cascine"], ["C002", "Maremma"], ["C003", "Chianti"]], ["#d5f0e6", "#dfe9f5", "#eeeeee"])
    tab(6.3, 3.0, ["campione", "conc", "sito"], [["C001", "32", "Cascine"], ["C002", "0.4", "Maremma"], ["C004", "9", "NaN"]], ["#d5f0e6", "#dfe9f5", "#f5d5d5"])
    ax.text(1.4, 3.55, "misure", ha="center", fontsize=9); ax.text(4.3, 3.55, "metadati", ha="center", fontsize=9)
    ax.text(7.9, 3.55, "pd.merge(misure, metadati, on='campione', how='left')", ha="center", fontsize=9, family="monospace")
    ax.text(5, 0.35, "how='left': tutte le righe di sinistra; chi non trova corrispondenza riceve NaN.\n"
                     "how='inner': solo le chiavi presenti in entrambe (C004 sparisce).", ha="center", fontsize=9)
    salva(fig, "merge")


# 6. k-fold ---------------------------------------------------------------
def kfold():
    fig, ax = tela(9, 3.6)
    k = 5
    for f in range(k):
        y = 2.8 - f * 0.55
        for j in range(k):
            col = ROS if j == f else "#dfe9f5"
            ax.add_patch(Rectangle((1.5 + j * 1.2, y), 1.15, 0.45, facecolor=col, edgecolor="black", lw=0.8))
        ax.text(1.3, y + 0.22, f"fold {f + 1}", ha="right", va="center", fontsize=9)
        ax.text(7.8, y + 0.22, f"→ accuratezza {f + 1}", va="center", fontsize=9)
    ax.text(4.5, 3.4, "Validazione crociata a 5 fold: ogni campione finisce nel test UNA volta", ha="center", fontsize=10)
    ax.add_patch(Rectangle((1.5, 0.05), 0.5, 0.3, facecolor="#dfe9f5", edgecolor="black")); ax.text(2.1, 0.2, "addestramento", va="center", fontsize=9)
    ax.add_patch(Rectangle((4.2, 0.05), 0.5, 0.3, facecolor=ROS, edgecolor="black")); ax.text(4.8, 0.2, "test", va="center", fontsize=9)
    ax.text(7.0, 0.2, "risultato = media ± dev.st.", va="center", fontsize=9)
    salva(fig, "kfold")


# 7. overfitting -----------------------------------------------------------
def overfitting():
    rng = np.random.default_rng(1)
    x = np.linspace(0, 1, 12); y = 1.5 * x + rng.normal(0, 0.25, 12)
    xx = np.linspace(0, 1, 200)
    fig, axs = plt.subplots(1, 3, figsize=(9.5, 3), sharey=True)
    for ax, deg, tit in zip(axs, [0, 1, 11], ["troppo semplice", "adeguato", "troppo complesso (overfitting)"]):
        ax.plot(x, y, "o", color="black", ms=5)
        p = np.polyfit(x, y, deg); ax.plot(xx, np.polyval(p, xx), color=BLU, lw=1.5)
        ax.set_title(tit, fontsize=10); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-0.6, 2.3)
    axs[1].set_xlabel("il modello 'adeguato' sbaglia un po' sui dati visti ma generalizza;\n"
                      "quello complesso li passa tutti e sbaglia su quelli nuovi", fontsize=9)
    fig.tight_layout()
    salva(fig, "overfitting")


# 8. fuga di informazione / pipeline --------------------------------------
def leakage():
    fig, ax = tela(10, 3.8)
    box(ax, 0.3, 2.4, 2.2, 0.8, "SBAGLIATO\nscaler.fit(tutti i dati)", colore="#f5d5d5", fs=9)
    freccia(ax, 2.5, 2.8, 3.1, 2.8)
    box(ax, 3.1, 2.4, 2.0, 0.8, "split train / test", fs=9)
    freccia(ax, 5.1, 2.8, 5.7, 2.8)
    box(ax, 5.7, 2.4, 2.0, 0.8, "modello", fs=9)
    ax.text(8.8, 2.8, "il test set ha già\ninfluenzato media e\ndev.st. → stima ottimista", ha="center", va="center", fontsize=8, color=ROS)
    box(ax, 0.3, 0.6, 2.2, 0.8, "GIUSTO\nsplit train / test", colore="#d5f0e6", fs=9)
    freccia(ax, 2.5, 1.0, 3.1, 1.0)
    box(ax, 3.1, 0.6, 4.6, 0.8, "Pipeline( scaler → modello ).fit(SOLO train)", colore="#d5f0e6", fs=9)
    ax.text(8.8, 1.0, "il test set resta\nmai visto fino\nalla valutazione", ha="center", va="center", fontsize=8, color=VER)
    ax.text(5, 3.55, "Fuga di informazione (data leakage) nel preprocessing", ha="center", fontsize=11)
    salva(fig, "pipeline_leakage")


# 9. PCA ----------------------------------------------------------------
def pca():
    rng = np.random.default_rng(3)
    X = rng.multivariate_normal([0, 0], [[3, 2.2], [2.2, 2]], 120)
    fig, ax = plt.subplots(figsize=(5, 4.2))
    ax.plot(X[:, 0], X[:, 1], "o", ms=4, color="#888888", alpha=0.7)
    w, v = np.linalg.eigh(np.cov(X.T)); ordine = np.argsort(w)[::-1]
    for i, (col, lab) in enumerate(zip([BLU, ROS], ["PC1 (varianza massima)", "PC2 (ortogonale a PC1)"])):
        d = v[:, ordine[i]] * np.sqrt(w[ordine[i]]) * 2.2
        ax.annotate("", xy=d, xytext=-d, arrowprops=dict(arrowstyle="<->", color=col, lw=2))
        ax.text(d[0] * 1.15, d[1] * 1.15, lab, color=col, fontsize=9, ha="center")
    ax.set_xlabel("variabile 1 (standardizzata)"); ax.set_ylabel("variabile 2 (standardizzata)")
    ax.set_aspect("equal"); ax.set_title("PCA: nuovi assi lungo le direzioni di massima varianza", fontsize=10)
    fig.tight_layout()
    salva(fig, "pca_concetto")


# 10. flusso ML ---------------------------------------------------------
def workflow():
    fig, ax = tela(10, 2.2)
    tappe = ["dati grezzi", "matrice\ncampioni × variabili", "preprocessing\n(scaling, NaN)", "modello", "valutazione\n(CV, metriche)", "conclusione\nonesta"]
    cols = ["#eeeeee", "#dfe9f5", "#fde6c4", "#d5f0e6", "#f5d5d5", "#eeeeee"]
    for k, (t, c) in enumerate(zip(tappe, cols)):
        box(ax, 0.2 + k * 1.65, 0.7, 1.45, 0.9, t, colore=c, fs=8)
        if k < 5:
            freccia(ax, 1.65 + k * 1.65, 1.15, 1.85 + k * 1.65, 1.15)
    ax.text(5, 1.9, "Il flusso di lavoro del machine learning (giorno 4)", ha="center", fontsize=11)
    salva(fig, "workflow_ml")


# 11. anatomia di una figura matplotlib --------------------------------
def anatomia_figura():
    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 50); y = np.sin(x) + rng.normal(0, 0.1, 50)
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    fig.patch.set_facecolor("#f4f4f4")
    ax.plot(x, y, "o-", ms=4, label="serie A")
    ax.set_xlabel("etichetta x  ← ax.set_xlabel()"); ax.set_ylabel("etichetta y  ← ax.set_ylabel()")
    ax.set_title("titolo  ← ax.set_title()")
    ax.legend(title="legenda ← ax.legend()")
    ax.annotate("Axes (ax): il riquadro con i dati", xy=(0.5, 0.5), xycoords="axes fraction", ha="center",
                fontsize=11, color=BLU, bbox=dict(boxstyle="round", fc="white", ec=BLU))
    fig.text(0.02, 0.97, "Figure (fig): il foglio intero", color=ROS, fontsize=10, va="top")
    ax.annotate("tick e tick label ← ax.tick_params()", xy=(2, -1.1), xytext=(4.5, -1.4), fontsize=8,
                arrowprops=dict(arrowstyle="->", lw=0.8), annotation_clip=False)
    fig.subplots_adjust(bottom=0.2)
    salva(fig, "anatomia_figura")


# 12. traceback -----------------------------------------------------------
def traceback_schema():
    fig, ax = tela(9, 3.4)
    tb = ("Traceback (most recent call last):\n"
          "  File \"<cell>\", line 3, in <module>\n"
          "    media = calcola_media(valori)\n"
          "  File \"<cell>\", line 1, in calcola_media\n"
          "    return sum(v) / len(v)\n"
          "TypeError: unsupported operand type(s) for /: 'str' and 'int'")
    ax.text(0.3, 3.1, tb, family="monospace", fontsize=9, va="top")
    ax.annotate("1. leggi l'ULTIMA riga: tipo di errore e spiegazione", xy=(5.9, 0.75), xytext=(5.6, 0.25),
                fontsize=9, color=ROS, arrowprops=dict(arrowstyle="->", color=ROS))
    ax.annotate("2. risali alla riga di codice TUA più vicina", xy=(3.3, 2.5), xytext=(5.2, 2.9),
                fontsize=9, color=BLU, arrowprops=dict(arrowstyle="->", color=BLU))
    ax.text(6.5, 1.7, "3. chiediti: che TIPO ha\n   davvero la variabile?", fontsize=9, color=VER)
    salva(fig, "traceback")


if __name__ == "__main__":
    for f in [indici_lista, broadcasting, dataframe, loc_iloc, groupby, merge, kfold, overfitting,
              leakage, pca, workflow, anatomia_figura, traceback_schema]:
        f()
