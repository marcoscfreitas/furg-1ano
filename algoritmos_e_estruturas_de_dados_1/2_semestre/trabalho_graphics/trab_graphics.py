# import graphics as gf # importa arquivos de graphics

# win = gf.GraphWin('minha janela',400,350) # cria uma janela

# c = gf.Circle(gf.Point(100,150), 10) # cria ponto
# cores = ['red','blue','green','orange','yellow','black']
# c.setFill('red') # deixa ponto vermelho
# c.draw(win) # fala em qual janela c deve ser draw
# cont = 0
# while True :
#     onde_cliquei =  win.getMouse() # printa onde esta o mouse
#     print(onde_cliquei.getX, onde_cliquei.getY) # coordanadas do clique
#     nova_bolinha = gf.Circle(onde_cliquei, 10)
#     nova_bolinha.setFill(cores[cont])
#     cont+=1
#     if cont == len(cores) :
#         cont = 0
#     nova_bolinha.draw(win)

# import graphics as gf # importa arquivos de graphics
# import random as rd
# win = gf.GraphWin('minha janela',400,350) # cria uma janela

# c = gf.Circle(gf.Point(100,150), 10) # cria ponto
# cores = ['red','blue','green','orange','yellow','black']
# c.setFill('red') # deixa ponto vermelho
# c.draw(win) # fala em qual janela c deve ser draw
# cont = 0
# while True :
#    onde_cliquei =  win.getMouse() # printa onde esta o mouse
#    print(onde_cliquei.getX, onde_cliquei.getY) # coordanadas do clique
#    nova_bolinha = gf.Circle(onde_cliquei, 10)
#    cor = rd.randint(0,len(cores))
#    cont+=1
#    if cont == len(cores) :
#        cont = 0
#    nova_bolinha.draw(win)


import graphics as gf  #trazer o arquivo da graphics
import random as rd 

win = gf.GraphWin(  "Minha Janela"  , 400, 350)   #cria uma janela
# c = gf.Circle(gf.Point(100, 150), 10)             #cria o ponto
# c.setFill('red')
# c.draw(win)                                       #fala em qual janela o ponto deve ser draw
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink']

def foi_no_botao(botao,onde_cliquei):
	bt_x = botao.getP1().getX()
	bt_y = botao.getP1().getY()
	bt2_x = botao.getP2().getX()
	bt2_y = botao.getP2().getY()
	#print(f'--> ({bt_x},{bt_y})({bt2_x},{bt2_y})')
	return True

#cont = 0
controller = True
cliques = []
cliquesMenor = []
cliquesMaior = []

botao = gf.Rectangle(gf.Point(10,10), gf.Point(190,50))
botao.setFill('yellow')
botao.draw(win)

while controller == True:
	cont1 = 1
	cont2 = 10
	onde_cliquei = win.getMouse()
	if foi_no_botao(botao,onde_cliquei) :
		botao.setFill('red')
	else :
		botao.setFill('yellow')

	posicao = onde_cliquei.getX() - onde_cliquei.getY()

	while cont1 < 11 :
		cliquesMenor.append(posicao+cont1)
		cont1+=1
	while cont2 > 0 :
		cliquesMaior.append(posicao-cont2)
		cont2-=1

	nova_bolinha = gf.Circle(onde_cliquei, 10)
	cor = rd.randint(0, len(cores) - 1)
	nova_bolinha.setFill(cores[cor])
	nova_bolinha.draw(win)

	if posicao not in cliques :
		cliques.append(posicao)
		print('entrou')
	else :
		controller = False

	print(cliques)
	#print(cliquesMenor)
	#print(cliquesMaior)