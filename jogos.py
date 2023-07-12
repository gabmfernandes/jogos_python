import forca
import adivinhacao

def escolher_jogo():
    print("*"*30)
    print("Escolha o seu jogo!")
    print("*"*30)

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo executar?"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == '__main__'):
    escolher_jogo()