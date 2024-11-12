num = input()
cont = 0
numero_ruim = False

while cont < (len(num)-1) :
    if num[cont] == '1' and num[cont+1] == '3':
        numero_ruim = True 
    # if '13' in numero :
    #    numero_ruim = True
    cont+=1

if numero_ruim :
    print(f'{num} es de Mala Suerte')
else :
    print(f'{num} NO es de Mala Suerte')