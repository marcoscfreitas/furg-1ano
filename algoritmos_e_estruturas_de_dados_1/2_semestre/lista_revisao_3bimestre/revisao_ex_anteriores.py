# 1) (5 Pontos) Considere um programa em Python que simula um jogo de cartas com um
# baralho completo. O baralho é inicializado com 52 cartas, divididas em 4 naipes
# (Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). O
# programa deve utilizar listas para armazenar o baralho e sortear duas cartas para
# cada um de 6 jogadores. Mostre na tela cada uma das cartas sorteadas para cada
# jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.

'''import random

def sortearCartas() :
    naipes = ['paus','ouros','copas','espadas']
    valores = ['2','3','4','5','6','7','8','9','10','valete','dama','rei','as']
    baralhosTotais = []
    cartasSorteadas = []
    for _ in range(6) :
        baralhoJogador = []
        while len(baralhoJogador) != 2 :
            sorteiaNaipe = naipes[random.randint(0,3)]
            sorteiaValor = valores[random.randint(0,12)]
            carta = sorteiaValor + ' ' + sorteiaNaipe
            if carta not in cartasSorteadas :
                baralhoJogador.append(carta)
                cartasSorteadas.append(carta)
        baralhosTotais.append(baralhoJogador)

    return baralhosTotais

baralhosTotais = sortearCartas()

# for index in range(len(baralhosTotais)) :
#     print(f'jogador {index+1}: {baralhosTotais[index]}')

for index in range(len(baralhosTotais)) :
    cartas = ', '.join(baralhosTotais[index])
    print(f'jogador {index+1}: {cartas}')'''

# 2) (5 Pontos) O Instagram é uma popular plataforma de mídia social que permite aos
# usuários compartilhar fotos e vídeos. Considere um cenário em que você está
# desenvolvendo uma funcionalidade para analisar os comentários em postagens do
# Instagram.

# a) Escreva um código em Python que verifique se uma string comentário contém a
# menção a um usuário. Uma menção começa com o símbolo "@" seguido por um
# nome de usuário válido (composto apenas por letras minúsculas e números), por
# exemplo: "@usuario123".

'''def contemUsuario(comentario) :
    alfaNum = 'abcdefghijklmnopqrstuvwxyz1234567890'
    saida = ''
    flag = False

    if '@' not in comentario :
        flag = False
    else :
        for index in range(len(comentario)) :
            if comentario.index('@') == len(comentario)-1 :
                flag = False
            elif comentario[index] == '@' and comentario[index+1] in alfaNum :
                flag = True
        if flag == True :
            saida = 'contém menção de usuário'
        else :
            saida = 'não contém menção de usuário'
    return saida

comentario = input('insira um comentário: ')
saida = contemUsuario(comentario)
print(saida)'''

# b) Escreva um código em Python que substitua todas as menções a usuários na string
# comentário por "USUARIO_MENCIONADO".

'''def substituirUsuario(comentario) :
    comentarioDividido = comentario.split(' ')
    for index in range(len(comentarioDividido)) :
        if '@' in comentarioDividido[index] :
            comentarioDividido[index] = 'USUARIO_MENCIONADO'
    comentarioDividido = ' '.join(comentarioDividido)
    return comentarioDividido

comentario = input('insira um comentário: ')
saida = substituirUsuario(comentario)
print(saida)'''

# c) Dado um conjunto de palavras proibidas, escreva um código em Python que
# verifique se a string comentário contém alguma das palavras proibidas. Se contiver,
# exiba "Conteúdo inadequado", caso contrário, exiba "Comentário permitido"

'''def palavrasProibidas(comentario) :
    proibido = ['eita','oxi','gremio','sapecagem']
    comentarioDividido = comentario.split(' ')
    saida = 'comentário permitido'
    for index in range(len(comentarioDividido)) :
        if comentarioDividido[index] in proibido :
            saida = 'conteúdo inadequado'
    return saida

comentario = input('insira um comentário: ')
saida = palavrasProibidas(comentario)
print(saida)'''

# Imagine que você está conduzindo um experimento científico em um laboratório e deseja analisar os dados coletados.
# Os dados são representados em forma de listas em um arquivo texto, e você precisa criar um programa em Python
# para realizar algumas operações de análise de dados. O arquivo possui o seguinte formato:

# ● 1a linha: uma lista de temperaturas medidas em graus Celsius, separadas por vírgula.
# ● 2a linha: uma lista de pressões medidas em Pascal, separadas por vírgula.
# ● 3a linha: uma lista de nomes dos experimentos correspondentes, separados por vírgula.

# O programa deve ser capaz de ler esse arquivo e fazer o seguinte:
# ● Calcular a temperatura média e a pressão média a partir das listas. V
# ● Identificar qual experimento teve a maior temperatura máxima. 
# ● Identificar qual experimento teve a menor pressão mínima.
# ● Exibir todos os experimentos em que a temperatura seja superior a 25 graus Celsius.

