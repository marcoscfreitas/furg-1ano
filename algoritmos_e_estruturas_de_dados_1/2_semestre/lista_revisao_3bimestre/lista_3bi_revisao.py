'''----------------------- EXERCICIOS AQUECIMENTO ------------------------'''

# 1) Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma
# lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a
# partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra
# conterá os números negativos. Mostre na tela como ficaram as três listas.

'''def lerNum (n) :
    listaNum = []
    while n > 0 :
        num = int(input('informe o número: '))
        listaNum.append(num)
        n-=1
    return listaNum

def lerNumPos(listaNum) :
    listaNumPos = []
    for i in listaNum :
        if i >= 0 :
            listaNumPos.append(i)
    return listaNumPos

def lerNumNeg(listaNum) :
    listaNumNeg = []
    for i in listaNum :
        if i < 0 :
            listaNumNeg.append(i)
    return listaNumNeg

n = int(input('informe a quantidade de números: '))
listaNum = lerNum(n)
listaNumPos = lerNumPos(listaNum)
listaNumNeg = lerNumNeg(listaNum)
print(f'lista de números:  {listaNum}\nlista de números positivos: {listaNumPos}\nlista de números negativos: {listaNumNeg}')'''

# 2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
# números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
# havia, o total de números remanescentes na lista de positivos e na de negativos.

'''def lerNum (n) :
    listaNum = []
    while n > 0 :
        num = int(input('informe o número: '))
        listaNum.append(num)
        n-=1
    return listaNum

def lerNumPos(listaNum) :
    listaNumPos = []
    qntZeros = 0
    for i in listaNum :
        if i > 0 :
            listaNumPos.append(i)
        elif i == 0 :
            qntZeros+=1
    return listaNumPos, qntZeros

def lerNumNeg(listaNum) :
    listaNumNeg = []
    for i in listaNum :
        if i < 0 :
            listaNumNeg.append(i)
    return listaNumNeg

n = int(input('informe a quantidade de números: '))
listaNum = lerNum(n)
listaNumPos = lerNumPos(listaNum)
listaNumNeg = lerNumNeg(listaNum)
print(f'lista de números:  {listaNum}\nlista de números positivos: {listaNumPos[0]}\nlista de números negativos: {listaNumNeg}\nQuantidade de zeros: {listaNumPos[1]}')'''

# 3) Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez
# colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por coluna.

'''def criarMatriz() :
    matriz = []
    for i in range(5) :
        linha = []
        for j in range(5) :
            num = int(input(f'informe o número da coluna {j+1} para linha {i+1}:'))
            linha.append(num)
        matriz.append(linha)
    return matriz

def mostrarMatriz(matriz) :
    for i in range(5) :
        print(matriz[i])

matriz = criarMatriz()
mostrarMatriz(matriz)'''

'''def inputMatriz() :
    matriz = []
    for i in range(5) :
        linha = input(f'informe os 4 números da linha {i+1} separados por espaço: ')
        linha = linha.split(' ')
        matriz.append(linha)
    return matriz

def mostrarMatriz(matriz) :
    for i in range(5) :
        print(matriz[i])

matriz = inputMatriz()
mostrarMatriz(matriz)'''

'''def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f'Informe o valor para a posição [{i}][{j}]: '))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def exibir_matriz_coluna_por_coluna(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for j in range(colunas):
        for i in range(linhas):
            print(matriz[i][j], end=' ')
        print()

# Código principal
linhas = 5
colunas = 5
matriz = criar_matriz(linhas, colunas)
print('Matriz exibida coluna por coluna:')
exibir_matriz_coluna_por_coluna(matriz)'''


# 4) Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e
# retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6
# divisores (1, 2, 3, 4, 6 e 12).

'''def retornaDivisores(n) :
    divisores = []
    for i in range(n) :
        if n%(i+1) == 0 :
            divisores.append(i+1)
    return divisores

n = 12
divisores = retornaDivisores(n)
print(f'dividores de {n}: {divisores}\nnúmero total de dividores: {len(divisores)}')'''

