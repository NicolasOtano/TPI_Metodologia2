import unittest
from baseline.sistema_base import gestionar, solicitudes
from solicitudes.modelos import Estado, Prioridad
from solicitudes.parametros import NuevaSolicitud
from solicitudes.repositorio import RepositorioSolicitudes
from solicitudes.servicio import ServicioSolicitudes

class RegresionTests(unittest.TestCase):
    
    def test_comportamiento_equivalente_registro(self):
        """Verifica que registrar en el 'antes' y en el 'después' da los mismos datos base."""
        # 1. Ejecutamos el código VIEJO
        solicitudes.clear() # Limpiamos la lista global
        gestionar("registrar", estudiante="Juan", tipo="Beca", prioridad="alta", descripcion="Prueba")
        
        # 2. Ejecutamos el código NUEVO
        repo = RepositorioSolicitudes()
        servicio = ServicioSolicitudes(repo)
        sol_nueva = servicio.registrar(NuevaSolicitud("Juan", "Beca", Prioridad.ALTA, "Prueba"))
        
        # 3. Comparamos que los datos coincidan
        self.assertEqual(solicitudes[0]["estudiante"], sol_nueva.estudiante)
        self.assertEqual(solicitudes[0]["tipo"], sol_nueva.tipo)
        self.assertEqual(solicitudes[0]["estado"], sol_nueva.estado.value)
        self.assertEqual(solicitudes[0]["prioridad"], sol_nueva.prioridad.value)

    def test_comportamiento_equivalente_reporte(self):
        """Verifica que el reporte por estado cuente igual en ambas versiones."""
        # Código VIEJO
        solicitudes.clear()
        gestionar("registrar", estudiante="Maria")
        reporte_viejo = gestionar("reporte")
        
        # Código NUEVO
        repo = RepositorioSolicitudes()
        servicio = ServicioSolicitudes(repo)
        servicio.registrar(NuevaSolicitud("Maria", "Constancia", Prioridad.BAJA, "Test"))
        reporte_nuevo = servicio.reporte_por_estado()
        
        # Verificamos (el viejo devuelve un string, el nuevo un dict)
        self.assertIn("abierta: 1", reporte_viejo)
        self.assertEqual(reporte_nuevo, {"abierta": 1})

if __name__ == "__main__":
    unittest.main()