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
def alleTicketsLaden():
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    print("Datenbank erstellt.")

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Gibt alle Datensätze aus der Datenbank zurück
    cursor.execute("SELECT * FROM tickets")
    datensaetze = cursor.fetchall()

    datenbank.close()

    #Gibt alle Datensätze aus der Datenbank zurück
    return datensaetze


#Löscht einen Datensatz
def ticketLoeschen(ticketID):
    datenbank = dbOpen()
    cursor = datenbank.cursor()

    #Gibt ggf. Fehler zurück
    dbFehlerFang(cursor)

    #Löscht den Datensatz mit der übergebenen ID
    cursor.execute(
        "DELETE FROM tickets WHERE idDatensatz = ?",
        (ticketID,)
    )
    
    datenbank.commit()
    print("Gelöschte ID:", ticketID)
    
    datenbank.close()