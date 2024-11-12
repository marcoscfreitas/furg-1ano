tabela_ascii = ''.join(chr(i) for i in range(32, 127))
listaTextoBase = []
listaPrimeira = []
listaSegunda = []
listaTerceira = []

n = int(input(''))

for i in range(n) :
    textoBase = input('')
    listaTextoBase.append(textoBase)

for palavra in listaTextoBase :
    newLetter = ''
    for letra in palavra :
        if letra in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' :
            newIndex = tabela_ascii.index(letra) + 3
            newLetter = newLetter + tabela_ascii[newIndex]
        if letra not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' :
            newIndex = tabela_ascii.index(letra)
            newLetter = newLetter + tabela_ascii[newIndex]
    listaPrimeira.append(newLetter)

#print(listaPrimeira)

for palavra in listaPrimeira :
    palavra = palavra[::-1]
    listaSegunda.append(palavra)

#print(listaSegunda)

for palavra in listaSegunda :
    cont = len(palavra)//2
    newLetter = palavra[:len(palavra)//2]
    while cont < len(palavra) :
        newIndex = tabela_ascii.index(palavra[cont])-1
        newLetter = newLetter + tabela_ascii[newIndex]
        cont+=1
    listaTerceira.append(newLetter)

#print(listaTerceira)

for final in listaTerceira :
    print(final)