# 2) (3,0 Pontos) Crie uma função que receba uma data em formato DD/MM/AAAA e
# retorne seu nome por extenso. A função deve receber como parâmetro o nome da
# cidade base. Considere que a data entregue é válida. Não precisa perder tempo
# validando a data.

def nomeExtenso(data,cidade) :
    mesesExtenso = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    data = data.split('/')
    saida = []
    dia = int(data[0])
    mes = int(data[1])

    if dia == 1 :
        data[0] = '1o'

    for _ in range(len(mesesExtenso)) :
        data[1] = mesesExtenso[mes-1]
    
    for i in range(len(data)) :
        saida.append(data[i])
    saida.append(cidade)
    
    return saida

data = input('informe uma data DD/MM/AAAA: ')
cidade = input('informe uma cidade: ')
saida = nomeExtenso(data,cidade)
print(f'{saida[3]}, {saida[0]} de {saida[1]} de {saida[2]}')