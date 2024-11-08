
n = int(input())
lista = input().split()
listaNum = []
# i = 0
# print(lista)

for n in lista :
    listaNum.append(int(n)) # str
# print(listaNum)

# while i < len(lista) :
#     lista[i] = int(lista[i])
#     i+=1
# print(lista)

cont = 1
menorPos = 0
menorNum = listaNum[0]

while cont < len(listaNum) :
    if listaNum[cont] < menorNum :
        menorNum = listaNum[cont]
        menorPos = cont
    cont+=1
print(f'Menor valor: {menorNum}')
print(f'Posicao: {menorPos}')