# 5) Faça uma função em Python para calcular X elevado à Y. A função deverá receber,
# por parâmetro, X e Y, e retornar o resultado da chamada da subrotina. Exemplo: 2 elevado à
# 3 é igual à 2*2*2 = 8. Os parâmetros são 2 e 3, e o retorno será 8. Obs: implementar
# exatamente como no exemplo, ou seja, a exponenciação deve ser calculada por
# multiplicações sucessivas.

'''def calculaElevado(x,y) :
    resultado = x
    for _ in range(y-1) :
        resultado *=  x
    return resultado

x = int(input('informe o valor de x: '))
y = int(input('informe o valor de y: '))
resultado = calculaElevado(x,y)
print(resultado)'''

# ----------------------- EXERCICIOS ------------------------

# 6) Faça um programa em Python que leia duas listas de números compostas por cinco
# elementos informados de maneira ordenada (números em ordem crescente). Crie uma
# terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
# soma dos seus elementos contidos.

'''def gerarLista1() :
    lista1 = []
    somaLista1 = 0
    for _ in range(5) :
        num = int(input('informe um número para lista 1: '))
        lista1.append(num)
    for num in lista1 :
        somaLista1 +=num
    return lista1, somaLista1

def gerarLista2() :
    lista2 = []
    somaLista2 = 0
    num = input('informe os número para lista 2 separados por espaço: ')
    num = num.split(' ')

    for i in num :
        i = int(i)
        lista2.append(i)

    for num in lista2 :
        somaLista2 +=num
    return lista2, somaLista2

def gerarLista3(lista1, lista2) :
    lista3 = lista1[0]+lista2[0]
    somaLista3 = 0
    lista3.sort()
    for num in range(len(lista3)+1) :
        somaLista3 += num
    return lista3, somaLista3

lista1 = gerarLista1()
lista2 = gerarLista2()
lista3 = gerarLista3(lista1,lista2)
print(f'Lista 1: {lista1[0]}\nSoma lista 1: {lista1[1]}\nLista 2: {lista2[0]}\nSoma lista 2: {lista2[1]}\nLista 3: {lista3[0]}\nSoma lista 3: {lista3[1]}')'''


# 7) Altere o programa anterior para desprezar os números iguais, caso estes existam.
# Portanto, a lista final não deve possuir números iguais armazenados.

'''def gerarLista1() :
    lista1 = []
    somaLista1 = 0
    # for _ in range(5) :
    #     num = int(input('informe um número para lista 1: '))
    #     if num not in lista1 :
    #         lista1.append(num)
    num = input('informe os número para lista 1 separados por espaço: ')
    num = num.split(' ')

    for i in num :
        i = int(i)
        if i not in lista1 :
            lista1.append(i)

    for num in lista1 :
        somaLista1 +=num
    return lista1, somaLista1

def gerarLista2() :
    lista2 = []
    somaLista2 = 0
    num = input('informe os número para lista 2 separados por espaço: ')
    num = num.split(' ')

    for i in num :
        i = int(i)
        if i not in lista2 :
            lista2.append(i)

    for num in lista2 :
        somaLista2 +=num
    return lista2, somaLista2

def gerarLista3(lista1, lista2) :
    lista3 = []
    somaLista3 = 0
    for num1 in lista1[0] :
        if num1 not in lista3 :
            lista3.append(num1)
    for num2 in lista2[0] :
        if num2 not in lista3 :
            lista3.append(num2)
    for num3 in lista3 :
        somaLista3 += num3
    lista3.sort()
    return lista3, somaLista3

lista1 = gerarLista1()
lista2 = gerarLista2()
lista3 = gerarLista3(lista1,lista2)
print(f'Lista 1: {lista1[0]}\nSoma lista 1: {lista1[1]}\nLista 2: {lista2[0]}\nSoma lista 2: {lista2[1]}\nLista 3: {lista3[0]}\nSoma lista 3: {lista3[1]}')'''

