import matplotlib.pylab as pt
import numpy as np

x = np.linspace(-np.pi, np.pi, 201)
pt.plot(x, np.sin(x))
pt.xlabel('Angle [rad]')
pt.ylabel('sin(x)')
pt.axis('tight')
pt.show()
