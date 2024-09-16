# peça para o usuário informar seu nome e a hora do dia, escreva uma mensagem conforme a hora

nome = input('informe seu nome: ')
time = int(input('informe a hora atual: '))

if time >= 1 and time <= 11 :
	print('bom dia,', nome , '!')
if time >= 12 and time <= 17 :
	print('boa tarde,', nome , '!')
if time >= 18 and time <= 24 :
	print('boa noite,', nome , '!')
'''

nome = input('informe seu nome: ')
time = int(input('informe a hora atual: '))

if time >= 1 and time <= 11 :
	print('bom dia,', nome , '!')
else :
	if time >= 12 and time <= 17 :
		print('boa tarde,', nome , '!')
	else :
		print('boa noite,', nome , '!')
'''



'''
nome = input('digite o nome: ')
hora = int(input('digite a hora atual: '))

if hora > 12 :
	if hora > 18:
		saudacao = 'boa noite'
	else :
		saudacao = 'boa tarde'
else :
	if hora > 5 :
		saudacao = 'bom dia'
	else :
		saudacao = 'boa noite'
print(f'{saudacao},{nome}')
'''

'''
if hora > 6 and hora < 12:
	saudacao = 'bom dia'
else:
	if hora > 12 and hora < 18 :
		saudacao = 'boa tarde'
	else :
		saudacao = 'boa noite'
print(saudacao)
'''
