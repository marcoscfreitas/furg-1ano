# crie um programa em python que solicite um numero inteiro positivo. deve dividir sucessivamente por 2 até que o resultado seja menor que 1. mostrar o resultado da divisao e ao fim, exibir "chegou ao zero"

num = int(input('digite um número inteiro positivo: '))
while num > 1 :
    num = num/2
    if num >= 1 :
        print(f'resultado da divisão: {num}')
print('chegou a zero!')
