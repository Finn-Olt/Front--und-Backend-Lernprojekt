import sqlite3
from backend.datensatzStruktur import ImportDatensatz

#Erstellt die Datenbank, falls noch nicht vorhanden, sonst wird die Verbindung hergestellt
def dbOpen():
    datenbank = sqlite3.connect("tickets.db")
    return datenbank

def dbFehlerFang(cursor):
    try:
        cursor.execute("tickets")
    except Exception as e:
        print(e)


#Erstellt eine Tabelle
def dbInit():
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Durch das "IF NOT EXISTS" wird eine bereits vorhandene Tabelle nicht verändert
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        idDatensatz TEXT,
        quellDatei TEXT,
        titel TEXT,
        beschreibung TEXT,
        prio TEXT,
        status TEXT,
        fachrichtung TEXT
    )
    """)

    datenbank.commit()
    datenbank.close()


#Schreiben des Objekts in die Datenbank
def ticketSpeichern(ticket: ImportDatensatz):
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Erstellt einen Eintrag in der Datenbank
    cursor.execute("""
    INSERT INTO tickets (
        idDatensatz,
        quellDatei,
        titel,
        beschreibung,
        prio,
        status,
        fachrichtung
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket.id,
        ticket.quellDatei,
        ticket.titel,
        ticket.beschreibung,
        ticket.prio,
        ticket.status,
        ticket.fach
    ))

    #Änderungen speichern
    datenbank.commit()
    #print(ticket " Hinzugefügt")
    datenbank.close()

#Gesamte Datenbank ausgeben
def alleTicketsLaden() -> list[ImportDatensatz]:
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    print("Datenbank erstellt.")

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Gibt alle Datensätze aus der Datenbank zurück
    cursor.execute("SELECT * FROM tickets")
    datensaetze = cursor.fetchall()

    datenbank.close()

    tickets = []
    for datensatz in datensaetze:
        ticket = ImportDatensatz(
            id=datensatz[0],
            quellDatei=datensatz[1],
            titel=datensatz[2],
            beschreibung=datensatz[3],
            prio=datensatz[4],
            status=datensatz[5],
            fach=datensatz[6]
        )

        tickets.append(ticket)

    #Gibt alle Datensätze aus der Datenbank zurück
    return tickets

#Ticket mit genau der ID laden 
def einTicketLaden(idTicket: str) -> list[ImportDatensatz]:
    datenbank = dbOpen()
    cursor = datenbank.cursor() 

    print("Datenbank erstellt.")

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Gibt alle Datensätze aus der Datenbank zurück // ? ist der Platzhalter
    cursor.execute("SELECT * FROM tickets WHERE idDatensatz = ?",(idTicket,))
    datensaetze = cursor.fetchall()

    datenbank.close()

    tickets = []
    for datensatz in datensaetze:
        ticket = ImportDatensatz(
            id=datensatz[0],
            quellDatei=datensatz[1],
            titel=datensatz[2],
            beschreibung=datensatz[3],
            prio=datensatz[4],
            status=datensatz[5],
            fach=datensatz[6]
        )

        tickets.append(ticket)

    #Gibt alle Datensätze aus der Datenbank zurück, als Liste mit importDatensatz Objekten
    return tickets


#Alle Tickets löschen
def alleTicketsLoeschen():
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    #Löscht alle Einträge, aber Tabellenstruktur bleibt erhalten
    cursor.execute("DELETE FROM tickets")
    datenbank.commit()
    datenbank.close()


#Löscht einen Datensatz
def ticketLoeschen(ticketID) -> list[ImportDatensatz]:
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    cursor.execute("SELECT * FROM tickets WHERE idDatensatz = ?",(ticketID,))
    datensaetze = cursor.fetchall()

    #Löscht den Datensatz mit der übergebenen ID
    cursor.execute(
        "DELETE FROM tickets WHERE idDatensatz = ?",
        (ticketID,)
    )
    
    datenbank.commit()
    print("Gelöschte ID:", ticketID)
    
    datenbank.close()
    
    tickets = []
    for datensatz in datensaetze:
        ticket = ImportDatensatz(
            id=datensatz[0],
            quellDatei=datensatz[1],
            titel=datensatz[2],
            beschreibung=datensatz[3],
            prio=datensatz[4],
            status=datensatz[5],
            fach=datensatz[6]
        )

        tickets.append(ticket)
    
    
    return datensaetze