console.log("Uploadseite wird geladen.");

//Wenn die Webseite neu/gerade geladen wurde, dann führe die Funktion aus 
//Brauche ich hier nicht, die Anzeigetexte etc. sowie das Aussehen stehen hier schon, muss nur den Button auswerten!
//document.addEventListener("DOMContentLoaded", () => {ladeUploadFormular()});

//document = komplette HTML-Seite // querySelector = Suche mir das erste HTML-Element mit der Klasse uploadButton
const uploadButton = document.querySelector(".uploadButton");

//Warte auf das Event "click" bein Upload und Get Button // <Eventtype>, <Funktion>
uploadButton.addEventListener("click", uploadTickets);

async function uploadTickets(){
    //Zum Testen
    console.log("Ticket hochgeladen gedrückt");

    //findet das HTML-Element mit id="importDatei" // Platz 1(bzw. 0) der Liste der gefundenen Dateien
    const datei = document.getElementById("importDatei").files[0];

    //Holt sich das Element Fehlermeldung und setzt den Anzeigetext
    const fehler = document.getElementById("fehlermeldung");
    if (!datei) {
        fehler.textContent = "Bitte wählen Sie eine Datei aus.";
        return;
    }
    // "===" ist der starke Vergleichsoperator (nur 5 = 5) und "==" ist der schwache Vergleichsoperator (hier ist auch 5 = "5" korrekt)
    if (datei.size === 0) {
        fehler.textContent = "Die Datei ist leer.";
        return;
    }

    //Erstellt ein neues Objekt (eingebautes Browser Objekt), was als "UploadFile" Datei an die API geschickt werden kann 
    //Fungiert als Transportbehälter für Dokumente und Dateien
    const formData = new FormData();

    //Lade/Lese und speichere den Inhalt der importDatei
    formData.append("importDatei", datei);

    //Benutzt den Upload Endpunkt und schickt die hochgeladene Datei
    const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
            method: "POST",
            body: formData
        }
    );

    //Einlesen der API Antwort
    const antwort = await response.json();

    console.log(antwort);
}