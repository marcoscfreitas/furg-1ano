n = int(input(''))
fraseList = []
fraseFinal = []
fraseFinalFinal = []
for i in range(n) :
    frase = input('')
    fraseList.append(frase)

for i in fraseList :
    fraseMod = i.split(' ')
    fraseFinal.append(fraseMod)

for i in fraseFinal :
    if len(i[0]) == len(i[1]) :
        cont1 = 0
        fraseMod2 = ''
        while cont1 != len(i[1]) :
            fraseMod2 = fraseMod2 + i[0][cont1] + i[1][cont1]
            cont1+=1
        fraseFinalFinal.append(fraseMod2)

    if len(i[0]) > len(i[1]) :
        cont1 = 0
        cont2 = len(i[1])
        fraseMod2 = ''
        while cont1 < len(i[1]) :
            fraseMod2 = fraseMod2 + i[0][cont1] + i[1][cont1]
            cont1+=1
            if cont1 == len(i[1]) :
                while cont2 < len(i[0]) :
                    fraseMod2 = fraseMod2 + i[0][cont2]
                    cont2+=1
        fraseFinalFinal.append(fraseMod2)
        
    if len(i[1]) > len(i[0]) :
        cont1 = 0
        cont2 = len(i[0])
        fraseMod2 = ''
        while cont1 < len(i[0]) :
            fraseMod2 = fraseMod2 + i[0][cont1] + i[1][cont1]
            cont1+=1
            if cont1 == len(i[0]) :
                while cont2 < len(i[1]) :
                    fraseMod2 = fraseMod2 + i[1][cont2]
                    cont2+=1
        fraseFinalFinal.append(fraseMod2)

for i in fraseFinalFinal :
    print(i)
