from backend.importExportFunktionen import jsonRead, csvRead, xmlRead, jsonWriteInDatabase, csvWriteInDatabase, xmlWriteInDatabase
from backend.database import alleTicketsLaden, ticketLoeschen, einTicketLaden, alleTicketsLoeschen
from backend.datensatzStruktur import ImportDatensatz
from pathlib import Path
from dataclasses import asdict
from fastapi import FastAPI, UploadFile, File, HTTPException, Request


#todo die Verbindung wird nicht Zugelassen UND was sind CORS?
#Wenn ich einen Server für die Webseite (HTML) benutze, werde ich das sehr wahrscheinlich nicht mehr brauchen!
""" Sollte die Verbindung nicht zugelassen werden, aufgrund der unterschiedlichen Ursprünge (Vom lokalen Datenträger und API IP)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    #Welche Webseite darf die API über JavaScript aufrufen
    allow_origins=[
        "http://127.0.0.1:5500"
    ],
    #Welche HTTP-Methoden erlaubt sind
    allow_methods=["*"],
    #Welche HTTP-Header erlaubt sind
    allow_headers=["*"],
)
"""

app = FastAPI()

#Für post (Hochladen) // Bedeutet "Die Funktion darunter soll aufgerufen werden, wenn jemand eine POST-Anfrage an /process schickt."
@app.post("/upload")
async def upload(request: Request, importDatei: UploadFile = File(...)):
    #Wenn die IP nicht die local-host IP ist, wird der Zugriff verweigert
    if request.client.host != "127.0.0.1":
        raise HTTPException(status_code=403, detail="Zugriff verweigert")

    dateiInhalt = await importDatei.read()

    #Importverzeichnis erstellen, dann checks durchführen und die Importdatei in das Importverzeichnis schreiben
    dateiPfadUndName, dateiname = importVerzeichnisErstellen(importDatei)
    importDateiCheckUndDateiKopieren(dateiInhalt, dateiname, dateiPfadUndName)
    
    dateiTyp = dateiname.split(".")[-1].lower()
    tickets = writeFile(str(dateiPfadUndName), dateiTyp)
    
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )   
    return {"status": "saved", "ticket": [asdict(ticket) for ticket in tickets]}


#Für DELETE
@app.delete("/delete/{story_id}")
async def deleteTicket(story_id: str):
    tickets = ticketLoeschen(story_id)
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )
    return {"status": "deleted", "ticketID": story_id}

@app.delete("/delete")
async def deleteAllTickets(importDatei: UploadFile = File(...)):
    alleTicketsLoeschen()
    return {"status": "Es wurden alle Einträge der Datenbank gelöscht."}


#Für GET
@app.get("/readtickets/{ticket_id}")
async def readTicket(ticket_id: str):
    tickets: list[ImportDatensatz] = einTicketLaden(ticket_id)
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )
    return {"status": "read", "ticket": [asdict(ticket) for ticket in tickets]}

@app.get("/readtickets")
async def readTickets():
    tickets: list[ImportDatensatz] = alleTicketsLaden()
    return {"status": "read", "tickets": [asdict(ticket) for ticket in tickets]}





#Hilfsfunktionen
#Erstellt "imports" Ordner im Projektverzeichnis und gibt Dateinamen und Pfad zurück
def importVerzeichnisErstellen(importDatei):
    speicherPfad = Path("imports")
    speicherPfad.mkdir(exist_ok=True)

    dateiname = Path(importDatei.filename).name
    dateiPfadUndName = speicherPfad / dateiname
    
    return dateiPfadUndName, dateiname

#Checks + schreiben der importieren Datei
def importDateiCheckUndDateiKopieren(dateiInhalt, dateiname, dateiPfadUndName):
    #Dateityp kontrollieren
    if not dateiname.endswith((".csv", ".json", ".xml", ".CSV", ".JSON", ".XML")):
        raise HTTPException(status_code=400, detail="Ungültiger Dateityp")

    #Dateigröße Checken
    maxDateiGroesse = 5 * 1024 * 1024
    if len(dateiInhalt) > maxDateiGroesse:
        raise HTTPException(status_code=401, detail="Importdatei zu groß")

    with open(dateiPfadUndName, "wb") as f:
        f.write(dateiInhalt)

#Liest die Importdatei, verarbeitet den Inhalt und schreibt ihn in die Datenbank, 
#anschließend wird das Objekt, bzw. die Objekte zurück gegeben
def writeFile(dateiname, dateiTyp) -> list[ImportDatensatz]:
    match dateiTyp:
        case "json":
            return jsonWriteInDatabase(dateiname)

        case "csv":
            return csvWriteInDatabase(dateiname)

        #case "xml":
        #   return xmlWriteInDatabase(dateiname)
        

def readFile(dateityp, dateiName):
    match dateityp:
        case "json":
            return jsonRead(dateiName)

        case "csv":
            return csvRead(dateiName)

        #case "xml":
        #    return xmlRead(dateiName)






