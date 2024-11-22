def tabuada (num) :
    saida = ''
    for i in range(11) :
        mult = num*i
        saida = saida + (f'{num} x {i} = {mult}\n')
    return saida

# num = int(input('digite um número para tabuada: '))

# print(tabuada(num))

for num in range(11) :
    print(f'--- tabuada do {num} ---')
    print(tabuada(num))
    print('- - - - - * - - - - -') 