# 8) Faça um programa em Python que leia três listas compostas por cinco números fornecidos
# pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as
# colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido.

'''def gerarListas(num1,num2,num3) :
    lista1 = []
    lista2 = []
    lista3 = []
    matriz = []

    num1 = num1.split(' ')
    for i in num1 :
        i = int(i)
        lista1.append(i)

    num2 = num2.split(' ')
    for i in num2 :
        i = int(i)
        lista2.append(i)

    num3 = num3.split(' ')
    for i in num3 :
        i = int(i)
        lista3.append(i)

    matriz.append(lista1)
    matriz.append(lista2)
    matriz.append(lista3)

    return matriz

def verificarMaior (matriz) :
    maiorValor = 0
    for linha in matriz :
        for num in linha :
            if num > maiorValor :
                maiorValor = num
    return maiorValor

def mostrarMatriz(matriz) :
    for linha in matriz :
        print(linha)

num1 = input('informe números para lista 1 separados por espaço: ')
num2 = input('informe números para lista 2 separados por espaço: ')
num3 = input('informe números para lista 3 separados por espaço: ')
matriz = gerarListas(num1,num2,num3)
maiorValor = verificarMaior(matriz)
mostrarMatriz(matriz)
print(f'Maior valor da matriz: {maiorValor}')'''

# 9) Faça um programa em Python para jogar o “jogo da velha”. O algoritmo deve permitir que
# dois jogadores joguem uma partida, usando o computador para ver o tabuleiro. Cada
# jogador vai alternadamente informando a posição onde deseja colocar a sua peça (O ou
# X). O programa deverá impedir jogadas inválidas, e determinar automaticamente quando o
# jogo terminou, e quem foi o vencedor (jogador1 ou jogador2). A cada nova jogada, o
# programa deve atualizar a situação do tabuleiro na tela.

# 10) Escreva um programa em Python que calcule o comprimento da mais longa sequência de
# espaços em branco em uma string lida.

'''def contaBranco(texto) :
    temp = 0
    maiorSeq = 0

    for i in range(len(texto)) :
        if texto[i] == ' ' :
            temp+=1
        else: 
            if temp > maiorSeq :
                maiorSeq = temp
                temp = 0
    return maiorSeq

texto = input('informe uma frase: ')
maiorSeq = contaBranco(texto)
print(f'o maior comprimento de espaços brancos tem {maiorSeq} de tamanho')'''

# 11) Implementar um programa para somar matrizes.
# Obs.: as matrizes obrigatoriamente têm a mesma dimensão.

'''def gerarMatriz1() :
    matriz1 = []
    for i in range(2) :
        linha = []
        for j in range(2) :
            valor = int(input(f'MATRIZ 1\ninforme o valor para a linha {i} coluna {j}: '))
            linha.append(valor)
        matriz1.append(linha)
    return matriz1

def gerarMatriz2() :
    matriz2 = []
    for i in range(2) :
        linha = []
        for j in range(2) :
            valor = int(input(f'MATRIZ 2\ninforme o valor para a linha {i} coluna {j}: '))
            linha.append(valor)
        matriz2.append(linha)
    return matriz2

def somarMatrizes(matriz1,matriz2) :
    matriz3 = []
    for i in range(len(matriz1)) :
        linha = []
        for j in range(len(matriz1[0])) :
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz3.append(linha)
    return matriz3

def mostrarMatriz(matriz3) :
    for linha in matriz3 :
        print(linha)

matriz1 = gerarMatriz1()
matriz2 = gerarMatriz2()
matriz3 = somarMatrizes(matriz1,matriz2)

final = mostrarMatriz(matriz3)'''

# 12) Implementar um programa para multiplicar matrizes.
# Obs (nro de elementos em cada dimensão):
# 1a matriz = (Linhas1 x Colunas1)
# 2a matriz = (Linhas2 x Colunas2)
# Multiplicação: (Linhas1 x Colunas1) x (Linhas2 x Colunas2), onde Colunas1 = Linhas2
# Resultado: (Linhas1 x Colunas2)

