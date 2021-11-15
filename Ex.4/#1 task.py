import numpy as np

m = np.arange(12).reshape((3,4))

print(m)
print(m.mean())
print(m.mean(axis=1))
print(m.mean(axis=0))