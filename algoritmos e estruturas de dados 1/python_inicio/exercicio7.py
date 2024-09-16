# leia o ano que nasceu e escreva se pode votar ou se é facultativo

ano = int(input('informe o ano de nascimento: '))
anoA = 2024
idade = anoA-ano
print(idade)

if idade >= 16 and idade < 18 or idade >= 70 :
	print('voce tem',idade,'anos, então seu voto é FACULTATIVO')
if idade >= 18 and idade <= 70 :
	print('voce tem',idade,'anos, então seu voto é OBRIGATÓRIO')
if idade < 16 :
	print('voce tem',idade,'anos, então NAO PODE VOTAR')
	
