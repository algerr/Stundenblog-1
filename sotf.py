import random
import gc
import pygame


class Wesen(object):
    # Die Genomgröße bestimmt die Größe des Erbguts. Je höher diese liegt, desto schwieriger ist die Berechnung, aber es kommt eine "intelligentere" Spezies dabei raus
    # Mbp = Megabasenpaare (Gegenüberliegende Nukleobasen (G,T,C,A)), der Mensch hat 3200 Mbp (Genomgröße = 3200)
    # Pneumokokken haben 2,2 Mbp, kommen unserem Modell also sehr nahe
    # Genomgröße 6 bedeutet, dass 6x Gene vorhanden sind.
    # Also 6x [x_gen[0][1], y_gen[0][1], z_gen]
    def __init__(self, GenomGröße):
        # Jedes Wesen hat eine Liste an Genen, in der x_Gen, y_Gen und z_Gen gespeichert sind
        # Sozusagen das Erbgut
        self.Gene = []
        Temp = GenomGröße
        while Temp > 0:
            # Wenn die aktuelle Generation die erste ist oder es keine Überlebenden der vorigen Generation gibt
            if Generation[0] <= 1 or len(Überlebende) == 0:
                self.Gene.append(
                    gene([random.randrange(2),
                          random.randrange(2)],
                         [random.randrange(8),
                          random.randrange(8)], random.randrange(9)))
            Temp -= 1
        # Die Position wird zufällig bestimmt
        self.pos = [random.randrange(Größe[0]), random.randrange(Größe[1])]


# Für das Handling jedes einzelnen Gens wird dieses Objekt initiiert
class gene(object):

    def __init__(self, x_gen, y_gen, z_gen):
        # Das Wesen hat 3 verschiedene Genarten
        # x_gen, y_gen, z_gen
        self.x_gen = x_gen
        self.y_gen = y_gen
        self.z_gen = z_gen
        # Bei einer Chance von 1 zu 50 mutiert das Gen
        
        if random.randrange(50) == 0:
            self.mutation()

    def mutation(self):
        # Hierbei lassen sich die Werte, also die Wahrscheinlichkeiten für verschiedene Mutationen beliebig ändern
        MutationsWert = random.randrange(16)
        if MutationsWert < 2:
            # Entweder Höhe oder Breite werden zufällig mit 0 oder 1 belegt
            self.x_gen[MutationsWert] = random.randrange(2)
        elif MutationsWert >= 2 and MutationsWert < 5:
            # Die
            self.y_gen[0] = random.randrange(8)
        # Die Verbindung wird zu einem anderen Wesen hergestellt
        elif MutationsWert >= 5 and MutationsWert < 8:
            self.y_gen[1] = random.randrange(8)
        # Mit einer Wahrscheinlichkeit von 50% verändert sich die connectionStrength zu einem Wert zwischen -8 und 8
        else:
            self.z_gen = random.randrange(17) - 8


def generieren():
    Temp = GesamtAnzahl
    # Es wird sichergestellt, dass sich mehr als 0 Wesen in der Simulation befinden
    while Temp > 0:
        WesenListe.append(Wesen(GenomGröße))
        Temp -= 1


