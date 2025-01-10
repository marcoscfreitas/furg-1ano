# 1 Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.
'''
largura = int(input('informe a largura da figura: '))
comprimento = int(input('informe o comprimento da figura: '))

if largura <= 0 or comprimento <= 0 :
    print('por favor, informe valores válidos')
else :
    if largura == comprimento :
        print('é um quadrado')
    else : 
        print('é um retângulo')
'''  
# 2 Faça um programa em python que pergunte ao usuário o seguinte:
#	- A viagem custará menos de R$ 30?
#	- Terá Wifi?
#	- Terá piscina?
#	- Terá churrasqueira?
#		O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
#			- Deverá custar menos de R$ 30
#			- Tem que ter wifi e piscina
#			- Se não tiver wifi ou piscina, tem que ter churrasqueira
'''
valor = int(input('a viagem custará menos de R$30,00?\n1 - SIM\n2 - NÃO\n'))
wifi = int(input('terá wifi?\n1 - SIM\n2 - NÃO\n'))
piscina = int(input('terá piscina?\n1 - SIM\n2 - NÃO\n'))
churras = int(input('terá churrasqueira?\n1- SIM\n2 - NÃO\n'))

if valor == 2 :
    print('a viagem não ocorrerá')
else :
    if churras == 1 :
        print('a viagem ocorrerá')
    else :
        if wifi == 1 and piscina == 1 :
            print('a viagem ocorrerá')
        else :
            print('a viagem não ocorrerá')
'''
# 3 Construa um programa em python que, informadas três medidas a, b e c pelo usuário, verifique se elas podem ser lados de um triângulo. Se não puderem ser, primeiramente o algoritmo deve informar isso. Se for possível serem lados de triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas (isósceles, escaleno ou equilátero). A condição para formar um triângulo: comprimento do maior segmento seja inferior à soma dos comprimentos dos dois menores. 
'''
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
'''
# 4 Crie um programa em Python que leia as notas do estudante nos 4 bimestres da nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante passou por média, rodou ou ficou em exame. Para passar por média, o estudante deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao menos fazer o exame. O estudante que tiver menos de 75% de frequência também está rodado na disciplina.
'''
nota1 = float(input('informe a nota do 1º bimestre: '))
nota2 = float(input('informe a nota do 2º bimestre: '))
nota3 = float(input('informe a nota do 3º bimestre: '))
nota4 = float(input('informe a nota do 4º bimestre: '))
freq = float(input('informe a frequência do estudante: '))
media = (nota1 + nota2 + nota3 + nota4)/4

if freq < 75 :
	print('o estudante rodou por frequência')
else :
	if media < 3 :
		print('o estudante rodou direto, média:',media)
	else :
		if media >= 3 and media < 7 :
			print('o estudante ficou em exame, média:',media)
		else :
			print('o estudante passou por média')
'''
# 5 Crie um programa em Python que leia um número e diga se ele é par ou ímpar.
'''
num = int(input('informe um número inteiro: '))

if num % 2 == 0 :
    print(f'o número {num} é PAR.')
else :
    print(f'o número {num} é ÍMPAR')
'''
# 6 Faça um programa em python que leia 3 números e os mostre em ordem crescente.
'''
num1 = int(input('informe um número: '))
num2 = int(input('informe um número: '))
num3 = int(input('informe um número: '))

if num1 >= num2 and num1 >= num3 :
	if num3 >= num2 :
		print(num2,num3,num1)
	else :
		print(num3,num2,num1)
else :
	if num2 >= num1 and num2 >= num3 :
		if num3 >= num1 :
			print(num1,num3,num2)
		else :
			print(num3,num1,num2)
	else : 
		if num3 >= num1 and num3 >= num2 :
			if num2 >= num1 :
				print(num1,num2,num3)
			else :
				print(num2,num1,num3)
'''	
# 7 Crie um programa em Pyhon que leia uma data (DD/MM/AAAA) e diga se a data é válida. a) Desconsidere anos bissextos. b) Considere anos bissextos
'''
# SEM ANO BISSEXTO

dia = int(input('digite um DIA: '))
mes = int(input('digite um MÊS: '))
ano = int(input('digite um ANO: '))

if dia > 31 or dia < 1 or mes < 1 or mes > 12 :
	print('não é válido')
else :
	if dia > 28 and mes == 2 :
		print('não é válido')
	else :
		if dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 7 and mes != 8 and mes != 10 and mes != 12 :
			print('não é válido')
		else :
			print('é válido')	
'''
'''
# COM ANO BISSEXTO
			
dia = int(input('digite um DIA: '))
mes = int(input('digite um MÊS: '))
ano = int(input('digite um ANO: '))
print(ano%4,ano%100,ano%400)
if dia > 31 or dia < 1 or mes < 1 or mes > 12 :
	print('não é válido')
else :
	if dia == 29 and mes == 2 and ano % 100 == 0 and ano % 400 == 0:
			print('é válido')
	else :
			if dia == 29 and mes == 2 and ano % 100 == 0 :
				print('não é válido')
			else :
					if dia == 29 and mes == 2 and ano % 4 == 0 :
						print('é válido')
					else :
						if dia > 28 and mes == 2 :
							print('não é válido')
						else :
							if dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 7 and mes != 8 and mes != 10 and mes != 12 :
								print('não é válido')
							else :
								print('é válido')
'''
# 8 Faça um programa em python que leia o nome de 4 times de futebol que estão em uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4. Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual time foi campeão (se empatar, perguntar quem foi campeão).
'''
t1 = int(input('informe os gols do TIME 1: '))
t2 = int(input('informe os gols do TIME 2: '))
print('----- proxima partida -----')
t3 = int(input('informe os gols do TIME 3: '))
t4 = int(input('informe os gols do TIME 4: '))
nomeT1 = 'TIME 1'
nomeT2 = 'TIME 2'
nomeT3 = 'TIME 3'
nomeT4 = 'TIME 4'

if t1 > t2 :
	x = t1
	nomeX = nomeT1
	print('TIME 1 passa para final com ',x,' gols!')
if t2 > t1 :
	x = t2
	nomeX = nomeT2
	print('TIME 2 passa para final com ',x,' gols!')
if t1 == t2 :
	nomeX = input('TIME 1 e TIME 2 tiveram um empate, digite qual time venceu:')
	print(f'{nomeX} passa para a final com {t1} gols!')
if t3 > t4 :
	y = t3
	nomeY = nomeT3
	print('TIME 3 passa para final com',y,' gols!')
if t4 > t3 :
	y = t4
	nomeY = nomeT4
	print('TIME 4 passa para final com ',y,' gols!')
if t3 == t4 :
	nomeY = input('TIME 3 e TIME 4 tiveram um empate, digite qual time venceu:')
	print(f'{nomeY} passa para a final com {t3} gols!')


print('----- FINAL -----')
Tx = int(input(f'informe os gols do {nomeX} da FINAL:'))
Ty = int(input(f'informe os gols do {nomeY} da FINAL:'))
if Tx > Ty :
	print(nomeX,'vence o campeonato, com',Tx,'gols!')
if Ty > Tx :
	print(nomeY,'vence o campeonato, com',Ty,'gols!')
if Tx == Ty :
	nomeZ = input(f'{nomeX} e {nomeY} tiveram um empate, digite qual time venceu:')
	if nomeZ == nomeX :
		print(nomeX,'vence o campeonato, com',Tx,'gols!')
	else :
		print(nomeY,'vence o campeonato, com',Ty,'gols!')
'''
# 9 Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne o quanto ele deve pagar de imposto.
'''
rendM = int(input('informe o seu rendimento mensal: '))
mod = int(input('qual o modelo de imposto?\n1 - SEM CORREÇÃO\n2 - COM CORREÇÃO DAS PERDAS BOLSONARO\n3 - COM CORREÇÃO INTEGRAL\n'))
if mod == 1 :
	if rendM < 1904 :
		print('você está isento de impostos')
	else:
		if rendM >= 1904 and rendM<= 2827 :
			imp = (rendM*7.50)/100
			print('você deve pagar 7.50% do seu rendimento de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 2827 and  rendM <= 3751 :
			imp = (rendM*15.00)/100
			print('você deve pagar 15.00% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 3751 and rendM <= 4665 :
			imp = (rendM*22.50)/100
			print('você deve pagar 22.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 4665 :
			imp = (rendM*27.50)/100
			print('você deve pagar 27.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
if mod == 2 :
	if rendM < 2500 :
		print('você está isento de impostos')
	else:
		if rendM >= 2500 and rendM<= 3712 :
			imp = (rendM*7.50)/100
			print('você deve pagar 7.50% do seu rendimento de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 3712 and  rendM <= 4926 :
			imp = (rendM*15.00)/100
			print('você deve pagar 15.00% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 4926 and rendM <= 6126 :
			imp = (rendM*22.50)/100
			print('você deve pagar 22.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 6126 :
			imp = (rendM*27.50)/100
			print('você deve pagar 27.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
if mod == 3 :
	if rendM < 4710 :
		print('você está isento de impostos')
	else:
		if rendM >= 4710 and rendM<= 6993 :
			imp = (rendM*7.50)/100
			print('você deve pagar 7.50% do seu rendimento de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 6993 and  rendM <= 9208 :
			imp = (rendM*15.00)/100
			print('você deve pagar 15.00% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 9208 and rendM <= 11540 :
			imp = (rendM*22.50)/100
			print('você deve pagar 22.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
		if rendM >= 11540 :
			imp = (rendM*27.50)/100
			print('você deve pagar 27.50% do seu rendiment de imposto, ou seja:\nvocê pagará: R$:',imp)
'''
#------------------------- repetição -------------------------

