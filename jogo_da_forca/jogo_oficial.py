#como eu coloquei todas as funções em um outro arquivo eu preciso importa-lo para poder utiliza-lo
from .funcoes_da_forca import *

def forca():
    print()
    print("bem vindo ao jogo da forca! selecione uma categoria")
    print()
    print("1. divas pop")
    print("2. presentes de casamento")
    print("3. séries e filmes")
    print()
    categoria = input(str("digite o numero de acordo com a categoria: "))

    if categoria == "1" :
        print()
        print("a categoria escolhida foi 'divas pop'")

    if categoria == "2" :
        print()
        print("a categoria escolhida foi 'presentes de casamento'")

    if categoria == "3" :
        print()
        print("a categoria escolhida foi 'séries e filmes'")

    #guardando a palavra secreta do outro arquivo na variavel palavra secreta
    palavra_secreta = escolhe_palavra (categoria)

    #quando chamar a mascara obrigatoriamente é necessario passar a palavra para retonar uma lista contendo seus respectivos underlines ("_")
    lista = cria_mascara(palavra_secreta)
    print(*lista)

    print()

    #perguntando a letra
    contador = 0

    #quantidade de vidas
    vida = 7

    #lista vazia
    ja_foi = []

    while vida > 0 :
        contador = contador + 1
        
        letra_escolhida = str(input("chute uma letra: ")).upper()

        substituicao = preenche_mascara(palavra_secreta, letra_escolhida, lista)
        print(*substituicao)
        
        ja_foi.append(letra_escolhida)
        print(ja_foi)

        #se a palavra digitada for igual a palavra secreta
        if letra_escolhida == palavra_secreta :
            print(*palavra_secreta)
            print("voce venceu!")
            break

        if letra_escolhida in palavra_secreta :
            print(f"faltam {vida} vidas")

        if letra_escolhida not in palavra_secreta :
            
            vida = vida - 1
        
            print(f"faltam {vida} vidas")

        if "_" not in lista :
            print("você ganhou!")
            break

        #if letra_escolhida != palavra_secreta :
            #print(f"você perdeu, a palavra era {palavra_secreta}")
            #break

        if vida == 0 :
            print(f"você perdeu, a palavra era {palavra_secreta}")
            break