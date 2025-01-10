#leia a distancia percorrida e o tempo gasto. escreva a velocidade

dist = int(input('digite a distancia percorrida (km): '))
t = int(input('digite o tempo gasto (horas): '))
vel = dist/t
print(f'a velocidade média foi de: {vel:.2f}km/h') #print(vel)
