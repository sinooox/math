#16

import math

x = float(input('enter x: '))

z1 = (x**2+2*x-3+(x+1)*math.sqrt(x**2-9)) / (x**2-2*x-3+(x-1)*math.sqrt(x**2-9))
z2 = math.sqrt((x+3)/(x-3))

print(f'z1 = {z1}')
print(f'z2 = {z2}')
