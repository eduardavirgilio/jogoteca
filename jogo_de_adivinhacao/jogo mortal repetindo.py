import random

tentativas = 0
numero_usuario = 0

print("seja bem vindo ao JOGO MORTAL 💕")
print("você pode escolher o nivel facil, medio, dificil e o NIVEL SENAI... escolha com cuidado.")
dificuldade = str(input("escolha um nivel de dificuldade: "))

if dificuldade == "facil" :
    print("pense em um numero de 1 a 5 tentando adivinhar o numero que eu pensei")
    limite = 5
    numero_aleatorio = random.randint(1, 5)
    
if dificuldade == "medio" :
    print("pense em um numero de 1 a 20 tentando adivinhar o numero que eu pensei")
    limite = 20
    numero_aleatorio = random.randint(1, 20)

if dificuldade == "dificil" :
    print("pense em um numero de 1 a 50 tentando adivinhar o numero que eu pensei")
    limite = 50
    numero_aleatorio = random.randint(1, 50)

if dificuldade == "senai" :
    print("pense em um numero de 1 a 1000 tentando adivinhar o numero que eu pensei")
    limite = 100
    numero_aleatorio = random.randint(1, 100)

while True :
    numero_usuario = int(input("digite o numero pensado: "))
    tentativas = tentativas + 1
    if numero_usuario > limite :
        print("voce passou do valor maximo burro") 
    if numero_usuario != numero_aleatorio :
        print("tente novamente")
    if numero_usuario > numero_aleatorio :
        print("o numero que voce deve adivinhar é menor")
    if numero_usuario < numero_aleatorio :
        print("o numero que voce deve adivinhar é maior")
    if numero_usuario == numero_aleatorio :
        break

print("parabens!! você conseguiu adivinhar!")
print(f"você usou {tentativas} tentativas")
     

        
    