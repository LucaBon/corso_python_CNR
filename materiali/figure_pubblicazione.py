"""
figure_pubblicazione.py
Impostazioni Matplotlib e funzione di export per figure conformi ai requisiti
delle principali riviste scientifiche (Elsevier, ACS, Springer, Wiley).

Uso tipico in un notebook:

    from figure_pubblicazione import stile_rivista, LARGHEZZE, salva_figura
    stile_rivista()            # globale; in alternativa:  with stile_rivista_ctx(): ...
    fig, ax = plt.subplots(figsize=(LARGHEZZE['acs_singola'], 2.5))
    ...
    salva_figura(fig, 'figura1', formati=('pdf', 'tif'), dpi=600)
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------------------------------
# Larghezze di colonna, in POLLICI (matplotlib ragiona in pollici, non in cm)
# --------------------------------------------------------------------------
LARGHEZZE = {
    'acs_singola':     3.33,   # ACS: max 240 pt
    'acs_doppia':      7.00,   # ACS: tra 4.167 e 7 in
    'elsevier_singola': 3.54,  # ~90 mm
    'elsevier_1_5':     5.51,  # ~140 mm
    'elsevier_doppia':  7.48,  # ~190 mm
}

CM = 1 / 2.54  # per scrivere le dimensioni in cm: figsize=(9*CM, 6*CM)


def _parametri_rivista(base_font=8, famiglia=('Arial', 'Helvetica', 'DejaVu Sans')):
    """Dizionario di rcParams conformi ai requisiti editoriali (usato da stile_rivista e stile_rivista_ctx)."""
    return {
        # --- Font ---------------------------------------------------------
        'font.family': 'sans-serif',
        'font.sans-serif': list(famiglia),
        'font.size': base_font,
        'axes.labelsize': base_font,
        'axes.titlesize': base_font,
        'xtick.labelsize': base_font - 1,
        'ytick.labelsize': base_font - 1,
        'legend.fontsize': base_font - 1,

        # --- Font EMBEDDATI come TrueType, non Type 3 ---------------------
        # Cruciale: il default di Matplotlib e' Type 3, che molti editori
        # rifiutano o rendono male in fase di tipografia.
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'svg.fonttype': 'none',   # testo modificabile in Illustrator/Inkscape

        # --- Spessori: ACS chiede linee non piu' sottili di 0.5 pt --------
        'lines.linewidth': 1.0,
        'axes.linewidth': 0.8,
        'xtick.major.width': 0.8,
        'ytick.major.width': 0.8,
        'grid.linewidth': 0.5,

        # --- Estetica sobria ---------------------------------------------
        'axes.spines.top': False,
        'axes.spines.right': False,
        'legend.frameon': False,
        'figure.facecolor': 'white',
        'savefig.facecolor': 'white',
        'savefig.dpi': 600,
        'figure.constrained_layout.use': True,
    }


def stile_rivista(base_font=8, famiglia=('Arial', 'Helvetica', 'DejaVu Sans')):
    """Imposta i parametri globali di Matplotlib secondo i requisiti editoriali.

    base_font : dimensione del testo in punti NELLA FIGURA FINALE.
                ACS chiede >= 4.5 pt (consigliato 8), Elsevier >= 6-7 pt.
    L'effetto e' GLOBALE (vale per tutte le figure successive): per tornare
    allo stile di default usare mpl.rcdefaults(), oppure usare stile_rivista_ctx.
    """
    mpl.rcParams.update(_parametri_rivista(base_font, famiglia))


def stile_rivista_ctx(base_font=8, famiglia=('Arial', 'Helvetica', 'DejaVu Sans')):
    """Come stile_rivista, ma solo dentro un blocco `with`:

        with stile_rivista_ctx():
            fig, ax = plt.subplots(figsize=(LARGHEZZE['elsevier_singola'], 2.5))
            ...
            salva_figura(fig, 'figura1')

    All'uscita dal blocco i parametri tornano quelli di prima.
    """
    return mpl.rc_context(_parametri_rivista(base_font, famiglia))


def salva_figura(fig, nome, formati=('pdf',), dpi=600, cartella='figure'):
    """Salva la figura nei formati richiesti, con le accortezze editoriali.

    formati:
      'pdf' / 'eps' / 'svg'  -> vettoriale (preferito da tutti gli editori)
      'tif'                  -> raster, convertito in RGB senza canale alpha
      'png'                  -> solo per bozze e presentazioni

    NOTA: non si usa bbox_inches='tight', perche' modifica la dimensione
    finale della figura e fa perdere la corrispondenza esatta con la
    larghezza di colonna richiesta. Il layout e' gestito da constrained_layout.
    """
    cartella = Path(cartella)
    cartella.mkdir(exist_ok=True)
    prodotti = []

    for fmt in formati:
        percorso = cartella / f'{nome}.{fmt}'

        if fmt == 'tif':
            # Matplotlib scrive TIFF in RGBA. Molti editori non vogliono il
            # canale alpha: si converte in RGB con Pillow.
            from PIL import Image
            tmp = cartella / f'_{nome}_tmp.tif'
            fig.savefig(tmp, dpi=dpi, facecolor='white', transparent=False)
            Image.open(tmp).convert('RGB').save(
                percorso, dpi=(dpi, dpi), compression='tiff_lzw')
            tmp.unlink()

        elif fmt == 'eps':
            # Il backend PostScript non supporta la trasparenza: gli elementi
            # con alpha < 1 vengono resi OPACHI (Matplotlib emette un avviso).
            # Evitare alpha nelle figure destinate a EPS.
            fig.savefig(percorso, format='eps')

        else:
            fig.savefig(percorso, dpi=dpi)

        prodotti.append(percorso)
        print(f'salvato: {percorso}')

    return prodotti


def controlla_font(nome='Arial'):
    """Verifica che il font richiesto sia davvero installato.

    Se non lo e', Matplotlib ripiega su DejaVu Sans stampando un messaggio
    'findfont' su stderr, facilissimo da non notare in un notebook.
    """
    from matplotlib import font_manager as fm
    trovato = Path(fm.findfont(nome, fallback_to_default=True)).stem
    if nome.lower().replace(' ', '') not in trovato.lower().replace(' ', ''):
        print(f"ATTENZIONE: '{nome}' non installato. In uso: {trovato}")
        return False
    print(f"Font '{nome}': disponibile")
    return True


def verifica_figura(fig, larghezza_max=7.0, font_min=4.5, linea_min=0.5):
    """Controllo rapido prima della sottomissione: dimensioni, font, spessori."""
    w, h = fig.get_size_inches()
    print(f'Dimensioni: {w:.2f} x {h:.2f} in  ({w*2.54:.1f} x {h*2.54:.1f} cm)')
    if w > larghezza_max:
        print(f'  ATTENZIONE: larghezza oltre {larghezza_max} in')
    if h > 9.167:
        print('  ATTENZIONE: altezza oltre il massimo ACS (9.167 in)')
    testi = []
    linee = []
    for ax in fig.axes:
        testi += [ax.xaxis.label, ax.yaxis.label, ax.title]
        testi += ax.get_xticklabels() + ax.get_yticklabels() + list(ax.texts)
        leg = ax.get_legend()
        if leg is not None:
            testi += list(leg.get_texts())
            if leg.get_title().get_text():
                testi.append(leg.get_title())
        linee += [l for l in ax.get_lines() if l.get_linestyle() not in ('None', '', ' ')]
    testi = [t for t in testi if t.get_text()]
    troppo_piccoli = [t for t in testi if t.get_fontsize() < font_min]
    if troppo_piccoli:
        print(f'  ATTENZIONE: {len(troppo_piccoli)} testi sotto {font_min} pt '
              f'(es. "{troppo_piccoli[0].get_text()[:20]}" a {troppo_piccoli[0].get_fontsize():.1f} pt)')
    else:
        print(f'  Font: ok ({len(testi)} testi, minimo {min(t.get_fontsize() for t in testi):.1f} pt)'
              if testi else '  Font: nessun testo')
    sottili = [l for l in linee if l.get_linewidth() < linea_min]
    if sottili:
        print(f'  ATTENZIONE: {len(sottili)} linee sotto {linea_min} pt')
    else:
        print('  Linee: ok')
    print(f'  Pixel a 600 dpi: {int(w*600)} x {int(h*600)}')


if __name__ == '__main__':
    import numpy as np
    stile_rivista()
    x = np.linspace(-0.4, 0.6, 300)
    fig, ax = plt.subplots(figsize=(LARGHEZZE['acs_singola'], 2.4))
    for c, lab in zip([1.0, 0.6, 0.3], ['100 uM', '60 uM', '30 uM']):
        ax.plot(x, c * np.exp(-((x - 0.15) / 0.08) ** 2), label=lab)
    ax.set_xlabel('E vs Ag/AgCl (V)')
    ax.set_ylabel('i (uA)')
    ax.legend(title='Analita')
    controlla_font('Arial')
    verifica_figura(fig)
    salva_figura(fig, 'esempio_voltammogramma',
                 formati=('pdf', 'eps', 'tif'), cartella='figure_prova')
