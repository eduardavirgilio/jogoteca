import random

def escolhe_gesto (gesto:str) :

    if gesto == "papel" or gesto == "pedra" or gesto == "tesoura" :

        lista_palavras = ["pedra", "papel", "tesoura"]

        palavra_escolhida = random.choice(lista_palavras)
        palavra_escolhida_limpa = palavra_escolhida.strip()
        return palavra_escolhida_limpa
