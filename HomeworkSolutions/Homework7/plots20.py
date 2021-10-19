import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


x = np.linspace(0, 100, 1000)
plt.plot(x, np.sqrt(x), color="black")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Plot of $f(x) = \sqrt{x}$")

plt.savefig("plots20.pgf")

