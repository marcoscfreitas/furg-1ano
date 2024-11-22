def dobro (num) :
    saida = num * 2
    return saida

def verificaPar (valor) :
    if valor % 2 == 0 :
        return True
    return False

def teste() :
    print('volta as aulas!')
    return 2
    print('amamos a grama sendo cortada')

teste()


numero = int(input('digite o número: '))
duplo = dobro(numero)
print(duplo)

print(verificaPar(numero))

if verificaPar(numero) :
    print('é par!')
else :
    print('é ímpar!')