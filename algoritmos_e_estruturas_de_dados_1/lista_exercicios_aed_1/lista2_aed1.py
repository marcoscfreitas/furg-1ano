# 1) Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.
'''
lista = []
listaFinal = []
palavra = ' '
cont = 0

while palavra != '' :
    palavra = input('informe uma palavra: ')
    lista.append(palavra)

while cont < len(lista) :
    if len(lista[cont]) > 5 :
        listaFinal.append(lista[cont])
        cont+=1
    else :
        cont+=1
print(lista)
print(listaFinal)
'''
# 2) Escreva um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números pares. 0 Finaliza o programa
'''
lista = []
listaFinal = []
numero = ''
cont = 0

while numero != 0 :
    numero = int(input('informe uma numero: '))
    lista.append(numero)
print(lista)

while cont < len(lista) :
    if lista[cont]%2 == 0 :
        listaFinal.append(lista[cont])
        cont+=1
    else :
        cont+=1
print(lista)
print(listaFinal)
'''
# 3) Escreva um programa que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.
'''
listaUm = []
listaDois = []
listaFinal = []
cont1 = 0
cont2 = 0
elementoUm = ' '
elementoDois = ' '

while elementoUm != '' :
    elementoUm = input('informe um elemento para lista UM: ')
    listaUm.append(elementoUm)
listaUm.pop(-1)
while elementoDois != '' :
    elementoDois = input('informe um elemento para lista DOIS: ')
    listaDois.append(elementoDois)
listaDois.pop(-1)

while cont1 != len(listaUm) :
    while cont2 != len(listaDois) :
        if listaUm[cont1] == listaDois[cont2] :
            listaFinal.append(listaUm[cont1])
            cont2+=1
        else :
            cont2+=1
    if cont2 == len(listaDois) :
        cont1+=1
        cont2 = 0

print(listaUm)
print(listaDois)
print(listaFinal)
'''
# 4) Dada uma lista de números inteiros informada pelo usuário, escreva um programa em Python que conte quantos números únicos (diferentes) estão presentes na lista. 
# A digitação dos elementos da lista deve encerrar quando for digitado o número zero.



# 5) Faça um programa em python em que o usuário digite uma lista de números inteiros (até digitar zero).
# Após, o programa deve mostrar a frequência de cada número na lista, ou seja, quantos números 1 tem, quantos números 2, etc.
'''
lista = []
listaProcessados = []
numero = None
cont1 = 0
cont2 = 0
freq = 0

while numero != 0 :
    numero = int(input('informe um número: '))
    if numero != 0 :
        lista.append(numero)
print(lista)

while cont1 < len(lista) :
    if lista[cont1] not in listaProcessados :
        while cont2 < len(lista) :
            if lista[cont1] == lista[cont2] :
                freq+=1
            cont2+=1
        print(f'o número {lista[cont1]} aparece {freq} vezes.')
        listaProcessados.append(lista[cont1])
    cont1 += 1
    cont2 = 0
    freq = 0
'''
# 6) Faça um programa que gerencie uma lista de times de futebol. Você precisa criar um programa que armazene uma lista de times de futebol.
# O programa deve permitir ao usuário adicionar novos times à lista, remover times existentes e exibir a lista completa de times.
# Crie um menu em que o usuário fique escolhendo a opção desejada.
'''
listaTimes = []
time = None
menu = None
cont = 0
navbar = ('=====================\n1- adicionar novo time\n2- remover time\n3- ver todos os times\n0- sair\n=====================')

print(navbar)
while menu != 0 :
    menu = int(input('qual opção você deseja? '))
    if menu == 1 :
        time = input('digite o nome do time: ')
        listaTimes.append(time)
    if menu == 2 :
        print(navbar)
        i = 0
        while i < len(listaTimes) :
            print(f'{i} -> {listaTimes[i]}')
            i+=1
        cont = int(input('digite o time que você quer remover: '))
        listaTimes.pop(cont)
        i = 0
        while i < len(listaTimes) :
            print(f'{i} -> {listaTimes[i]}')
            i+=1
        print(navbar)
    if menu == 3 :
        print(navbar)
        i = 0
        while i < len(listaTimes) :
            print(f'-> {listaTimes[i]}')
            i+=1
'''
# 7) Faça um programa para reserva de ingressos de um cinema. O usuário pode escolher o lugar a ser reservado (fileira e a poltrona desejada - tamanho 5x5).
# Escreva um programa em Python que, através de um menu, permita ao usuário reservar ingressos, exibir a disponibilidade de lugares e exibir a lista de lugares reservados.
'''
poltronas = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
controller = ''

while controller != 4 :
    for linha in poltronas:
        print(*linha)
    interface = 'o que você gostaria de fazer?\n1- reservar ingresso\n2- exibir disponibilidade de lugares\n3- exibir lista de lugares reservados\n4- sair'
    print(interface)
    controller = int(input())

    if controller == 1 :
        linhaLetra = input('qual linha está a poltrona desejada? (A,B,C,D ou E) ').upper()
        if linhaLetra == 'A' :
            print(poltronas[0])
            linhaNumero = int(input('qual o número da poltrona desejada? (1,2,3,4  ou 5) '))
            if linhaNumero >= 1 and linhaNumero <= 5 :
                poltronas[0][linhaNumero-1] = 'XX'
        if linhaLetra == 'B' :
            print(poltronas[1])
            linhaNumero = int(input('qual o número da poltrona desejada? (1,2,3,4  ou 5) '))
            if linhaNumero >= 1 and linhaNumero <= 5 :
                poltronas[1][linhaNumero-1] = 'XX'
        if linhaLetra == 'C' :
            print(poltronas[2])
            linhaNumero = int(input('qual o número da poltrona desejada? (1,2,3,4  ou 5) '))
            if linhaNumero >= 1 and linhaNumero <= 5 :
                poltronas[2][linhaNumero-1] = 'XX'
        if linhaLetra == 'D' :
            print(poltronas[3])
            linhaNumero = int(input('qual o número da poltrona desejada? (1,2,3,4  ou 5) '))
            if linhaNumero >= 1 and linhaNumero <= 5 :
                poltronas[3][linhaNumero-1] = 'XX'
        if linhaLetra == 'E' :
            print(poltronas[4])
            linhaNumero = int(input('qual o número da poltrona desejada? (1,2,3,4  ou 5) '))
            if linhaNumero >= 1 and linhaNumero <= 5 :
                poltronas[4][linhaNumero-1] = 'XX'
'''
# 8) O algoritmo bag-of-words é uma representação simplificada usada no processamento de linguagem natural.
# Nesse modelo, um texto é representado como a bolsa de suas palavras, desconsiderando a gramática e até mesmo a ordem das palavras, mas mantendo a multiplicidade, ou seja, a quantidade de vezes que cada palavra aparece.
# Faça um programa em python que implemente o “bag-of-words”, contando quantas vezes cada palavra aparece em um texto e após construa um gráfico com o resultado.

