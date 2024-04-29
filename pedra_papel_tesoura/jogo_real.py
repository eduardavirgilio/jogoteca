from .funcoes_do_jogo import *

def jogo_pedra ():

    import random

    import os 

    os.system("cls")

    print ("seja bem vindo ao jogo pedra, papel e tesoura!")
    print ("você pode escolher entre pedra, papel e tesoura e o computador irá jogar contra você")
    print ("★")
    print ("boa sorte !")
    print ()

    escolha = str(input("faça a sua jogada: "))

    gesto_aleatorio = escolhe_gesto (escolha)
    print (f"a jogada do computador foi: {gesto_aleatorio}")

    #se os dois forem iguais
    if escolha == gesto_aleatorio :
        print("deu empate")

    print()
    #eu ganhando

    #voce ganha (papel ganha de pedra)
    if escolha == "papel" and gesto_aleatorio == "pedra":
        print("você ganhou!")

    #voce ganha (pedra ganha de tesoura)
    if escolha == "pedra" and gesto_aleatorio == "tesoura" :
        print("você ganhou!")

    #voce ganha (tesoura ganha de papel)
    if escolha == "tesoura" and gesto_aleatorio == "papel" :
        print("você ganhou!")

    #o pc ganhando
        
    if gesto_aleatorio == "papel" and escolha == "pedra":
        print("você perdeu")

    #voce ganha (pedra ganha de tesoura)
    if gesto_aleatorio == "pedra" and escolha == "tesoura" :
        print("você perdeu")

    #voce ganha (tesoura ganha de papel)
    if gesto_aleatorio == "tesoura" and escolha == "papel" :
        print("você perdeu")

    print()

    input()