""" Brauche ich nicht, per Doppelklick auf die HTML Datei öffnet sich die Webseite und über den JS Code werden die Endpunkte ausgeführt
#FastAPI muss den static Ordner kennen, um die Designs, etc. laden/benutzen zu können
from fastapi.staticfiles import StaticFiles
#FastAPI-Komponente, die Dateien direkt an den Browser ausliefern kann
from fastapi.templating import Jinja2Templates

#Damit der Browser die Dateien laden kann // Alles, was im Browser mit /static angefragt wird, soll aus dem Ordner static geladen werden
app.mount("/static", StaticFiles(directory="static"), name="static")
#FastAPI HTML-Dateien aus dem Ordner templates laden
templates = Jinja2Templates(directory="templates")

#Startseite
@app.get("/")
async def startseite(request: Request):
    #Zum Testen, wenn ich Status OK sehe, ist der Fehler bei Jinja2 oder templates/index.html
    #return {"status": "ok"}
    
    #Lade die Datei index.html // Übergib Daten an die HTML-Seite
    return templates.TemplateResponse({"request": request}, "index.html")
"""
"""
#import sys => sys.exit()

def main():
    #Hier muss die Datei ankommen => Name muss in "dateiname" gespeichert werden
    #0. API-Anbindung
   
    #TODO wieder ausbauen! NUR ZUM TESTEN !
    modus = "show"
    dateiname = "issue.csv"
   
   #Check, ob die hochgeladene Datei wirklich eine CSV oder JSON Datei ist 
    if not dateiname.endswith((".csv", ".json")):
        raise Exception("Ungültiger Dateityp")
    
    #Die maximale Dateigröße setzen // Prüfung einbauen?
    MAX_SIZE = 5 * 1024 * 1024  # 5 MB
    content = await importDatei.read()
    if len(content) > MAX_SIZE:
        return {"error": "Datei zu groß"}
    
    
    print(dateiname)
    print(modus)

    
    #1. Check welcher Modus
    match modus:
        case "dele":
            #"if dateiname" <=> "if dateiname is not none:"
            if dateiname:
                #Namen und Typ splitten
                print("Geht in dele rein.")
                dateiTyp = dateiname.split(".")[-1].lower()
                if dateiTyp:
                    tickets = readFile(dateiTyp, dateiname)
                    for ticket in tickets:
                        ticketID = ticket.id
                        ticketLoeschen(ticketID)
            
        case "save":
            if dateiname:
                #Namen und Typ splitten
                dateiTyp = dateiname.split(".")[-1].lower()
                if dateiTyp:
                    print("Typ korrekt, Geht in save rein.")
                    writeFile(dateiname, dateiTyp)
    
        case "show":
            print("Geht in show rein.")
            datensaetze = alleTicketsLaden()
            for datensatz in datensaetze:
                print(datensatz)
            #Datensätze an die Webseite zurück geben
            #Dafür eine JSON Datei mit allen Datensätzen schreiben?
    
    #Beendet das Programm
    sys.exit()

#Hierdurch startet das Programm über die main() Funktion
if __name__ == "__main__":
    main()
"""









#from fastapi import FastAPI, UploadFile
#app = FastAPI()

#@app.post("/upload")
#async def upload_datei(datei: UploadFile):
 #   inhalt = await datei.read()
  #  print(datei.filename)
   # return {"Datei erhalten": datei.filename}
   
   
"""
Extrem wichtig für Python-Projekte:
1. CMD mit Pfad des Projekts öffnen/dahin welchseln 
2. "py -m venv venv" => erstellt eine "virtuelles Environment (venv)" 
3. Danach in der CMD zum aktivieren der "venv": venv\Scripts\activate in der CMD 
    ->mit "deactivate" in dem CMD macht man die "venv" wieder aus

Riesen Vorteil:
-So kann ich z.B. FastAPI NUR für dieses eine Projekt installieren, anstatt global
-Kriege keine Versionsprobleme mit anderen Projekten
-Ist der professionelle Standard

Dazu gut: "pip freeze > requirements.txt"
-Alle installierten Pakete/Software wird mit Version gespeichert (z.B. für dieses Projekt: "fastapi==0.136.3")
-Um alles auf einem neuen PC zu installieren/einzurichten, benutzt man: "pip install -r requirements.txt"

------------------------------------------------------------------------

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "API läuft"}


uvicorn main:app --reload in der CMD
Dann im Browser:
http://127.0.0.1:8000

Und Doku automatisch:
http://127.0.0.1:8000/docs


from fastapi import FastAPI, UploadFile, File
app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()

    return {
        "filename": file.filename,
        "size": len(content)
    }

Wenn die main direkt im Projektverzeichnis liegt 
uvicorn main:app --host 127.0.0.1 --port 8000, in der CMD

Wenn die main in einem Unterverzeichnis liegt
uvicorn backend.main:app --host 127.0.0.1 --port 8000, in der CMD

------------------------------------------------------------------------

Front-End und Back-End
    -Front-End  = Weboberfläche (HTML, CSS und JavaScript(Für Funktionen der Webseite/Aktualisieren der Webseite etc.))
    -Back-End   = API Endpunkte, Python Code(für die Verarbeitung, Speicherung in der Datenbank, etc.)

Was ist eine Webseite?
    -Die Webseite ist das HTML Dokument, dort ist auch die zu benutzende CSS und JavaScript Datei hinterlegt (Name + Pfad)

Was ist die API?
    -FastAPI Endpunkte, die im JS Code per z.B. "fetch" ausgeführt werden können

Was passiert, wenn der Webserver nicht gestartet wird?
    -Die fetch-Funktionen im JS Code werden keine korrekten Werte liefern, da die Endpunkte nicht aufgerufen werden können

Wie öffne ich eine Webseite?
    -Ich doppelklicke auf das HTML Dokument, dann wird die Webseite geöffnet



Frontend-Webserver
Wechsle in den Frontend-Ordner:
    -cd frontend //Wichtig, das muss im "Routverzeichnis" sein und ALLE benötigten Dateien müssen auf der Ebene oder in Unterordnern sein
                 //Sonst wird das mit dem Zugriff schwer/problematisch
                 
Dann starte einen einfachen Python-Webserver:
    -py -m http.server 5500 --bind 127.0.0.1  //Ohne das Bind kann der Webserver sehr wahrscheinlich auch von anderen Geräten im Netz gefunden werden

Jetzt ist deine Webseite erreichbar unter:
    -http://127.0.0.1:5500

""" 

