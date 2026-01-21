from spillObjekt import SpillObjekt
import random
bredde, hoyde = 800, 600

# Arver fra spillobjekt
class Ball(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, hastighet_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._hastighet_y = hastighet_y