# Implementation Binärer Suchbaum



class Abschluss:
    "Abschluss modelliert Blätter des Baumes"
    def __init__(self):
        "Konstruktor"
        pass                                # keine Attribute 
    
    def __repr__(self):
        return ""

    def einfügen(self, element, altKnot):
        "Blatt einfügen"
        if element < altKnot.element:       # falls neues Element kleiner...
            altKnot.lnach = Knoten(element)
        else:                               # falls neues Element größer ...
            altKnot.rnach = Knoten(element)
        return True
  
    def inOrder(self):                      
        "gibt Leerstring zurück"
        pass

    def preOrder(self):                     
        "gibt Leerstring zurück"
        pass

    def postOrder(self):                    
        "gibt Leerstring zurück"
        pass

    def suchen(self, vergleich):            
        "gibt Misserfolg zurück"
        pass

    def restKnotenZahl(self):
        "gibt Null zurück"
        pass

    def gibKleinstes(self, altKnot):
        "gibt kleinstes Element zurück"
        pass
    
    def löscheKleinstes(self, vorgänger, vorvorgänger):
        "löscht Knoten mit kleinstem Element und gibt dieses zurück"
        pass

    def gibGrößtes(self, altKnot):
        "gibt größtes Element zurück"
        pass

    def gibHöhe(self):
        "gibt Hoehe -1 zurück"
        return -1

    def gibTiefe(self,element):
        "gibt False für nicht enthaltenes Datenelement zurück"
        pass

    def grafik(self,schrittweite):
        "löscht den Ast (3 letzte turtle-Befehle) zu diesem Abschluss"
        pass



class Knoten:
    "Knoten und Blätter des Baums"
    def __init__(self, element, lnach=Abschluss(), rnach=Abschluss()):
        self.element = element
        self.lnach = lnach
        self.rnach = rnach
        
    def __repr__(self):
        return self.element                     # gib Element auf Konsole aus

    def gibGrößtes(self, altKnot):
        "kleinster Knoten im Teilbaum"
        pass

    def gibKleinstes(self, altKnot):
        "größter Knoten im Teilbaum"
        pass
        
    def löscheKleinstes(self, vorgänger, vorvorgänger):
        "löscht Knoten mit kleinstem Element und gibt dieses zurück"
        pass

    def einfügen(self, element, altKnot):
        "neues Element einfügen"
        if element == self.element:             # vergleiche mit eig. Element... 
            print("Element schon vorhanden!")
            return False
        if element < self.element:              # falls neues Element kleiner... 
            return self.lnach.einfügen(element, self) # ...dann rek. Aufruf links
        else:
            return self.rnach.einfügen(element, self) # ...dann rek. Aufruf rechts

    def inOrder(self):
        "Element sortiert in ZWISCHENORDNUNG ausgeben"
        pass

    def preOrder(self):
        """Elemente in VORORDNUNG als Zeichenkette mit Zeilenumbruch
        zur Serialisierung des Baumes für Dateiablage"""
        pass

    def postOrder(self):
        "Elemente in NACHORDNUNG ausgeben"
        pass

    def suchen(self, vergleich):
        "Suche nach Zeichenkette"
        pass
    
    def restKnotenZahl(self):
        "gibt Anzahl der Knoten zurück"
        pass

    def gibHöhe(self):
        "gibt größere Teilbaumhöhe zurück"
        pass
        
    def gibTiefe(self,element):
        "gibt Tiefe eines Knotens(elem) zurück"
        pass

    def grafik(self,schrittweite):
        "gibt Knoten als Turtle-Grafik in neuem Fenster aus"
        pass

class Baum:
    """Klasse implementiert binären Baum"""
    def __init__(self, element):
        "erzeuge Binärbaum mit Wurzelknoten"
        self.wurzel = Knoten(element)
        print("Neuer Baum erzeugt")

    def __repr__(self):
        pass
       
    def einfügen(self, element):
        "Einfügen eines Knotens"
        self.wurzel.einfügen(element, self)
               
    def inOrder(self):
        "liste alle Knoten in sortierter (Haupt-)Reihenfolge"
        pass

    def preOrder(self):
        "liste alle Knoten in symmetrischer Reihenfolge"
        pass

    def postOrder(self):
        "liste alle Knoten in Nebenreihenfolge"
        pass

    def suchen(self,vergleich):
        "Suche nach Zeichenkette"
        pass

    def knotenZahl(self):
        "gibt Anzahl der Knoten im Baum"
        pass

    def gibKleinstes(self):
        "gibt kleinstes Element zurück"
        pass

    def löscheKleinstes(self):
        "löscht Knoten mit kleinstem Element und gibt dieses zurück"
        pass

    def gibGrößtes(self):
        "gibt größtes Element zurück"
        pass

    def gibHöhe(self):
        "gibt Höhe des Baums zurück"
        return self.wurzel.gibHöhe()

    def gibTiefe(self,element):
        "gibt Tiefe eines Knotens aus"
        pass


    def grafik(self,farbe="black"):
        "Baum mittels Turtle-Grafik visualisieren"
        pass

    def speichern(self,filename = 'baum.txt'):  # speichere in Datei 'filename'
        "Baum in Datei  speichern"
        pass

    def laden(self, filename="baum.txt"):
        "Baum aus Datei laden"
        pass
    
    
if __name__=="__main__":
    b = Baum("Fritz")
    b.einfügen("Boeck")
    b.einfügen("Mecke")
    b.einfügen("Baecker")
    b.einfügen("Bolte")
    b.einfügen("Max")
    b.einfügen("Moritz")
    #b.grafik()
    #print("Inorder-Durchlauf:   ",b.inOrder())
    #print("Preorder-Durchlauf:  ",b.preOrder())
    #print("Postorder-Durchlauf:",b.postOrder())
    #b.speichern()
    #nb = b.laden()
    #print(nb.inOrder())
