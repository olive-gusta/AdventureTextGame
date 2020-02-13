class Player_act():
    def __init__(self, input_com):
        self.input_com = input_com 
        act = {
               
                "NORTE":N, "N":N,"SUL":S, "S":S, "LESTE":L, "L":L, "OESTE":O, "O":O, "ATACAR":att, "ATT":att
                
                }

    def acao(self.input_com):
        #ignorando aqui as letras minusculas
        self.input_com = self.input_com.upper().strip()
        
        return act.get(input_com)



class Cena():
    def __init__(self, N=False, S=False, L=False, O=False, att=False):
        self.N = N
        self.S = S
        self.L = L
        self.O = O
        self.att = att
    #os nums são outras cenas
    def N(num):
        N = !N
        return num

    def S(num):
        S = !S
        return num

    def L(num):
        L = !L
        return num

    def O(num):
        O = !O
        return num

#class Item():
    
#class Criatura():








