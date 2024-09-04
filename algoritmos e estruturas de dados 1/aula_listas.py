# listas são um tipo estruturado que armazena qualquer coisa, é mutável e um objeto
# python -> programação orientada a objetos

compras = ['nutella', 'pão', 'queijo', 'coquinha', 'patê', 'carne']
print(compras)
compras[4] = 'brigadeiro'
print(compras)
compras.append('nescau')
compras.insert(0,'inicio')
print(compras)

# percorrer lista

i=0
while i <len(compras) :
    print(compras[i])
    i+=1

# iteração (for)

for produto in compras :
    print(produto)


# exemplo lista de compras
'''
lista = []
item = ' '

while item != '' :
    item = input('digite um item para lista de compras: ')
    lista.append(item)

print('LISTA DE COMPRAS:')
for item in lista :
    print(f' -> {item}')

# para não printar o último
    if item == '' :
        break;
    else :

'''

lista = []
lista_preco = []
item = ' '
preco = ' '
total = 0

while item != '' :
    item = input('digite um item para lista de compras: ')
    preco = input(f'digite o valor do {item}: ')
    if item != '' : 
        lista.append(item)
        lista_preco.append(float(preco))
        total = total + float(preco)
    else :
        print('LISTA DE COMPRAS:')
        i=0
        while i <len(lista) :
            print(f'> {lista[i]} ------- R${lista_preco[i]:.2f}')
            i+=1
        print('--------------------')
        print(f'TOTAL ------- R${total:.2f}')

# python3.8 > saida.hmtl