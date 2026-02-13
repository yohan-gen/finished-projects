# pythagoras theorem

print("enter the values of the legs and/or the hypotenuse, after that the missing value will be returned")
print("now enter the values, for the missing value just type 0, if it is a fraction, type the denominator value, if not, just type 1")

C1 = float(input(" leg 1 - "))
dem1 = float(input(" denominator leg 1 - "))
C2 = float(input(" leg 2 - "))
dem2 = float(input(" denominator leg 2 - "))
H = float(input(" hypotenuse - "))
demh = float(input(" denominator hypotenuse - "))

if C1 == 0 :
    
    rd2 = C2/dem2
    rh = H/demh
    res1 = rd2**2 
    res2 = rh**2
    res3 = res2 - res1
    C1 = res3**0.5

    print("perfect, the calculation was done and here are the results")
    print("\\")
    print("C1 - ", C1 , "\\ C2 - ", rd2 , "\\ H - ", rh)

elif C2 == 0 :
    
    rd1 = C1/dem1
    rh = H/demh
    res1 = rd1**2 
    res2 = rh**2
    res3 = res2 - res1
    C2 = res3**0.5

    print("perfect, the calculation was done and here are the results")
    print("\\")
    print("C1 - ", rd1 , "\\ C2 - ", C2 , "\\ H - ", rh)

elif H == 0 :
    
    rd1 = C1/dem1
    rd2 = C2/dem2
    res1 = rd1**2 
    res2 = rd2**2
    res3 = res2 + res1
    H = res3**0.5

    print("perfect, the calculation was done and here are the results")
    print("\\")
    print("C1 - ", rd1 , "\\ C2 - ", rd2 , "\\ H - ", H)
