# crie um programa em python que leia um número inteiro entre 1000 e 9999 e escreva o número com os dígitos invertidos ex: 1412 = 2141 / 2024 = 4202 / 1000 / 1. sem usar strings

x = int(input('digite um número entre 1000 e 9999 para inverter: '))
temp = x
dig1 = 0
dig2 = 0
dig3 = 0
dig4 = 0
final = 0

dig1 = x%10
temp = temp//10

dig2 = temp%10
temp = temp//10

dig3 = temp%10
temp = temp//10

dig4 = temp%10

dig1 = dig1*1000
dig2 = dig2*100
dig3 = dig3*10

final = dig1+dig2+dig3+dig4

print(final)
