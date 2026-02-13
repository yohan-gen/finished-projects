import math
while True:
    print("\n=== Trigonometric Calculator ===")
    print("1 - Calculate sine (sin)")
    print("2 - Exit")
    
    opcao = input("Choose an option: ")

    if opcao == "1":
        ang = float(input("Enter the angle in degrees: "))
        sen = math.sin(math.radians(ang))
        print(f"sin({ang}) = {sen}")
    elif opcao == "2":
        print("Exiting...")
        break
    else:
        print("Invalid option!")
