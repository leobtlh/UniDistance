import numpy as np
import matplotlib.pyplot as plt

# start: -2, end: 2, number of points: 100
x = np.linspace(-2, 2, 100)

# fct. f: [-2, 2] → R, f(x) = x² - 1
f = x**2 - 1

plt.plot(x, f)
plt.xlabel("x")
plt.ylabel("y")
plt.title('Homework 2: (ii)')
plt.grid(True)
plt.show()
