# limite = int(input('informe o tamanho da tabuada: '))
# with open ('saida.html', 'w') as arq:
#     numero1 = 1
#     numero2 = 1
#     arq.write('<table border = 1>')
#     while numero1 <= 10 and numero2<=10 :
#         arq.write('<tr>')
#         arq.write(f'<td>{numero1}x{numero2}</td>')
#         arq.write(f'<td>{numero1*numero2}</td>')
#         arq.write('</tr>')
#         numero2+=1
#         if numero2 > limite :
#             arq.write('</table>&nbsp;')
#             numero1+=1
#             numero2=1
#             arq.write('<table border = 1>')

# jeito prisco

# n = int(input('digite o numero maximo da tabuada: '))
# saida = 'o incrivel sistema de tabuadas<hr>'
# for um_n in range(n+1) :
#     saida += '<table border= 1>'
#     for i in range(11) :
#         mult = i * um_n
#         saida += f'<tr><td>{um_n}x{i} =</td><td>{mult}</td></tr>\n'
#     saida += '</table><br>'
# with open ('tabuada.html', 'w') as arq :
#     arq.write(saida)

with open ('tabuada.py', 'r') as arq :
    texto = arq.read()
print(texto)