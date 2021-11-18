import numpy as np
import matplotlib.pyplot as plt

# x(t) = 2 tan^(-1)(tanh(1/4 (c_1 + t^2)))

t = np.linspace(-3, 3, 1000)
x = np.arctan(np.tanh((t**2)/4))

# t^2/2 - t^6/48 + t^10/768 - (61 t^14)/645120 + O(t^18)
# (Taylor series)
x2 = (t**2)/2 - (t**6)/48 + (t**10)/768 - (61 * t**14)/645120

x3 = (1/2)*(t**2)*np.cos(np.sin((t**2)/2))

plt.plot(t, x, t, x2, t, x3)
plt.ylim((-.2, 1))
plt.show()
