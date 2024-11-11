n = int(input(''))
listaPomekon = []
listaPomekonAdd = []

for pomekon in range(n) :
    pomekon = input('')
    listaPomekon.append(pomekon)
    
cont1 = 1
cont2 = 0

while cont2 <= len(listaPomekon)-1 :
    if listaPomekon[cont2] not in listaPomekonAdd :
        listaPomekonAdd.append(listaPomekon[cont2])
    cont2+=1

print(f'Falta(m) {151-len(listaPomekonAdd)} pomekon(s).')