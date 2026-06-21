import json
import csv
import xml.etree.ElementTree as ET

from backend.datensatzStruktur import ImportDatensatz
from backend.database import *
from backend.fachZuweisung import matching

def jsonRead(dateiname):
    #Schauen, von welchem Datentyp "dateiname" ist, MUSS "str, bytes or os.PathLike object" sein
    print(type(dateiname))
    
    with open(dateiname, "r", encoding="utf-8") as datei:
        datensatz = json.load(datei)
        
    #Wandelt den JSON Datensatz in ein "ticket" Datensatz um und gibt das Ticket als ImportDatensatz Objekt zurück
    return jsonToTicket(datensatz, dateiname)


#Da ich die @dataclass benutze, hier besser auch typitisieren
#Funktion erwartet einen "datensatz" von Typ Dictionary und einen "datennamen" von Typ String
#Rückgabetyp-Annotation => Funktion gibt ein Objekt vom Typ "ImportDatensatz" zurück
def jsonToTicket(datensatz: dict, dateiname: str) -> ImportDatensatz:
    return ImportDatensatz(
        id=datensatz["author"]["id"],
        quellDatei=dateiname,
        titel=datensatz["title"],
        beschreibung=datensatz["body"],
        prio="",
        status=datensatz["state"]
    )

"""
#Mapping, da die Dateien unterschiedlich aufgebaut sind // Python Objekt befüllen
def jsonToTicket(datensatz, dateiname):
    return ImportDatensatz(
        id=datensatz["author"]["id"],
        quellDatei=dateiname,
        titel=datensatz["title"],
        beschreibung=datensatz["body"],
        prio="",
        status=datensatz["state"],
    )       
"""

def csvRead(dateiname):
    #CSV hat meistens mehrere Datensätze, deshalb Array zum Speichern der Datensätze
    tickets = []
    
    #Schauen, von welchem Datentyp "dateiname" ist, MUSS "str, bytes or os.PathLike object" sein
    print(type(dateiname))

    with open(dateiname, "r", encoding="utf-8") as datei:
        datensaetze = csv.DictReader(datei)

        for datensatz in datensaetze:
            #ticket = csvToTicket(datensatz)
            #Wandelt den CSV Datensatz in ein ticket Datensatz um und speichert ihn im tickets Array 
            tickets.append(csvToTicket(datensatz,dateiname))

    #Gibt das Array zurück
    return tickets

#Für das Mapping von CSV zu allg. Datensatz
def csvToTicket(datensatz: dict, dateiname: str) -> ImportDatensatz:
    return ImportDatensatz(
        id=datensatz["id"],
        quellDatei=dateiname,
        titel=datensatz["titel"],
        beschreibung=datensatz["beschreibung"],
        prio=datensatz["prio"],
        status=datensatz["status"],
    )


def xmlRead(dateiname):
    #Schauen, von welchem Datentyp "dateiname" ist, MUSS "str, bytes or os.PathLike object" sein
    print(type(dateiname))
    
    baum = ET.parse(dateiname)
    wurzel = baum.getroot()

    ticket = ImportDatensatz(
        wurzel.find("id").text,
        wurzel.find("quellDatei").text,
        wurzel.find("titel").text,
        wurzel.find("beschreibung").text
    )

    return ticket


#Schreiben von dem Ticket in die Datenbank
def jsonWriteInDatabase(dateiname):
    dbInit()
    ticket = jsonRead(dateiname)
    print(ticket)
    ticket = matching(ticket)
    ticketSpeichern(ticket)
    return ticket

    
#Schreiben der Tickets in die Datenbank
def csvWriteInDatabase(dateiname):
    dbInit()
    tickets = csvRead(dateiname)
    for ticket in tickets:
        print(ticket)
        ticket = matching(ticket)
        ticketSpeichern(ticket)
    return tickets


def xmlWriteInDatabase(dateiname):
    dbInit()
    ticket = xmlRead(dateiname)
    print(ticket)
    ticket = matching(ticket)
    ticketSpeichern(ticket)
