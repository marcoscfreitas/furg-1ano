# EXERCÍCIOS DE ARQUIVOS - 06/12/2024
# 1) Escreva uma função que receba o estado e retorne a UF.
'''
def capEstado(estado) :
    estadoCap = ''
    cont = 0
    while cont != len(estado) :
        if estado[cont] == ' ' :
            estadoCap+= ' ' + estado[cont+1].upper()
            cont+=1
        else :
            estadoCap += estado[cont]
        cont+=1
    return estadoCap

def retornaUF(estadoCap, dados) :
    uf = ''
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if estadoCap == lista[1] :
            uf = lista[2]
    return uf

estado = input('digite o estado: ').capitalize()
arq = open('estados.csv', 'r') 
dados = arq.readlines()
arq.close()

estadoCap = capEstado(estado)
uf = retornaUF(estadoCap,dados)
print(f'o UF do estado de {estadoCap} é{uf}')
'''
# 2) Escreva uma função que receba a UF retorne o estado.
'''
def retornaEstado(uf, dados) :
    estado = ''
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if uf == lista[2].strip() :
            estado = lista[1]
    return estado

uf = input('digite a UF: ').upper()
arq = open('estados.csv', 'r') 
dados = arq.readlines()
arq.close()

estado = retornaEstado(uf,dados)
print(f'o estado da uf {uf} é {estado}')
'''
# 3) Escreva uma função que retorne o estado com o nome do mais longo e o mais curto.
'''
def retornaMaior(dados) :
    maior = ''
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if len(lista[1]) > len(maior) :
            maior = lista[1]
    return maior

def retornaMenor(dados) :
    menor = '      '
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if len(lista[1]) < len(menor) :
            menor = lista[1]
    return menor

arq = open('estados.csv', 'r')
dados = arq.readlines()
arq.close
print(f'o estado com maior nome é: {retornaMaior(dados)}')
print(f'o estado com menor nome é: {retornaMenor(dados)}')
'''