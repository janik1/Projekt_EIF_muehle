runde = 1  #Wird bei der GUI-Berechnung jeweils addiert
feld = [[[0, 0, 0], [0, 3, 0], [0, 0, 0]], \
         [[0, 0, 0], [0, 4, 0], [0, 0, 0]], \
         [[0, 0, 0], [0, 3, 0], [0, 0, 0]]]
anzahl_steine = [9, 9]
event_koordinate_1 = [0, 0, 0]  #Diese Koordinaten werden durch die Interaktionen des Spieler auf dem GUI erstellt
event_koordinate_2 = [0, 0, 0]

def momentaner_spieler(runde):
    if runde % 2 == 0:
        return 2
    else:
        return 1

def setzen(koordinate2):
    feld[koordinate2[0]][koordinate2[1]][koordinate2[2]] = momentaner_spieler(runde)
    anzahl_steine[momentaner_spieler(runde) - 1] += 1
    return feld

def entfernen(koordinate1):
    feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] = 0
    anzahl_steine[momentaner_spieler(runde) - 1] -= 1
    return feld

def umplatzieren(koordinate1, koordinate2):
    if feld[koordinate1[0]][koordinate1[1]][koordinate1[2]] == momentaner_spieler(runde) and feld[koordinate2[0]][koordinate2[1]][koordinate2[2]] == 0:
        entfernen(koordinate1)
        setzen(koordinate2)
        print("Verschoben")
    else:
        print("Fehler")

def verschieben(koordinate1, koordinate2):
    if koordinate1[1] == koordinate2[1] and koordinate1[2] == koordinate2[2]:
        if ((koordinate1[0] == koordinate2[0] + 1) or (koordinate1[0] == koordinate2[0] - 1)) and (koordinate1[1] == 1 or koordinate1[2] == 1):
            umplatzieren(koordinate1, koordinate2)
        else:
            print("Fehler")
    if koordinate1[0] == koordinate2[0] and koordinate1[2] == koordinate2[2]:
        if (koordinate1[1] == koordinate2[1] + 1) or (koordinate1[1] == koordinate2[1] - 1):
            umplatzieren(koordinate1, koordinate2)
        else:
            print("Fehler")
    if koordinate1[0] == koordinate2[0] and koordinate1[1] == koordinate2[1]:
        if (koordinate1[2] == koordinate2[2] + 1) or (koordinate1[2] == koordinate2[2] - 1):
            umplatzieren(koordinate1, koordinate2)
        else:
            print("Fehler")

def mühle():
    schlagen = False
    for i in range(3):
        for j in range(3):
            if (feld[0][i][j] == feld[1][i][j] == feld[2][i][j]) and (i == 1 or j == 1):
                schlagen = True
            elif feld[j][0][i] == feld[j][1][i] == feld[j][2][i]:
                schlagen = True
            elif feld[i][j][0] == feld[i][j][1] == feld[i][j][2]:
                schlagen = True
    return schlagen