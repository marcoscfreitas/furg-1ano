# leia os lados de um triangulo e esceva: se é um triangulo válido e o tipo (equilatero, escaleno, isoceles)

lado1 = int(input('informe lado 1: '))
lado2 = int(input('informe lado 2: '))
lado3 = int(input('informe lado 3: '))
soma1 = lado2 + lado3
soma2 = lado1 + lado3
soma3 = lado1 + lado2
print(lado1,lado2,lado3)
print(soma1,soma2,soma3)

if soma1 <= lado1 or soma2 <= lado2 or soma3 <= lado3 :
	print('não é um triangulo válido')
else :
	if lado1 == lado2 and lado2 == lado3 and lado1 == lado3 :	
		print('é triangulo EQUILATERO')
	else :
		if lado1 == lado2 or lado2 == lado3 or lado1 == lado3 :
			print('é triangulo ISOCELES')
		else :
			print('é triangulo ESCALENO')
