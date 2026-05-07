from kerri import Kerri


class KerriElektrik(Kerri):

    def __init__(self,emri,viti,modeli,bateria):
        super().__init__(emri,viti,modeli)
        self.bateria=bateria



    def rritjeShpejtesis(self):
        print("kerri elektrik eshte duke e rri shpejtesin")


    def mbusheBaterin(self):
        print("mbushe baterin")