# Sistema de Gestión de Solicitudes Académicas

## 1\. Descripción del proyecto

Este proyecto se desarrolla en el marco de la asignatura **Metodología de Sistemas II**.

Nuestro sistema permite gestionar solicitudes académicas mediante operaciones de registro, modificación de estado, asignación de responsables, búsqueda, filtrado y generación de reportes.

El trabajo se centra en comparar una versión inicial del sistema con una versión refactorizada, identificando problemas de diseño y aplicando mejoras que favorezcan la legibilidad, la mantenibilidad, la separación de responsabilidades y la capacidad de realizar pruebas.

## 2\. Objetivos

- Analizar la calidad interna y externa del sistema.
- Identificar deuda técnica y problemas de diseño en la implementación inicial.
- Aplicar buenas prácticas de Clean Code y principios SOLID cuando corresponda.
- Separar las responsabilidades en componentes específicos.
- Aplicar técnicas de refactoring para mejorar la estructura interna del código.
- Verificar el comportamiento del sistema mediante pruebas automatizadas.
- Documentar las decisiones técnicas y las mejoras realizadas.

## 3\. Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- **Registrar solicitudes:** permite crear solicitudes con los datos del estudiante, tipo, prioridad y descripción.
- **Cambiar estado:** permite actualizar el estado de una solicitud existente.
- **Asignar responsable:** permite asociar un responsable o área a una solicitud.
- **Buscar solicitudes:** permite buscar por estudiante, tipo o descripción.
- **Filtrar por estado:** permite consultar solicitudes según su estado actual.
- **Generar reportes:** permite obtener un conteo de solicitudes agrupadas por estado.

### Estados disponibles

- Abierta.
- En proceso.
- Resuelta.
- Cerrada.

### Prioridades disponibles

- Baja.
- Media.
- Alta.

## 4\. Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar el sistema.
- **dataclasses:** para definir estructuras de datos.
- **Enum:** para representar los estados y las prioridades mediante valores definidos.
- **collections.Counter:** para contabilizar solicitudes agrupadas por estado.
- **unittest:** biblioteca estándar utilizada para implementar pruebas automatizadas.
- **Git y GitHub:** para el control de versiones y la gestión del repositorio.

## 5\. Estructura del proyecto

text

```
proyecto/
├── baseline/
│   └── sistema_base.py
├── solicitudes/
│   ├── __init__.py
│   ├── modelos.py
│   ├── parametros.py
│   ├── repositorio.py
│   └── servicio.py
├── tests/
│   └── test_servicio.py
├── main.py
└── README.md
```

### Descripción de los archivos principales

- `baseline/sistema_base.py`: contiene la versión inicial del sistema, en la que las operaciones se concentran en una única función.
- `solicitudes/modelos.py`: define la entidad `Solicitud` y los enumerados `Estado` y `Prioridad`.
- `solicitudes/parametros.py`: define la clase `NuevaSolicitud`, que agrupa los datos necesarios para registrar una solicitud.
- `solicitudes/repositorio.py`: administra el almacenamiento y la recuperación de solicitudes en memoria.
- `solicitudes/servicio.py`: contiene la lógica de negocio y coordina las operaciones del sistema.
- `tests/test_servicio.py`: contiene las pruebas automatizadas del servicio.
- `main.py`: permite ejecutar una demostración del funcionamiento del sistema.
- `docs/`: destinada a reunir las evidencias, el checklist de revisión técnica y las decisiones de diseño.

## 6\. Instalación y ejecución

### Requisitos previos

- Python 3.10 o superior.
- Git, para clonar el repositorio.

El proyecto utiliza módulos de la biblioteca estándar de Python, por lo que no requiere instalar dependencias externas para las funcionalidades presentadas.

### Clonar el repositorio

bash

```
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
```

### Ejecutar el sistema

Desde el directorio raíz del proyecto, ejecutar:

bash

```
python main.py
```

El programa registra una solicitud de ejemplo, asigna un responsable, cambia su estado, muestra los resultados de la búsqueda y genera un reporte por estado.

### Ejecutar las pruebas automatizadas

Desde el directorio raíz del proyecto, ejecutar:

bash

```
python -m unittest discover -s tests -v
```

Este comando ejecuta las pruebas definidas en `tests/test_servicio.py` y muestra los resultados de cada caso.

## Refactoring y mejoras de diseño

