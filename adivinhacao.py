import random
def jogar():
    print("*"*30)
    print("Bem vindo ao jogo da Adivinhação!")
    print("*"*30)


    numero_secreto = random.randint(1,101)
    dificuldade = int(input("Digite o nível de dificuldade (1) Fácil (2) Médio (3) Difícil:"))
    rodada = 1
    pontuacao = 1000

    if (dificuldade == 1):
        qtd_tentativas = 20
    elif(dificuldade == 2):
        qtd_tentativas = 10
    else:
        qtd_tentativas = 5




    for rodada in range(1,qtd_tentativas+1):
        print(f"\nVocê tem {qtd_tentativas+1-rodada} tentativas para adivinhar o número!")
        print(f"Tentativa {rodada} de {qtd_tentativas}\n")

        chute = int(input("Digite um numero de 1 a 100:"))
        print(f"Numero digitado: {chute}")

        pontos_perdidos = abs(numero_secreto - chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto


        if(acertou):
            print(f"Você acertou e obteve {pontuacao} pontos!")
            break
        elif(maior):
            pontuacao = pontuacao - pontos_perdidos
            print("Você errou!Tente um numero menor")
            if (rodada == qtd_tentativas):
                print(f"O número secreto era: {numero_secreto}. Você obteve {pontuacao} pontos!")
        else:
            pontuacao = pontuacao - pontos_perdidos
            print("Você errou!Tente um numero maior")
            if (rodada == qtd_tentativas):
                print(f"O número secreto era: {numero_secreto}. Você obteve {pontuacao} pontos!")

        rodada = rodada + 1


    print("Fim do jogo!")

if(__name__ == '__main__'):
    jogar()