import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
fig = plt.figure()
plt.plot(x, np.sin(x), "-")
plt.plot(x, np.cos(x), "--")

fig.savefig("my_figure.png")