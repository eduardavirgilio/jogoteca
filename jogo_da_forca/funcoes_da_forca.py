import random
#escolhendo a palavra aleatoria
#por enquanto so retorna a mesma palavra, mas será alterada
def escolhe_palavra (categoria:str)->str: #não precisa passar parametro, mas se fosse de soma precisaria dos valores, por exemplo
    #tupla_de_palavra = ("ARIANA-GRANDE", "TAYLOR-SWIFT", "LADY-GAGA", "SZA", "MADONNA", "ADELE", "BRITNEY-SPEARS", "DEMI-LOVATO", "")
    #palavra_escolhida = random.choice(tupla_de_palavra)
    
    if categoria == "1" :
        arquivo = open("jogo_da_forca/divas pop.txt", "r", encoding='utf8')
        lista_palavras = arquivo.readlines()
        arquivo.close()

        palavra_escolhida = random.choice(lista_palavras)
        palavra_escolhida_limpa = palavra_escolhida.strip()
        return palavra_escolhida_limpa 
    
    if categoria == "2" :
        arquivo = open("jogo_da_forca/presentes casamento.txt", "r", encoding='utf8')
        lista_palavras = arquivo.readlines()
        arquivo.close()

        palavra_escolhida = random.choice(lista_palavras)
        palavra_escolhida_limpa = palavra_escolhida.strip()
        return palavra_escolhida_limpa
    
    if categoria == "3" :
        arquivo = open("jogo_da_forca/series e filmes.txt", "r", encoding='utf8')
        lista_palavras = arquivo.readlines()
        arquivo.close()

        palavra_escolhida = random.choice(lista_palavras)
        palavra_escolhida_limpa = palavra_escolhida.strip()
        return palavra_escolhida_limpa

#todas as funções são totalmente diferentes e separadas


#função para colocar a palavra em uma lista
def cria_mascara(palavra:str) -> list :

    #variavel que conta a quantidade de numeros ate ele ser igual a quantidade de letras na palavra
    #contador = 0
    #contando a quantidade de letras da palavra do def cria_mascara, para determinar a quantidade de "_"
    #numero = len(palavra)

    #criando a lista vazia
    lista = []
    
    #while contador < numero :
    for letra in palavra :

        #preenchendo com _ na lista

        if letra == " " :
            lista.append(" ")
        
        else :
            lista.append("_")

    #retornando a lista para o outro arquivo
    return lista
    
def preenche_mascara(palavra_secreta:str,letra_escolhida:str,mascara:list) -> list:

    indice_contador = 0

    for letra in palavra_secreta :
        
        if letra == letra_escolhida:
            
            mascara[indice_contador] = letra_escolhida
        indice_contador = indice_contador + 1

    return mascara