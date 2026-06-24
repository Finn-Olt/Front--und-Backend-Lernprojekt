# Readme nicht ganz komplett und ACHTUNG, der JS-Code ist noch nicht fertig, so wird der Code also nicht über den Webserver/ die Webseite lauffähig sein.
## TODOs: 
1. JS Code (Dynamische Belegung der HTML Objekte, damit sich die Seite verändert und der Inhalt von der API auf der Webseite angezeigt werden kann + Löschen Funktion)
2. CSS (Ich muss die ganzen Seiten noch schön designen)

# README

## Installation

1. Nachdem Sie alle Projektdateien heruntergeladen haben, erstellen Sie bitte einen Ordner, in den Sie das gesamte Projekt kopieren.

2. Erstellen Sie anschließend eine virtuelle Python-Umgebung (VENV), indem Sie folgenden Befehl in der Eingabeaufforderung (CMD) ausführen:

   `py -m venv venv`

3. Aktivieren Sie anschließend die VENV in der Eingabeaufforderung mit folgendem Befehl:

   `venv\Scripts\activate`

4. Nachdem die VENV erstellt und aktiviert wurde, installieren Sie alle benötigten Bibliotheken mit folgendem Befehl:

   `pip install -r requirements.txt`

5. Danach können Sie den API-Server starten. Beispiel:

   `uvicorn main:app --host 127.0.0.1 --port 8000`

6. Danach den Webserver starten. Besispiel: (Über den Webserver werden die Dateien im Verzeichnis an den Browser geliefert)

   `py -m http.server 5500 --bind 127.0.0.1`

7. Öffnen Sie einen Browser und geben Sie die Adresse ein, mit der Sie den Webserver gestartet haben. In diesem Beispiel:

   `http://127.0.0.1:5500`

8. Nun können Sie über die Weboberfäche testen.

---

## Module erklärt

### main.py

Enthält die API-Endpunkte sowie Hilfsfunktionen, die die Funktionen der anderen Module aufrufen und die Kommunikation zwischen API und Anwendungslogik steuern.

### database.py

Enthält alle Funktionen zur Arbeit mit der Datenbank. Dazu gehören das Erstellen und Öffnen der Datenbank, das Schreiben und Auslesen von Datensätzen sowie das Löschen von Einträgen.

### datensatzStruktur.py

Enthält die Dataclass-Definition, die als gemeinsame Datenstruktur innerhalb der verschiedenen Module verwendet wird.

### fachZuweisung.py

Dieses Modul führt ein Matching zwischen Schlüsselwörtern der einzelnen Schulfächer und den Textinhalten der importierten Dateien durch. Das ermittelte Fach wird anschließend dem Datensatz hinzugefügt. Falls mehrere Fächer die gleiche Übereinstimmungsanzahl besitzen, können auch mehrere Fachrichtungen zugeordnet werden.

### importExportFunktionen.py

Dieses Modul übernimmt die Verarbeitung der Upload-Dateien. Dazu gehört das Einlesen der Importdateien, die Aufbereitung der Daten für die weitere Verarbeitung sowie das Anstoßen weiterer Funktionen, beispielsweise zum Speichern der Daten in der Datenbank.

# TODO HTML, CSS und JS Module hier noch erklären
