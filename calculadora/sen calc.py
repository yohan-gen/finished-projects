

while True:
    print("\n=== Calculadora Trigonométrica ===")
    print("1 - Calcular seno (sen)")
    print("2 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ang = float(input("Digite o ângulo em graus: "))
        sen = math.sin(math.radians(ang))
        print(f"sen({ang}) = {sen}")
    elif opcao == "2":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
