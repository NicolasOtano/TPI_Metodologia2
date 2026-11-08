from typing import Protocol, List
from .modelos import Solicitud

class RepositorioSolicitudesPuerto(Protocol):
    """
    Contrato que define qué operaciones debe tener cualquier repositorio.
    Al usar Protocol, cualquier clase que tenga estos métodos servirá, 
    sin necesidad de heredar explícitamente.
    """
    def agregar(self, solicitud: Solicitud) -> None: ...
    def obtener(self, solicitud_id: int) -> Solicitud: ...
    def listar(self) -> List[Solicitud]: ...