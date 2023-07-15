import random

def jogar():
    print_boas_vindas()

    palavra_secreta = definir_palavra()

    letras_acertadas = inicializar_palavra(palavra_secreta)
    print(letras_acertadas)

    letras_chutadas = []

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()
        if(chute in letras_chutadas):
            print("\nVocê já digitou essa letra antes. Por favor, tente outra")
            continue
        letras_chutadas.append(chute)
        
        if (chute in palavra_secreta):
            adicionar_letra(chute,palavra_secreta,letras_acertadas)
            if ('_' not in letras_acertadas):
                acertou = True
        else:
            erros = erros + 1
            desenha_forca(erros)
            if (erros == 7):
                break
            print(f"\nTente outra letra. Restam {7-erros} tentativas")
        
    if(acertou):
        print_vencedor() 
    else:
        print_perdedor(palavra_secreta)
    print("\nFim do jogo!")

def print_boas_vindas():
    print("*" * 30)
    print("Bem vindo ao jogo da Forca!")
    print("*" * 30)

def definir_palavra():
    arquivo = open("palavras.txt","r")

    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()
    
    palavra_secreta = random.choice(palavras).upper()

    return palavra_secreta

def inicializar_palavra(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    return input("\nDigite uma letra: ").strip().upper()

def adicionar_letra(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = chute
        print(letras_acertadas[index],end='')
        index+=1

def print_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()
