from dataclasses import dataclass
from enum import Enum


class Estado(str, Enum):
    ABIERTA = "abierta"
    EN_PROCESO = "en_proceso"
    RESUELTA = "resuelta"
    CERRADA = "cerrada"

class Prioridad(str, Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"

@dataclass
class Solicitud:
    id: int
    estudiante: str
    tipo: str
    prioridad: Prioridad
    descripcion: str
    estado: Estado = Estado.ABIERTA
    responsable: str | None = None
