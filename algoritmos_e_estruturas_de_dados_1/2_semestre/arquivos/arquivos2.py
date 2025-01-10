# with open('alunos.csv', 'r') as arq : #nao precisa fazer close

readlines # le linha por linha
arq.seek(offset,local)
arq.seek(local) # move cursor para local designado

with open ('alunos.csv', 'w') as arq :
    arq.write('string')