from solicitudes.modelos import Estado, Prioridad
from solicitudes.parametros import NuevaSolicitud
from solicitudes.repositorio import RepositorioSolicitudes
from solicitudes.servicio import ServicioSolicitudes


def main():
    servicio = ServicioSolicitudes(RepositorioSolicitudes())
    una = servicio.registrar(NuevaSolicitud(
        "Estudiante Demo", "Certificado", Prioridad.ALTA,
        "Solicito certificado de materias aprobadas"
    ))
    servicio.asignar_responsable(una.id, "Área de Alumnado")
    servicio.cambiar_estado(una.id, Estado.EN_PROCESO)
    print("=== Gestor de Solicitudes Académicas ===")
    for s in servicio.buscar():
        print(f"#{s.id} | {s.estudiante} | {s.tipo} | {s.prioridad.value} | "
              f"{s.estado.value} | responsable: {s.responsable}")
    print("Reporte:", servicio.reporte_por_estado())

if __name__ == "__main__":
    main()
