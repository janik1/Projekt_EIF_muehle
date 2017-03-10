

import pygame, sys


# COLORS
#           R      G     B
WHITE   =   (255, 255, 255)
BLACK   =   (  0,   0,   0)
BROWN   =   (191,  128,  64)

FENSTERBREITE = 800
FENSTERHÖHE = FENSTERBREITE

feld = [[[2, 2, 1], [1, 3, 1], [1, 1, 2]], \
          [[2, 2, 0], [1, 4, 1], [2, 2, 0]], \
          [[2, 1, 2], [2, 3, 1], [0, 1, 1]]]
event_koordinate_1 = [0, 0, 0]
radius = 20
runde = 1


def fenster():

    pygame.init()

    ANZEIGE = pygame.display.set_mode((FENSTERBREITE, FENSTERHÖHE), 0, 32)
    pygame.display.set_caption("Mühlestein")
    ANZEIGE.fill(BROWN)


    def brett(x, y, abstand):

        for j in range (3):
            x = 100

            for i in range(3):
                if feld[0] [j] [i] == 0:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 1)
                if feld[0][j][i] == 1:
                    pygame.draw.circle(ANZEIGE, WHITE, (x, y), radius, 0)
                if feld[0][j][i] == 2:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 0)
                x = x + abstand
            y = y + abstand
        abstand = 200

        y = 200
        for j in range (3):
            x = 200
            for i in range(3):
                if feld[1] [j] [i] == 0:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 1)
                if feld[1] [j] [i] == 1:
                    pygame.draw.circle(ANZEIGE, WHITE, (x, y), radius, 0)
                if feld[1] [j] [i] == 2:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 0)
                x = x + abstand
            y = y + abstand

        abstand = 100
        x = 300
        y = 300
        for j in range (3):
            x = 300
            for i in range(3):
                if feld[2] [j] [i] == 0:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 1)
                if feld[2] [j] [i] == 1:
                    pygame.draw.circle(ANZEIGE, WHITE, (x, y), radius, 0)
                if feld[2] [j] [i] == 2:
                    pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 0)
                x = x + abstand
            y = y + abstand
        print(x, y)
        pygame.draw.circle(ANZEIGE, BROWN, (400, 400), 20, 1)

    brett(100, 100, 300)



    while True:
        for event in pygame.event.get():
            abstand = 300
            y = 100
            y1 = y
            for j in range(3):
                pos_x, pos_y = pygame.mouse.get_pos()
                x = 100
                x1 = x
                for i in range(3):
                    if ((pos_y - y1) ** 2 + (pos_x - x1) ** 2) ** 0.5 <= 20:
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos_x, pos_y = pygame.mouse.get_pos()
                            event_koordinate_1[0] = 0
                            event_koordinate_1[1] = j
                            event_koordinate_1[2] = i
                            print(event_koordinate_1)
                    x = x + abstand
                    x1 = x1 + abstand
                y = y + abstand
                y1 = y1 + abstand

            abstand = 200
            y = 200
            y1 = y
            for j in range(3):
                pos_x, pos_y = pygame.mouse.get_pos()
                x = 200
                x1 = x
                for i in range(3):
                    if ((pos_y - y1) ** 2 + (pos_x - x1) ** 2) ** 0.5 <= 20:
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos_x, pos_y = pygame.mouse.get_pos()
                            event_koordinate_1[0] = 1
                            event_koordinate_1[1] = j
                            event_koordinate_1[2] = i
                            print(event_koordinate_1)
                    x = x + abstand
                    x1 = x1 + abstand
                y = y + abstand
                y1 = y1 + abstand

            abstand = 100
            y = 300
            y1 = y
            for j in range(3):
                pos_x, pos_y = pygame.mouse.get_pos()
                x = 300
                x1 = x
                for i in range(3):
                    if ((pos_y - y1) ** 2 + (pos_x - x1) ** 2) ** 0.5 <= 20:
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos_x, pos_y = pygame.mouse.get_pos()
                            event_koordinate_1[0] = 2
                            event_koordinate_1[1] = j
                            event_koordinate_1[2] = i
                            print(event_koordinate_1)
                    x = x + abstand
                    x1 = x1 + abstand
                y = y + abstand
                y1 = y1 + abstand

            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                print(pos_x,pos_y)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()

fenster()

