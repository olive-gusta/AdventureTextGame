import comandos as com
import numpy as np

arquivo = np.genfromtxt("cenas.txt", delimiter=";", comments="#", dtype=[   ('id',int), 
                                                                            ('Text', "|U2400"),
                                                                            ('N',int),
                                                                            ('S',int),
                                                                            ('L',int),
                                                                            ('O',int),
                                                                            ('subir',int), 
                                                                            ('descer',int), 
                                                                            ('item',"|U10")
                                                                        ]
                        )

arquivo_item = np.genfromtxt("items.txt", delimiter=";", comments="#", dtype=[ 
                                                                            ('Nome', "U15"),
                                                                            ('Tipo', "U15"),
                                                                            ('Usar', bool),
                                                                            ('Beber', bool),
                                                                            ('Equipar', bool),
                                                                            ('Largar', bool),
                                                                            ('Puxar', bool),
                                                                            ('Empurrar', bool),
                                                                            ('Abrir', bool),
                                                                            ('Olhar', "U15")
                                                                            ]
                            )

#precisamos de uma função que sempre escuta o que o jogador tem a dizer
def file_find(cenas, tipo="cena"):
    if tipo == "cena":
        cenas = int(cenas)
        cenas_file = arquivo[cenas]
        return cenas_file
    elif tipo == "item":
        item_file = int(cenas)
        item_file = arquivo_item[(int(item_file)-1)]
        return item_file

cena = 0

while True:
    #apresentando a cena
    cena_atual = file_find(cena)
    cena_atual = com.Cena(cena_atual)
    items_atual = []
    for i in list(cena_atual.obj_cenario()):
        if i != " ":
            items_atual.append(com.Item(file_find(i, tipo="item")))
            
    print(cena_atual.texto_cena())
    for i in range(len(items_atual)): print(items_atual[i].texto_item())

    #pegando a informaçãod do jogador
    action = input("> ")
    action = com.Player_act(action)
    action = action.acao()

    #aqui verificamos se é uma ação de coordenada e mudamos para a cena correspondente aquela coordenada
    if action in ['N', 'S', 'L', 'O', 'subir', 'descer']:
        cena = cena_atual.mudar_coord(action)
    elif action in ["interações"]: print("")
    else: print("Eu acho que não é possivel fazer isso")