# 9) Implemente um programa em python que recebe um texto como entrada e realiza a seguinte análise:
# Conte e mostre o número total de caracteres no texto (incluindo espaços em branco).
# Conte e mostre o número total de palavras no texto.
# Conte e mostre o número total de frases no texto.
# Obs: considere que uma palavra é uma sequência de caracteres separada por espaços em branco e uma frase é uma sequência de palavras terminada por um ponto, ponto de exclamação ou ponto de interrogação.
'''
texto = input('informe um texto: ')
cont = 0
palavras = 1
frases = 0

while cont < len(texto) :
    if texto[cont] == ' ' :
        palavras+=1
        cont+=1
    elif texto[cont] == '.' or texto[cont] == '!' or texto[cont] == '?' :
        frases+=1
        cont+=1
    else :
        cont+=1

print('o texto contém:')    
print(f'{len(texto)} caracteres')
print(f'{palavras} palavras')
print(f'{frases} frases')
'''
# 10) Faça um programa em python que receba uma lista de números inteiros como entrada e retorne a maior soma dos números ímpares consecutivos da lista. Caso não haja números ímpares na lista, o programa deve retornar 0.
# Exemplo de uso da função:
# lista = [1, 2, 3, 5, 6, 7, 9, 10]
# Saída esperada:16

####### LISTA 2 #######

