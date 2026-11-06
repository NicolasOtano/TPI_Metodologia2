import unittest

from solicitudes.modelos import Estado, Prioridad
from solicitudes.parametros import NuevaSolicitud
from solicitudes.repositorio import RepositorioSolicitudes
from solicitudes.servicio import ServicioSolicitudes


class ServicioSolicitudesTests(unittest.TestCase):
    def setUp(self):
        self.servicio = ServicioSolicitudes(RepositorioSolicitudes())

    def registrar(self, estudiante="Ana Demo", tipo="Certificado", descripcion="Certificado de materias"):
        return self.servicio.registrar(NuevaSolicitud(estudiante, tipo, Prioridad.MEDIA, descripcion))

    def test_registrar_asigna_id_y_estado_inicial(self):
        solicitud = self.registrar()
        self.assertEqual(solicitud.id, 1)
        self.assertEqual(solicitud.estado, Estado.ABIERTA)

    def test_rechaza_campos_obligatorios_vacios(self):
        with self.assertRaises(ValueError):
            self.registrar(estudiante="  ")

    def test_cambia_estado(self):
        solicitud = self.registrar()
        self.servicio.cambiar_estado(solicitud.id, Estado.EN_PROCESO)
        self.assertEqual(solicitud.estado, Estado.EN_PROCESO)

    def test_asigna_responsable_y_rechaza_vacio(self):
        solicitud = self.registrar()
        self.servicio.asignar_responsable(solicitud.id, " Secretaría ")
        self.assertEqual(solicitud.responsable, "Secretaría")
        with self.assertRaises(ValueError):
            self.servicio.asignar_responsable(solicitud.id, " ")

    def test_busqueda_no_distingue_mayusculas(self):
        self.registrar()
        self.assertEqual(len(self.servicio.buscar("ANA")), 1)

    def test_filtra_por_estado(self):
        solicitud = self.registrar()
        self.servicio.cambiar_estado(solicitud.id, Estado.RESUELTA)
        self.assertEqual(len(self.servicio.buscar(estado=Estado.ABIERTA)), 0)
        self.assertEqual(len(self.servicio.buscar(estado=Estado.RESUELTA)), 1)

    def test_reporte_por_estado(self):
        self.registrar()
        self.assertEqual(self.servicio.reporte_por_estado(), {"abierta": 1})

    def test_busqueda_sin_resultados(self):
        self.registrar()
        self.assertEqual(self.servicio.buscar("no existe"), [])

if __name__ == "__main__":
    unittest.main()
