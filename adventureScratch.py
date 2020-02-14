import comandos as com
import numpy as np

arquivo = np.genfromtxt("cenas.txt", delimiter=";", comments="#", dtype=[('id',int), 
                                            ('Text', "|U2400"), 
                                            ('N',int), 
                                            ('S',int), 
                                            ('L',int), 
                                            ('O',int), 
                                            ('com',bool)])

#precisamos de uma função que sempre escuta o que o jogador tem a dizer
def file_find(cenas):
    return arquivo[cenas]

cena = 0

while True:
    #apresentando a cena
    cena_atual = com.Cena(file_find(cena))
    print(cena_atual.texto_cena())
    
    #pegando a informaçãod do jogador
    action = input("> ")
    action = com.Player_act(action)
    action = action.acao()

    #aqui verificamos se é uma ação de coordenada e mudamos para a cena correspondente aquela coordenada
    if action in ['N', 'S', 'L', 'O']:
        cena = cena_atual.mudar_coord(action)
        print(cena)
    else: print('error')