# 1) Faça um programa em python que leia uma frase e a passe para maiúscula. Você não deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.
'''
fraseInicial = input('informe uma frase em minusculo: ')
fraseFinal = []
cont1 = 0
cont2 = len(fraseInicial)

while cont1 < cont2 :
    letraConvertida = chr((ord(fraseInicial[cont1])) - 32)
    if letraConvertida == '\x00' :
        fraseFinal.append(' ')
    fraseFinal.append(letraConvertida)
    cont1+=1
print(''.join(fraseFinal))
'''
# 2) Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra de cada palavra. Você não deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.
'''
fraseInicial = input('informe uma frase em minusculo: ')
fraseFinal = []
cont1 = 0
cont2 = len(fraseInicial)

while cont1 < cont2 :
    if cont1 == 0 :
        letraConvertida = chr((ord(fraseInicial[cont1])) - 32)
        fraseFinal.append(letraConvertida)
    elif fraseInicial[cont1] == ' ' :
        letraConvertida = chr((ord(fraseInicial[cont1+1])) - 32)
        fraseFinal.append(' ')
        fraseFinal.append(letraConvertida)
        cont1+=1
    else :
        fraseFinal.append(fraseInicial[cont1])
    cont1+=1
print(''.join(fraseFinal))
'''
# 3) Escreva um programa que recebe uma string do usuário e imprime a string invertida.
'''
fraseInicial = input('informe uma frase: ')
fraseInvertida = []
cont1 = len(fraseInicial)-1

while cont1 >= 0 :
    letra = fraseInicial[cont1]
    fraseInvertida.append(letra)
    cont1-=1
print(''.join(fraseInvertida))
'''
# 4) Escreva um programa que recebe uma string do usuário e imprime a string com todas as letras maiúsculas convertidas para minúsculas e vice-versa.
'''
fraseInicial = input('informe uma frase em minusculo: ')
fraseFinal = []
cont1 = 0

while cont1 < len(fraseInicial) :
    if ord(fraseInicial[cont1]) >= 65 and ord(fraseInicial[cont1]) <= 90 : 
        letraConvertida = chr((ord(fraseInicial[cont1])) + 32)
        fraseFinal.append(letraConvertida)
    elif ord(fraseInicial[cont1]) >= 97 and ord(fraseInicial[cont1]) <= 122 : 
        letraConvertida = chr((ord(fraseInicial[cont1])) - 32)
        fraseFinal.append(letraConvertida)
    elif fraseInicial[cont1] == ' ' :
        fraseFinal.append(' ')
    cont1+=1
print(''.join(fraseFinal))
'''
# 5) Escreva um programa que recebe uma frase do usuário e conta o número de palavras na frase.	
'''
frase = input('digite uma frase: ')
cont = 0
numPalavras = 1

while cont < len(frase) :
    if frase[cont] == ' ' :
        numPalavras+=1
        cont+=1
    else :
        cont+=1
print(f'o número de palavras na frase "{frase}" é {numPalavras}')
'''
# 6) Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
# Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
# Senha média: possui letras minúsculas, números e caracteres especiais, mas não possui letras maiúsculas.
# Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.

'''
#Leia uma senha  e diga se ela é 

Forte: 3 tipos
Média: 2 tipos
Fraca: 1 tipo

Numérico
Alfabético
Especial


S = str(input('Digite sua senha e veja se ela é \nForte\nMédia\nFraca: '))

Mai = False
Min = False
Num = False
Esp = False
CS = ''
for C in S:
   V = ord(C)
   if 65 <= V <= 90:
      Mai = True
   elif 97 <= V <= 122:
      Min = True
   elif 48 <= V <= 57:
      Num = True
   else:
      Esp = True
      
if Mai and Min and Num and Esp:
  CS = 'Sua senha é Forte'
elif Mai and Min and Num:
  CS = 'Sua senha é Media'
else:
  CS = 'Sua senha é Fraca'
  
print(CS)
'''

'''
# Leia uma senha e diga se ela é forte
# Tipos: Numérico, Alfabético e Especial
# Forte: 3 tipos
# Média: 2 tipos
# Fraca: 1 tipo

senha = input("Digite a senha: ")

numeros = "0123456789"
i = ord("A")
j = ord("a")
letras = ""
while i < ord("Z"):
    letras += chr(i) + chr(j)
    i += 1
    j += 1

tem_numero = False
tem_letra = False
tem_especial = False

forca = 0
tipos = ["Inválida", "Fraca", "Média", "Forte"]

for char in senha:
    if char in numeros:
        tem_numero = True
    else:
        if char in letras:
            tem_letra = True
        else:
            tem_especial = True

if tem_numero:
    forca += 1
if tem_letra:
    forca += 1
if tem_especial:
    forca += 1

print(tipos[forca])
'''
# Leia uma senha e diga se ela é: FRACA -> 1 tipo; MÉDIA: 2 tipos; FORTE: 3 tipos. Tipos: alfabético, númerico e especial. 
'''
senha = input('Crie uma senha: ')
alf = False
num = False
esp = False
i = 0
while i < len(senha):
	p = ord(senha[i])
	if (p >= 65 and p < 91) or (p >= 97 and p < 123):
		alf = True
	elif p >= 48 and p < 58:
		num = True
	else:
		esp = True
	i += 1

if alf == True and num == False and esp == False:
	print('Senha FRACA. Tente outra.')
elif alf == True and num == True and esp == False:
	print('Senha MÉDIA.')
else:
	print('Senha FORTE')
'''

