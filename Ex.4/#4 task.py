import numpy as np
import matplotlib.pylab as plt

m = np.linspace(0, 2*np.pi, 100)
tenth = m[10::10]
reverse = m[::-1]
diff = m[abs(np.sin(m) - np.cos(m)) < 0.1]
plt.plot(m, np.sin(m))
plt.plot(m, np.cos(m))
# plt.plot(m, abs(np.sin(m) - np.cos(m)) < 0.4)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x) cos(x)')
plt.axis('tight')
plt.show()


print(m)
# print(tenth)
# print(reverse)
print(diff)