import pylab as p
import numpy as np
import matplotlib; 
import matplotlib.pyplot; 

print("Your Python Backend:")
print(matplotlib.backends.backend)

print("Printing Test Image")
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

p.plot(C,S)
p.show()