'''def gerarMatriz1() :
    matriz1 = []
    for i in range(2) :
        linha = []
        for j in range(2) :
            valor = int(input(f'MATRIZ 1\ninforme o valor para a linha {i} coluna {j}: '))
            linha.append(valor)
        matriz1.append(linha)
    return matriz1

def gerarMatriz2() :
    matriz2 = []
    for i in range(2) :
        linha = []
        for j in range(2) :
            valor = int(input(f'MATRIZ 2\ninforme o valor para a linha {i} coluna {j}: '))
            linha.append(valor)
        matriz2.append(linha)
    return matriz2

def multiplicarMatrizes(matriz1, matriz2):
    matriz3 = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz2[0])):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            linha.append(soma)
        matriz3.append(linha)
    return matriz3

def mostrarMatriz(matriz3) :
    for linha in matriz3 :
        print(linha)

matriz1 = gerarMatriz1()
matriz2 = gerarMatriz2()
matriz3 = multiplicarMatrizes(matriz1,matriz2)

final = mostrarMatriz(matriz3)'''

# 13) Faça uma função, em Python, cujo protótipo é QuantosDias(dia, mes, ano),
# que retorne a quantidade de dias do ano até a data informada por parâmetro. Para tanto, é
# preciso verificar o número de dias em cada mês. O mês de fevereiro pode ter 28 ou 29 dias,
# dependendo se o ano for bissexto (verificar).

# 14) Um anagrama é uma espécie de jogo de palavras, resultando do rearranjo das letras de
# uma palavra ou frase para produzir outras palavras, utilizando todas as letras originais
# exatamente uma vez. Um exemplo conhecido é o nome da personagem “Iracema”, um
# anagrama de “América”, no romance de José de Alencar. Escreva um programa, em Python,
# para ler um valor N correspondente ao número de palavras a serem informadas. Após, ler as
# N palavras, e dizer se formam um anagrama. Considerar 1 <= N <= 5, e palavras com, no
# máximo, 10 caracteres.

'''def verificaAnagrama(palavra1,palavra2) :
    palavra1Lista = []
    palavra2Lista = []
    letrasLidas = []

    for letra in palavra1 :
        palavra1Lista.append(letra)
    for letra in palavra2 :
        palavra2Lista.append(letra)

    if len(palavra1Lista) != len(palavra2Lista) :
        return False
    else :
        for index in range(len(palavra1Lista)) :
            if palavra1Lista[index] in palavra2Lista :
                letrasLidas.append(palavra1Lista[index])

        if letrasLidas == palavra1Lista :
            return True
        else :
            return False

palavra1 = input('informe uma palavra: ')
palavra2 = input('informe outra palavra: ')

if verificaAnagrama(palavra1,palavra2) :
    print('são anagramas')
else :
    print('não são anagramas')'''


# 15) Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade,
# em um determinado dia. Em um arquivo texto é fornecido, para cada casa visitada, o
# número do canal (4, 5, 7, 12) e o número de pessoas que o estavam assistindo naquela casa,
# separados por ponto e vírgula. Se a televisão estivesse desligada, nada era anotado, ou seja,
# esta casa não entrava na pesquisa. Faça uma função, em Python, que receba dois
# parâmetros, o nome do arquivo com os dados e o número do canal, e retorne a
# porcentagem de audiência deste canal.

