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

import graphics as gf # importa arquivos de graphics
import random as rd
win = gf.GraphWin('minha janela',400,350) # cria uma janela

c = gf.Circle(gf.Point(100,150), 10) # cria ponto
cores = ['red','blue','green','orange','yellow','black']
c.setFill('red') # deixa ponto vermelho
c.draw(win) # fala em qual janela c deve ser draw
cont = 0
while True :
    onde_cliquei =  win.getMouse() # printa onde esta o mouse
    print(onde_cliquei.getX, onde_cliquei.getY) # coordanadas do clique
    nova_bolinha = gf.Circle(onde_cliquei, 10)
    cor = rd.randint(0,len(cores))
    cont+=1
    if cont == len(cores) :
        cont = 0
    nova_bolinha.draw(win)