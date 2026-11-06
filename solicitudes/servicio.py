from collections import Counter

from .modelos import Estado, Solicitud
from .parametros import NuevaSolicitud
from .puertos import  RepositorioSolicitudesPuerto


class ServicioSolicitudes:
    """Coordina reglas de negocio sin ocuparse de la interfaz ni del almacenamiento físico."""
    def __init__(self, repositorio: RepositorioSolicitudesPuerto):
        self._repositorio = repositorio
        self._siguiente_id = 1

    def registrar(self, datos: NuevaSolicitud) -> Solicitud:
        campos = (datos.estudiante.strip(), datos.tipo.strip(), datos.descripcion.strip())
        if not all(campos):
            raise ValueError("Estudiante, tipo y descripción son obligatorios")
        solicitud = Solicitud(
            id=self._siguiente_id,
            estudiante=campos[0],
            tipo=campos[1],
            prioridad=datos.prioridad,
            descripcion=campos[2],
        )
        self._repositorio.agregar(solicitud)
        self._siguiente_id += 1
        return solicitud

    def cambiar_estado(self, solicitud_id: int, nuevo_estado: Estado) -> Solicitud:
        solicitud = self._repositorio.obtener(solicitud_id)
        solicitud.estado = nuevo_estado
        return solicitud

    def asignar_responsable(self, solicitud_id: int, responsable: str) -> Solicitud:
        if not responsable.strip():
            raise ValueError("El responsable no puede estar vacío")
        solicitud = self._repositorio.obtener(solicitud_id)
        solicitud.responsable = responsable.strip()
        return solicitud

    def buscar(self, texto: str = "", estado: Estado | None = None) -> list[Solicitud]:
        termino = texto.casefold().strip()
        return [
            s for s in self._repositorio.listar()
            if (not termino or termino in s.estudiante.casefold()
                or termino in s.tipo.casefold() or termino in s.descripcion.casefold())
            and (estado is None or s.estado == estado)
        ]

    def reporte_por_estado(self) -> dict[str, int]:
        conteo = Counter(s.estado.value for s in self._repositorio.listar())
        return dict(sorted(conteo.items()))
