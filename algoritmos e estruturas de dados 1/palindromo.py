'''
#1) Leia um String e verifique se é um palindromo Renner = renneR
P = input('Escreva uma palavra e verifique se ela é um PALINDROMO: ')
esp = ''
C = 0
pala = ''

while C < len(P):
    if P[C] != ' ':
        pala = P[C] + pala 
    else:
        esp = esp + pala + ' '  
        pala = '' 
    C += 1

esp = esp + pala

if esp == P:
 print('PALÍNDROMO')
else:
 print('NÃO PALINDROMO')
 '''

'''
 # Leita uma string e verifique se é palíndromo

palavra = input("Digite uma palavra: ").lower()

i = 1
arvalap = ""
while i <= len(palavra):
    arvalap += palavra[-i]
    i += 1

if palavra == arvalap:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
 '''

p = input('Digite uma palavra: ')
c = 0
c1 = -1
espelho = ''

while c < len(p):
	espelho += p[c1]
	c += 1
	c1 -= 1

if p == espelho:
	print(f'{p.capitalize()} é um PALINDROMO')
else:
	print(f'{p.capitalize()} NÃO é um palindromo')