'''def porcentagemAudiencia(dados, canal) :
    canalAudiencia = 0
    totalAudiencia = 0
    for linha in dados :
        linha = linha.strip().split(';')
        if linha[0] == canal :
            canalAudiencia+=int(linha[1])
            totalAudiencia+=int(linha[1])
        else :
            totalAudiencia+=int(linha[1])
    porcentagem = (canalAudiencia/totalAudiencia)*100
    return porcentagem

arq = open('audiencia_tv.txt', 'r') 
dados = arq.readlines()
canal = input('digite um canal para verificar a porcentagem de audiência: ')
porcentagem = porcentagemAudiencia(dados,canal)
print(f'a porcentagem do canal {canal} é de {porcentagem:.2f}%')'''

    # if linha[0] == '4' :
    #     canal4 += int(linha[1])
    # elif linha[0] == '5' :
    #     canal5 += int(linha[1])
    # elif linha[0] == '7' :
    #     canal7 += int(linha[1])
    # elif linha[0] == '12' :
    #     canal12 += int(linha[1])

# 16) Uma universidade deseja fazer um levantamento a respeito de seu processo de seleção.
# Para cada curso, é fornecido um arquivo texto com o seguinte conjunto de valores:
# - Nome do curso;
# - Código do curso;
# - Número de vagas;
# - Número de candidatos do sexo masculino;
# - Número de candidatos do sexo feminino
# Fazer um programa em Python que:
# • Calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de
# candidatos do sexo feminino (escreva também o código correspondente do curso);
# • Determine o maior número de candidatos por vaga e escreva esse número juntamente
# com o código do curso correspondente (supor que não haja empate);
# • Calcule e escreva o total de candidatos.

'''arq = open('cursos_universidade.txt', 'r')
dados = arq.readlines()

maiorCandidatoVaga = 0
maiorCandidatoVagaCurso = ''
maiorCandidatoVagaCodigo = ''
totalCandidatos = 0
for linha in dados :
    linha = linha.strip().split(';')
    totalCandidatos += int(linha[3])
    totalCandidatos += int(linha[4])
    candidatoVaga = (int(linha[3])+int(linha[4]))/int(linha[2])
    if candidatoVaga > maiorCandidatoVaga :
        maiorCandidatoVaga = candidatoVaga
        maiorCandidatoVagaCurso = linha[0]
        maiorCandidatoVagaCodigo = linha[1]
    porcentagemFem = (int(linha[4])*100)/(int(linha[3])+int(linha[4]))
    print(f'{linha[0]}({linha[1]}): {candidatoVaga:.2f} pessoas por vaga. {porcentagemFem:.2f}% de candidatas mulheres.')
print(f'o curso com maior candidatos por vaga é {maiorCandidatoVagaCurso}({maiorCandidatoVagaCodigo}), com {maiorCandidatoVaga} candidatos por vaga.')
print(f'total de candidatos: {totalCandidatos}')'''

# 17) Crie as seguintes listas derivadas da lista informada:
# L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# ● Intervalo de 1 a 9
# ● Intervalo de 8 a 13
# ● Números pares
# ● Números ímpares
# ● Lista reversa

'''def listaUmNove(lista) :
    saida = lista[0:10]
    return saida

def listaOitoTreze(lista) :
    saida = lista[8:14]
    return saida

def listaPares(lista) :
    saida = []
    for numero in lista :
        if numero%2 == 0 :
            saida.append(numero)
    return saida

def listaImpares(lista) :
    saida = []
    for numero in lista :
        if numero%2 != 0 :
            saida.append(numero)
    return saida

def listaReversa(lista) :
    saida = []
    for numero in lista[::-1] :
        saida.append(numero)
    return saida

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listaUmNove = listaUmNove(lista)
listaOitoTreze = listaOitoTreze(lista)
listaPares = listaPares(lista)
listaImpares = listaImpares(lista)
listaReversa = listaReversa(lista)

print(listaUmNove)
print(listaOitoTreze)
print(listaPares)
print(listaImpares)
print(listaReversa)'''

# 18) Faça um programa em Python que receba a temperatura média de cada mês de um
# determinado ano, e armazene-as em uma lista. Em seguida, calcule a média anual das
# temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, . . . ).

