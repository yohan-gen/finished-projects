# lei do cosseno

import math

print("insira os valores dos lados e o angulo entre eles, apos isso os valores serao retornados com o valor faltante")
print("agora insira os valores, se for fração, digite o valor do denominador, se não, apenas digite 1")

l1 = float(input(" comprimento lado 1 - "))
l2 = float(input(" comprimento lado 2 - "))
ang = float(input(" valor do angulo entre os lados - "))
rang = math.radians(ang)
tang = math.cos(rang)

total = (l1**2)+(l2**2)-(2*l1*l2*tang)
print(total**0.5)