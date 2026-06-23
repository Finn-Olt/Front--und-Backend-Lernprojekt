console.log("Startseite wird geladen.");

//Wenn die Webseite neu/gerade geladen wurde, dann führe die Funktion aus
document.addEventListener("DOMContentLoaded", () => {ladeTickets()});

//document = komplette HTML-Seite // querySelector = Suche mir das erste HTML-Element mit der Klasse uploadButton
const uploadButton = document.querySelector(".uploadButton");
const ticketsButton = document.querySelector(".ticketsButton");

//Warte auf das Event "click" bein Upload und Get Button // <Eventtype>, <Funktion>
uploadButton.addEventListener("click", uploadTicketsSeite);
uploadButton.addEventListener("click", TicketsSeite);


//JS soll nicht einfrieren, deshalb async, außerdem für "await"
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

        //TODO Hier müsste dann die Tabelle auf der Webseite befüllt werden (Ticketanzahl, SDM, EVP, GID, unzugewiesen)
        +++

        console.log(tickets);

    } catch (error) {
        console.error(error);
    }
}


function uploadTicketsSeite() {
    window.location.href = "upload.html";
}

function TicketsSeite() {
    window.location.href = "tickets.html";
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

/*
Zwei Arten Webseiten dynamisch zu machen => Klicke auf ein Element und aufeinmal sieht die Webseite ganz anders aus und zeigt andere Sachen an

1. Möglichkeit:
Ich erstelle mehrere HTML Dateien, z.B.: 
    -index.html     => Als Startseite
    -tickets.html   => Als Anzeigefenster für die Tickets (z.B. bei Lade alle/ein Ticket(s))
    -upload.html    => Als Seite, zum Hochladen der Dateien (Anwender klickt auf den Upload Button)

Vorteile:
    -Sehr einfach zu verstehen
    -Sehr simpler Aufbau

Nachteil:
    -Redundanter Code / Elemente, wie die Button
    -Seiten und Elemente sind teils dynamisch, aber durch das "eingeschränkte" HTML Dokument, können Elemente Fehlen, um eine neue Ansicht zu bauen
        ->Würde dann auch für die Einheitlichkeit ein komplett neues HTML Dokument erstellen

=>Benutzen, wenn es nur eine oder maximal zwei "Ansichten" geben soll UND von anfang an klar ist, dass das Projekt nicht sehr groß wird 


2. Möglichkeit:
Ich erstelle ein HTML Dokument, in das ich ALLES rein schreibe und passe das momentane Aussehen über JavaScript an

Vorteil:
    -Keine Redundanten Elemente 
    -Kein Neuladen der Webseite erforderlich
    -Sehr dynamisch, da ich theoretisch mit den Elementen aus dem HTML Dokument auch eine ganz neue Seite bauen kann, wenn ich möchte
    -Wird auch so oder sehr ähnlich von Framesworks wie React, Vue, etc. genutzt

Nachteil:
    -Das HTML Dokument kann sehr größ werden

=>Benutzen, wenn man ein Projekt bauen möchte, bei dem die Ausmaße und ggf. Erweiterungen nicht einschätzen kann, bzw. sehr "frei" 
  im Erstellen der Seite sein möchte.


Beispiel HTML Code:
<body>
    <div id="seiteStart">
        <button id="uploadButton">
            Upload
        </button>
    </div>

    <div id="seiteUpload">
        <input type="file">
    </div>

    <div id="seiteTickets">
        <ul id="ticketListe">
        </ul>
    </div>
</body>  

CSS:
.versteckt {
    display: none;
}

JS:
document.getElementById("seiteStart").classList.add("versteckt");
document.getElementById("seiteUpload").classList.remove("versteckt");


3. Möglichkeit:
Man vermischt diese beiden obrigen Möglichkeiten

Kann man benutzen, wenn z.B. von anfang an klar ist, dass die Ansicht/Webseite immer GENAU SO aussehen soll, 
z.B. nach dem Klick auf "Kontak" das Kontaktformular

*/