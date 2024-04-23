#para limpar o terminal

import os 

def velha():
    os.system("cls")

    #o que ele digitar -1

    #usuario = str(input("seja bem vindo ao jogo da velha! o primeiro usuario será 'X' ou 'O'?: "))
    #usuario_02 = str(input("e o segundo usuario?: "))

    jogador_x = "X"
    jogador_o = "O"
    jogador_numero = 0
    jogador_numero2 = 0
    velha = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    contar = 0

    numero = 0

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #o 5 altera o espaçamento
    #e o ^ deixa no meio 

    while True:
        while True: #pergunta a jogada ate ser uma jogada valida
            print (f"{lista[0]:^5}|{lista[1]:^5}|{lista[2]:^5}") 
            print (" ---------------")
            print (f"{lista[3]:^5}|{lista[4]:^5}|{lista[5]:^5}")
            print (" ---------------")
            print (f"{lista[6]:^5}|{lista[7]:^5}|{lista[8]:^5}")

    #jogador X
        
            jogador_numero = int(input("é a vez do jogador 01 ('X'), escolha um dos numeros: "))
    
            if lista[jogador_numero - 1] == "X" or lista[jogador_numero - 1] == "O" :
                print("jogada invalida. tente novamente")
        
        #caso o jogador coloque o mesmo numero que o outro
            #if jogador_numero == jogador_numero2 :
                #print("jogada invalida. tente novamente")
            else: 
                break
            
        #para substituir o numero escolhido por X
        jogador_x = "X"

        lista[jogador_numero - 1] = (jogador_x)

        #imprimindo com o numero substituido
        print()

        print (f"{lista[0]:^5}|{lista[1]:^5}|{lista[2]:^5}") 
        print (" ---------------")
        print (f"{lista[3]:^5}|{lista[4]:^5}|{lista[5]:^5}")
        print (" ---------------")
        print (f"{lista[6]:^5}|{lista[7]:^5}|{lista[8]:^5}")

        print()

        contar = contar + 1

        #descobrir o vencedor

        #ganhou na horizontal 1, 2, 3
        if (lista[0]) == "X" and (lista[1]) == "X" and (lista[2]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na vertical 1, 4, 7
        if (lista[0]) == "X" and (lista[3]) == "X" and (lista[6]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na diagonal 1, 5, 9
        if (lista[0]) == "X" and (lista[4]) == "X" and (lista[8]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na vertical 3, 6, 9
        if (lista[2]) == "X" and (lista[5]) == "X" and (lista[8]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na horizontal 7, 8, 9
        if (lista[6]) == "X" and (lista[7]) == "X" and (lista[8]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na diagonal 3, 5, 7
        if (lista[2]) == "X" and (lista[4]) == "X" and (lista[6]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        #ganhou na vertical 2, 5, 7
        if (lista[1]) == "X" and (lista[4]) == "X" and (lista[6]) == "X" :
            print("parabens jogador 01!! voce ganhou")
            break

        
    #jogador O
        jogador_numero2 = int(input("é a vez do jogador 02 ('O'), escolha um dos numeros: "))
        
        #caso o jogador coloque o mesmo numero que o outro

        if lista[jogador_numero2 - 1] == "X" or lista[jogador_numero2 - 1] == "O" :
                print("jogada invalida. tente novamente")

        #para substituir o numero escolhido por O
        
        jogador_o = "O"
    
        lista[jogador_numero2 - 1] = (jogador_o)

        print()

        print (f"{lista[0]:^5}|{lista[1]:^5}|{lista[2]:^5}") 
        print (" ---------------")
        print (f"{lista[3]:^5}|{lista[4]:^5}|{lista[5]:^5}")
        print (" ---------------")
        print (f"{lista[6]:^5}|{lista[7]:^5}|{lista[8]:^5}")

        print()

        contar = contar + 1


        #ganhou na horizontal 1, 2, 3
        if (lista[0]) == "O" and (lista[1]) == "O" and (lista[2]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na vertical 1, 4, 7
        if (lista[0]) == "O" and (lista[3]) == "O" and (lista[6]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na diagonal 1, 5, 9
        if (lista[0]) == "O" and (lista[4]) == "O" and (lista[8]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na vertical 3, 6, 9
        if (lista[2]) == "O" and (lista[5]) == "O" and (lista[8]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na horizontal 7, 8, 9
        if (lista[6]) == "O" and (lista[7]) == "O" and (lista[8]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na diagonal 3, 5, 7
        if (lista[2]) == "O" and (lista[4]) == "O" and (lista[6]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        #ganhou na vertical 2, 5, 7
        if (lista[1]) == "O" and (lista[4]) == "O" and (lista[6]) == "O" :
            print("parabens jogador 02!! voce ganhou")
            break

        if contar > 9 :
            print("deu velha")
            break


    


    