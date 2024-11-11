numeros = input().split(' ')
numerosInt = []
for n in numeros :
    numerosInt.append(int(n))

soma = numerosInt[0] + numerosInt[1]
soma = str(soma)

for i in soma :
    if i == '0' :
        soma = soma.replace('0','')
print(soma)


# def tirarZero(numeros) :
#     n1 = int(numeros[0])
#     n2 = int(numeros[1])
#     soma = n1 + n2
#     soma = str
#     saida = ''
#     for num in soma :
#         if num != '0' :
#             saida = saida + num
#     return saida

# numeros = input().split(' ')

# print(tirarZero(numeros))
