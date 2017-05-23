#Mühle
import pygame, sys

WHITE   =   (255, 255, 255)
BLACK   =   (  0,   0,   0)
BROWN   =   (191,  128,  64)

FENSTERHÖHE = 800
FENSTERBREITE = int(FENSTERHÖHE * 1.5)
radius = int(FENSTERHÖHE/30)
feld = [[[0, 0, 0], [0, 3, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 4, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 3, 0], [0, 0, 0]]]
anzahl_steine = [0, 0]  # Anzeige auf dem Bild (Am besten rechts/links vom Feld)
anzahl_geschlagene_steine = [0, 0]  # Anzeige auf dem Bild (Am besten rechts/links vom Feld)
event_koordinate_1 = [0, 0, 0]
event_koordinate_2 = [0, 0, 0]
mühle_koordinaten = []
neu_entfernen = False
runde = 0  # Anzeige auf dem Bild (Am besten oberhalb vom Feld)
schritt = 1
anzeigeschrift = 0
pygame.init()
pygame.font.init()

pygame.display.set_caption("Mühlestein")

ANZEIGE = pygame.display.set_mode((FENSTERBREITE, FENSTERHÖHE), 0, 32)

class Hintergrund(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def momentaner_spieler(runde):  # Anzeige auf dem Bild (Am besten oberhalb vom Feld)
    if runde % 2 == 0:
        return 2
    else:
        return 1

def setzen(koordinate2):
    if feld[koordinate2[0]][koordinate2[1]][koordinate2[2]] == 0:
        feld[koordinate2[0]][koordinate2[1]][koordinate2[2]] = momentaner_spieler(runde)
        anzahl_steine[momentaner_spieler(runde) - 1] += 1
    else:
        print("Fehler beim setzen")
        return False

def entfernen_durch_mühle(koordinate1):
    entfernen = False
    if feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] == momentaner_spieler(runde + 1):
        for i in range(len(mühle_koordinaten)):
            for j in range(3):
                if koordinate1 == mühle_koordinaten[i][j]:
                    entfernen = False
                    print("Stein aus Mühle darf nicht entfernt werden")
                    return entfernen
                else:
                    entfernen = True
        if len(mühle_koordinaten) == 0:
            entfernen = True
    if entfernen == True:
        feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] = 0
        anzahl_geschlagene_steine[momentaner_spieler(runde) - 1] += 1
        anzahl_steine[momentaner_spieler(runde) - 1] -= 1
        return True
    else:
        print("Fehler beim entfernen")
        return False

def entfernen_durch_verschieben(koordinate1):
    if feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] == momentaner_spieler(runde):
        feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] = 0
        anzahl_steine[momentaner_spieler(runde) - 1] -= 1
        return True
    else:
        print("Fehler beim entfernen")
        return False

def umplatzieren(koordinate1, koordinate2):
    entfernen_durch_verschieben(koordinate1)
    if setzen(koordinate2) == False:
        print("Fehler beim setzen")
        return False
    print("Verschoben")

def verschieben(koordinate1, koordinate2):
    if koordinate1[1] == koordinate2[1] and koordinate1[2] == koordinate2[2]:
        if ((koordinate1[0] == koordinate2[0] + 1) or (koordinate1[0] == koordinate2[0] - 1)) and (koordinate1[1] == 1 or koordinate1[2] == 1):
            if umplatzieren(koordinate1, koordinate2) == False:
                return False
        else:
            return False
            print("Fehler beim verschieben. Falscher Ort")
    if koordinate1[0] == koordinate2[0] and koordinate1[2] == koordinate2[2]:
        if (koordinate1[1] == koordinate2[1] + 1) or (koordinate1[1] == koordinate2[1] - 1):
            if umplatzieren(koordinate1, koordinate2) == False:
                return False
        else:
            return False
            print("Fehler beim verschieben. Falscher Ort")
    if koordinate1[0] == koordinate2[0] and koordinate1[1] == koordinate2[1]:
        if (koordinate1[2] == koordinate2[2] + 1) or (koordinate1[2] == koordinate2[2] - 1):
            if umplatzieren(koordinate1, koordinate2) == False:
                return False
        else:
            return False
            print("Fehler beim verschieben. Falscher Ort")