La versión inicial presenta una función centralizada que utiliza una serie de condiciones para ejecutar las distintas operaciones del sistema. Esta implementación concentra responsabilidades relacionadas con el registro, la actualización, la búsqueda y la generación de reportes, dificultando su mantenimiento y evolución.

En la versión refactorizada, el código se organiza en módulos con responsabilidades diferenciadas.

### Principales mejoras de diseño

- **Separación de responsabilidades:** los modelos, el repositorio y el servicio tienen funciones específicas dentro del sistema.
- **Encapsulamiento del almacenamiento:** el repositorio centraliza las operaciones para agregar, obtener y listar solicitudes.
- **Simplificación de parámetros:** la clase `NuevaSolicitud` agrupa los datos requeridos para registrar una solicitud.
- **Mejora de legibilidad:** se utilizan nombres descriptivos, enumerados y anotaciones de tipos.
- **Validación de datos:** se controlan los campos obligatorios y se evita asignar un responsable vacío.
- **Manejo de errores:** el repositorio informa cuando una solicitud no existe o cuando se intenta registrar un identificador duplicado.
- **Facilidad de prueba:** la lógica de negocio se encuentra separada de la ejecución de ejemplo, lo que permite verificar sus operaciones de manera independiente.

Estas mejoras buscan aumentar la cohesión de los componentes, reducir el acoplamiento y facilitar futuras modificaciones.

## Pruebas y verificación

El proyecto incluye ocho pruebas automatizadas implementadas con `unittest`.

Los casos contemplados son:

1. Registro de una solicitud con identificador y estado inicial.
2. Rechazo de campos obligatorios vacíos.
3. Cambio de estado de una solicitud.
4. Asignación de responsable y rechazo de valores vacíos.
5. Búsqueda sin distinción entre mayúsculas y minúsculas.
6. Filtrado de solicitudes por estado.
7. Generación de reportes por estado.
8. Búsqueda sin resultados.

Las pruebas nos permiten verificar el comportamiento de las principales operaciones de la versión refactorizada. Para demostrar la seguridad del refactoring, estos resultados deben complementarse con evidencias de comparación entre la versión inicial y la versión final.

## Persistencia de datos

El sistema utiliza un repositorio en memoria implementado mediante un diccionario de Python.

Las solicitudes se mantienen disponibles durante la ejecución del programa, pero no se almacenan de forma permanente. Al finalizar la ejecución, los datos se pierden.

Esta decisión permite trabajar con una implementación sencilla y concentrar el desarrollo en la organización del código, las responsabilidades de los componentes y la verificación de las operaciones.

La incorporación de persistencia permanente mediante archivos o una base de datos queda como una posible mejora futura.

## Control de versiones y documentación técnica

El repositorio permite organizar y documentar la evolución del sistema desde su versión inicial hasta la versión refactorizada.

De acuerdo con los requisitos del TPI, se contemplan las siguientes etiquetas:

### Etiquetas de estado

- `estado-inicial`: identifica la versión base del sistema.
- `estadorefactorizado`: identifica la versión final refactorizada.

### Etiquetas de etapas

- `etapadiagnostico`: identifica el hito de diagnóstico.
- `etapa-refactoring`: identifica el hito de refactoring.
- `etapa-pruebas`: identifica el hito de pruebas.
- `etapa-docs`: identifica el hito de documentación.

--------------------------------------------------
--------------------------------------------------
--------------------------------------------------
--------------------------------------------------

**Repositorio de GitHub:** Agregar enlace al repositorio.

## Mejoras futuras

Como posibles mejoras futuras del sistema consideramos:

- Incorporar persistencia permanente mediante archivos o una base de datos.
- Ampliar las pruebas automatizadas con casos límite y escenarios adicionales.
- Incorporar una interfaz de usuario.
- Validar las transiciones permitidas entre estados.
- Mejorar la trazabilidad de las operaciones realizadas.
- Ampliar la documentación técnica y las evidencias de revisión de código.

## Información académica

**Asignatura:** Metodología de Sistemas II\
**Trabajo:** Trabajo Práctico Integrador (TPI)\
**Título:** Evolución profesional de un sistema existente: calidad, deuda técnica, refactoring y revisión técnica\
**Integrantes:** Ocete Rocio Milagros, Otaño Nicolas y Nicolás Azcuy\
**Comisión:** 7 (Ocete), (Otaño), (Azcuy)\
**Fecha de entrega:** 


--------------------------------------------------
--------------------------------------------------
--------------------------------------------------
--------------------------------------------------
=======


