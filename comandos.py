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
        self.coords = [self.file_cena[2],self.file_cena[3],self.file_cena[4],self.file_cena[5]]

    def id_cena(self):
        return self.file_cena[0]

    def texto_cena(self):
        return self.file_cena[1]

    #essa função é um metodo para mudar para a coordenada passada
    def mudar_coord(self, coord):
        if coord == 'N':# and self.coords[0] != 0:
            return self.coords[0]
        if coord == 'S':# and self.coords[1] !=0:
            return self.coords[1]
        if coord == 'L':# and self.coords[2] != 0:
            return self.coords[2]
        if coord == 'O':# and self.coords[3] != 0:
            return self.coords[3]
        
        
#class Item():
    
#class Criatura():