'''def receberTemperatura() :
    temperaturaLista = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto',
    'setembro','outubro','novembro','dezembro']

    # for i, mes in enumerate(temperaturaLista):
    #     temperatura = int(input(f'Informe a temperatura de {mes}: '))
    #     temperaturaLista[i] = temperatura
    for index in range(len(temperaturaLista)) :
        temperatura = int(input(f'informe a temperatura de {temperaturaLista[index]}: '))
        temperaturaLista[index] = temperatura
    return temperaturaLista

def calculaMedia(temperaturaLista) :
    media = 0
    for temperatura in temperaturaLista :
        media += temperatura
    media = media/12
    return media

def verificaMedia(temperaturaLista,media) :
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto',
    'setembro','outubro','novembro','dezembro']
    saida = []
    for index in range(len(temperaturaLista)) :
        if temperaturaLista[index] > media :
            saida.append(meses[index])
    return saida

temperaturaLista = receberTemperatura()
media = calculaMedia(temperaturaLista)
saida = verificaMedia(temperaturaLista, media)
print(temperaturaLista)
print(media)
print(saida)'''

# 19) A Furg está tendo problemas de espaço em disco no seu servidor de arquivos. Para
# tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço
# ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um
# programa obtido na Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125

# Neste arquivo, o nome do usuário possui exatamente 15 caracteres. A partir deste arquivo,
# você deve criar um programa em Python que gere um relatório, chamado "relatório.txt", no
# seguinte formato:

# Furg Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário   Espaço utilizado % do uso
# 1  alexandre   434,99 MB       16,85%
# 2  anderson    1187,99 MB      46,02%
# 3  antonio     117,73 MB       4,56%
# 4  carlos      87,03 MB        3,37%
# 5  cesar       0,94 MB         0,04%
# 6  rosemary    752,88 MB       29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# A conversão do espaço ocupado em disco, de bytes para megabytes, deverá ser feita através
# de uma função separada, que será chamada pelo programa principal. O cálculo do
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo
# programa principal.


# 20) Faça um programa em Python que simule um lançamento de um dado. Lance o dado
# 100 vezes e armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor
# foi conseguido. Use uma lista para armazenar os resultados da contagem de cada valor (1-6)
# e uma função para gerar números aleatórios, simulando os lançamentos do dado.

'''import random

def jogaDado() :
    listaDados = []
    for _ in range(100) :
        dado = random.randint(1,6)
        listaDados.append(dado)

    return listaDados

def contaDado(listaDados) :
    listaContagem = [0, 0, 0, 0, 0, 0]
    for dado in listaDados :
        if dado == 1 :
            listaContagem[0] += 1
        elif dado == 2 :
            listaContagem[1] += 1
        elif dado == 3 :
            listaContagem[2] += 1
        elif dado == 4 :
            listaContagem[3] += 1
        elif dado == 5 :
            listaContagem[4] += 1
        elif dado == 6 :
            listaContagem[5] += 1

    return listaContagem

listaDados = jogaDado()
listaContagem = contaDado(listaDados)

print(f'os dados lançados foram: {listaDados}\nnúmero 1 apareceu: {listaContagem[0]} vezes\n\
número 2 apareceu: {listaContagem[1]} vezes\nnúmero 3 apareceu: {listaContagem[2]} vezes\n\
número 4 apareceu: {listaContagem[3]} vezes\nnúmero 5 apareceu: {listaContagem[4]} vezes\n\
número 6 apareceu: {listaContagem[5]} vezes\n')'''

# 21) Crie uma função em Python que receba por parâmetro uma string e uma letra. Retorne a
# string equivalente à enviada como parâmetro, mas sem a letra informada. Por exemplo:
# retira(“Antonia Piedade”,”a”) —> “ntoni Piedde”
# ● Crie a função usando qualquer recurso Python, como split, search e etc;
# ● Crie a função usando apenas recursos básicos, sem as funções para manipulação de
# strings.

'''def removeLetra(texto,letra) :
    saida = texto.replace(letra, '')
    return saida

texto = input('informe o texto: ')
letra = input('informe a letra para ser removida: ')
saida = removeLetra(texto,letra)
print(saida)'''

