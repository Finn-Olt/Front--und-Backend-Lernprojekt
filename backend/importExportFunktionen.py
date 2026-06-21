import json
import csv
#import xml.etree.ElementTree as ET

from backend.datensatzStruktur import ImportDatensatz
from backend.database import *
from backend.fachZuweisung import matching

#JSON
def jsonRead(dateiname) -> list[ImportDatensatz]:
    #Schauen, von welchem Datentyp "dateiname" ist, MUSS "str, bytes or os.PathLike object" sein
    print(type(dateiname))
    
    with open(dateiname, "r", encoding="utf-8") as datei:
        datensatz = json.load(datei)
    
    tickets:list[ImportDatensatz] = jsonToTicket(datensatz, dateiname)
    #Wandelt den JSON Datensatz in ein "ticket" Datensatz um und gibt das Ticket als ImportDatensatz Objekt zurück
    return tickets

def jsonToTicket(datensatz: dict, dateiname: str) -> ImportDatensatz:
    return ImportDatensatz(
        id=datensatz["author"]["id"],
        quellDatei=dateiname,
        titel=datensatz["title"],
        beschreibung=datensatz["body"],
        prio="",
        status=datensatz["state"]
    )

#Schreiben von dem Ticket in die Datenbank
def jsonWriteInDatabase(dateiname):
    dbInit()
    ticket = jsonRead(dateiname)
    print(ticket)
    ticket = matching(ticket)
    ticketSpeichern(ticket)
    return ticket

#CSV
def csvRead(dateiname: str) -> list[ImportDatensatz]:
    #CSV hat meistens mehrere Datensätze, deshalb Liste zum Speichern der Datensätze
    tickets: list[ImportDatensatz]

    with open(dateiname, "r", encoding="utf-8") as datei:
        datensaetze = csv.DictReader(datei)

        for datensatz in datensaetze:
            #Wandelt den CSV Datensatz in ein ticket Datensatz um und speichert ihn in der Liste 
            tickets.append(csvToTicket(datensatz,dateiname))

    #Gibt die Liste zurück
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

#Schreiben der Tickets in die Datenbank
def csvWriteInDatabase(dateiname) -> list[ImportDatensatz]:
    dbInit()
    tickets = csvRead(dateiname)
    for ticket in tickets:
        print(ticket)
        ticket = matching(ticket)
        ticketSpeichern(ticket)
    return tickets


#XML
"""
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
"""
"""
def xmlWriteInDatabase(dateiname):
    dbInit()
    ticket = xmlRead(dateiname)
    print(ticket)
    ticket = matching(ticket)
    ticketSpeichern(ticket)
"""