# 7) Escreva um programa em python que leia um texto e diga se é ou não um palíndromo (ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função no python que trabalhe com strings.
# Exemplos:
# Ama
# Mirim
# A grama é amarga
'''
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
'''
# 8) Faça um programa em python que:
# Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
# Descubra a senha criada (força bruta - tentar todas possibilidades).
# Obs: para encontrar a senha, você não pode comparar pedaços da senha, precisa comparar toda senha (ex: if senha_gerada==senha_tentada: ).
'''
import random
caracteres = 'abcdefghiklmnopqrstuvwxyz0123456789'
senhaGerada = []
contGerada = 0
igualdade = False

while igualdade != True :
    while contGerada < 6 :
        senhaGerada.append(caracteres[random.randint(0,34)])
        contGerada+=1
    senhaGerada =''.join(senhaGerada)

    contTentada = 0
    senhaTentada = []
    while contTentada < 6 :
        senhaTentada.append(caracteres[random.randint(0,34)])
        contTentada+=1
    senhaTentada =''.join(senhaTentada)

    if senhaTentada == senhaGerada :
        igualdade = True
        print(f'você advinhou a senha gerada {senhaGerada} e a tentativa foi {senhaTentada}')
    else :
        print(f'a senha gerada é {senhaGerada}, a tentativa foi {senhaTentada}')
'''
# 9) Escreva um programa em python que leia uma string, e substitua cada segmento de dois ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada qualquer função no python que trabalhe com strings.

# 10) Faça um programa em python que leia três textos. O programa deve imprimir o primeiro texto substituindo todas as ocorrências do segundo pelo terceiro. Não deve ser utilizada qualquer função no python que trabalhe com strings.


#ex1

# import random

# cartas = []
# naipes = ['paus', 'ouros', 'copas', 'espadas']
# sorteadas = []
# valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'reis', 'ás']
# for i in range(len(valores)):
#     for b in range(len(naipes)):
#         cartas.append([valores[i], naipes[b]])

# for x in range(0,12):
#     # print(x)
#     sort1 = random.randint(0, 51)
#     sort2 = random.randint(0, 51)    
#     if sort2 != sort1 and cartas[sort1] not in sorteadas and cartas[sort2] not in sorteadas:
#         sorteadas.append(cartas[sort1])
#         sorteadas.append(cartas[sort2])
#     else:
#         sort1 = random.randint(0, 51)
#         sort2 = random.randint(0, 51)  
# count = 1
# for c in range(0, 12, 2):
#     print(f'Jogador {count}: {sorteadas[c:c+2]}')
#     count+=1

#ex2

# alfanum = 'abcdefghijklmnopqrstuvwxyz1234567890'
# comentario = input("Digite o comentário: ")
# palavras = []
# user= []
# situacao = True
# versao1 = comentario.split(" ")


# if '@' not in comentario:
#     situacao = False

# else:
#     for i in range(len(versao1)):
#         if '@' in versao1[i]:
#             for b in range(len(versao1[i])):
#                 user.append(versao1[i][b])
#             for x in range(len(user)):
#                 if user[x] != '@' and user[x] not in alfanum:
#                     situacao = False
#                     break
#                 else:
#                     situacao = True
#                     break

# if situacao == True:
#     print("contém a menção a um usuário")
# else: 
#     print("não contém")

#ex3

# comentario = input("Digite o comentário: ")
# versao1 = comentario.split(" ")
# novocomentario = ''
# for i in range(len(versao1)):
#     if '@' in versao1[i] and len(versao1[i]) > 1:
#         versao1[i] = "USUARIO_MENCIONADO"
#     novocomentario += versao1[i] + " "
# print(novocomentario)

#ex4

# comentario = input("Digite o comentário: ")
# proibidas = ['teste', 'onibus', 'cassino']
# proibidasc = 0
# versao1 = comentario.replace(',', '')
# versao2 = versao1.split(" ")
# for i in range(len(versao2)):
#     if versao2[i] in proibidas:
#         proibidasc += 1
# if proibidasc > 0:
#     print("Conteúdo inadequado")
# else:
#     print("Comentário permitido")

# FUNÇÕES AUXILIARES
# chr: retorna o caractere que é apontado pelo inteiro i no código Unicode. Por exemplo, chr(97) retorna a string 'a'.
# ord: dada um caractere Unicode, retorna um número inteiro representando o código Unicode desse caractere. Por exemplo, ord('a') retorna o número inteiro 97. 
# randint: retorna um número inteiro aleatório entre 2 números.
# import random
# print(random.randint(3, 9))

