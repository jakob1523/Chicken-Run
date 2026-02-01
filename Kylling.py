from spillObjekt import SpillObjekt
bredde, hoyde = 800, 600

# Arver fra spillobjekt
class Kylling(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, fart_y, gravity):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._fart_y = fart_y
        self._gravity = gravity
        self.hopper = False


    def hopp(self):
        if self.pos_y >= 230 - self.size_y:
            self._fart_y = -10  # negativ fart for å hoppe opp
            self.hopper = True

    def oppdater(self):
        self._fart_y += self._gravity
        self.pos_y += self._fart_y
        if self.pos_y >= 230 - self.size_y:
            self.pos_y = 230 - self.size_y
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
    



                    
