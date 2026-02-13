# sides and angles calculator

import math

print("welcome to the geometric calculator of sides and angles, to start, choose the calculation to be performed : \n")

esc = int(input("\n 1 - pythagorean theorem (for right triangles) "
                "\n 2 - law of sines (2 angles and one value) "
                "\n 3 - law of cosines (2 values and the angle between them) \n"))

if esc == 1 :

    # pythagorean theorem

    print("\nenter the values of the legs and/or the hypotenuse, after that the missing value will be returned")
    print("\n now enter the values, for the missing value just type 0, if it is a fraction, type the denominator value, if not, just type 1")

    C1 = float(input("\n leg 1 - "))
    dem1 = float(input("\n denominator leg 1 - "))
    C2 = float(input("\n leg 2 - "))
    dem2 = float(input("\n denominator leg 2 - "))
    H = float(input("\n hypotenuse - "))
    demh = float(input("\n denominator hypotenuse - \n"))

    if C1 == 0 :
        
        rd2 = C2/dem2
        rh = H/demh
        res1 = rd2**2
        res2 = rh**2
        res3 = res2 - res1
        C1 = res3**0.5

        print ("\n perfect, the calculation was done and here are the results \n")
        print("C1 - ", C1 , "\n C2 - ", rd2 , "\n H - ", rh)

    elif C2 == 0 :
        
        rd1 = C1/dem1
        rh = H/demh
        res1 = rd1**2
        res2 = rh**2
        res3 = res2 - res1
        C2 = res3**0.5

        print ("\nperfect, the calculation was done and here are the results")
        print("\n")
        print("C1 - ", rd1 , "\\ C2 - ", C2 , "\\ H - ", rh)

    elif H == 0 :
        
        rd1 = C1/dem1
        rd2 = C2/dem2
        res1 = rd1**2
        res2 = rd2**2
        res3 = res2 + res1
        H = res3**0.5

        print ("perfect, the calculation was done and here are the results")
        print("\n")
        print("C1 - ", rd1 , "\\ C2 - ", rd2 , "\\ H - ", H)

elif esc == 2 :

    # law of sines

    print("\nnow enter the values, for the unknown value just put 1")

    escSIN = int(input("\n do you want to calculate an angle or a side?"
                       "\nside - (type 1) "
                       "\nangle - (type 2) "))

    if escSIN == 1 :

        l1 = float(input("\n length side 1 - "))
        ang1 = float(input("\n angle opposite to side 1 - "))
        ang2 = float(input(" \nangle opposite to side 2 - "))

        rang1 = math.radians(ang1)
        rang2 = math.radians(ang2)

        sang1 = math.sin(rang1)
        sang2 = math.sin(rang2)

        total = (l1*sang2)/(sang1)
        print(total)

    elif escSIN == 2 :

        l1 = float(input("\n length side 1 - "))
        l2 = float(input("\n length side 2 - "))
        ang1 = float(input("\n angle opposite to side 1 - "))

        rang1 = math.radians(ang1)
        sang1 = math.sin(rang1)

        total = (l2*sang1)/(l1)
        tang2 = math.degrees(total)

        print(tang2)

elif esc == 3 :
        
    # law of cosines

    print("enter the values of the sides and the angle between them, after that the missing value will be returned")
    print("now enter the values")

    l1 = float(input(" length side 1 - "))
    l2 = float(input(" length side 2 - "))
    ang = float(input(" value of the angle between the sides - "))

    rang = math.radians(ang)
    cang = math.cos(rang)

    total = (l1**2)+(l2**2)-(2*l1*l2*cang)
    print(total**0.5)