# ----------------------------------------------
# list.append(x): O método append adiciona um item ao final da lista. list.append("Python") Adiciona a string "Python" ao final de list.
# list.insert(): Insere um elemento em uma posição específica. lista.insert(1, "world")
# list.extend(iterable): O método extend também serve para adicionar mais elementos a uma lista. list.extend(outra_lista) Estende list adicionando elementos de outra_lista.
# list.remove(x): O método remove retira da lista o primeiro elemento cujo valor seja igual a x. list.remove("Hello") Remove a primeira ocorrência de "Hello" de list.
# list.pop([i]): O método pop deve ser utilizado para remover um elemento com um índice específico. Ou seja, ao utilizar a.pop(2), o elemento de índice 2 será removido e também retornado pelo método, pode usar em variavel.
# list.clear(): O método clear é mais radical, remove todos os elementos de uma lista.
# list.index(): Retorna o índice do primeiro elemento igual ao valor especificado. indice = minha_lista.index(x) 
# list.count(): Conta quantas vezes um elemento aparece na lista. contador = minha_lista.count("Python")
# list.sort(): Ordena os elementos da lista. Ordena a lista numeros em ordem crescente. numeros.sort()
# list.reverse(): Inverte a ordem dos elementos na lista. numeros.reverse()

# Iterando Sobre Listas

# É possível percorrer cada elemento de uma lista utilizando um loop for. Aqui imprimimos cada elemento de minha_lista.

# for item in minha_lista:
#     print(item)

# List Comprehensions

# List comprehensions oferecem uma maneira concisa de criar listas a partir de listas existentes.

# No exemplo no abaixo o ****código cria uma nova lista quadrados contendo os quadrados dos números de 0 a 9.

# quadrados = [x**2 for x in range(10)]

# ----------------------------------------------

# import random

# def lancar_dados():

#     print("\nLançando dados...")
#     dado1 = random.randint(1,6)
#     dado2 = random.randint(1,6)

#     soma = dado1+dado2
#     return soma

# def validar_aposta(valor):
#     if valor >=2 and valor <= 12:
#         return True
#     else:
#         return False


# def iniciarJogo():
#     print("Bem-vindo ao Jogo de Dados!")
#     valor = int(input("Digite o valor alvo (2-12): "))


#     if validar_aposta(valor):
#         soma = lancar_dados()
#         print(f"Os números nos dados somam {soma}\n")
#         if soma >= valor:
#             print(f'Você ganhou a aposta! A soma dos dados é maior ou igual a {valor}.')
#         else:
#             print(f'Você perdeu! A soma dos dados não é maior ou igual a {valor}.')
#     else:
#         print("Você digitou um número inválido")

# iniciarJogo()
# ----------------------------------------------


# ----------------------------------------------
# 28, 30, 24, 27, 29
# 101325, 101550, 101200, 101700, 101400
# "Experimento A", "Experimento B", "Experimento C", "Experimento D", "Experimento E"
# dados = open("dados.txt", "r")

# def CalculoDados(arquivo):
#     readDados = arquivo.readlines()
#     temperaturas = []
#     pressao = []
#     nomes = []
#     media1 = 0
#     media2 = 0

#     temperaturas = readDados[0].split(",")
#     pressao = readDados[1].split(",")
#     nomes = readDados[2].split(",")

#     maiorTemp = temperaturas[0]
#     menorPressao = pressao[0]
#     maior25 = []
#     stringnomes= ''

#     for i in temperaturas:
#         media1 += int(i)
#         mediaTemp = media1/len(temperaturas)
#         if int(i) > int(maiorTemp):
#             maiorTemp = i
#         if int(i)>25:
#             maior25.append(i)

#     for i in maior25:
#         pos = temperaturas.index(i)
#         stringnomes += nomes[pos] + " "
#     pos = temperaturas.index(maiorTemp)
#     nomeMaiorTemp = nomes[pos]

#     for i in pressao:
#         media2 += int(i)
#         mediaPressao = media2/len(pressao)
#         if int(i) < int(menorPressao):
#             menorPressao = i

#     pos2 = pressao.index(menorPressao)
#     nomeMenosPressao = nomes[pos2]

#     return print(f'Temperatura média: {mediaTemp}\nPressão média: {mediaPressao}\nExperimento com maior temperatura máxima: {nomeMaiorTemp}\nExperimento com menor pressão mínima: {nomeMenosPressao}\nExperimentos com temperatura superior a 25 graus: {stringnomes}')


# CalculoDados(dados)
# # print(101200 < 101325)
# ----------------------------------------------