# 22) Crie uma função em Python que receba por parâmetro uma lista e uma letra. Retorne
# uma lista equivalente à enviada como parâmetro, mas sem a letra informada. A ordem dos
# elementos deve ser mantida. Por exemplo:
# retira([a,b,c,a,f,a,a,k],a) —> [b,c,f,k]

'''def removeLetraList(lista,letra) :
    for i in lista :
        if i == letra :
            lista.remove(i)
    return lista

lista = input('digite uma lista separada por espaço: ')
letra = input('digite a letra a ser removida: ')
lista = lista.split(' ')

saida = removeLetraList(lista,letra)
print(saida)'''

# 23) Dado o código abaixo, responda:
# x = 10
# y = 10
# print("x = ", x, "\n")
# print("1o print - Endereço de x", id(x))
# print("2o print - Endereço de y", id(y))
# x -= 1
# print("x = ", x, "\n")
# print(x)
# print("3o print - Endereço de x", id(x))

# a) Os endereços apresentados na tela das variáveis nos 1o e 2o prints são iguais? Por que?
'''sim, pois armazenam o mesmo valor, logo o computador atribui o mesmo espaço de memória para ambos'''
# b) De acordo com a resposta no item (a), qual será o endereço apresentado no 3o print do
# código?
'''será um endereço diferente de quando no print 1, pois o valor foi alterado, logo, nao pode estar no mesmo endereço'''


# 24) Dado o código abaixo, responda:
# str = "Algoritmo e Estrutura de "
# print(str)
# print("1o print - Endereço de str", id(str))
# str += "Dados"
# print(str)
# print("2o print - Endereço de str", id(str))
# Os endereços apresentados na tela são os mesmos? Por que?
'''não, pois strings são valores imutaveis e quando mudamos seu valor atribuindo uma nova variavel, o endereço também muda'''

# 25) Dado o seguinte código:
# def step(x,value):
#     x = x + value
#     print("2o print - Endereço de x", id(x))

# cont = 0
# print("1o print - Endereço de cont", id(cont))
# while cont < 10:
#     step(cont,1)

# print("3o print - Endereço de cont", id(cont))
# print(cont)

# O código executará até o final (últimos prints)? Se não, como tu resolverias alterando o
# mínimo, valendo-se do conhecimento sobre ponteiros em Python?
'''não executará até o fim pois ficará preso em um loop infinito, uma vez que o cont continua 0 infinitamente,
o que poderia mudar é incrementar o cont com mada chamada da função, assim o ultimo print apareceria, porém, com cada
mudança do cont, seu endereço também mudaria'''

# 26) Crie uma função que receba duas strings e retorne a similaridade entre elas. A similaridade é dada pela
# quantidade de caracteres em comum entre as duas strings dividida pela quantidade total de caracteres das duas
# strings. Por exemplo, a similaridade entre as strings 'casa' e 'cama' é 0.5, pois metade dos caracteres são iguais.
# A função deve retornar um número entre 0 e 1, onde 0 significa que as strings são completamente diferentes e 1 
# significa que são iguais.

'''def similaridadeStrings(string1,string2) :
    caracteresComuns = 0
    similaridade = 0
    caracteresLidos = []
    string1Lista = []
    string2Lista = []
    
    for letra in string1 :
        string1Lista.append(letra)
    for letra in string2 :
        string2Lista.append(letra)

    for i in range(len(string1Lista)) :
        if string1Lista[i] == string2Lista[i] and string1Lista[i] not in caracteresLidos:
            caracteresComuns+=1
            caracteresLidos.append(string1Lista[i])

    similaridade = (caracteresComuns*2)/(len(string1)+len(string2))
    print(caracteresComuns, caracteresLidos, similaridade)

string1 = input('informe um texto1: ')
string2 = input('informe um texto2: ')
similaridadeStrings(string1,string2)'''