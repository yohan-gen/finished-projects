# law of cosines

import math

print("enter the values of the sides and the angle between them, after that the missing value will be returned")
print("now enter the values, if it is a fraction, type the denominator value, if not, just type 1")

l1 = float(input(" length side 1 - "))
l2 = float(input(" length side 2 - "))
ang = float(input(" value of the angle between the sides - "))

rang = math.radians(ang)
tang = math.cos(rang)

total = (l1**2)+(l2**2)-(2*l1*l2*tang)
print(total**0.5)
