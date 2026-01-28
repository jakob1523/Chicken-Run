from spillObjekt import SpillObjekt
import random

class Hindring(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, fart_x):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._fart_x = fart_x

    def bevege(self):
        self.pos_x -= self._fart_x
    
    def opprett(self):
        if self.pos_x + self.size_x <= 0:
            self.pos_x = 900
            self.pos_y = 180