import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)

plt.figure().set_figheight(18)
plt.figure().set_figwidth(25)

for i in range(10):
    f = open(f'run{i}', "r")
    lines = f.readlines()
    y = [float(l.strip()) for l in lines]

    plt.plot(x, y, label = f'Best scores run {i}')

plt.legend(loc="upper left")
plt.savefig(f'no_max_scoresI.png')