# 10 Escreva um programa que mostre os números de 1 a 10.
'''
cont = 0

while cont < 10 :
    print(cont)
    cont= cont + 1
'''
# 11 Escreva um programa que mostre os números de 10 a 1.
'''
cont = 10

while cont > 0 :
    print(cont)
    cont = cont - 1
'''    
# 12 Escreva um programa que mostre os números pares de 1 a 200.
'''
cont = 1

while cont <= 200 :
    if cont%2==0 :
        print(cont)
        cont = cont + 1
    else :
        cont= cont + 1
'''
# 13 Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário.
'''
num = 10
cont1 = 0
cont = 0

while cont1 <= num :
	cont = 0
	print(f'----- tabuada do {cont1} -----')
	while cont <= 10 :
		print(f'{cont1} X {cont} = {cont1*cont}')
		cont+=1
	cont1+=1
'''
# 14 Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:

#   1
#   2 2
#   3 3 3
#  	4 4 4 4
#   5 5 5 5 5
#   …
#   N N N N N N N …
'''
cont = 1
contStr = str(cont)

num = int(input('informe um valor: '))

while cont != num+1 :
    print(contStr * cont)
    cont = cont + 1
    contStr = str(cont) + ' '
'''
# 15 Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize as equações de progressão aritmética.
'''
cont = 0
soma = 0
num = int(input('informe um valor: '))

while cont <= num :
    soma = soma + cont
    cont = cont + 1
print(soma)
'''
# 16 Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.
'''
cont = 1
div = 0
num = int(input('informe um valor positivo: '))

while cont <= num:
    if num % cont == 0 :
        div = div + 1
    cont = cont + 1
if div > 2 :
    print('não é primo\nnúmero de dividores:',div)
else :
    print('é primo\nnúmero de dividores:',div)
'''
# outra maneira
'''
num = int(input('digite o numero: '))
teste = 2
primo = True

while teste < num and primo :
	resto = num % teste
	if resto == 0 :
		primo = False        
	print(f'{num} e {teste} --> {resto} primo? {primo}')
	teste = teste + 1
if primo :
	print(f'{num} é primo')
else :
	print(f'{num} nao é primo')
'''
# 17 Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo
# (n deve ser informado pelo usuário).
# A sequência de Fibonacci é aquela em que cada termo é a soma dos dois termos anteriores.
# Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.
'''
n = int(input('informe quantos números terá a sequência: '))
cont = 0
fibo1 = 0
fibo2 = 1
fiboX = 0

while cont <= n :
	print(fibo1)
	fiboX = fibo1 + fibo2
	fibo1 = fibo2
	fibo2 = fiboX
	cont+=1
'''
# 18 Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.
'''
n = int(input('informe um número: '))
cont = 1
r = 1
while cont <= n :
	r = r * cont
	cont+=1
print(f'a fatorial de {n} é {r}')
'''
# 19 Escreva um programa que leia diversos números até que o usuário digite zero. Em seguida escreva a média dos números digitados.
'''
n = int(input('digite um número: '))
med = 0
div= 0

while n != 0 :
	med= med + n
	n = int(input('digite mais um número: '))
	div+=1
print(f'a média dos {div} números informados é: {med/div}')
'''
# 20 Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim”. Em seguida escreva:
#	O nome do funcionário com maior salário
#	O nome do funcionário com menor salário
#	A média dos salários digitados
'''
nome = input('informe o nome do funcionário: ')
sal = int(input('informe o salário do funcionário: '))
cont = 1
somaSal = sal
tempNm = nome
tempNM = nome
salMax = sal
salMin = sal

while nome != 'fim' :
	nome = input('informe o nome do funcionário: ')
	if nome == 'fim' :
		print('cabou-se')
	else :
		sal = int(input('informe o salário do funcionário: '))
		if sal <= salMin :
			salMin = sal
			tempNm = nome
		if sal >= salMax :
			salMax = sal
			tempNM = nome
		somaSal = somaSal + sal
		cont = cont + 1
		medSal = somaSal/cont
print(f'MAIOR SALÁRIO: {tempNM}, R$:{salMax}\nMENOR SALÁRIO: {tempNm}, R$:{salMin}\nMÉDIA DOS SALÁRIOS: {medSal}\nSOMA DOS SALÁRIOS: {somaSal}\nSALÁRIOS INFORMADOS: {cont}')
'''
# 21 Escreva um programa de adivinhação de número. O programa deve conter um número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o programa deve dizer se o número chutado é maior ou menor que o número secreto. O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como sortear um número aleatório entre 0 e 10 em python:
# import random
# sorteado = random.randint(0,10)
'''
import random
sorteado = random.randint(0,100) 
r = int(input('qual número você acha que é?'))

while r != sorteado :
    if r > sorteado:
        r = int(input('errou! é um número menor, tente novamente: '))
    else :
        r = int(input('errou! é um número maior, tente novamente: '))
print('parabéns você acertou!')
'''
# 22Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, inclusive o X se for o caso. Por exemplo, para o número 8, a saída será “9,11,13,15,17,19”.
'''
x = int(input('informe um número: '))
cont = 0

while cont < 6 :
	if x % 2 != 0 :
		print(x)
		x+=1
		cont+=1
	else :
		x+=1
cont+=1
'''
# 23 Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva: 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.
'''
cont = 1
div = 0
num = int(input('informe um valor positivo: '))

while cont <= num:
    if num % cont == 0 :
        div = div + 1
    cont = cont + 1
if div > 2 :
    print('não é primo\nnúmero de dividores:',div)
else :
    print('é primo\nnúmero de dividores:',div)
    '''

