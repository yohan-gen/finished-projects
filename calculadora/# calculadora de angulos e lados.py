# calculadora de angulos e lados

import math

print("bem vindo a calculadora geometrica de lados e angulos, para começar, escola o calculo a ser realizado : \n")

esc = int(input("\n 1 - teorema de pitagoras(para triangulos retangulos) "
                "\n 2 - lei dos senos (2 angulos e um valor) "                # aqui ele vai explicar cada escolha que pode ser feita 
                "\n 3 - lei dos cosseno (2 valores e o angulo entre eles) \n"))   # voce tem que digitar o numero correspondente a opção que deseja
if esc == 1 :

    # pythagoras theorem

    print("\ninsira os valores dos catetos e/ou a hipotenusa, apos isso os valores serao retornados com o valor faltante")
    print("\n agora insira os valores, o valor que faltar apenas digite 0, se for fração, digite o valor do denominador, se não, apenas digite 1")
    C1 = float(input("\n cateto 1 - "))
    dem1 = float(input("\n denominador cateto 1 - "))    # o denominador é para representar uma fração, se não for fração apenas digite 1
    C2 = float(input("\n cateto 2 - "))                  # pois qualquer numero dividido por 1 é ele mesmo
    dem2 = float(input("\n denominador cateto 2 - "))    #atribuindo valor aos catetos e a hipotenusa, se colocar um valor como 0 nos
    H = float(input("\n hipotenusa - "))                 #catetos ou na hipotenusa, a calcudora entendera essa variavel como a desconhecida
    demh = float(input("\n denominador hipotenusa - \n"))  # ou seja o valor que tem que descobrir

    if C1 == 0 :
        
        rd2 = C2/dem2 # dividir o cateto/hipotenusa pelo denominador, se for 1, o numero sera ele mesmo
        rh = H/demh
        res1 = rd2**2 # elevamos o resultado ao quadrado
        res2 = rh**2                # se o primeiro cateto for 0, faremos uma equação que o resultado sera o valor do cateto 1
        res3 = res2 - res1 # hipotenusa menos o cateto
        C1 = res3**0.5 # e fazemos raiz quadrada pelo exponente de 0.5
        print ("\n perfeito, o calculo foi feito e aqui estão os resultados \n")
        print("C1 - ", C1 , "\n C2 - ", rd2 , "\n H - ", rh)

    elif C2 == 0 :
        
        rd1 = C1/dem1
        rh = H/demh
        res1 = rd1**2               # se o segundo cateto for zero o resultado dessa equação sera o valor do cateto 2
        res2 = rh**2
        res3 = res2 - res1 # hipotenusa menos o cateto
        C2 = res3**0.5
        print ("\nperfeito, o calculo foi feito e aqui estão os resultados")
        print("\n")
        print("C1 - ", rd1 , "\\ C2 - ", C2 , "\\ H - ", rh)

    elif H == 0 :   #se a hipotenusa for 0 a soma dos catetos ao quadrado é igual a raiz da hipotenusa
        
        rd1 = C1/dem1 # cateto 1 e cateto 2, divide pelo denominador, se for 1 o numero n vai mudar
        rd2 = C2/dem2
        res1 = rd1**2 # elevamos os catetos ao quadrado
        res2 = rd2**2                
        res3 = res2 + res1 # soma os catetos
        H = res3**0.5 # a soma dos catetos, eleva a 0.5 para ter a raiz quadrada, a hipotenusa
        print ("perfeito, o calculo foi feito e aqui estão os resultados")
        print("\n")

        print("C1 - ", rd1 , "\\ C2 - ", rd2 , "\\ H - ", H) # no final de cada conta o print mostra o valor de todos os valores

elif esc == 2 : # se a escolha for 2 aplicaremos a formula da lei do seno

    #lei do seno

    print("\nagora insira os valores, o valor desconhecido apenas coloque como 1")

    escSIN = int(input("\n voce quer calcular um angulo ou um lado?" # aqui damos uma escolha ao user para saber o que 
                       "\nlado - (digite 1) "                        # ele quer calcular, pode ser um angulo, ou um lado desconhecido
                       "\nangulo - (digite 2) "))

    if escSIN == 1 : # se quiser descobrir o valor de um lado desconhecido esse sera o procedimento

        l1 = float(input("\n comprimento lado 1 - "))
        ang1 = float(input("\n angulo oposto ao lado 1 - "))     # variaveis serao atribuido valores conforme os lados e angulos
        ang2 = float(input(" \nangulo oposto ao lado 2 - "))
        rang1 = math.radians(ang1)   #transformamos o angulo em radiano
        rang2 = math.radians(ang2)   
        sang1 = math.sin(rang1)      #transformamos o valor RAD no valor de seno do angulo
        sang2 = math.sin(rang2)
        total = (l1*sang2)/(sang1)   #expressão que representa a lei dos senos
        print(total) # lado faltante

    elif escSIN == 2 :  # mas se quiser descobrir um angulo o procedimento sera levemente diferente

        l1 = float(input("\n comprimento lado 1 - "))
        l2 = float(input("\n comprimento lado 2 - "))
        ang1 = float(input("\n angulo oposto ao lado 1 - "))     # variaveis serao atribuido valores conforme os lados e angulos
        rang1 = math.radians(ang1)   #transformamos o angulo em radiano  
        sang1 = math.sin(rang1)      #transformamos o valor RAD no valor de seno do angulo
        total = (l2*sang1)/(l1)   #expressão que representa a lei dos senos
        tang2 = math.degrees(total) # converter o valor para o angulo aproximado
        print(tang2)

elif esc == 3 :
        
     # lei do cosseno

    print("insira os valores dos lados e o angulo entre eles, apos isso os valores serao retornados com o valor faltante")
    print("agora insira os valores")

    l1 = float(input(" comprimento lado 1 - "))
    l2 = float(input(" comprimento lado 2 - "))         # atribuido o valor dos lados e angulos para as variaveis para realizar o calculo
    ang = float(input(" valor do angulo entre os lados - "))
    rang = math.radians(ang)
    cang = math.cos(rang)

    total = (l1**2)+(l2**2)-(2*l1*l2*cang)  # expressao que representa o valor da lei dos cossenos
    print(total**0.5)   # usamos ** para representar exponentes, um numero elevado a **0.5 representa sua raiz quadrada
                        # agora **2 e ao quadrado, **3 ao cubo, e assim sucessivamente