def renderFenster(Fenster):
    # Grauer Hintergrund
    Fenster.fill((50, 50, 50))
    # Das Simulationsfenster wird gerendert
    # Damit es an die Fenstergröße angepasst ist, wird es 8x so groß gemacht
    # pygame.draw.rect(fenster, (r,g,b), (x,y))
    pygame.draw.rect(Fenster, (0, 0, 0),
                     (29, 29, Größe[0] * 8 + 1, Größe[1] * 8 + 1))
    for x, zielpunkt_der_safezone in enumerate(Safezone):
        # Die Safezone wird gerendert
        # Die Größe ist an die des gesamten Fensters angepasst
        pygame.draw.rect(Fenster, (0, 100, 0),
                         (30 + zielpunkt_der_safezone[0] * 8,
                          30 + zielpunkt_der_safezone[1] * 8, 7, 7))

    # Hiermit wird der Schweif hinter dem Wesen gezeichnet
    # i markiert den Index der jeweiligen Position in der Liste der gespeicherten Positionen und generation den Wert (also die Positionsdaten)
    for i, generation in enumerate(PositionsListe):
        # Nun wird durch die Positionsdaten (also generation) iteriert und das Ganze in "altePosition" gespeichert
        for j, altePosition in enumerate(generation):
            # Je nachdem, welchen Index die Position hat, wird sie dunkler/heller gefärbt
            # Der erste gespeicherte Wert (die älteste Position) wird mit i=0 gezeichnet
            # Also (5 + 0*10)
            # Somit ist der RGB Wert ((5+0*10),(5+0*10),(5+0*10)) also (5,5,5)
            # Je neuer der gespeicherte, alte Wert ist, also, je näher er an der aktuellen Position liegt,
            # desto heller wird er.
            # Somit wird der jüngste gespeicherte Wert (nach dem aktuellen) mit i = 7 gezeichnet
            # Also ist der RGB Wert ((5+7*10),(5+7*10),(5+7*10)) also (75,75,75), welcher definitiv heller ist als (5,5,5)
            # Die altePosition wird mit dem Faktor 8 und dem Summanden 30 an die Größe des Fensters angepasst
            # Und anschließend wird jede altePosition in ihrer Farbe gezeichnet
            pygame.draw.rect(
                Fenster, (5 + i * 10, 5 + i * 10, 5 + i * 10),
                (30 + altePosition[0] * 8, 30 + altePosition[1] * 8, 7, 7))
    # Die Bewegung der Wesen wird hiermit visualisiert
    LoopCount = 7
    # Jede Position des Wesens wird an PositionsListe[0] gespeichert.
    # Jedes Mal, wenn eine neue Position dazukommt, wird dieser Wert um einen Index nach hinten "geschoben"
    # Die Liste kann 8 Elemente beinhalten, deshalb ist der LoopCount bei 7, da bei 0 angefangen wird, zu zählen.
    # (7,6,5,4,3,2,1,0)
    while LoopCount > 0:
        PositionsListe[7 - LoopCount] = PositionsListe[8 - LoopCount]
        LoopCount -= 1
    # Anschließend wird die Position an letzter Stelle gelöscht, sodass Platz für eine neue vorhanden ist
    PositionsListe[7] = []
    for i, Wesen in enumerate(WesenListe):
        # Die Standardfarbe ist grau
        farbe = [125, 125, 125]
        FunktionellesGenom = 0
        # Für jedes x_gen[1], das den Wert 1 hat, wird das Genom als funktionell deklariert.
        # Das bedeutet, dass funktionelle Wesen eine hellere Farbe haben
        for j, gene in enumerate(Wesen.Gene):
            if gene.x_gen[1] == 1:
                FunktionellesGenom += 1
        for j, gene in enumerate(Wesen.Gene):
            if gene.x_gen[1] == 1 and gene.y_gen[1] == 0:
                farbe[0] += min(
                    254 - farbe[0],
                    int(40 + abs(gene.z_gen * 60)) * 2 / FunktionellesGenom)
            if gene.x_gen[1] == 1 and gene.y_gen[1] == 1:
                farbe[0] -= min(
                    farbe[0],
                    int(40 + abs(gene.z_gen * 60)) * 2 / FunktionellesGenom)
            if gene.x_gen[1] == 1 and gene.y_gen[1] == 2:
                farbe[1] += min(
                    254 - farbe[1],
                    int(40 + abs(gene.z_gen * 60)) * 2 / FunktionellesGenom)
            if gene.x_gen[1] == 1 and gene.y_gen[1] == 3:
                farbe[1] -= min(
                    farbe[1],
                    int(40 + abs(gene.z_gen * 60)) * 2 / FunktionellesGenom)
            if gene.x_gen[1] == 1 and gene.y_gen[1] == 4:
                farbe[2] += max(
                    -farbe[2],
                    min(254 - farbe[2],
                        (80 + gene.z_gen * 60) / FunktionellesGenom))
        #print(farbe[0])
        #print(farbe[1])
        #print(farbe[2])
        # Alle Wesen werden gezeichnet                                         (Passende x und y Position im Fenster),     passende Breite und Höhe
        pygame.draw.rect(Fenster,
                         (int(farbe[0]), int(farbe[1]), int(farbe[2])),
                         (30 + Wesen.pos[0] * 8, 30 + Wesen.pos[1] * 8, 7, 7))
        # Die Positionen der Wesen werden gespeichert
        PositionsListe[7].append([Wesen.pos[0], Wesen.pos[1]])
    # Die Schriftart (keine Besondere) und Größe werden festgelegt
    generationDisplay = pygame.font.Font(None, 30)
    # Es soll Generation: (Generationsnummer) in Orange geschrieben werden.
    # Das True bezieht sich auf Antialiasing. Damit werden unerwünschte Pixel, die durch das Pixelraster entstehen, vermindert.
    # Der Text ist geglättet und nicht verpixelt
    generationsRendering = generationDisplay.render(
        "Generation:" + str(Generation[0]), True, (255, 120, 0))
    # Der Text wird oben rechts über dem Simulationsfenster geschrieben
    Fenster.blit(
        generationsRendering,
        generationsRendering.get_rect(center=(Größe[0] * 8 + 59 - 90, 20)))
    # Das Ganze wird geupdatet
    pygame.display.update()