# 24 Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça um programa em Python que receba o nome do(a) ginasta, e as notas de sua apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e a pior nota para calcular a média). As notas não são informadas em ordem (crescente ou decrescente).
'''
nome = input('informe o nome da ginasta: ')
nota = int(input('informe a nota do jurado: '))
cont = 1
somaNota = nota
notaMax = nota
notaMin = nota

while cont < 7 :
		nota = int(input('informe a nota do jurado: '))
		if nota < notaMin :
			notaMin = nota
		if nota > notaMax :
			notaMax = nota
		cont = cont + 1
		somaNota = somaNota + nota
medNota = ((somaNota-notaMin-notaMax)/5)
print(f'MAIOR NOTA: {notaMax}\nMENOR NOTA: {notaMin}\nMÉDIA DAS NOTAS(sem maior e menor): {medNota}')
'''
# 25 Considere uma sequência de números que atende a todos critérios abaixo:
# a - Possui sempre 2 dígitos , nem mais , nem menos.
# b - A representação do número possui pelo menos um dígito 1 ou um dígito 2.
# c - O número é múltiplo de 3.
# Faça um programa que implemente e mostre essa sequência.
# obs: tem que usar repetição para mostrar a sequência. Não pode mostrar os números “na mão”. 
'''
n = 10

while n < 100 :
    if n%3 == 0 and n%10 == 1 or n%10 == 2 or n//10 == 1 or n//10 == 2 :
        print(n)
    n+=1
'''
# 26 Construa um programa em Python que escreva uma contagem de 10 (dez) minutos, ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01,  ..., até 10:00.
'''
h = 0
m = 00
while h < 10 :
    m+=1
    if m == 60 and h < 10:
        h+=1
        m = -1
    else :
    	print(f'{h:02}:{m:02}')
print(f'{h:02}:{m+1:02}')   
'''
# 27 Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade de andares.
# Ex: 	Informe o tijolo: A
# 	Informe a quantidade de andares: 5

