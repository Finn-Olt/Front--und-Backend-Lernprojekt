console.log("Tickets Seite wird geladen.");

//Wenn die Webseite neu/gerade geladen wurde, dann führe die Funktion aus
document.addEventListener("DOMContentLoaded", () => {ladeTickets()});



//document = komplette HTML-Seite // querySelector = Suche mir das erste HTML-Element mit der Klasse uploadButton
const anzeigeButton = document.querySelector(".");+++

//Geht nicht, da ich ALLE delete Button brauche, um den korrekten Auswerten zu können
const deleteButton = document.querySelector(".deleteButton");+++

//Warte auf das Event "click" bein Upload und Get Button // <Eventtype>, <Funktion>
deleteButton.addEventListener("click", deleteTickets);
anzeigeButton.addEventListener("click", +++);



//Benötigt, um alle Tickets auf der Webseite anzeigen zu können
async function ladeTickets(){
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

        //Verarbeiten der JSON und Speichern der Objekte in einem Array?
        +++

        //TODO Hier müsste dann das die Webansicht geändert werden
        //Neue Ansicht mit einer Liste aller erhaltenen Tickets
        +++

        console.log(tickets);

    } catch (error) {
        console.error(error);
    }
}


//Muss das korrekte Ticket löschen
//Idee/TODO: 
//  Wenn ich am Anfang die Anzahl ermittel, kann ich einfach über die Button Nr den korrekten Loop Platz finden 
//  und mir da die ID raus holen, um den korrekten Datensatz in der Datenbank zu löschen
+++
async function deleteTickets(){
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

        //Die Tickets nach dem Löschen neu laden und die Webseite neu aufbauen
        ladeTickets();

        console.log(tickets);

    } catch (error) {
        console.error(error);
    }
}