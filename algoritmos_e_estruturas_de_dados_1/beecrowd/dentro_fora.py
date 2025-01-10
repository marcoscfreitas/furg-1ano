n = int(input())
palavrasEmbaralhadas = []
palavrasFinais = []


for _ in range(n) :
    palavra = input('')
    palavrasEmbaralhadas.append(palavra)


for palavra in palavrasEmbaralhadas :
    cont1 = len(palavra)/2 - 1
    cont2 = len(palavra) - 1
    esquerda = ''
    direita = ''
    for letra in palavra :
        if cont1 >= 0 :
            esquerda+=letra
            cont1-=1
        else :
            direita+=letra
            cont2-=1
    esquerda = esquerda[::-1]
    direita = direita[::-1]
    saida = esquerda+direita
    palavrasFinais.append(saida)

for _ in palavrasFinais :
    print(_)