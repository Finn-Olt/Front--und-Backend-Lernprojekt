console.log("Hallo Welt");

//document = komplette HTML-Seite // querySelector = Suche mir das erste HTML-Element mit der Klasse uploadButton
const uploadButton = document.querySelector(".uploadButton");
const getButton = document.querySelector(".getButton");

//Warte auf das Event "click" bein Upload und Get Button // <Eventtype>, <Funktion>
uploadButton.addEventListener("click", uploadTickets);
getButton.addEventListener("click", ladeTickets);


//JS soll nicht einfrieren, deshalb async, außerdem für "await"
async function ladeTickets() {
    //Zum Testen
    console.log("Tickets laden angeklickt");
    
    //Fehlerhandling
    try {
        //Holt sich über den Endpunkt alle Tickets, die in Form von einer JSON Datei zurück geliefert werden 
        const response = await fetch("http://127.0.0.1:8000/get-tickets");
        //
        if (!response.ok) { 
            throw new Error("Serverfehler");
        }
        //Einlesen der zurückerhaltenen JSON
        const tickets = await response.json();

        console.log(tickets);

    } catch (error) {
        console.error(error);
    }
}

async function uploadTickets() {
    //Zum Testen
    console.log("Ticket hochgeladen gedrückt");

    //findet das HTML-Element mit id="importDatei" // Platz 1(0) der Liste der gefundenen Dateien
    const datei = document.getElementById("importDatei").files[0];

    //Erstellt ein neues Objekt (eingebautes Browser Objekt), was als "UploadFile" Datei an die API geschickt werden kann // Transportbehälter für Dokumente und Dateien
    const formData = new FormData();

    //Lade/Lese und speichere den Inhalt der importDatei
    formData.append("importDatei", datei);

    //todo schauen, ob formData Inhalt besitzt, sonst Fehlermeldung
    +++


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



/*
Dateitypen etc.
    -let = veränderbare Variable
    -const, wie in C++



Liste auf der Webseite dynamisch befüllen
let liste = document.getElementById("ticketListe");

let eintrag = document.createElement("li");
eintrag.textContent = "Neues Ticket";

liste.appendChild(eintrag);

*/