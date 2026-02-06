#% Imports

import numpy as np

print("%10s %10s %10s %10s" %("x   ", "sin(x)", "cos(x)", "tan(x)"))
for x in np.arange(0,11,1):
    degree = x * np.pi / 180
    print("%10.5f %10.5f %10.5f %10.5f" %(x, np.sin(degree),
                                          np.cos(degree), np.tan(degree)))
print("") # Insert newline

for x in np.arange(5,86,1): # Calculate from 5 degree to 85 degree
    degree = x * np.pi / 180
    print("%10.5f %10.5f %10.5f %10.5f" %(x, np.sin(degree),
                                          np.cos(degree), np.tan(degree)))
