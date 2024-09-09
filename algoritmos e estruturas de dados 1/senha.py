'''
#Leia uma senha  e diga se ela é 

Forte: 3 tipos
Média: 2 tipos
Fraca: 1 tipo

Numérico
Alfabético
Especial


S = str(input('Digite sua senha e veja se ela é \nForte\nMédia\nFraca: '))

Mai = False
Min = False
Num = False
Esp = False
CS = ''
for C in S:
   V = ord(C)
   if 65 <= V <= 90:
      Mai = True
   elif 97 <= V <= 122:
      Min = True
   elif 48 <= V <= 57:
      Num = True
   else:
      Esp = True
      
if Mai and Min and Num and Esp:
  CS = 'Sua senha é Forte'
elif Mai and Min and Num:
  CS = 'Sua senha é Media'
else:
  CS = 'Sua senha é Fraca'
  
print(CS)
'''

'''
# Leia uma senha e diga se ela é forte
# Tipos: Numérico, Alfabético e Especial
# Forte: 3 tipos
# Média: 2 tipos
# Fraca: 1 tipo

senha = input("Digite a senha: ")

numeros = "0123456789"
i = ord("A")
j = ord("a")
letras = ""
while i < ord("Z"):
    letras += chr(i) + chr(j)
    i += 1
    j += 1

tem_numero = False
tem_letra = False
tem_especial = False

forca = 0
tipos = ["Inválida", "Fraca", "Média", "Forte"]

for char in senha:
    if char in numeros:
        tem_numero = True
    else:
        if char in letras:
            tem_letra = True
        else:
            tem_especial = True

if tem_numero:
    forca += 1
if tem_letra:
    forca += 1
if tem_especial:
    forca += 1

print(tipos[forca])
'''
# 2) Leia uma senha e diga se ela é: FRACA -> 1 tipo; MÉDIA: 2 tipos; FORTE: 3 tipos. Tipos: alfabético, númerico e especial. 
senha = input('Crie uma senha: ')
alf = False
num = False
esp = False
i = 0
while i < len(senha):
	p = ord(senha[i])
	if (p >= 65 and p < 91) or (p >= 97 and p < 123):
		alf = True
	elif p >= 48 and p < 58:
		num = True
	else:
		esp = True
	i += 1

if alf == True and num == False and esp == False:
	print('Senha FRACA. Tente outra.')
elif alf == True and num == True and esp == False:
	print('Senha MÉDIA.')
else:
	print('Senha FORTE')
