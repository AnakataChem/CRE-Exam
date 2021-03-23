import numpy as np
from matplotlib.pylab import plt
import tikzplotlib

x = np.linspace(0, 1, 100)
y = 50*x/(2+5*x)**2

plt.xticks([])
plt.yticks([])

plt.ylim([0,1.5])
plt.xlim([0,1.05])

plt.xlabel('$p_A$')
plt.ylabel('$r$')

plt.annotate('1st order', xy=(0.075, 0.5), xytext=(0.075, 0.5), rotation=70)
plt.annotate('zero order', xy=(0.3, 1.3), xytext=(0.3, 1.3))
plt.annotate('-1st order', xy=(0.7, 1.15), xytext=(0.7, 1.15), rotation=-12)
plt.plot(x, y)
tikzplotlib.save("plot_LH.tex", axis_height="9cm", axis_width="10cm")