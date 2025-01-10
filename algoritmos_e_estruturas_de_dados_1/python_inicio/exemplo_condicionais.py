idade = int(input('digite sua idade:'))
if idade >= 18:
	print('pode beber cerveja!')
	carteira = input('possui cnh?')
	if carteira == 'sim':
		print('pode dirigir!')
	else :
		print('vá de busão')
else:
	print('beba leite e ande de bike')
