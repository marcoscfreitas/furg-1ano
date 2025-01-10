# escreva um programa em python que leia o desempenho de um carro e um trajeto escolhido em um mês.
# Escreva o quanto foi gasto em reais, considerando a gasolina R$5,85.
# exemplo: desempenho: 12km/l trajeto 1000km gasto 487,50
# exemplo: desempenho: 16km/l trajeto 1500km gasto 548,44
# exemplo: desempenho: 8,9km/l trajeto 2000km gasto 1314,60

desempenho = float(input('escreva o desempenho do carro (km/l): '))
trajeto = int(input('informe o trajeto realizado pelo carro (km): '))
gasolina = 5.85

gasto = (trajeto/desempenho) * gasolina
print(f'o gasto é de R$:{gasto:.2f}')