'''
cont = 5
senhaR = 'iloveprisco'
senha= input(f'tentativas restantes: {cont}\ndigite sua senha:');
print('----------xxx----------')

while senha != senhaR and cont > 1 :
		cont = cont - 1
		senha = input(f'tentativas restantes: {cont}\nsenha incorreta\ndigite sua senha novamente: ')
		print('----------xxx----------')
		
if senha == senhaR:
	print('sucesso! acessando sistema...')
else :
	print('senha incorreta, sem tentativas restantes.')
'''

'''
print('começou!')
cont = 1
while cont <= 5 :
	print(cont, 'eu odeio o prisco')
	cont = cont + 1
print('no fundo eu amo')
'''

'''
# leia o número e mostre sua tabuada até o 10
num = int(input('informe um número: '))
cont = 0

while cont <= 10 :
	print(f'{num} X {cont} = {num*cont}')
	cont = cont + 1
print('fim')
'''
'''
resposta = 'canguru'
cont = 1
tent = 5

tentativa = input(f'tentativas: {tent}\ninforme um animal:\n')

while tentativa != resposta:
    tent -= 1
    cont += 1
    print('----------xxx----------')

    if cont == 2:
        print('dica: anda em duas patas\n')
    if cont == 3:
        print('dica: é um mamífero\n')
    if cont == 4:
        print('dica: natural da Austrália\n')
    if cont >= 5:
        print('dica: pula, pula, pula\n')

    if tent > 0:
        tentativa = input(f'errou.\n\ntentativas: {tent}\ninforme outro animal:\n')
    else:
        break

if tentativa == resposta:
    print('você acertou!')
else:
    print('você perdeu.')
'''