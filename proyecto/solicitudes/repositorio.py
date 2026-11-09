from .modelos import Solicitud


class RepositorioSolicitudes:
    """Responsable exclusivamente de almacenar y recuperar solicitudes."""
    def __init__(self):
        self._solicitudes: dict[int, Solicitud] = {}

    def agregar(self, solicitud: Solicitud) -> None:
        if solicitud.id in self._solicitudes:
            raise ValueError(f"Ya existe una solicitud con id {solicitud.id}")
        self._solicitudes[solicitud.id] = solicitud

    def obtener(self, solicitud_id: int) -> Solicitud:
        try:
            return self._solicitudes[solicitud_id]
        except KeyError as exc:
            raise LookupError(f"No existe la solicitud {solicitud_id}") from exc

    def listar(self) -> list[Solicitud]:
        return list(self._solicitudes.values())
