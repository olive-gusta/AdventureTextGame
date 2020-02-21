class Player_act():
    def __init__(self, input_com):
        self.input_com = input_com 
        self.act = {
                "NORTE":'N', 
                "N":'N', 
                "SUL":'S', 
                "S":'S', 
                "LESTE":'L', 
                "L":'L', 
                "OESTE":'O', 
                "O":'O', 
                "ATACAR": 'att', 
                "ATT": 'att'
                }

    def acao(self):
        #ignorando aqui as letras minusculas
        self.input_com = self.input_com.upper().strip()
        
        return self.act.get(self.input_com)

    




class Cena():
    def __init__(self, file_cena):
        self.file_cena = file_cena
        self.coords = [ self.file_cena[2],
                        self.file_cena[3],
                        self.file_cena[4],
                        self.file_cena[5],
                        self.file_cena[6],
                        self.file_cena[7]]
        self.itens = self.file_cena[8]

    def id_cena(self):
        return self.file_cena[0]

    def texto_cena(self):
        return self.file_cena[1]

    #essa função é um metodo para mudar para a coordenada passada
    def mudar_coord(self, coord):
        '''
        Em mudar coordenadas definimos as movimentações possíveis entre cenas.
        Sendo elas:
        Norte, Sul, Leste, Oeste, Subir e Descer

        Para interações dentre da cena veja interações
        '''
        if coord == 'N':# and self.coords[0] != 0:
            return self.coords[0]
        if coord == 'S':# and self.coords[1] !=0:
            return self.coords[1]
        if coord == 'L':# and self.coords[2] != 0:
            return self.coords[2]
        if coord == 'O':# and self.coords[3] != 0:
            return self.coords[3]
        if coord == 'SUBIR':
            return self.coords[4]
        if coord == 'DESCER ':
            return self.coords[5]

    def obj_cenario(self):
        return self.itens

    def interacoes(self, interacao):
        '''
    Aqui definimos as açoes possíveis dentro de uma cena.
    Sendo elas:
    Atacar, Usar, Beber, Equipar, Largar, Puxar ou Empurrar, Abrir, Olhar, Falar...

    Para mundança de cena veja mudar_coord
        '''
        if interacao == 'ATT':
           return None
        
        if interacao == 'USAR':
           return None
        
        if interacao == 'BEBER':
           return None

        if interacao == 'EQUIPAR':
           return None

        if interacao == 'LARGAR':
           return None

        if interacao == 'PUXAR':
           return None

        if interacao == 'EMPURRAR':
           return None

        if interacao == 'ABRIR':
           return None

        if interacao == 'OLHAR':
           return None

        if interacao == 'FALAR':
           return None

class Item():
    '''
    Aqui definimos todos os possíveis items dentro do jogo
    Objetos serão definidos como dicionarios que possuem algumas carateristicas acessíveis
    '''
    def __init__(self, objeto):
        self.objeto = objeto

    def texto_item(self):
        return self.objeto['Nome']

    def pers_itm(self, obj):
        '''
        Objetos que o jogador pode possuir, bem como pegar usar ...
        '''


    def cen_itm():
        '''
        Objetos que fazem parte do cenário, como portas, janelas, alavancas ...
        '''



#class Criatura():

class Personagem():
    def __init__(self, other):
        self.vida = int
        self.mochila = []
        self.mao = 0
        self.equipamento = int

    def items():
        self.mochila = []





