# leia um string e escreva letra por letra
'''
x = input('informe uma string: ')
cont = 0

while cont < len(x) :
    print(x[cont])
    cont+=1
 '''
# leia um nome e escreva apenas as vogais do nome, diga quantas vogais tem
'''
x = input('informe uma string: ')
cont = 0
vogal = 0

while cont < len(x) :
    if x[cont] == 'a' or x[cont] == 'e' or x[cont] == 'i' or x[cont] == 'o' or x[cont] == 'u' :
        vogal+=1
        print(x[cont])
    cont+=1
print(f'existem {vogal} vogais na string informada.')
'''
# leia uma palavra e mostre seu espelho (ao contrario)
'''
x = input('informe uma string: ')
cont = len(x)
espelho = ''

while cont > 0 :
    espelho = espelho + x[cont-1]
    cont-=1
print(espelho)
'''
# leia uma palavra e mostre seu espelho (ao contrario) nome por nome dois loops. loopao ,se for espaço entra loopinho igual ja feito
'''
x = input('informe uma string: ')
cont = len(x)
final = ''
final1 = ''
while cont > 0 :
    final = final + x[cont-1]
    cont-=1
    if x[cont] == ' ' :
        final1 = final  + final1
        final = ''
final1 = final + ' ' + final1
print(final1)
'''
# fazer programa do sapo nao lava o pe
'''
x = input('digite um texto:')
vogal = input('qual letra voce quer substituir?')
final = ''
cont = 0

while cont < len(x) :
    letra = x[cont]
    if x[cont] == 'a' or x[cont] == 'e' or x[cont] == 'i' or x[cont] == 'o' or x[cont] == 'u' :
        final = final + vogal
    else  :
        final = final + letra
    cont+=1
print(x)
print('----------------')
print(final)
'''
# ler um nome e mostrar um por um
'''
nome = input('informe o nome completo: ')
cont = 0
final = ''

while cont < len(nome) :
    char = nome[cont]
    final = final + char
    if char == ' ' or cont == len(nome)-1 :
        print(final)
        final = ''
        cont+=1
    else :
        cont+=1
'''
# ler um nome completo em minúsculo e capitalizar a primeira letra, menos os "de"
'''
nome = input('informe um nome completo: ')
cont = 0
final = ''
resultado = ''

while cont < len(nome) :
    char = nome[cont]
    final = final + char
    if char == ' ' or cont == len(nome)-1 :
        final = final[0].upper() + final
        resultado =  resultado + final
        final = ''
    cont+=1
print(resultado)
'''
nome = input('informe um nome completo: ')
cont = 0
parcial = ''
final = ''
while cont < len(nome) :
    if len(parcial) == 0:
        char = nome[cont].upper()
        parcial = parcial + char
        cont+=1
    if len(parcial) > 0:
        char = nome[cont].lower()
        parcial = parcial + char
    if char == ' ' or cont == len(nome)-1 :
        if len(parcial) <= 4:
            final = final + parcial.lower()
            parcial = ''
        else :
            final =  final + parcial
            parcial = ''
    cont+=1
print(final, parcial)

#leia um nome e coloque as letras minusculuas
'''
nome = input('digite um nome: ')
indice = 0
while indice < len(nome) :
    letra = nome[indice]
    codigo = ord[letra]
    print(codigo, letra)
    indice = indice + 1
'''
'''
nome = input('digite um nome: ')
indice = 0
nome_minusculo = ''
while indice < len(nome) :
    letra = nome[indice]
    codigo = ord[letra]
    minusculo = codigo + 32
    #print(codigo,letra,minusculo,chr(minusculo))
    nome_minusculo = nome_minusculo + chr(minusculo)
    incide = indice + 1

print(nome_minusculo)
'''