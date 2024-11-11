n = int(input())
listaPalavrasEscritas = []
contErros = 0
palavraCerta = ''
cont = 0
cont1 = 0
cont2 = 0

while cont < n : 
    palavraEscrita = input()
    listaPalavrasEscritas.append(palavraEscrita)
    cont+=1
# print(listaPalavrasEscritas)

while cont2 < len(listaPalavrasEscritas) :
    # print(listaPalavrasEscritas[cont2])
    if len(listaPalavrasEscritas[cont2]) == 5 :
        print(3)
    else :
        palavraCerta = 'two'
        while cont1 < 3 :
            if listaPalavrasEscritas[cont2][cont1] != palavraCerta[cont1] :
                contErros+=1
                cont1+=1
            else :
                cont1+=1
        if contErros > 1 :
            print(1)
            contErros = 0
            cont1 = 0
        else :
            print(2)
            contErros = 0
            cont1 = 0
    cont2+=1
