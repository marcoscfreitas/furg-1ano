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
        if letra in 'abcdefghijklmnopqrstuvwxyz' :
            newLetter += chr(((ord(letra) - ord('a') + 3) % 26) + ord('a'))
        
        elif letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
            newLetter += chr(((ord(letra) - ord('A') + 3) % 26) + ord('A'))

        else :
            newLetter+= letra
    listaPrimeira.append(newLetter)

#print(listaPrimeira)

for palavra in listaPrimeira :
    palavra = palavra[::-1]
    listaSegunda.append(palavra)

#print(listaSegunda)

for palavra in listaSegunda :
    cont = len(palavra)//2
    newLetter = palavra[:cont]
    while cont < len(palavra) :
        newLetter += chr(ord(palavra[cont]) - 1)
        cont+=1
    listaTerceira.append(newLetter)

# print(listaTerceira)

for final in listaTerceira :
    print(final)