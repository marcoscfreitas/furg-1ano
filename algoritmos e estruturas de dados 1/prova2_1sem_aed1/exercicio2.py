# crie um programa em python que leia uma data de 2024 ou de 2025 e escreva qual o dia da semana que corresponde a data.
# observe que 2024 é um ano bissexto e que o ano começou numa segunda feira.
# exemplo: 12/01/2024 retorna sexta feira
# exemplo: 03/04/2024 retorna quarta feira
# exemplo: 31/03/2025 retorna segunda feira
# exemplo: 06/04/2025 retorna domingo

dia = int(input('digite o dia: '))
mes = int(input('digite o mês: '))
ano = int(input('digite o ano (2024 ou 2025): '))

dias_totais = dia

if mes > 1:
    dias_totais += 31
if mes > 2:
    if ano == 2024:
        dias_totais += 29
    else:
        dias_totais += 28
if mes > 3:
    dias_totais += 31
if mes > 4:
    dias_totais += 30
if mes > 5:
    dias_totais += 31
if mes > 6:
    dias_totais += 30
if mes > 7:
    dias_totais += 31
if mes > 8:
    dias_totais += 31
if mes > 9:
    dias_totais += 30
if mes > 10:
    dias_totais += 31
if mes > 11:
    dias_totais += 30

if ano == 2024:
    dia_da_semana = (dias_totais - 1) % 7
if ano == 2025 : 
    dia_da_semana = (dias_totais + 1) % 7

if dia_da_semana == 0:
    print(f'a data {dia}/{mes}/{ano} é segunda-feira')
if dia_da_semana == 1:
    print(f'a data {dia}/{mes}/{ano} é terça-feira')
if dia_da_semana == 2:
    print(f'a data {dia}/{mes}/{ano} é quarta-feira')
if dia_da_semana == 3:
    print(f'a data {dia}/{mes}/{ano} é quinta-feira')
if dia_da_semana == 4:
    print(f'a data {dia}/{mes}/{ano} é sexta-feira')
if dia_da_semana == 5:
    print(f'a data {dia}/{mes}/{ano} é sábado')
if dia_da_semana == 6:
    print(f'a data {dia}/{mes}/{ano} é domingo')