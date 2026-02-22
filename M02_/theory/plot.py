import numpy as np
import matplotlib.pyplot as plt

# start: 1.5 (doit être > 1 pour log(log(x))), end: 20, step: 0.2
x = np.arange(0., 50., 0.2)

# On utilise np.log() et on l'applique sur le tableau 'x'
f = 2*np.log2(x)
g = np.log2(x)**2 / np.log2(3)

# Ajout du paramètre 'label' pour la légende
plt.plot(x, f, label='y = 2x')
plt.plot(x, g, label='y = x² / log2(3)')

plt.xlabel("x")
plt.ylabel("y")
plt.title('Comparaison de log(x) et log(log(x))')
plt.grid(True)
plt.legend() # Affiche la légende
plt.show()
