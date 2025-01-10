'''
nome = 'Marcos FrEitAs'

print(nome)
lista = nome.split()
print(lista)
'''
nome = 'Marcos FrEitAs'
print(nome)
ls_nome = nome.capitalize()
print(ls_nome)

print(nome)
ls_nome = nome.split(' ')
print(ls_nome)

novo_nome = ''

for um_nome in ls_nome:
   codigo = ord(um_nome[0])
   if codigo >= ord('a') and codigo <= ord('z'): #se for minusculo
      novo_nome = novo_nome + chr(codigo-32)  
   else:
      novo_nome = novo_nome + um_nome[0] #se ja for maiusculo   
 
   #Transformando em minuscula
   i = 1 
   while i < len(um_nome):
     codigo = ord(um_nome[i])
     if codigo >= ord('A') and codigo <= ord('Z'):  
       novo_nome = novo_nome + chr(codigo+32)
     else:
      novo_nome = novo_nome + um_nome[i] 
     i = i + 1
   novo_nome = novo_nome + ' '
print(novo_nome)
