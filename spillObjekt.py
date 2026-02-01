import pygame
pygame.init()
 

bredde, hoyde = 800, 600
FPS = 60

skjerm = pygame.display.set_mode((bredde, hoyde))


# Superklasse som kylling og hindring 

class SpillObjekt:
    def __init__(self, posisjon_x: int, posisjon_y: int, storrelse_x: int, storrelse_y: int):
        self.pos_x = posisjon_x
        self.pos_y = posisjon_y
        self.size_x = storrelse_x
        self.size_y = storrelse_y

# metode for å spill objekter på skjermen
    def tegn(self, farge):
        pygame.draw.rect(skjerm, farge, (self.pos_x, self.pos_y, self.size_x, self.size_y))