def nicht_mehr_mühle():
    for g in range(len(mühle_koordinaten)):
        if feld[mühle_koordinaten[g][0][0]][mühle_koordinaten[g][0][1]][mühle_koordinaten[g][0][2]] == \
            feld[mühle_koordinaten[g][1][0]][mühle_koordinaten[g][1][1]][mühle_koordinaten[g][1][2]] == \
            feld[mühle_koordinaten[g][2][0]][mühle_koordinaten[g][2][1]][mühle_koordinaten[g][2][2]]:
            pass
        else:
            mühle_koordinaten.pop(g)
            return mühle_koordinaten

def mühle():
    schlagen = False
    reihe = []
    for i in range(3):
        for j in range(3):
            if (feld[0][i][j] == feld[1][i][j] == feld[2][i][j] in [1, 2]) and (i == 1 or j == 1):
                reihe = [[0, i, j], [1, i, j], [2, i, j]]
                for g in range(len(mühle_koordinaten)):
                    if reihe == mühle_koordinaten[g]:
                        schlagen = False
                        break
                    else:
                        schlagen = True
                if schlagen == True or len(mühle_koordinaten) == 0:
                    mühle_koordinaten.append(reihe)
                    return True
            if feld[j][0][i] == feld[j][1][i] == feld[j][2][i] in [1, 2]:
                reihe = [[j, 0, i], [j, 1, i], [j, 2, i]]
                for g in range(len(mühle_koordinaten)):
                    if reihe == mühle_koordinaten[g]:
                        schlagen = False
                        break
                    else:
                        schlagen = True
                if schlagen == True or len(mühle_koordinaten) == 0:
                    mühle_koordinaten.append(reihe)
                    return True
            if feld[i][j][0] == feld[i][j][1] == feld[i][j][2] in [1, 2]:
                reihe = [[i, j, 0], [i, j, 1], [i, j, 2]]
                for g in range(len(mühle_koordinaten)):
                    if reihe == mühle_koordinaten[g]:
                        schlagen = False
                        break
                    else:
                        schlagen = True
                if schlagen == True or len(mühle_koordinaten) == 0:
                    mühle_koordinaten.append(reihe)
                    return True
    print("Mühle:", schlagen)
    print("Neue Mühlereihe", reihe, "Alte Mühlen:", mühle_koordinaten)
    return schlagen

def event_koordinate_bestimmen(pos_x, pos_y):
    event_koordinate = [1, 1, 1]
    for k in range (3):
        y = (k + 1) * int(FENSTERHÖHE / 8) + int(FENSTERHÖHE / 16)
        abstand = int(FENSTERHÖHE / 3) - k * int(FENSTERHÖHE / 8)
        y1 = y
        for j in range(3):
            x = (k + 1) * int(FENSTERHÖHE / 8) + int(FENSTERHÖHE / 4)
            x1 = x
            for i in range(3):
                if ((pos_y - y1) ** 2 + (pos_x - x1) ** 2) ** 0.5 <= radius:
                    event_koordinate[0] = k
                    event_koordinate[1] = j
                    event_koordinate[2] = i
                x = x + abstand
                x1 = x1 + abstand
            y = y + abstand
            y1 = y1 + abstand
    if event_koordinate == [1, 1, 1]:
        return False
    return event_koordinate

