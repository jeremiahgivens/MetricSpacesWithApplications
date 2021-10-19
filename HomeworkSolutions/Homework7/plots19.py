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


for n in range(1, 500):
    x = np.linspace(0, 1, 2)
    y = [0, (1.0/n)*x[1]]
    plt.plot(x, y, color="black")

x = np.linspace(.5, 1, 2)
plt.plot(x, 0*x, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of $K$")

plt.savefig("plots19.pgf")
