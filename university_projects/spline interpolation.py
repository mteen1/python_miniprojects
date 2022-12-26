import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# numerical analysis, Prof. Mostafa Jani
# Cubic-spline interpolation for f(x) = cos(x)


x = np.arange(0, 1.2, 0.2)
y = np.cos(x)
spl = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, 1, 0.00001)
ynew = interpolate.splev(xnew, spl, der=0)

xpoint = [0.5]
ypoint = [interpolate.splev(xpoint, spl, der=0)]
plt.figure()
plt.plot(x, y, 'x', xnew, ynew,'r', xpoint, ypoint, '.',markersize=10)
plt.legend(['data','spline','x = 0.5 with spline'])
plt.axis([-0.05, 1.05, 0.5, 1.05])
plt.title('Cubic-spline interpolation')
plt.show()
