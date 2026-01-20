import pygame
pygame.init()
 
font = pygame.font.SysFont('Impact', 24)

bredde, hoyde = 1000, 300
hvit = (255, 255, 255)
FPS = 60

skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Chicken Run')
clock = pygame.time.Clock()

class Spill:
    def __init__(self):
        self.aktiv = True
    
    #spill løkken
    def loop(self):
        while self.aktiv == True:
            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False

        # Restarter sjermen hver gang løkken kjører
            skjerm.fill((0, 0, 0))

            # oppdater skjerm
            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()