def menu():
    menu = True
    ANZEIGE.fill(WHITE)
    menuText = pygame.font.SysFont("Comic Sans MS", 50)
    erstes_Feld = menuText.render("Spiel starten", True, BLACK)
    zweites_Feld = menuText.render("Regeln", True, BLACK)
    drittes_Feld = menuText.render("Optionen", True, BLACK)


    def auswahl():

        x = int(FENSTERBREITE/3)
        y = int(FENSTERHÖHE/6)
        width = int(FENSTERBREITE/3)
        heigh = int(FENSTERHÖHE/6)
        Feld_x = x + int(width / 4)
        mitte_Feld_y = y + int(heigh/3)

        for i in range (3):
            pygame.draw.rect(ANZEIGE, BLACK, (x, y, width ,heigh), 1)
            y += int(FENSTERHÖHE/5)

        ANZEIGE.blit(erstes_Feld, (Feld_x, mitte_Feld_y))
        ANZEIGE.blit(zweites_Feld, (Feld_x, (mitte_Feld_y + int(FENSTERHÖHE/5))))
        ANZEIGE.blit(drittes_Feld, (Feld_x, (mitte_Feld_y +int(FENSTERHÖHE/2.5))))

    def menuklick(pos_x, pos_y):
        x = int(FENSTERBREITE / 3)
        y = int(FENSTERHÖHE / 6)
        width = int(FENSTERBREITE / 3)
        heigh = int(FENSTERHÖHE / 6)
        for i in range(3):
            y = y + i*(int(FENSTERHÖHE / 5))

            if pos_x >= x and  pos_x <= (x + width) and pos_y >= y and pos_y <= (y + heigh):
                return i

    while menu:
        auswahl()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if menuklick(pos_x, pos_y) == 0:
                    return
                if menuklick(pos_x, pos_y) == 1:
                    regeln()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def regeln():

    HinterGrund = Hintergrund("/home/janik/Bilder/muehle_regeln", [0, 0])
    ANZEIGE.blit(HinterGrund.image, HinterGrund.rect)
    regeln = True

    while regeln:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("return")
                    ANZEIGE.fill(WHITE)
                    return

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def fenster():
    pygame.init()
    pygame.font.init()
    menu()
    def anzeige():
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        ANZEIGE.fill(BROWN)
        momentane_runde = myfont.render("Runde:" + str(runde), True, BLACK)
        spieler_weiss = myfont.render("Weiss:" + str(anzahl_steine[0]), True, BLACK)
        spieler_schwarz = myfont.render("Schwarz:" + str(anzahl_steine[1]), True, BLACK)
        ANZEIGE.blit(momentane_runde, (int(FENSTERBREITE / 2.5), int(FENSTERHÖHE / 30)))
        ANZEIGE.blit(spieler_weiss, (int(FENSTERBREITE / 10), int(FENSTERHÖHE /5 )))
        ANZEIGE.blit(spieler_schwarz, (int(FENSTERBREITE / 10*8), int(FENSTERHÖHE / 6)))

        global anzeigeschrift
        if anzeigeschrift == 0:
            aktueller_Spieler = myfont.render("Willkommen bei Mühle. Spieler Weiss beginnt mit setzen", True, BLACK)
            #Pause und dann 2ten Teil einblenden
        elif anzeigeschrift == 1:
            if momentaner_spieler(runde) == 1:
                aktueller_Spieler = myfont.render("Bitte Stein von Schwarz entfernen", True, BLACK)
            elif momentaner_spieler(runde) == 2:
                aktueller_Spieler = myfont.render("Bitte Stein von Weiss entfernen", True, BLACK)
        elif anzeigeschrift == 2:
            if momentaner_spieler(runde) == 1:
                aktueller_Spieler = myfont.render("Schwarz bitte Stein setzen", True, BLACK)
            elif momentaner_spieler(runde) == 2:
                aktueller_Spieler = myfont.render("Weiss bitte Stein setzen", True, BLACK)
        elif anzeigeschrift == 3:
            if momentaner_spieler(runde) == 1:
                aktueller_Spieler = myfont.render("Schwarz bitte Stein verschieben", True, BLACK)
            elif momentaner_spieler(runde) == 2:
                aktueller_Spieler = myfont.render("Weiss bitte Stein verschieben", True, BLACK)
        elif anzeigeschrift == 4:
            if momentaner_spieler(runde) == 1:
                aktueller_Spieler = myfont.render("Schwarz bitte Stein umplatzieren", True, BLACK)
            elif momentaner_spieler(runde) == 2:
                aktueller_Spieler = myfont.render("Weiss bitte Stein umplatzieren", True, BLACK)
        else:
            aktueller_Spieler = myfont.render("Error 404", True, BLACK)

        ANZEIGE.blit(aktueller_Spieler, (int(FENSTERBREITE/3), int(FENSTERHÖHE/11)))

    def brett():
        for k in range(3):
            y = (k + 1) * int(FENSTERHÖHE / 8) + int(FENSTERHÖHE / 16)
            abstand = int(FENSTERHÖHE / 3) - k * int(FENSTERHÖHE / 8)
            for j in range(3):
                x = (k + 1) * int(FENSTERHÖHE / 8) + int(FENSTERHÖHE / 4)
                if j == 0:
                    pygame.draw.rect(ANZEIGE, BLACK, (x, y, abstand * 2, abstand * 2), 1)
                for i in range(3):
                    if (k == 0 and j == 0 and i == 1) or (k == 2 and j == 0 and i == 1):
                        x_start1 = x
                        y_start1 = y
                    if (k == 0 and j == 1 and i == 0) or (k == 2 and j == 1 and i == 0):
                        x_start2 = x
                        y_start2 = y
                    if k == 0 and j == 2 and i == 1:
                        pygame.draw.line(ANZEIGE, BLACK, (x_start1 , y_start1 + radius), (x, y))
                    if k == 0 and j == 1 and i == 2:
                        pygame.draw.line(ANZEIGE, BLACK, (x_start2 + radius, y_start2), (x, y))
                    if k == 2 and j == 2 and i == 1:
                        pygame.draw.line(ANZEIGE, BROWN, (x_start1 , y_start1 + radius), (x, y))
                    if k == 2 and j == 1 and i == 2:
                        pygame.draw.line(ANZEIGE, BROWN, (x_start2 + radius, y_start2), (x, y))

                    if feld[k][j][i] == 0:
                        pygame.draw.circle(ANZEIGE, BROWN, (x, y), radius, 0)
                        pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 1)
                    if feld[k][j][i] == 1:
                        pygame.draw.circle(ANZEIGE, WHITE, (x, y), radius, 0)
                    if feld[k][j][i] == 2:
                        pygame.draw.circle(ANZEIGE, BLACK, (x, y), radius, 0)

                    x = x + abstand
                y = y + abstand

    while True:
        anzeige()
        brett()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                global runde
                global neu_entfernen
                global schritt
                global anzeigeschrift
                if mühle() or neu_entfernen == True:
                    anzeigeschrift = 1
                    pos_x, pos_y = pygame.mouse.get_pos()
                    if event_koordinate_bestimmen(pos_x, pos_y) == False:
                        neu_entfernen = True
                        continue
                    event_koordinate_1 = event_koordinate_bestimmen(pos_x, pos_y)
                    print("Eventkoordinate 1", event_koordinate_1)
                    if entfernen_durch_mühle(event_koordinate_1) == False:
                        neu_entfernen = True
                        continue
                    neu_entfernen = False
                    print("--------Mühle--------")
                    print("Geschlagene Steine", anzahl_geschlagene_steine)
                    print("@Spieler:", momentaner_spieler(runde + 1), "Bitte Stein setzen")
                    if runde < 17:
                        anzeigeschrift = 2
                    else:
                        anzeigeschrift = 3
                elif (anzahl_steine[0] < 3 or anzahl_steine[1] < 3) and runde > 18:
                    print("Spiel vorbei. Spieler", momentaner_spieler(runde), "hat gewonnen.")
                    pygame.quit()
                    sys.exit()

                else:
                    if runde < 18:
                        anzeigeschrift = 2
                        runde += 1
                        print("Spieler:", momentaner_spieler(runde), "Runde:", runde)
                        pos_x, pos_y = pygame.mouse.get_pos()
                        if event_koordinate_bestimmen(pos_x, pos_y) == False:
                            runde -= 1
                            continue
                        event_koordinate_2 = event_koordinate_bestimmen(pos_x, pos_y)
                        print("Eventkoordinate 2:", event_koordinate_2)
                        if setzen(event_koordinate_2) == False:
                            runde -= 1
                            continue
                        print("Anzahl Steine:", anzahl_steine)
                        print("--------setzen--------")
                        if mühle():
                            anzeigeschrift = 1
                            mühle_koordinaten.pop()
                            print("Mühle, bitte Stein von Spieler", momentaner_spieler(runde + 1), "entfernen")
                            print("-------setzen_Mühle---------")

                    elif anzahl_steine[momentaner_spieler(runde) - 1] > 3 and runde >= 18 and schritt == 1:
                        anzeigeschrift = 3
                        runde += 1
                        print("(Verschieben 1)Spieler:", momentaner_spieler(runde), "Runde:", runde)
                        pos_x, pos_y = pygame.mouse.get_pos()
                        if event_koordinate_bestimmen(pos_x, pos_y) == False:
                            runde -= 1
                            continue
                        event_koordinate_1 = event_koordinate_bestimmen(pos_x, pos_y)
                        print("Eventkoordinate 1", event_koordinate_1)
                        if entfernen_durch_verschieben(event_koordinate_1) == False:
                            runde -= 1
                            continue
                        else:
                            setzen(event_koordinate_1)
                            schritt = 2
                    elif anzahl_steine[momentaner_spieler(runde - 1) - 1] > 3 and runde >= 18 and schritt == 2:
                        print("(Verschieben 2)Spieler:", momentaner_spieler(runde), "Runde:", runde)
                        pos_x, pos_y = pygame.mouse.get_pos()
                        if event_koordinate_bestimmen(pos_x, pos_y) == False:
                            continue
                        event_koordinate_2 = event_koordinate_bestimmen(pos_x, pos_y)
                        print("Eventkoordinate 2", event_koordinate_2)
                        if verschieben(event_koordinate_1, event_koordinate_2) == False:
                            setzen(event_koordinate_1)
                            schritt = 2
                            print("Neu setzen")
                            continue
                        else:
                            nicht_mehr_mühle()
                            print("Verschoben....")
                            print("Anzahl Steine", anzahl_steine)
                            print("-------Verschieben von Spieler", momentaner_spieler(runde + 1), "---------")
                            schritt = 1

                    elif anzahl_steine[momentaner_spieler(runde) - 1] == 3 and runde > 18 and schritt == 1:
                        anzeigeschrift = 4
                        runde += 1
                        print("(Umplatzieren 1)Spieler:", momentaner_spieler(runde), "Runde:", runde)
                        pos_x, pos_y = pygame.mouse.get_pos()
                        event_koordinate_1 = event_koordinate_bestimmen(pos_x, pos_y)
                        print("Eventkoordinate 1", event_koordinate_1)
                        if entfernen_durch_verschieben(event_koordinate_1) == False:
                            runde -= 1
                            continue
                        else:
                            setzen(event_koordinate_1)
                            schritt = 2
                    elif anzahl_steine[momentaner_spieler(runde - 1) - 1] == 3 and runde >= 18 and schritt == 2:
                        print("(Umplatzieren 2)Spieler:", momentaner_spieler(runde), "Runde:", runde)
                        pos_x, pos_y = pygame.mouse.get_pos()
                        event_koordinate_2 = event_koordinate_bestimmen(pos_x, pos_y)
                        print("Eventkoordinate 2", event_koordinate_2)
                        if umplatzieren(event_koordinate_1, event_koordinate_2) == False:
                            setzen(event_koordinate_1)
                            schritt = 2
                            print("Neu setzen")
                            continue
                        else:
                            nicht_mehr_mühle()
                            print("Verschoben....")
                            print("Anzahl Steine", anzahl_steine)
                            print("-------Verschieben von Spieler", momentaner_spieler(runde + 1), "---------")
                            schritt = 1

            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

fenster()