def simulationsExitÜberprüfung():
    global WesenListe, Überlebende
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Wenn die Generation durch ist
    if Generation[1] < 0:
        # Die nicht mehr genutzten Objekte werden durch den Garbage Collecter gelöscht, sodass das Ganze flüssiger läuft.
        gc.collect()
        # Erhöht sich die Generationsnummer um 1
        Generation[0] += 1
        # Die Ablaufenden Ticks werden wieder auf 200 gesetzt
        Generation[1] = Generation[2]
        # Eine neue Liste mit den überlebenden Wesen, die es in die Safezone geschafft haben, wird definiert
        Überlebende = []
        for i, creature in enumerate(WesenListe):
            for x, Safespot in enumerate(Safezone):
                # Bei jedem Wesen wird geprüft, ob die Koordinaten mit denen der Safezone übereinstimmen
                if creature.pos[0] == Safespot[0] and creature.pos[
                        1] == Safespot[1]:
                    # Wenn das Ganze zutrifft, wird ein neues Wesen erschaffen
                    neuesWesen = Wesen(0)
                    for j, genom in enumerate(creature.Gene):
                        # Und die Gene des überlebenden Wesen werden diesem zugeschrieben
                        neuesWesen.Gene.append(
                            gene([genom.x_gen[0], genom.x_gen[1]],
                                 [genom.y_gen[0], genom.y_gen[1]],
                                 genom.z_gen))
                    # Somit lässt sich eine Liste der Überlebenden mitsamt ihren Genen erstellen
                    Überlebende.append(neuesWesen)
        # Die Liste der Wesen wird nach jeder Generation geleert
        WesenListe = []
        # Die Anzahl der Wesen in Überlebende (den Überlebenden) wird ausgegeben
        print('SurvivalCount:' + str(len(Überlebende)))
        Temp = GesamtAnzahl
        # Für jedes der Wesen (in unserem Beispiel 200)
        while Temp > 0:
            # Wird ein Wesen aus der Liste der Überlebenden ausgewählt
            ChosenCreature = Überlebende[random.randrange(len(Überlebende))]
            neuesWesen = Wesen(0)
            for j, genom in enumerate(ChosenCreature.Gene):
                # Und gibt seine Erbinformation (Bewegung, Farbe, etc.) an ein anderes Wesen weiter
                # Starke/gute Gene werden weitergegeben
                neuesWesen.Gene.append(
                    gene([genom.x_gen[0], genom.x_gen[1]],
                         [genom.y_gen[0], genom.y_gen[1]], genom.z_gen))
            # Das neue Wesen wird zur Liste der Wesen hinzugefügt
            WesenListe.append(neuesWesen)
            # Das Ganze geht so lange, bis durch alle Wesen durch iteriert wurde
            Temp -= 1
    # Hiermit lässt sich ein "Survival of the fittest" nach Charles Darwin simulieren


