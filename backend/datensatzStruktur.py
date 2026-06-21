from dataclasses import dataclass, field

#Hat den Vorteil, Objekt kann leicht in ein Dictionary umwandelt werden => das kann FastAPI direkt als z.B. JSON zurückgeben
@dataclass
class ImportDatensatz:
    id: str
    quellDatei: str
    titel: str
    beschreibung: str
    prio: str
    status: str
    #String Array // immer wenn ein neues Objekt erstellt wird, wird automatisch eine leere Liste erstellt
    fach: list[str] = field(default_factory=list)

    #Erlaubt zwei Inhalte, einen String oder NONE => Macht die Inhaltszuweisung optional
    #fach: list | None = None #Nachteil: Wenn der Wert auch NONE sein kann, muss ich das später immer beachten




#Es gibt keine richtigen "Kommentarblöcke", das hier bewirkt: ein unzugewiesener String wird in Python vom Interpreter ignoriert
"""
#Normale Python Klasse
class ImportDatensatz:
    #Init des Objekts, wird automatisch ausgeführt beim erzeugen eines neuen Objekts
    def __init__(
        self,
        id,
        quellDatei,
        titel,
        beschreibung,
        prio,
        status,
        fach=None
    ):
        self.id = id
        self.quellDatei = quellDatei
        self.titel = titel
        self.beschreibung = beschreibung
        self.prio = prio
        self.status = status
        self.fach = fach


    #Wie die Rückgabe/Ausgabe eines Objektes ist
    def __str__(self):
        return (
            f"Ticket-ID: {self.id}\n"
            f"Titel: {self.titel}\n"
            f"Beschreibung: {self.beschreibung}\n"
            f"Status: {self.status}\n"
            f"Priorität: {self.prio}\n"
            f"Quelldatei: {self.quellDatei}"
        )
"""