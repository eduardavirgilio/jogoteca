import random

def tabuada_mortal():
    resultado = 0

    print ("bem vindo a TABUADA EXTREME")
    print("vamos gerar uma tabuada aleatoria e voce ira calcular ela")

    tabuada_esquerda = random.randint(1, 10)
    tabuada_direita = random.randint(1, 10)
    resultado = tabuada_esquerda * tabuada_direita

    print (f"{tabuada_esquerda} x {tabuada_direita} = ?")
    calculo = int(input("digite o resultado: "))

    print (f"{tabuada_esquerda} x {tabuada_direita} = {calculo}")

    if calculo == resultado :
        print("parabens voce acertou!")

    if calculo != resultado :
        print("voce errou mona")

input("aperte enter para sair")