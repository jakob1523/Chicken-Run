import pygame
import random
from Kylling import Kylling
from hindring import Hindring

pygame.init()

# Pygame setup
bredde, hoyde = 900, 300
FPS = 60
skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption("Chicken Run")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Impact", 24)

# Spillobjekter
kylling = Kylling(50, 230, 30, 60, 0, 0.6)

# Hindringer
hindring1 = Hindring(900, 180, 30, 50, 10)
hindring2 = Hindring(900, 120, 40, 60, 10)
hindring3 = Hindring(900, 180, 50, 30, 10)
hindring4 = Hindring(900, 200, 80, 30, 10)
hindring5 = Hindring(900, 175, 30, 20, 15)


hindringer = [hindring1, hindring2, hindring3, hindring4, hindring5]
aktive_hindringer = []

# Variabler
teller = 0
fart_okning = 0
restart_tekst = font.render("Trykk R for restart", True, (255, 255, 255))

# Farger
Hvit = (255, 255, 255)
Rood = (255, 0, 0)

# Oppretter Spill klasse
class Spill:
    def __init__(self):
        self.aktiv = True
        self.score = 0
        self.spill_over = False
        self.dukker = False

    # Game loop metode
    def loop(self):
        global teller
        global fart_okning

        while self.aktiv:
            teller += 1

            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False

                # Controls
                # Trykker space for å hoppe
                if hendelse.type == pygame.KEYDOWN:
                    if hendelse.key == pygame.K_SPACE and not self.dukker:
                        kylling.hopp()
                    if hendelse.key == pygame.K_UP and not self.dukker:
                        kylling.hopp()

                # Trykker pil ned for å dukke
                    if hendelse.key == pygame.K_DOWN and not self.dukker:
                        kylling.size_y = 30
                        if not kylling.hopper:
                            kylling.pos_y = 200
                        kylling._gravity = 1.7
                        self.dukker = True
                    
                    # Trykker R for restart
                    if hendelse.key == pygame.K_r and self.spill_over:
                        aktive_hindringer.clear()
                        self.score = 0
                        fart_okning = 0
                        self.spill_over = False


                # Slipper pil ned for å stå
                if hendelse.type == pygame.KEYUP:
                    if hendelse.key == pygame.K_DOWN:
                        kylling.size_y = 60
                        if not kylling.hopper:
                            kylling.pos_y = 230
                        kylling._gravity = 0.6
                        self.dukker = False
                
            # Bakgrunn
            skjerm.fill((0, 0, 0))
            pygame.draw.rect(skjerm, (18, 181, 181), (0, 0, 900, 270))
            pygame.draw.rect(skjerm, (150, 75, 0), (0, 230, 900, 100))
            pygame.draw.rect(skjerm, (18, 207, 14), (0, 230, 900, 15))

            if teller % 300 == 0:
                fart_okning += 1

            # Ny hindring hvert sekund
            if teller % FPS == 0 and not self.spill_over:
                hindringen = random.choice(hindringer)
                ny_hindring = Hindring(
                    900,
                    hindringen.pos_y,
                    hindringen.size_x,
                    hindringen.size_y,
                    hindringen._fart_x
                )
                ny_hindring._fart_x += fart_okning
                aktive_hindringer.append(ny_hindring)

            # Håndterer hindringer
            for hindring in aktive_hindringer:
                hindring.tegn(Rood)
                if not self.spill_over:
                    hindring.bevege()

                if kylling.kollisjon(hindring):
                    self.spill_over = True
                    hindring._fart_x = 0

                # fjerner hindring fra listen når det går ut a skjermen
                if hindring.pos_x + hindring.size_x < 0:
                    aktive_hindringer.remove(hindring)

            # Håndterer Score
            if not self.spill_over and teller % 7 == 0:
                self.score += 1
                

            score_tekst = font.render(str(self.score), True, (255, 255, 255))
            skjerm.blit(score_tekst, (bredde - 100, 20))

            # Spill over
            if self.spill_over:
                skjerm.blit(restart_tekst, (bredde / 2 - 100, hoyde / 2 - 40))
                tap = font.render(f"Du fikk {self.score} score", True, (255, 255, 255))
                skjerm.blit(tap, (bredde / 2 - 90, 50))

            # Kylling
            kylling.oppdater()
            kylling.tegn(Hvit)

            pygame.display.flip()
            clock.tick(FPS)

# Kjører game loop
Spill().loop()
pygame.quit()