# Mit dieser Funktion wird überprüft, ob die Position aller Wesen im Bereich des Fensters (zwischen 0 und 100) liegt
def überprüfeValidität(x, y):
    if x >= 0 and y >= 0 and x < Größe[0] and y < Größe[1]:
        for i, Wesen in enumerate(WesenListe):
            if Wesen.pos[0] == x and Wesen.pos[1] == y:
                return False
        return True


def simulationStart():
    # Voraussetzung wird gegeben, dass die Simulation mehr als 0 Ticks haben soll. (Dass sie läuft)
    if Generation[1] >= 0:
        for i, Wesen in enumerate(WesenListe):
            stabilerWert = [[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            for j, genom in enumerate(Wesen.Gene):
                #print(Wesen.Gene)
                # Wenn der x_gen bei 0 liegt (es gibt entweder 0 oder 1 (Bitflip))
                if genom.x_gen[0] == 0:
                    # Die Veränderung wird in einer Variable, der Veränderung, ausgedrückt, der hier anfangs mit 0 definiert wird
                    Veränderung = 0
                    # Nun ist die Frage, was für Gene das Wesen hat, je nachdem wird die Veränderung anders
                    if genom.y_gen[0] == 0:
                        # Die Höhe des Wesens wird der Veränderung hinzugefügt
                        Veränderung += Wesen.pos[1] * genom.z_gen / Größe[1] * 8
                    elif genom.y_gen[0] == 1:
                        # Die Breite des Wesens wird der Veränderung hinzugefügt
                        Veränderung += Wesen.pos[0] * genom.z_gen / Größe[0] * 8
                    elif genom.y_gen[0] == 2:
                        # Der aktuelle Zeitwert wird der Veränderung hinzugefügt
                        Veränderung += Generation[
                            1] * genom.z_gen / Generation[2] * 2
                    elif genom.y_gen[0] == 3:
                        # Das Factum, dass sich das Wesen in der Safezone befindet wird als Wert des halben z_gens der Veränderung hinzugefügt
                        for x, zielpunkt_der_safezone in enumerate(Safezone):
                            if Wesen.pos[0] == zielpunkt_der_safezone[
                                    0] and Wesen.pos[
                                        1] == zielpunkt_der_safezone[1]:
                                Veränderung += genom.z_gen / 2
                    elif genom.y_gen[0] == 4:
                        # Ein zufälliger Wert wird der Veränderung hinzugefügt
                        Veränderung += (random.randrange(9) -
                                        4) * genom.z_gen / 8
                    elif genom.y_gen[0] == 5:
                        Veränderung += (random.randrange(9) -
                                        5) * genom.z_gen / 8
                    elif genom.y_gen[0] == 6:
                        #print('Noch nicht implementiert')
                        pass

                    # Der veränderliche Wert wird im stabilen Wert gespeichert [[0,0,0,0],[0,0,0,0,0,0,0,0]]
                    # Das x_Gen entscheidet ob in der 4er oder 8er Liste und daraufhin entscheidet auch das y_Gen über die Stelle, an der der Wert gespeichert wird
                    stabilerWert[genom.x_gen[1]][int(
                        genom.y_gen[1] / (2 - genom.x_gen[1]))] += Veränderung
                    #print(stabilerWert)
            for j, genom in enumerate(Wesen.Gene):
                if genom.x_gen[0] == 1:
                    if genom.y_gen[0] == 0 or genom.y_gen[0] == 1:
                        # Der eingetragene Wert wird positiv
                        stabilerWert[genom.x_gen[1]][int(
                            genom.y_gen[1] / (2 - genom.x_gen[1]))] += abs(
                                stabilerWert[0][0]) * genom.z_gen / 8
                    elif genom.y_gen[0] == 4 or genom.y_gen[0] == 5:
                        wesenAnzahl = 0
                        for x, wesen in enumerate(Wesen.Gene):
                            if wesen.x_gen[1] == 0 and (wesen.y_gen[1] == 4 or
                                                        wesen.y_gen[1] == 5):
                                wesenAnzahl += 1
                        stabilerWert[genom.x_gen[1]][int(
                            genom.y_gen[1] / (2 - genom.x_gen[1])
                        )] += stabilerWert[0][2] * genom.z_gen / max(
                            1, wesenAnzahl) * 8
                    elif genom.y_gen[0] == 4 or genom.y_gen[0] == 5:
                        # Eine zufällige Zahl wird hinzugefügt
                        stabilerWert[genom.x_gen[1]][int(
                            genom.y_gen[1] /
                            (2 - genom.x_gen[1]))] += (stabilerWert[0][3] +
                                                       random.randrange(3) -
                                                       1) * genom.z_gen / 8
                        #print(stabilerWert)

            # Diese Liste wird genutzt, um eine zufällige Bewegung zu ermöglichen
            ZufälligeBewegungen = []

            # Durch die Liste wird iteriert und, wenn der Wert erreicht wird,
            for a, Ausführung in enumerate(stabilerWert[1]):
                # Wird dieser, mit einer zufälligen Zahl von 0 bis 39 multipliziert, der Liste angehängt
                ZufälligeBewegungen.append(Ausführung * random.randrange(40))
                #print(ZufälligeBewegungen)

            for s, Aktion in enumerate(ZufälligeBewegungen):
                # Der Wert muss größer als 0 sein
                #print(s)
                #print(Aktion)
                if Aktion > 0 and Aktion == max(
                        ZufälligeBewegungen[0], ZufälligeBewegungen[1],
                        ZufälligeBewegungen[2], ZufälligeBewegungen[3],
                        ZufälligeBewegungen[4], ZufälligeBewegungen[5],
                        ZufälligeBewegungen[6], ZufälligeBewegungen[7]):

                    # Nun kann die zufällige Bewegung erfolgen.
                    # An der Stelle in der Liste ZufälligeBewegungen, an der der Wert angehängt wurde, markiert s den Index [s=0,s=1,s=2,s=3,s=4,...]
                    # Je nachdem, welchen Wert s hat, bewegt sich das Wesen nach oben, unten, links, rechts oder einfach zufällig
                    # Das ist ein wenig wie beim russisch Roulette (man geht so oft das Magazin des Revolvers durch, bis schließlich die Patrone erreicht ist)

                    # Überprüfung, dass x - 1 immernoch im Bereich des Fensters liegt
                    if s == 0 and überprüfeValidität(Wesen.pos[0] - 1,
                                                     Wesen.pos[1]):
                        # Bewegung nach links (um einen Schritt) (x - 1)
                        Wesen.pos[0] -= 1
                    # Überprüfung, dass x + 1 immernoch im Bereich des Fensters liegt
                    elif s == 1 and überprüfeValidität(Wesen.pos[0] + 1,
                                                       Wesen.pos[1]):
                        # Bewegung nach rechts (um einen Schritt) (x + 1)
                        Wesen.pos[0] += 1
                    # Überprüfung, dass y - 1 immernoch im Bereich des Fensters liegt
                    elif s == 2 and überprüfeValidität(Wesen.pos[0],
                                                       Wesen.pos[1] - 1):
                        # Bewegung nach oben (um einen Schritt) (y - 1)
                        Wesen.pos[1] -= 1
                    # Überprüfung, dass y + 1 immernoch im Bereich des Fensters liegt
                    elif s == 3 and überprüfeValidität(Wesen.pos[0],
                                                       Wesen.pos[1] + 1):
                        # Bewegung nach unten (um einen Schritt) (y + 1)
                        Wesen.pos[1] += 1
                    elif s == 4:  #move random
                        # Zufällige Bewegung
                        #      [random x Wert (-1,0,1) , random y Wert (-1,0,1) ]
                        Temp = [
                            random.randrange(3) - 1,
                            random.randrange(3) - 1
                        ]
                        # Überprüfung, dass die Summe aus der aktuellen Position und dem Zufallswert im Simulationsfenster liegen
                        if überprüfeValidität(Wesen.pos[0] + Temp[0],
                                              Wesen.pos[1] + Temp[1]):
                            # Zu der aktuellen x und y Postion wird der jeweilige Zufallswert addiert
                            Wesen.pos[0] += Temp[0]
                            Wesen.pos[1] += Temp[1]

                    # Noch implementierbar
                    #elif s == 5:
                    #    print('Noch nicht implementiert')
                    #    pass
                    #elif s == 6:
                    #    print('Noch nicht implementiert')
                    #    pass
                    #elif s == 7:
                    #    print('Noch nicht implementiert')
                    #    pass

        # Nach jedem Tick wird der anfängliche Wert von 200 um einen verringert
        # Deswegen dauert das Ganze auch mit beispielsweise höherer Genomgröße länger
        Generation[1] -= 1


def main():
    # Definierung der Parametern als Global, sodass jedes Objekt und jede Funktion darauf zugreifen können
    global WesenListe, Generation, Größe, GenomGröße, PositionsListe, Safezone, Überlebende, GesamtAnzahl
    pygame.init()
    # Hier werden alle Wesen drin gespeichert
    WesenListe = []
    # Von jedem Wesen werden 8 Positionen gespeichert, sodass die Bewegung nachverfolgbar ist
    PositionsListe = [[], [], [], [], [], [], [], []]
    # Alle Überlebenden werden darin gespeichert
    Überlebende = []
    # [Aktuelle Generation, Ablaufende Ticks, Reset-Wert für die ablaufenden Ticks]
    # Eine Generation dauert 200 Ticks, es sei denn, die Wesen bewegen sich vorher nicht mehr.
    # Danach werden die ablaufenden Ticks (Generation[1]) wieder auf 200 gesetzt und das Ganze beginnt von Neuem
    Generation = [1, 200, 200]
    # Größe des Simulationsbereichs
    Größe = [100, 100]
    # Anzahl der Wesen
    GesamtAnzahl = 200
    # Beinhaltet alle Pixel, die die Safezone markieren
    Safezone = []
    SafezoneX = Größe[0] - 1
    while SafezoneX >= 0:
        SafezoneY = Größe[1] - 1
        while SafezoneY >= 0:
            # Über die Intervalle für X und Y lässt sich die Safezone bestimmen
            # Es wird von 100 bis 0 iteriert und, wenn sich SafezoneX/SafezoneY im Safezone-Bereich befinden, werden diese der Safezone Liste angehänt
            if SafezoneX >= 0 and SafezoneX <= 30 and SafezoneY >= 0 and SafezoneY <= 30:
                # Die Safezone Pixel werden festgehalten
                Safezone.append([SafezoneX, SafezoneY])
            SafezoneY -= 1
        SafezoneX -= 1
        #print(SafezoneX)
        #print(SafezoneY)
    # Die Gräße (Komplexität in der Berechnung) des Erbguts wird festgelegt. Je gräßer, desto komplizierter der Organismus (Beispiel: Bakterium = 1
    #                                                                                                                                 Mensch = 1000)
    GenomGröße = 10

    # Mit den definierten Parametern werden die Wesen generiert
    generieren()

    # Die Fenstergröße wird festgelegt (Der Faktor 8 und der Summand 59 fungiert wieder als Anpassung an die Größe des Pygame Fensters)
    Fenster = pygame.display.set_mode((Größe[0] * 8 + 59, Größe[1] * 8 + 59))

    # Fenstertitel: 'Survival of the fittest - Wer ist am besten angepasst ?' wird festgelegt
    pygame.display.set_caption(
        'Survival of the fittest - Wer ist am besten angepasst ?')

    # Während das Programm läuft, gibt es nach jeder Generation eine 5ms Pause.
    # Daraufhin wird das Fenster gerendert, überprüft, ob die Simulation überhaupt noch läuft und dann die main-Funktion ausgeführt
    while True:
        pygame.time.delay(5)
        renderFenster(Fenster)
        simulationsExitÜberprüfung()
        simulationStart()
    pass


if __name__ == "__main__":
    main()
