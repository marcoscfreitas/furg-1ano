def GetVogalRisada (risada) :
    risadaVogal = ''
    for vogal in risada :
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u' :
            risadaVogal = risadaVogal + vogal
    return risadaVogal
    
def GetVogalRisadaInversa (risada) :
    risadaVogalInversa = ''
    cont2 = (len(risada)-1)
    while cont2 >= 0 :
        if risada[cont2] == 'a' or risada[cont2] == 'e' or risada[cont2] == 'i' or risada[cont2] == 'o' or risada[cont2] == 'u' :
            risadaVogalInversa = risadaVogalInversa + risada[cont2]
        cont2-=1
    return risadaVogalInversa

def comparaVogal (risadaVogal, risadaVogalInversa) :
    if risadaVogal == risadaVogalInversa :
        saida = 'S'
    else :
        saida = 'N'
    return saida


risada = input('')
risadaVogal = GetVogalRisada(risada)
risadaVogalInversa = GetVogalRisadaInversa(risada)
print(comparaVogal(risadaVogal, risadaVogalInversa))
