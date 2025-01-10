# crie um programa em python que leia um número inteiro e escreva todos os divisores desse numero
# exemplo: 14 == 1,2,7,14
# exemplo: 17 == 1,17
# exemplo: 24 == 1,2,3,4,6,8,12,24

numero = int(input('digite um número inteiro positivo: '))
cont = 1

while cont <= numero :
    if numero%cont == 0 :
        print(cont)
        cont+=1
    else :
        cont+=1