# EXERCÍCIOS DE ARQUIVOS - 06/12/2024
# 1) Faça uma função que recebe um código de estado e retorne quantas cidades há para aquele código.
'''def numCidadesDoCod(lista, cod_uf):
    num_cidades = 0
    for linha in lista:
        coluna = linha.split(',')
        if coluna[0] == cod_uf:
            num_cidades += 1
    return num_cidades
            

arq = open('municipios.csv', 'r')
dados = arq.readlines()
cod_uf = input('Insira o código de Estado: ')
num_cidades = numCidadesDoCod(dados, cod_uf)
print(f'Existem {num_cidades} cidades com o código de Estado {cod_uf}.')
arq.close()'''

# 2) Faça uma função que recebe uma string e retorne quais cidades contem a string. EX: 'rio' -> Rio Grande, Rio de Janeiro...
'''def contemPalavra(dados, palavra):
    lista_cidades = []
    for linha in dados:
        coluna = linha.split(',')
        posicao = coluna[2].find(palavra)
        if posicao != -1:
            lista_cidades.append(coluna[2])
    cidades = ''.join(lista_cidades)
        #if palavra in coluna[2]:
            #cidades.append(coluna[2])
    return cidades

arq = open('municipios.csv', 'r')
dados = arq.readlines()
palavra = input('Digite a palavra que deseja buscar: ').capitalize()
cidades = contemPalavra(dados, palavra)
print(f'Cidades que contem a palavra "{palavra}": \n{cidades}')
arq.close()
'''
# 3) Semelhante a 2, porém, retorna o número de cidades.
'''def contemPalavra(dados, palavra):
    num_cidades = 0
    for linha in dados:
        coluna = linha.split(',')
        posicao = coluna[2].find(palavra)
        if posicao != -1:
            num_cidades += 1
    return num_cidades


arq = open('municipios.csv', 'r')
dados = arq.readlines()
palavra = input('Digite a palavra que deseja buscar: ').capitalize()
num_cidades = contemPalavra(dados, palavra)
print(f'Cidades que contem a palavra "{palavra}": {num_cidades}')
arq.close()'''

# EXERCÍCIOS DE ARQUIVOS - 06/12/2024
# 1) Escreva uma função que receba o estado e retorne a UF.
'''def capitalize(estado):
    estado_capitalize = ''
    for i, letra in enumerate(estado):
        if letra == ' ':
            estado_capitalize += ' ' + estado[i + 1].capitalize()
        elif ord(letra) >= 65 or ord(letra) <= 90:

        else:
            estado_capitalize += letra
    return estado_capitalize'''

'''def EstadoParaUf(lista, estado):
    for linha in lista[1:]:
        coluna = linha.split(',')
        if estado == coluna[1]:
            uf = coluna[2][:-1]
            return uf

arq = open('estados.csv', 'r')
dados = arq.readlines()
estado = 'São Paulo'
uf = EstadoParaUf(dados, estado)
print(f'O estado correspondente a uf{uf} é {estado}.')
arq.close()'''

# 2) Escreva uma função que receba a UF retorne o estado.
'''def ufParaNome(lista, uf):
    #print(lista, uf)
    for linha in lista[1:]:
        coluna = linha.split(',')
        #print(f"({coluna[2][1:-1]}) ({uf})")
        uf_refatorado = coluna[2][1:-1]
        if uf_refatorado == uf:
            estado = coluna[1]
            print(estado)
            return estado

arq = open('estados.csv', 'r')
dados = arq.readlines()
uf = input('Digite a UF: ').upper()
estado = ufParaNome(dados, uf)
print(f'O estado correspondente a uf {uf} é {estado}.')
arq.close()'''

# 3) Escreva uma função que retorne o estado com o nome do mais longo e o mais curto.
'''def estadoMaisLongo(lista):
    maior = 'São Paulo'
    for linha in lista[1:]:
        um_estado = linha.split(',')
        print(len(um_estado[1]))
        if len(um_estado[1]) > len(maior):
            maior = um_estado[1]
    return maior

def estadoMaisCurto(lista):
    menor = 'São Paulo'
    for linha in lista[1:]:
        um_estado = linha.split(',')
        print(len(um_estado[1]))
        if len(um_estado[1]) < len(menor):
            menor = um_estado[1]
    return menor
            

arq = open('estados.csv', 'r')
dados = arq.readlines()
estado_longo = estadoMaisLongo(dados)
estado_curto = estadoMaisCurto(dados)
print(f'Estado de nome mais longo: {estado_longo} \nEstado de nome mais curto: {estado_curto}')
arq.close()
'''