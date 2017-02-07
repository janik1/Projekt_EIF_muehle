import pygame, sys, random





# COLORS
#           R      G     B
WHITE   =   (255, 255, 255)
BLACK   =   (  0,   0,   0)
BROWN   =   (139,  69,  19)


class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(1, groesse - 1):
            self.felder[i][i] = 1

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1


def main():

    WINDOWWIDTH = 700
    WINDOWHEIGHT = 700
    CELLSIZE = 20
    FPS = 20

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Mühlestein')
    DISPLAYSURF.fill(BROWN)


    assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
    my_feld = Spiel(CELLWIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        pygame.display.update()

feld = [[[2, 1, 1], [1, 3, 1], [1, 1, 2]], \
          [[2, 2, 0], [1, 4, 1], [2, 2, 0]], \
          [[2, 1, 2], [2, 3, 1], [0, 1, 1]]]


print(feld)
schlagen = False


for i in range(2):
     for j in range(2):
         if (feld[0][i][j] == feld[1][i][j] == feld[2][i][j]) and (i == 1 or j == 1):
             schlagen = True
         elif feld[j][0][i] == feld[j][1][i] == feld[j][2][i]:
             schlagen = True
         elif feld[i][j][0] == feld[i][j][1] == feld[i][j][2]:
             schlagen = True

print(schlagen)
print(feld)
main()



