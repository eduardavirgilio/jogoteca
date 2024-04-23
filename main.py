#### JOGOTECA ####
# desenvolvido por: eduarda virgilio

import os 

os.system("cls")
print()
print("----------------------------------------")
print("| seja bem-vinda(o) a SUPER ★ JOGOTECA |")
print("| aqui você encontrará jogos incriveis!|")
print("----------------------------------------")

print()

idade = int(input("digite sua idade: "))

if idade >= 18: 
    print("----------------------------------------")
    print("| escolha um para jogar:               |")
    print("| 1. jogo da velha                     |")
    print("| 2. jogo da forca                     |")
    print("| 3. jogo da tabuada                   |")
    print("| 4. jogo da adivinhação               |")
    print("----------------------------------------")
    escolha = int(input("digite o numero de acordo com o jogo escolhido: "))

else:
    print("você não tem permissão para jogar.")