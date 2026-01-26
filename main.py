import pygame
import sys
from Kylling import Kylling
from spillObjekt import SpillObjekt
from hindring import Hindring
pygame.init()
 
font = pygame.font.SysFont('Impact', 24)

bredde, hoyde = 900, 300
hvit = (255, 255, 255)
FPS = 60


skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Chicken Run')
clock = pygame.time.Clock()

try:
    kylling_bilde = pygame.image.load("bilder/ninja_kylling.png")
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

kylling = Kylling(50, 100, 30, 30, 5)
hindring = Hindring(900, 180, 30, 50, 10)


class Spill:
    def __init__(self):
        self.aktiv = True
    
    #spill løkken
    def loop(self):
        while self.aktiv == True:
            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False

            # Restarter skjermen hver gang løkken kjører
            skjerm.fill((0, 0, 0))
            pygame.draw.rect(skjerm, (18, 181, 181), (0, 0, 900, 270))
            pygame.draw.rect(skjerm, (150, 75, 0), (0, 230, 900, 100))
            pygame.draw.rect(skjerm, (18, 207, 14), (0, 230, 900, 15))

            # Kollisjonssjekk
            if kylling.kollisjon(hindring):
                print("Kollisjon! Spillet er over.")
                self.aktiv = False
                continue

            hindring.bevege()
            kylling.fall()
            kylling.tegn()
            hindring.tegn()

            # oppdater skjerm
            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()