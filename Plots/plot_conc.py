import numpy as np
from matplotlib.pylab import plt
import tikzplotlib

x = np.linspace(0, 2, 100)
y = 5 * np.exp(np.log(1/5) / 2 * x)
y21 = np.full(x.size, 5)
y22 = np.full(x.size, 3)
y23 = np.full(x.size, 1)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

fig.tight_layout()

ax1.set_yticks([])
ax1.set_ylim([0,8])
ax1.set_xticks([])
ax1.set_xlim([0,2.75])
ax1.set_ylabel('$c_A$')
ax1.set_xlabel('$t$')
ax1.annotate('$t = t_R$', xy=(2.1, 1), xytext=(2.1, 1))
ax1.plot(x, y)

ax2.set_yticks([])
ax2.set_ylim([0,8])
ax2.set_xticks([])
ax2.set_xlim([0,2.75])
ax2.set_ylabel('$c_A$')
ax2.set_xlabel('$x$')
ax2.margins(x=0)
ax2.plot(x, y21, 'tab:red')
ax2.annotate('$t = 0$', xy=(2.1, 5), xytext=(2.1, 5))
ax2.plot(x, y22, 'tab:red')
ax2.annotate('$t = t_1$', xy=(2.1, 3), xytext=(2.1, 3))
ax2.plot(x, y23, 'tab:red')
ax2.annotate('$t = t_R$', xy=(2.1, 1), xytext=(2.1, 1))

ax3.set_yticks([])
ax3.set_ylim([0,8])
ax3.set_xticks([])
ax3.set_xlim([0,2.75])
ax3.set_ylabel('$c_A$')
ax3.set_xlabel('$t$')
ax3.margins(x=0)
ax3.plot(x, y21, 'tab:blue')
ax3.annotate('$x = 0$', xy=(2.1, 5), xytext=(2.1, 5))
ax3.plot(x, y22, 'tab:blue')
ax3.annotate('$x = x_1$', xy=(2.1, 3), xytext=(2.1, 3))
ax3.plot(x, y23, 'tab:blue')
ax3.annotate('$x = L$', xy=(2.1, 1), xytext=(2.1, 1))

ax4.set_yticks([])
ax4.set_ylim([0,8])
ax4.set_xticks([])
ax4.set_xlim([0,2.75])
ax4.set_ylabel('$c_A$')
ax4.set_xlabel('$x$')
ax4.plot(x, y, 'tab:red')
ax4.annotate('$x = L$', xy=(2.1, 1), xytext=(2.1, 1))

tikzplotlib.save("plot_conc.tex", axis_height="5cm", axis_width="6cm")
