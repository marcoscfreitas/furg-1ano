# 1)(3,5 Pontos) Aprendemos que em Python é usual representar uma matriz como uma
# lista de listas. Crie uma função de receba uma matriz representada dessa forma e:
# a) Verifique se ela é uma matriz válida retangular ou quadrada;
# b) Retorne um texto indicando se é válida e qual é o maior valor na matriz;
# c)​Se a matriz for quadrada (o número de linhas igual ao número de colunas),
# acrescente ao texto o somatório dos valores da diagonal principal.

def mostrarMatriz(matriz) :
    valida = False
    for i in range(len(matriz)) :
        print(matriz[i])

def verificaMatriz(matriz) :
    valida = False
    quadrada = False
    maiorValor = 0
    somaDiagonal = 0
    for i in range(len(matriz)) :
        if len(matriz[i]) != len(matriz[0]) :
            return False
        else :
            valida = True
            for j in range(len(matriz[i])) :
                # print(i,j)
                # print(matriz[i][j])
                if matriz[i][j] >= maiorValor :
                    maiorValor = matriz[i][j]
                if i == j and len(matriz) == len(matriz[i]):
                    somaDiagonal += matriz[i][j]
                    quadrada = True

    if valida == True :
        print('matriz válida')
        print(f'o maior valor é {maiorValor}')
    if quadrada == True :
        print(f'soma diagonal: {somaDiagonal}')   

matriz = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
mostrarMatriz(matriz)
verificaMatriz(matriz)

if verificaMatriz(matriz) == False :
    print('matriz inválida.')    
