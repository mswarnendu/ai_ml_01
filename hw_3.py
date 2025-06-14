import numpy as np

x0 = input("What value will we use for x?")
x0 = float(x0)
h = input("How much will be our increment?")
h = float(h)
f1 = np.sin(x0+h)
f2 = -np.sin(x0-h)
print("Numerical derivative for sin(x):\n")
print((f1+f2)/(2*h))

f3 = (x0+h)**3 + 2*(x0+h)**2 + (x0+h)
f4 = -(x0-h)**3 - 2*(x0-h)**2 - (x0-h)
print("Numerical derivative for x^3+2x^2+x:\n")
print((f3+f4)/(2*h))

f5 = np.tan(x0+h)
f6 = -np.tan(x0-h)
print("Numerical derivative of tan(x):\n")
print((f5+f6)/(2*h))






