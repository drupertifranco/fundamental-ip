# API de Gestión de Tareas

Este proyecto es una API construida con **FastAPI** para gestionar tareas (todos). Permite listar todas las tareas existentes y crear nuevas tareas.

## Tecnologías utilizadas
- **FastAPI**: Framework para construir APIs en Python.
- **Pydantic**: Para la validación de datos y definición de modelos.
- **MongoDB**: Base de datos utilizada para almacenar las tareas (se asume por el uso de `collection`).

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura la conexión a la base de datos MongoDB en el archivo `configuratio.py`.

4. Inicia la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

   La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### Obtener todas las tareas
- **Método**: `GET`
- **Ruta**: `/`
- **Respuesta**: Lista todas las tareas almacenadas en la base de datos.

### Crear una nueva tarea
- **Método**: `POST`
- **Ruta**: `/`
- **Body** (JSON):
  ```json
  {
    "field1": "value1",
    "field2": "value2",
    ...
  }
  ```
- **Respuesta**: Retorna el ID de la tarea creada o un error en caso de fallo.

## Estructura del proyecto
- `main.py`: Punto de entrada de la aplicación.
- `configuratio.py`: Configuración de la conexión a la base de datos.
- `database/`: Contiene los modelos y esquemas de la base de datos.
  - `schemas.py`: Esquemas para la validación de datos.
  - `models.py`: Modelos de datos (por ejemplo, `Todo`).

## Ejemplo de uso

1. Obtener todas las tareas:
   ```bash
   curl -X GET http://127.0.0.1:8000/
   ```

2. Crear una nueva tarea:
   ```bash
   curl -X POST http://127.0.0.1:8000/ -H "Content-Type: application/json" -d '{"field1": "value1", "field2": "value2"}'
   ```

## Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama con tu feature o corrección (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

