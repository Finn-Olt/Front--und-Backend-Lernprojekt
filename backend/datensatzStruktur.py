from dataclasses import dataclass, field
from typing import Optional

#Hat den Vorteil, Objekt kann leicht in ein Dictionary umwandelt werden => das kann FastAPI direkt als z.B. JSON zurückgeben
@dataclass
class ImportDatensatz:
    id: str
    quellDatei: Optional[str] = None
    titel: str
    beschreibung: str
    prio: Optional[str] = None
    status: Optional[str] = None
    #String Array // immer wenn ein neues Objekt erstellt wird, wird automatisch eine leere Liste erstellt
    fach: Optional [list[str]] = field(default_factory=list)