'''def tempMedia() :
    listaTemperaturas = dados[0].strip().split(', ')
    tempMedia = 0
    for temperatura in listaTemperaturas :
        temperatura = int(temperatura)
        tempMedia += temperatura
    tempMedia = tempMedia/len(listaTemperaturas)
    return tempMedia

def pressaoMedia() :
    listaPressao = dados[1].strip().split(', ')
    pressaoMedia = 0
    for pressao in listaPressao :
        pressao = int(pressao)
        pressaoMedia += pressao
    pressaoMedia = pressaoMedia/len(listaPressao)
    return pressaoMedia

def tempMaxima():
    listaTemperaturas = dados[0].strip().split(', ')
    listaExperimentos = dados[2].strip().split(', ')
    tempMaxima = 0
    experimentoMaxTemperatura = ''

    for temperatura in listaTemperaturas :
        temperatura = int(temperatura)
        if temperatura >= tempMaxima :
            tempMaxima = temperatura

    experimentoMaxTemperatura = listaExperimentos[listaTemperaturas.index(str(tempMaxima))]

    return experimentoMaxTemperatura

def pressaoMin() :
    listaPressao = dados[1].strip().split(', ')
    listaExperimentos = dados[2].strip().split(', ')
    menorPressao = int(listaPressao[0])

    for pressao in listaPressao :
        pressao = int(pressao)
        if pressao <= menorPressao :
            menorPressao = pressao

    experimentoMenorPressao = listaExperimentos[listaPressao.index(str(menorPressao))]

    return experimentoMenorPressao

def sup25() :
    listaTemperaturas = dados[0].strip().split(', ')
    listaExperimentos = dados[2].strip().split(', ')
    superior25 = []
    for temperatura in listaTemperaturas :
        temperatura = int(temperatura)
        if temperatura > 25 :
            superior25.append(listaExperimentos[listaTemperaturas.index(str(temperatura))])

    return superior25

arq = open('dados.txt', 'r') 
dados = arq.readlines()
# print(dados)

print(f'temperatura média: {tempMedia()}')
print(f'pressão média: {pressaoMedia()}')
print(f'exp. com temperatura máxima: {tempMaxima()}')
print(f'exp. com pressão mínima: {pressaoMin()}')
print(f'exp. com temperatura superior à 25º: {sup25()}')'''

# 2) Você deve criar um jogo de dados em Python onde o jogador lança dois
# dados de seis faces e tenta adivinhar se a soma dos números nos dados será maior
# ou igual a um determinado valor escolhido. Implemente uma função chamada
# lançar_dados, que simula o lançamento de dois dados de seis faces (sortear) e
# retorna a soma dos resultados. Implemente uma função chamada validar_aposta,
# que verifica se a aposta do jogador é um número inteiro positivo entre 2 e 12.
# Exemplo:
# Bem-vindo ao Jogo de Dados!
# Digite o valor alvo (2-12): 7
# Lançando os dados...
# Os números nos dados somam 8.
# Você ganhou a aposta! A soma dos dados é maior ou igual a 7

'''import random

def jogarDados() :
    soma = (random.randint(1,6)) + (random.randint(1,6))
    return soma

def validarAposta() :
    flag = False
    while flag == False :
        aposta = int(input('digite o valor alvo (2-12): '))
        if aposta >= 2 and aposta <= 12 :
            flag = True
        else :
            print('informe um valor válido')
    return aposta

def verificarResultado(soma,aposta) :
    if soma >= aposta :
        saida = f'voce ganhou a aposta! a soma dos dados é maior ou igual a {aposta}'
    else :
        saida = f'voce perdeu. a soma dos dados é inferior a {aposta}'
    return saida

print('bem vindo ao jogo de dados!')
aposta = validarAposta()
print('lançando os dados...')
soma = jogarDados()
print(f'o número dos dados somam {soma}')
saida = verificarResultado(soma,aposta)
print(saida)'''

# função recursiva que retorne os divisores de tal número

'''def divisores(num):
    if num != 1:
        result = num//2
        divisores(result)
        print(num)
    else:
        print(num)
divisores(100)'''

# leia o arquivo logs.txt e fale a frequencia de cada usuário em um novo arquivo.

'''arq = open('logs.txt', 'r')
novoLog = open("novoLog.csv", "w")
dados = arq.readlines()
lidos = []
qntLidos = []

for i in range(len(dados)) :
    dados[i] = dados[i].strip()
    if dados[i] not in lidos :
        lidos.append(dados[i])
        qntLidos.append(1)
    else :
        qntLidos[lidos.index(dados[i])] += 1
print(lidos,qntLidos)

for index in range(len(qntLidos)) :
    novoLog.writelines(f'{lidos[index]}: {qntLidos[index]}\n')'''

# faça um jogo da forca usando funções

'''def jogoDaForca(palavra) :
    tracinhos = []
    palavraLista = []
    tentativasRestantes = 6
    for i in range(len(palavra)) :
        tracinhos.append('_')
        palavraLista.append(palavra[i])

    while palavraLista != tracinhos and tentativasRestantes != 0 :
        print(''.join(tracinhos))
        letraChutada = input(f'tentativas restantes: {tentativasRestantes}\ndigite uma letra: ')
        for index in range(len(palavra)) :
            if palavra[index] == letraChutada :
                tracinhos[index] = letraChutada
        if letraChutada not in palavra :
            tentativasRestantes-=1

        if palavraLista == tracinhos :
            print(''.join(tracinhos))
            print('parabéns, você advinhou a palavra!')

        if tentativasRestantes == 0 :
            print(''.join(tracinhos))
            print(f'você perdeu, a palavra era: {palavra}')

palavra = 'eletricidade'
jogoDaForca(palavra)'''