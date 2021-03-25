import numpy as np
from matplotlib.pylab import plt
import tikzplotlib

x = np.linspace(0, 1, 100)
y = 1-np.exp(-10*x)

plt.xticks([])
plt.yticks([])

plt.ylim([0,1.5])
plt.xlim([0,1.05])

plt.xlabel('$p_A$')
plt.ylabel('$r$')

plt.annotate('1st order', xy=(0.075, 0.4), xytext=(0.075, 0.4), rotation=60)
plt.annotate('zero order', xy=(0.75, 1.05), xytext=(0.75, 1.05))
plt.plot(x, y)
tikzplotlib.save("plot_ER.tex", axis_height="9cm", axis_width="10cm")