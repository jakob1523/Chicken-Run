from spillObjekt import SpillObjekt
import random
bredde, hoyde = 800, 600

# Arver fra spillobjekt
class Kylling(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, fart_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._fart_y = fart_y
    
    def Hopp(self):
        pass

    # Kollisjon med hindring og bakke
    def kollisjon(self, hindring):

        # kolisjon med bakke
        if self.pos_y + self.size_y >= 230:
            self._fart_y = 0
            self.pos_y = 230 - self.size_y

        # Kollisjon med hindring
        if (
            self.pos_x < hindring.pos_x + hindring.size_x and
            self.pos_x + self.size_x > hindring.pos_x and
            self.pos_y < hindring.pos_y + hindring.size_y and
            self.pos_y + self.size_y > hindring.pos_y):
            return True

    def fall(self):
        self.pos_y += self._fart_y
