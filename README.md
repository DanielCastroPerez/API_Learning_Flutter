# API Educativa Flutter + FastAPI

Esta API está diseñada para brindar datos a una aplicación Flutter que enseña sobre widgets, propiedades y estructura de Flutter.

##  Tecnologías utilizadas
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (actualmente)
- JWT para autenticación

##  Cómo usar

1. Clona el repositorio  
2. Crea un entorno virtual:  
   python -m venv venv

## Activa el entorno virtual:

- Windows: venv\Scripts\activate
- 
- Linux/Mac: source venv/bin/activate

## Instala dependencias:

- Copiar
- Editar
- pip install -r requirements.txt
## Ejecuta el servidor:

- Copiar
- Editar
- uvicorn app:app --reload
## Estructura del proyecto
- pgsql
- Copiar
- Editar
.
├── app.py
├── config/
├── models/
├── routes/
├── schemas/
├── widgets_avanzado.json
├── .gitignore
├── README.md

## Estado actual
- CRUD básico implementado

## Autenticación JWT en desarrollo

- .gitignore configurado para ignorar archivos innecesarios

##  Convención de commits usada (Conventional Commits)

| Tipo        | Uso                                                                 |
|-------------|----------------------------------------------------------------------|
| `feat`      | Nueva funcionalidad                                                  |
| `fix`       | Corrección de bugs                                                   |
| `docs`      | Documentación (README, comentarios, etc.)                            |
| `style`     | Cambios de formato (espacios, puntos, comas) sin afectar el código   |
| `refactor`  | Reorganización del código sin cambiar su comportamiento              |
| `test`      | Añadir, corregir o mejorar pruebas                                   |
| `chore`     | Tareas menores (ej. `.gitignore`, dependencias)                      |
| `perf`      | Mejoras de rendimiento                                               |
| `ci`        | Cambios en configuración de integración continua (CI/CD)             |
| `build`     | Cambios en dependencias o compilación                                |
| `revert`    | Reversión de commits anteriores                                      |

## Ejemplo:
- git commit -m "feat: se agrega endpoint para obtener widgets por categoría"


## Autor
Daniel Castro Perez


