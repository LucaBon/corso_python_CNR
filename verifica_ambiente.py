"""Verifica dell'ambiente:  uv run python verifica_ambiente.py   (o: python verifica_ambiente.py con Miniforge)
Deve stampare 'tutto ok'.
Mandate l'output al docente almeno tre giorni prima del corso."""
import sys, platform
print(f"Python {sys.version.split()[0]} su {platform.system()} {platform.release()}")
errori = []
for modulo in ["numpy", "pandas", "matplotlib", "scipy", "sklearn", "seaborn", "openpyxl", "PIL", "IPython",
               "jupyterlab", "ipykernel"]:
    try:
        m = __import__(modulo)
        print(f"  {modulo:12s} {getattr(m, '__version__', 'ok')}")
    except Exception as e:
        errori.append(modulo)
        print(f"  {modulo:12s} MANCA  ({e})")
if errori:
    print("\nPROBLEMA: mancano", ", ".join(errori), "-> rilanciare 'uv sync' (o 'conda env create -f environment.yml')")
else:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, numpy as np
    fig, ax = plt.subplots(); ax.plot(np.linspace(0, 1, 5)); plt.close(fig)
    import pandas as pd
    if int(pd.__version__.split(".")[0]) < 3:
        print(f"\nATTENZIONE: pandas {pd.__version__}: il corso usa pandas 3. Funziona, ma alcuni output")
        print("(es. i tipi delle colonne di testo: 'object' invece di 'str') saranno diversi dagli output attesi.")
    print("\ntutto ok")