#         A
#       AAA
#     AAAAA
#   AAAAAAA
# AAAAAAAAA
'''
cont = 1
spc = ' '
contStr = input('do que a pirâmide será feita?')
altura = int(input('informe um valor: '))
contStr = contStr + spc

while cont != altura+1 :
    print((spc*(altura-cont)) + contStr * cont)
    cont = cont + 1
'''
# outra maneira [sem usar spc*(altura-cont)]
'''
altura = int(input('informe a altura: '))
tijolo = input('do que será feita?')
andar = 1
cont = 1
espaco = ' '
desloc = altura - 1

while andar <= altura :
	#print(desloc*espaco + cont * tijolo)
	cont2 = 0
	espaco_montado = ''
	while cont2 < desloc :
		espaco_montado = espaco_montado + espaco
		cont2 = cont2 + 1

	cont2 = 0
	tijolo_montado = ''
	while cont2 < cont :
		tijolo_montado = tijolo_montado + tijolo
		cont2 = cont2 + 1
		#print(espaco_montado)

	print(espaco_montado + tijolo_montado)

	andar = andar + 1
	cont = cont + 2
	desloc = desloc -1
'''
# crie um código que diga a raiz quadrada de dado numero inteiro
'''
import math
n = int(input('informe um valor para calcular a raiz quadrada: '))
cont = 0.0001
res = 0

while res != n :
    res = cont*cont
    if  int(cont)*int(cont) == n :
        print(f'a raiz de {n} é {int(cont)}')
        res = n
    if res > n :
        print(f'a raiz aproximada de  {n} é {cont:.3f}')
        res = n
    else :
        cont = cont + 0.0001
    print(res)

print(math.sqrt(n))
print(abs(res-math.sqrt(n)))
'''