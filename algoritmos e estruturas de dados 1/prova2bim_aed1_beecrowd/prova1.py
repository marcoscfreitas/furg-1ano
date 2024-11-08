def receberLista () :
    k = int(input())
    linguagens = []
    cont1 = 0
    while cont1 < k :
        lang = input()
        linguagens.append(lang)
        cont1+=1
    return linguagens

def escolherLinguagem (linguagens) :
    linguagem = linguagens[0]
    cont2 = 1
    while cont2 < len(linguagens) :
        if linguagens[cont2] != linguagem :
            linguagem = 'ingles'
            return linguagem
        cont2+=1
    return linguagem

n = int(input())
contTestes = 0

while contTestes < n :
    listaLinguagens = receberLista()
    linguagemFinal = escolherLinguagem(listaLinguagens)
    print(linguagemFinal)
    contTestes+=1


