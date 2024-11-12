alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
saida = []
n = int(input(''))

newLetter=''
while n != 0 :
    frase = input('').upper()
    deslocamento = int(input(''))
    for i in frase :
        newIndex = alfabeto.index(i) - deslocamento
        newLetter = newLetter + alfabeto[newIndex]
    saida.append(newLetter)
    newLetter = ''
    n-=1

for frase in saida :
    print(frase)
