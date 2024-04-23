import random

numero_aleatorio = random.randint(1, 10)
contador = 0
numero_usuario = 0

while True:
    numero_usuario = int(input("tente adivinhar o numero que eu estou pensando: "))
    contador = contador + 1
    if numero_usuario != numero_aleatorio :
        print("você errou, tente novamente")
    if numero_usuario == numero_aleatorio :
        break
print("parabens!! você conseguiu adivinhar!")
print(f"você usou {contador} tentativas")