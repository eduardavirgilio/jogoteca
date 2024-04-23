#### JOGOTECA ####
# desenvolvido por: eduarda virgilio

#if "__main__"

from jogo_de_adivinhacao.jogo_mortal import *


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
    print("| ★  escolha um para jogar:            |")
    print("| 1. jogo da adivinhação               |")
    print("| 2. jogo da forca                     |")
    print("| 3. jogo da tabuada                   |")
    print("| 4. jogo da velha                     |")
    print("----------------------------------------")

else:
    print("você não tem permissão para jogar.")

escolha = int(input("digite o numero de acordo com o jogo escolhido: "))

if escolha == 1 : #jogo da adivinhação
    os.system("cls")
    adivinhacao()
