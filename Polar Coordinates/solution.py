import math
import cmath
n=complex(input())
print(math.sqrt((n.real*n.real)+(n.imag*n.imag)))
print(cmath.phase(complex(n.real,n.imag)))
