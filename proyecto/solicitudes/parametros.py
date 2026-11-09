from dataclasses import dataclass

from .modelos import Prioridad


@dataclass(frozen=True)
class NuevaSolicitud:
    estudiante: str
    tipo: str
    prioridad: Prioridad
    descripcion: str
