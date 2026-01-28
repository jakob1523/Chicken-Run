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

kylling = Kylling(50, 230, 30, 60, 5)
hindring = Hindring(900, 180, 30, 50, 10)

hopper = True

restart = 'Trykk For Restart'
restart_setup = font.render(restart, True, (255,255,255))


class Spill:
    def __init__(self):
        self.aktiv = True
        self.score = 0
        self.spill_over = False

    #spill løkken
    def loop(self):
        global hopper

        while self.aktiv == True:
            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False
                if hendelse.type == pygame.KEYDOWN:
                    if hendelse.key == pygame.K_SPACE:
                        kylling.hopp()
                    
                if hendelse.type == pygame.KEYDOWN:
                    if hendelse.key == pygame.K_DOWN:
                        kylling.size_y = 30
                        kylling.pos_y = 210

                if hendelse.type == pygame.KEYUP:
                    if hendelse.key == pygame.K_DOWN:
                        kylling.size_y = 60
                        kylling.pos_y = 180

            # Restarter skjermen hver gang løkken kjører
            skjerm.fill((0, 0, 0))
            pygame.draw.rect(skjerm, (18, 181, 181), (0, 0, 900, 270))
            pygame.draw.rect(skjerm, (150, 75, 0), (0, 230, 900, 100))
            pygame.draw.rect(skjerm, (18, 207, 14), (0, 230, 900, 15))

            # Kollisjonssjekk
            if kylling.kollisjon(hindring):
                tap = (f'Du fikk {self.score} score')
                skjerm.blit(restart_setup, (bredde/2 - 85, hoyde/2 - 45))
                tap_setup = font.render(tap, True, (255,255,255))
                skjerm.blit(tap_setup, (bredde/2 - 80, 50))
                hindring._fart_x = 0
                kylling._fart_y = 0
                self.spill_over = True
                
                # Trykk for restarte
                if hendelse.type == pygame.MOUSEBUTTONDOWN:
                    hindring.pos_x = 900
                    hindring.pos_y = 180
                    hindring._fart_x = 10
                    kylling._fart_y = 5
                    self.score = 0
                    self.spill_over = False
                    
                
            # Håndterer score
            if self.spill_over == False:
                self.score += 1
            score_setup = font.render(str(self.score), True, (255,255,255))
            skjerm.blit(score_setup, (bredde - 100, 20))

            hindring.bevege()
            hindring.opprett()
            kylling.oppdater()
            kylling.tegn()
            hindring.tegn()

            # oppdater skjerm
            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()