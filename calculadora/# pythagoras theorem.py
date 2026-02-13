# pythagoras theorem

print("insira os valores dos catetos e/ou a hipotenusa, apos isso os valores serao retornados com o valor faltante")
print("agora insira os valores, o valor que faltar apenas digite 0, se for fração, digite o valor do denominador, se não, apenas digite 1")
C1 = float(input(" cateto 1 - "))
dem1 = float(input(" denominador cateto 1 - "))
C2 = float(input(" cateto 2 - "))
dem2 = float(input(" denominador cateto 2 - "))
H = float(input(" hipotenusa - "))
demh = float(input(" denominador hipotenusa - "))

if C1 == 0 :
    
    rd2 = C2/dem2
    rh = H/demh
    res1 = rd2**2 
    res2 = rh**2
    res3 = res2 - res1
    C1 = res3**0.5
    print ("perfeito, o calculo foi feito e aqui estão os resultados")
    print("\\")
    print("C1 - ", C1 , "\\ C2 - ", rd2 , "\\ H - ", rh)

elif C2 == 0 :
    
    rd1 = C1/dem1
    rh = H/demh
    res1 = rd1**2 
    res2 = rh**2
    res3 = res2 - res1
    C2 = res3**0.5
    print ("perfeito, o calculo foi feito e aqui estão os resultados")
    print("\\")
    print("C1 - ", rd1 , "\\ C2 - ", C2 , "\\ H - ", rh)

elif H == 0 :
    
    rd1 = C1/dem1
    rd2 = C2/dem2
    res1 = rd1**2 
    res2 = rd2**2
    res3 = res2 + res1
    H = res3**0.5
    print ("perfeito, o calculo foi feito e aqui estão os resultados")
    print("\\")
    print("C1 - ", rd1 , "\\ C2 - ", rd2 , "\\ H - ", H)

