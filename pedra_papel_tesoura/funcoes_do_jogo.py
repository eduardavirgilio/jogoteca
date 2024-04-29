import random

def escolhe_gesto (gesto:str) :
    arquivo = open("pedra_papel_tesoura/escolha_aleatoria.txt", "r", encoding='utf8')
    lista_palavras = arquivo.readlines()
    arquivo.close()

    palavra_escolhida = random.choice(lista_palavras)
    palavra_escolhida_limpa = palavra_escolhida.strip()
    return palavra_escolhida_limpa 