# EXERCÍCIOS DE ARQUIVOS - 06/12/2024
# 1) Faça uma função que recebe um código de estado e retorne quantas cidades há para aquele código.
'''
def mostrarCidades(dados,cod) :
    cidades = []
    numCidades = 0
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if lista[0] == cod :
            cidades.append(lista[2])
            numCidades+=1
    return cidades

cod = input('digite o código de estado (13-53): ')
arq = open('municipios.csv', 'r') 
dados = arq.readlines()
arq.close()

cidades = mostrarCidades(dados,cod)
for cidade in cidades :
    print(cidade)
print(f'Existem {len(cidades)} cidades com o código {cod}')
'''
# 2) Faça uma função que recebe uma string e retorne quais cidades contem a string, e o número de cidades. EX: 'rio' -> Rio Grande, Rio de Janeiro...
'''
def retornarString(pesq,dados) :
    cidades = []
    for linha in dados[1:] :
        lista = linha.strip().split(',')
        if lista[2].find(pesq) != -1 :
            cidades.append(lista[2])
    return cidades

pesq = input('pesquise uma cidade: ').capitalize()
arq = open('municipios.csv', 'r') 
dados = arq.readlines()
arq.close()

cidades = retornarString(pesq,dados)
for cidade in cidades :
    print(cidade)
print(f'Existem {len(cidades)} cidades com a string "{pesq}"')
'''