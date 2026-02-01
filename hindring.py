from spillObjekt import SpillObjekt

# Arver fra Spillobjekt
class Hindring(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, fart_x):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._fart_x = fart_x

    # metode for å bevege på hindringen
    def bevege(self):
        self.pos_x -= self._fart_x
    