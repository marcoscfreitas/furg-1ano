def verificaPrimo(n) :
    div = 1
    i= 1
    while i != n :
        if n%i == 0 :
            div+=1
            i+=1
        else :
            i+=1

    if div>2 :
        return False
    return True
    
n = int(input('digite um número para verificar se é primo: '))
print(verificaPrimo(n))

if verificaPrimo(n) :
    print('é primo')
else :
    print('não é primo')

# correção prisco

# def eh_primo(num) :
#     cont = 2
#     while cont < num :
#         if num % cont == 0 :
#             return False
#         cont = cont + 1
#     return True

# for i in range (100,200) :
#     if eh_primo(i) :
#         print(i)