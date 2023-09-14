import numpy as Np
import matplotlib.pyplot as Plt

# Sin(X) Chart

X = Np.arange(0.00, 2*Np.pi, 0.10)
Y = Np.sin(X)
Plt.plot(X, Y)
Plt.ylabel('( Y )')
Plt.xlabel('( X )')
Plt.title("Sin(X)")
Plt.show()
