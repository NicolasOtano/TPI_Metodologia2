# Versión didáctica deliberadamente acoplada: ejemplo de "antes".
solicitudes = []
contador = 0

def gestionar(accion, estudiante="", tipo="", prioridad="media", descripcion="",
              solicitud_id=None, estado="", responsable="", filtro=""):
    global contador
    # Una función concentra validación, persistencia, búsqueda, reportes y presentación.
    if accion == "registrar":
        contador += 1
        fila = {"id": contador, "estudiante": estudiante, "tipo": tipo,
                "prioridad": prioridad, "descripcion": descripcion,
                "estado": "abierta", "responsable": None}
        solicitudes.append(fila)
        return "Solicitud registrada: " + str(fila)
    elif accion == "estado":
        for fila in solicitudes:
            if fila["id"] == solicitud_id:
                fila["estado"] = estado
                return "Estado actualizado: " + str(fila)
        return "No encontrada"
    elif accion == "asignar":
        for fila in solicitudes:
            if fila["id"] == solicitud_id:
                fila["responsable"] = responsable
                return "Responsable asignado: " + str(fila)
        return "No encontrada"
    elif accion == "buscar":
        resultados = []
        for fila in solicitudes:
            if filtro.lower() in str(fila).lower():
                resultados.append(fila)
        return resultados
    elif accion == "reporte":
        salida = {}
        for fila in solicitudes:
            salida[fila["estado"]] = salida.get(fila["estado"], 0) + 1
        return "REPORTE\n" + "\n".join([k + ": " + str(v) for k,v in salida.items()])
    else:
        return "Acción desconocida"
