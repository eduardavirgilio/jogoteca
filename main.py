#### JOGOTECA ####
# desenvolvido por: eduarda virgilio

#if "__main__"

from jogo_de_adivinhacao.jogo_mortal import *
from jogo_da_velha.jogo_da_velha import*
from tabuada.tabuada_calculo import *
from jogo_da_forca.jogo_oficial import *

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
    exit()

escolha = int(input("digite o numero de acordo com o jogo escolhido: "))

if escolha == 1 : #jogo da adivinhação
    os.system("cls")
    adivinhacao()

if escolha == 2 : #jogo da forca
    os.system("cls")
    forca()

if escolha == 3 : #jogo da tabuada
    os.system("cls")
    tabuada_mortal()

if escolha == 4 : #jogo da velha
    os.system("cls")
    velha()


