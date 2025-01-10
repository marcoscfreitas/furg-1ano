#faça um programa que converta graus Celcius para Fahrenheit

x = int(input('deseja converter C -> F (1) ou F -> C (2)'))
while x != 1 and x != 2 :
	x = int(input('número inválido. digite 1 para C -> F ou 2 para F -> C: '))

if x==1 :
	celcius = float(input('digite a temperatura em celcius (C):'))
	faren = (celcius / 5) * 9 + 32
	print(f'{celcius}ºC equivale à {faren:.2f}°F')
else :
	faren = float(input('digite a temperatura em fahrenheit(F):'))
	celcius = (faren - 32) * (5/9)
	print(f'{faren}°F equivale à {celcius:.2f}ºC')
