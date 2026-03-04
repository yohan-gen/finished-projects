import random
from forcamedio import forcamedia
from forcadif import forcadiff
from forcaeng import englist

randword =                                                                                                                                                      ["janela", "bola", "amigo", "gato", "cidade", "livro", "mesa", "menina", "pato", "porta", "dado", "camisa", "peixe", "arvore", "casa", "sapato", "roupa", "prato", "coelho", "faca", "banho", "carro", "menino", "nuvem"]

tentativas = 6
errado = []

ok = True

while ok :
    print("Welcome ao jogo da forca...\n")
    print("primeiro, escolha a dificuldade : \n")
    print("[1] forca de nivel facil - 24 palavras\n"
        "[2] forca de nivel medio - 20 palavras\n"
        "[3] forca de nivel dificil - 16\n"
        "[4] forca de palavras em ingles, variando de palavras faceis até dificil, 16 palavras\n"
        "[5] parar de jogar")
    dif = int(input("escolha : \n"))


    if dif == 1 :
        
        palavra = random.choice(randword)
        letras = ["_" for _ in palavra]

        while tentativas > 0 and "_" in letras :


            print("\nPalavra:", " ".join(letras))
            print("Erros fatais:", errado)
            print("Vida restante:", tentativas)

            escolhida = input("\nEscolhe uma letra ai : ").lower()

            if not escolhida.isalpha() or len(escolhida) != 1:
                print("\nEscolha UMA letra seu filho da puta")
                continue

            if escolhida in letras or escolhida in errado:
                print("\nVocê já tentou essa bosta seu imundo")
                continue

            if escolhida in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == escolhida:
                        letras[i] = escolhida
                print("\nsó acerto dessa vez em seu lixo 👿")
            elif escolhida not in palavra:
                errado.append(escolhida)
                tentativas -= 1
                print("\nERROU otario! como esperado... mwahahhaha 😈")

        # FIM DO JOGO
        if "_" not in letras:
            print("\n🎉 só ganhou por que deixei em... a palavra era : ", palavra)
        elif tentativas == 0:
            print("\n💀 perdeuu hahahah, não que eu duvidasse do seu fracasso, a palavra era ", palavra)

    elif dif == 2 :

        palavra = random.choice(forcamedia())
        letras = ["_" for _ in palavra]

        while tentativas > 0 and "_" in letras :

            print("\nPalavra:", " ".join(letras))
            print("Erros fatais:", errado)
            print("Vida restante:", tentativas)

            escolhida = input("\nEscolhe uma letra ai : ").lower()

            if not escolhida.isalpha() or len(escolhida) != 1:
                print("\nEscolha UMA letra seu filho da puta")
                continue

            if escolhida in letras or escolhida in errado:
                print("\nVocê já tentou essa bosta seu imundo")
                continue

            if escolhida in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == escolhida:
                        letras[i] = escolhida
                        print("\nsó acerto dessa vez em seu lixo 👿")
            elif escolhida not in palavra:
                errado.append(escolhida)
                tentativas -= 1
                print("\nERROU otario! como esperado... mwahahhaha 😈")

        # FIM DO JOGO
        if "_" not in letras:
            print("\n🎉 só ganhou por que deixei em... a palavra era : ", palavra)
        elif tentativas == 0:
            print("\n💀 perdeuu hahahah, não que eu duvidasse do seu fracasso, a palavra era ", palavra)

    elif dif == 3 :
            
        palavra = random.choice(forcadiff())
        letras = ["_" for _ in palavra]

        while tentativas > 0 and "_" in letras :


            print("\nPalavra:", " ".join(letras))
            print("Erros fatais:", errado)
            print("Vida restante:", tentativas)

            escolhida = input("\nEscolhe uma letra ai : ").lower()

            if not escolhida.isalpha() or len(escolhida) != 1:
                print("\nEscolha UMA letra seu filho da puta")
                continue

            if escolhida in letras or escolhida in errado:
                print("\nVocê já tentou essa bosta seu imundo")
                continue

            if escolhida in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == escolhida:
                        letras[i] = escolhida
                print("\nsó acerto dessa vez em seu lixo 👿")
            elif escolhida not in palavra:
                errado.append(escolhida)
                tentativas -= 1
                print("\nERROU otario! como esperado... mwahahhaha 😈")

        # FIM DO JOGO
        if "_" not in letras:
            print("\n🎉 só ganhou por que deixei em... a palavra era : ", palavra)
        elif tentativas == 0:
            print("\n💀 perdeuu hahahah, não que eu duvidasse do seu fracasso, a palavra era ", palavra)

    elif dif == 4 :
        
        palavra = random.choice(englist())
        letras = ["_" for _ in palavra]

        while tentativas > 0 and "_" in letras :


            print("\nPalavra:", " ".join(letras))
            print("Erros fatais:", errado)
            print("Vida restante:", tentativas)

            escolhida = input("\nEscolhe uma letra ai : ").lower()

            if not escolhida.isalpha() or len(escolhida) != 1:
                print("\nEscolha UMA letra seu filho da puta")
                continue

            if escolhida in letras or escolhida in errado:
                print("\nVocê já tentou essa bosta seu imundo")
                continue

            if escolhida in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == escolhida:
                        letras[i] = escolhida
                print("\nsó acerto dessa vez em seu lixo 👿")
            elif escolhida not in palavra:
                errado.append(escolhida)
                tentativas -= 1
                print("\nERROU otario! como esperado... mwahahhaha 😈")

        # FIM DO JOGO
        if "_" not in letras:
            print("\n🎉 só ganhou por que deixei em... a palavra era : ", palavra)
        elif tentativas == 0:
            print("\n💀 perdeuu hahahah, não que eu duvidasse do seu fracasso, a palavra era ", palavra)
    
    elif dif == 5 :
        ok = False