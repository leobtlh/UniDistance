import numpy as np
import matplotlib.pyplot as plt

# start: 0, end: 20, step: 0.2
x = np.arange(0., 20., 0.2)

# fct. f(x) = -x + 10
f = -x + 10

plt.plot(x, f)
plt.xlabel("x")
plt.ylabel("y")
plt.title('Homework 2: (ii)')
plt.grid(True)
plt.show()
