# crie um programa em python que leia uma data inicial e um número de dias. calcule e escreva a data correspondente ao número de dias.
# exemplo: 01/01/2024  55  25/2/2024
# exemplo: 01/01/2024 150 31/5/2024
# exemplo: 01/01/2024 400 5/2/2025
# nao precisa considerar ano bissexto, ou seja, todo fevereiro tem 28 dias
# 30 dias = 2, 4, 6, 9, 11
# 31 dias = 1, 3, 5, 7, 8, 12

dia = int(input('informe um dia: '))
mes = int(input('informe um mês: '))
ano = int(input('informe um ano: '))
somaDias = int(input('informe os dias a serem somados: '))

while somaDias > 0 :
	dia+=1
	somaDias-=1
	#print(f'{dia}/{mes}/{ano}')

	if dia == 29 and mes == 2 :
		dia = 1
		mes+=1
		
	if dia == 31  :
		if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
			dia = 1
			mes+=1
	if dia == 32 :
		dia = 1
		mes+=1
		
	if mes == 13 :
		mes = 1
		ano+=1
		
print(f'{dia}/{mes}/{ano}')

