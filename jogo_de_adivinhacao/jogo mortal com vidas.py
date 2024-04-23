import random

tentativas = 0
numero_usuario = 0

print("seja bem vindo ao JOGO MORTAL 💕")
print("você pode escolher o nivel facil, medio, dificil e o NIVEL SENAI... escolha com cuidado, pois voce tera 5 chances")
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
    print("pense em um numero de 1 a 100 tentando adivinhar o numero que eu pensei")
    limite = 100
    numero_aleatorio = random.randint(1, 100)

while tentativas < 6 :
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
    
    if tentativas == 1 and tentativas != numero_usuario:
        print("ja perdeu 1 vida ein")
    if tentativas == 2 and tentativas != numero_usuario:
        print("ja perdeu 2 vidas ihh")
    if tentativas == 3 and tentativas != numero_usuario:
        print("ja perdeu 3 vidas...")
    if tentativas == 4 and tentativas != numero_usuario:
        print("ja perdeu 4 vidas ☠")
    if tentativas == 5 and tentativas != numero_usuario:
        print("kkkk sua ultima tentativa")
    
    if numero_usuario == numero_aleatorio :
        print("parabens!! você conseguiu adivinhar!")
        print(f"você usou {tentativas} tentativas")
        break

if tentativas >= 5 :
    print(" .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.")
    print("| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |")
    print("| |    ______    | || |      __      | || | ____    ____ | || |  _________   | | | |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |")
    print("| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | | | |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |")
    print("| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | | | |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |")
    print("| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | | | |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |")
    print("| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | | | |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |")
    print("| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | | | |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |")
    print("| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |")
    print("| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |")
    print("'----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'")