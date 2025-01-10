# printar todos dados da tela

# arq = open('alunos.csv','r')
# dados = arq.read()
# print(dados)
# arq.close()

# ou
# def mostra_nomes(lista) :
#     for linha in lista[1:] :
#         uma_lista = linha.split(';')
#         print(uma_lista[1])

# arq = open('alunos.csv','r')
# dados = arq.readlines()
# mostra_nomes(dados)

# for item in dados :
#     print(item)


# listar apenas os nomes dos alunos

# arq = open('alunos.csv','r')
# dados = arq.readlines()

# for lista in dados[1:] :
#     colunas = lista.split(';')
#     print(colunas[1])
# arq.close()

# mostrar quem é o aluno mais novo

# arq = open('alunos.csv','r')
# dados = arq.readlines()

# # print(dados)

# lista_nascimento = []
# for i in dados :
#     dados_lista = i.split(';')
#     lista_nascimento.append(dados_lista[2][:-1])
# lista_nascimento.pop(0)

# # print(lista_nascimento)

# for data in lista_nascimento :
#     resultado = data.split('/')
#     print(resultado)
#     for numero in resultado :


# def mais_novo(lista) :
#     novo = '10251231'
#     nome_do_novo = ''
#     dt_original = ''

#     for linha in lista[1:] :
#         uma_lista = linha.split(';')
#         data = uma_lista[2][:-1]
#         lista_data = data.split('/')
#         data_padrao = lista_data[2] + lista_data[1] + lista_data[0]
#         if data_padrao > novo :
#             novo = data_padrao
#             nome_do_novo = uma_lista[1]
#             dt_original = data
#     print(nome_do_novo,dt_original)

# arq = open('alunos.csv','r')
# dados = arq.readlines()
# mais_novo(dados)