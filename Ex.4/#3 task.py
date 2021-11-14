import numpy as np

m = np.arange(0., 6.0, 0.1).reshape((6, 10))
m[m % 1 < 0.4] = 0
print(m)