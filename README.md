# Sistema de Gestión de Solicitudes Académicas (Versión Base)

Este repositorio contiene la versión base (inicial) del prototipo para el Trabajo Práctico Integrador de **Metodología de Sistemas II**.

## Características
- Implementado en Python 3.x.
- Sin dependencias externas de terceros (utiliza la biblioteca estándar).
- Persistencia simple simulada mediante archivo JSON.

## Estructura del Proyecto
- `src/models.py`: Definiciones iniciales de entidades.
- `src/sistema.py`: Lógica principal del sistema (God Class / Monolito).
- `main.py`: Script de ejecución para demostración por consola.
- `tests/test_sistema.py`: Pruebas unitarias iniciales para verificar el comportamiento externo.

## Cómo Ejecutar
```bash
python main.py
```

## Cómo Ejecutar Pruebas
```bash
python -m unittest discover tests
```