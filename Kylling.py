from spillObjekt import SpillObjekt
import random
bredde, hoyde = 800, 600

GRAVITY = 0.6

# Arver fra spillobjekt
class Kylling(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, fart_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._fart_y = 0
        self.hopper = False
        self.start_fart = fart_y
        self.bakke_y = 230 - storrelse_y

    def hopp(self):
        if not self.hopper and self.pos_y >= self.bakke_y:
            self._fart_y = -12  # negativ fart for å hoppe opp
            self.hopper = True

    def oppdater(self):
        self._fart_y += GRAVITY
        self.pos_y += self._fart_y
        if self.pos_y >= self.bakke_y:
            self.pos_y = self.bakke_y
            self._fart_y = 0
            self.hopper = False

    # Kollisjon med hindring
    def kollisjon(self, hindring):
        # Kollisjon med hindring
        if (
            self.pos_x < hindring.pos_x + hindring.size_x and
            self.pos_x + self.size_x > hindring.pos_x and
            self.pos_y < hindring.pos_y + hindring.size_y and
            self.pos_y + self.size_y > hindring.pos_y):
            return True
        return False
    
    def dukk(self):
        self.size_y = 30
        self.pos_y = 210



                    
