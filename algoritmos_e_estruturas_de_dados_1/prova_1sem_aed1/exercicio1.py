# crie um programa que leie dois lados de um retângulo e escreva a sua área. verifique para que o usuário digite apenas números positivos para representar os lados

lado1 = int(input('informe o primeiro lado: '))
lado2 = int(input('informe o segundo lado: '))

while lado1 <= 0 or lado2 <= 0 :
	lado1 = int(input('informe o primeiro lado com valor POSITIVO: '))
	lado2 = int(input('informe o segundo lado com valor POSITIVO: '))
	
area = lado1*lado2
print(f'a area do retângulo é: {area}')
