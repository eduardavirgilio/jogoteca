from funcoes_do_jogo import *

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
print (gesto_aleatorio)
