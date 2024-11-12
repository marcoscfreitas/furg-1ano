n = int(input(''))
listaLed = []
ListaQntdLed = []

for i in range(n) :
    led = input('')
    listaLed.append(led)

cont = 0
qntdLed = 0
for i in listaLed :
    while cont < len(i) :
        if i[cont] == '1' :
            qntdLed+=2
        if i[cont] == '2' :
            qntdLed+=5
        if i[cont] == '3' :
            qntdLed+=5
        if i[cont] == '4' :
            qntdLed+=4
        if i[cont] == '5' :
            qntdLed+=5
        if i[cont] == '6' :
            qntdLed+=6
        if i[cont] == '7' :
            qntdLed+=3
        if i[cont] == '8' :
            qntdLed+=7
        if i[cont] == '9' :
            qntdLed+=6
        if i[cont] == '0' :
            qntdLed+=6
        cont+=1
    ListaQntdLed.append(qntdLed)
    cont = 0
    qntdLed = 0

for i in ListaQntdLed :
    print(f'{i} leds')
