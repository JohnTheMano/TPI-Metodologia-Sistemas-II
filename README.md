# Sistema de Gestión de Solicitudes Académicas (Versión Base)

Este repositorio contiene la versión inicial del prototipo **Sistema de Gestión de Solicitudes Académicas**, desarrollado para el Trabajo Práctico Integrador de la asignatura **Metodología de Sistemas II**, correspondiente a la Tecnicatura Universitaria en Programación.

El objetivo del proyecto es contar con un sistema funcional que permita gestionar solicitudes académicas y disponer de una versión inicial sobre la cual realizar un diagnóstico de calidad interna, identificar deuda técnica y aplicar técnicas de refactoring.

## Características

- Implementado en Python 3.x.
- Sin dependencias externas de terceros; utiliza la biblioteca estándar de Python.
- Persistencia de datos mediante un archivo JSON.
- Gestión de solicitudes académicas.
- Búsqueda y filtrado de solicitudes.
- Asignación de responsables.
- Cambio de estado de las solicitudes.
- Generación de reportes básicos.
- Pruebas unitarias iniciales mediante `unittest`.

## Tecnologías utilizadas

- Python 3.x.
- JSON para almacenamiento de datos.
- unittest para pruebas unitarias.
- Git y GitHub para control de versiones.

## Estructura del proyecto

```text
sistema_gestion_solicitudes_base/
│
├── main.py
├── README.md
├── data_solicitudes.json
│
├── src/
│   ├── models.py
│   └── sistema.py
│
├── tests/
│   └── test_sistema.py
│
└── docs/
    ├── decisiones-tecnicas.md
    └── checklist-code-review.md
```

## Requisitos previos

- Tener instalado Python 3.x.
- Disponer de una terminal o consola de comandos.

No es necesario instalar dependencias externas.

## Cómo ejecutar el sistema

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

## Cómo ejecutar las pruebas

Para ejecutar las pruebas unitarias disponibles, utilizar:

```bash
python -m unittest discover tests
```

## Persistencia de datos

El sistema utiliza el archivo `data_solicitudes.json` para almacenar la información y permitir su recuperación mediante los mecanismos implementados en el proyecto.

## Estado del proyecto

Este repositorio conserva la versión base del sistema, identificada mediante el tag de Git `estado-inicial`.

Esta versión será utilizada como referencia para el diagnóstico técnico y la posterior comparación con la versión refactorizada.

## Trabajo Práctico Integrador

El proyecto será utilizado para aplicar los contenidos de Metodología de Sistemas II relacionados con:

- Calidad interna y externa del software.
- Deuda técnica y code smells.
- Principios SOLID y Clean Code.
- Técnicas de refactoring.
- Pruebas y verificación del comportamiento.
- Revisión técnica del código (Code Review).

## Repositorio

[GitHub - TPI Metodología de Sistemas II](https://github.com/JohnTheMano/TPI-Metodologia-Sistemas-II)