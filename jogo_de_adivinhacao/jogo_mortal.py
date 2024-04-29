import random

def adivinhacao():

    print("seja bem vindo ao JOGO MORTAL 💕")
    print("você pode escolher o nivel facil, medio, dificil e o NIVEL SENAI... escolha com cuidado.")
    dificuldade = str(input("escolha um nivel de dificuldade: "))

    if dificuldade == "facil" :
        numero_aleatorio = random.randint(1, 5)
        numero_facil = int(input("digite um numero de 1 a 5 tentando adivinhar o numero que eu pensei: "))
    if numero_facil == numero_aleatorio :
        print("parabens!! voce acertou")
    else:
        print("voce errou!")

    if dificuldade == "medio" :
        numero_aleatorio = random.randint(1, 20)
        numero_facil = int(input("digite um numero de 1 a 20 tentando adivinhar o numero que eu pensei: "))
    if numero_facil == numero_aleatorio :
        print("parabens!! voce acertou")
    else:
        print("voce errou!")

    if dificuldade == "dificil" :
        numero_aleatorio = random.randint(1, 50)
        numero_facil = int(input("digite um numero de 1 a 50 tentando adivinhar o numero que eu pensei: "))
    if numero_facil == numero_aleatorio :
        print("parabens!! voce acertou")
    else:
        print("voce errou!")

    if dificuldade == "senai" :
        numero_aleatorio = random.randint(1, 1000)
        numero_facil = int(input("digite um numero de 1 a 1000 tentando adivinhar o numero que eu pensei: "))

    if numero_facil == numero_aleatorio :
        print("parabens!! voce acertou")
    else:
        print("voce errou!")

input("aperte enter para sair")