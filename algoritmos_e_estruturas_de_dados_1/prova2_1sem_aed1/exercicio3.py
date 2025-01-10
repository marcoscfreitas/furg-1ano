# crie um programa em python que leia um número inteiro e
# escreva a soma dos numeros correspondentes a cada dígito do número
# exemplo: 1412 == 8
# exemplo: 4341220 == 16
# exemplo: 101 == 2
# sem usar string

numero = int(input('informe um número positivo inteiro: '))
soma = 0
while numero > 0 :
    soma += numero%10
    numero = numero//10
print(f'a soma dos dígitos é: {soma}')

