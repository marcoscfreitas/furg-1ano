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
espelho = ''

while x[cont-1] != ' ' :
    espelho = espelho + x[cont-1]
    cont-=1
    print(espelho)

cont = 0
espelho = ' ' + espelho

while (len(x) - len(espelho)) > 0 :
    espelho = x[cont] + espelho
    cont+=1
print(espelho)
'''
# fazer programa do sapo nao lava o pe

x = input('digite um texto:')
vogal = input('qual letra voce quer substituir?')
final = ''
cont = 0
tamanho = len(x)

while cont < tamanho :
    letra = x[cont]
    if x[cont] == 'a' or x[cont] == 'e' or x[cont] == 'i' or x[cont] == 'o' or x[cont] == 'u' :
        final = final + vogal
    else  :
        final = final + letra
    cont+=1

print(x)
print('----------------')
print(final)