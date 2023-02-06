import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
U = np.array([8.66, 8.75, 8.83, 8.86, 8.89, 8.92, 0.727, 0.701, 0.723, 0.749, 0.781, 0.835])
I = np.array([1,2,5,10,20,50,100,200,500,1000,2000,5000])


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel(r'U in V')
ax1.set_ylabel(r'i in $\mu A$', color=color)
ax1.plot(U, I, '.--', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel(r'i in $\mu A$', color=color)  # we already handled the x-label with ax1
ax2.set_yscale('log')
ax2.plot(U, I, '.--', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Vierschichtdiode in Vorwärtsrichtung')

plt.grid(True)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
