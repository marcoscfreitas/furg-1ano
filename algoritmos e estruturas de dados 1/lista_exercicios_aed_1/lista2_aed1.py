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
# 7) Faça um programa para reserva de ingressos de um cinema. O usuário pode escolher o lugar a ser reservado (fileira e a poltrona desejada - tamanho 10x10).
# Escreva um programa em Python que, através de um menu, permita ao usuário reservar ingressos, exibir a disponibilidade de lugares e exibir a lista de lugares reservados.

# 8) O algoritmo bag-of-words é uma representação simplificada usada no processamento de linguagem natural.
# Nesse modelo, um texto é representado como a bolsa de suas palavras, desconsiderando a gramática e até mesmo a ordem das palavras, mas mantendo a multiplicidade, ou seja, a quantidade de vezes que cada palavra aparece.
# Faça um programa em python que implemente o “bag-of-words”, contando quantas vezes cada palavra aparece em um texto e após construa um gráfico com o resultado.

# 9) Implemente um programa em python que recebe um texto como entrada e realiza a seguinte análise:
# Conte e mostre o número total de caracteres no texto (incluindo espaços em branco).
# Conte e mostre o número total de palavras no texto.
# Conte e mostre o número total de frases no texto.
# Obs: considere que uma palavra é uma sequência de caracteres separada por espaços em branco e uma frase é uma sequência de palavras terminada por um ponto, ponto de exclamação ou ponto de interrogação.

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

# 6) Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
# Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
# Senha média: possui letras minúsculas, números e caracteres especiais, mas não possui letras maiúsculas.
# Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.

# 7) Escreva um programa em python que leia um texto e diga se é ou não um palíndromo (ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função no python que trabalhe com strings.
# Exemplos:
# Ama
# Mirim
# A grama é amarga

# 8) Faça um programa em python que:
# Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
# Descubra a senha criada (força bruta - tentar todas possibilidades). Obs: para encontrar a senha, você não pode comparar pedaços da senha, precisa comparar toda senha (ex: if senha_gerada==senha_tentada: ).

# 9) Escreva um programa em python que leia uma string, e substitua cada segmento de dois ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada qualquer função no python que trabalhe com strings.

# 10) Faça um programa em python que leia três textos. O programa deve imprimir o primeiro texto substituindo todas as ocorrências do segundo pelo terceiro. Não deve ser utilizada qualquer função no python que trabalhe com strings.


# FUNÇÕES AUXILIARES
# chr: retorna o caractere que é apontado pelo inteiro i no código Unicode. Por exemplo, chr(97) retorna a string 'a'.
# ord: dada um caractere Unicode, retorna um número inteiro representando o código Unicode desse caractere. Por exemplo, ord('a') retorna o número inteiro 97. 
# randint: retorna um número inteiro aleatório entre 2 números.
# import random
# print(random.randint(3, 9))
