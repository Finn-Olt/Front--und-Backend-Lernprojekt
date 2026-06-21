from backend.datensatzStruktur import ImportDatensatz

#Enthält drei Objekte und pro Objekt ein Array mit Matching-Begriffen 
faecher = {
    "SDM": [
        "datenmodell",
        "json",
        "csv",
        "xml",
        "import",
        "mapping",
        "validierung",
        "datensatz",
        "struktur"
    ],

    "EvP": [
        "api",
        "rest",
        "endpoint",
        "anfrage",
        "antwort",
        "webhook",
        "workflow",
        "integration"
    ],

    "GiD": [
        "nutzer",
        "kunde",
        "dokumentation",
        "bedienung",
        "übergabe",
        "beschreibung",
        "verständlichkeit",
        "darstellung"
    ]
}


def matching(ticket: ImportDatensatz):
    #Das Fach ermitteln
    besteFaecher = matchingDo(ticket)
    
    for fach in besteFaecher:
        if len(ticket.fach) > 0:
            ticket.fach[0] = besteFaecher[0]
        else:
            ticket.fach.append(besteFaecher[0])

    return ticket


#Per KeyWord matching
def matchingDo(ticket: ImportDatensatz) -> list:
    #Beschreibung an Titel stringen und alle Buchstaben in Lower-Case wandeln 
    text = (ticket.titel + " " + ticket.beschreibung).lower()

    punkte = {}
    for fach, begriffe in faecher.items():
        i = 0
        for begriff in begriffe:
            #Wenn der Begriff des Faches im Text vorkommt, dann Punkte +1
            if begriff in text:
                i += 1
        #Punkte pro Fach speichern // Ist das gleiche wie "punkte["SDM"] = i", nur variabel
        punkte[fach] = i

    #Regeln:
    #1. Wenn kein Fach mehr als 0 Punkte hat, dann sowas wie "Keine Fachzuweisung möglich" zurückgeben
    #2. Wenn Fächer die gleiche Punktzahl haben, dann mehrere Fächer zurück geben?
    #3. Wenn genau ein Fach die meisten Punkte hat, dann das Fach zurück geben
    
    #max Funktion => Vergleicht die values der Punkte und gibt die höchste Punktezahl zurück
    maxPunkte = max(punkte.values())

    #Alle Fächer mit der höchsten Punktzahl sammeln
    besteFaecher = []
    
    #Regel 1 - Kein Fach hat mehr als 0 Punkte 
    if (maxPunkte == 0):
        besteFaecher[0] = "Keine Fachzuweisung möglich"
        return besteFaecher

    #Wenn es mindestens ein Fach mit mehr als 0 Punkten gibt
    for fach, punktzahl in punkte.items():
        if punktzahl == maxPunkte:
            besteFaecher.append(fach)

    return besteFaecher

"""
    #Regel 3 - Ein Fach hat die höhchste Punktzahl
    if len(besteFaecher) == 1:
        return besteFaecher[0]

    #Regel 2 - Mehere Fächer haben die höchste Punktzahl // durch "join" werden die Array Positionen mit einem Komma getrennt und zurück gegeben
    return ", ".join(besteFaecher)
       

    #max Funktion => Vergleicht die Punkte, benutzt dafür als key die Punkte und gibt das Fach mit den meisten Punkten zurück 
    #max(punkte, key=punkte.get)
"""