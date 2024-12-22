[![Python][Py]][Py-url]
[![Ubuntu][DRF]][DRF-url]

# Chess games API

## Detalles generales

### 1. **Definición del Propósito**

- **Propósito de la API**: Proporcionar información detallada sobre partidas de ajedrez, incluyendo jugadores con su respectivo ELO y color en la partida, jugadas, lugar y fecha de la competición.

### 2. **Recursos Principales**

- **Partidas**:
    - **Endpoint**: `/games`
    - **Métodos**:
        - `GET /games`: Obtener una lista de partidas.
        - `GET /games/{id}`: Obtener detalles de una partida específica.
        - `POST /games`: Añadir una nueva partida (solo para administradores).
        - `PUT /games/{id}`: Actualizar los detalles de una partida (solo para administradores).
        - `DELETE /games/{id}`: Eliminar una partida (solo para administradores).
- **Competidores**:
    - **Endpoint**: `/players`
    - **Métodos**:
        - `GET /players/{id}`: Obtener detalles de un competidor.
        - `POST /players`: Añadir una nueva partida (solo para administradores).
        - `PUT /players/{id}`: Actualizar los detalles de una partida (solo para administradores).
        - - `DELETE /players/{id}`: Eliminar una partida (solo para administradores).

### 3. **Estructura de Datos**

- `games`
    
    ```json
    {
        "id": "integer",
        "white_id": "integer",
        "black_id": "integer",
        "moves": "String",
        "result": "integer",
        "date": "Date",
        "days_since_played": "MethodField",
        "location": "String",
        "pgn": "String(url) or null"
    }
    ```
    
- `players`
    
    ```json
    {
      "id": "integer", // Identificador único del jugador
      "last_name": "string", // Apellido del jugador
      "first_name": "string", // Nombre del jugador
      "played_as_black": "nested_games_list",
      "played_as_white": "nested_game_list",
      "elo": "number" // Puntuación ELO del jugador
    }
    
    ```

### 4. **Autenticación y Autorización**

- **Autenticación**: Utilización de admin users  para autenticar a los usuarios.
- **Roles de Usuario**:
    - **Usuario Común**: Puede buscar y ver detalles de partidas y los competidores.
    - **Administrador**: Además de las capacidades de un usuario común, puede añadir, actualizar, o eliminar partidas.

### 5. **Documentación de la API**

- **Swagger/ReDoc**: Documentación interactiva para que los desarrolladores puedan probar los endpoints y entender cómo interactuar con la API.

### 6. **Consideraciones de Rendimiento**

- **Paginación**: Implementar paginación para listas largas de resultados.
- **Throttling**: Limitación de acceso a la api en un rango de tiempo según el tipo de usuario. 

### 7. **Futuras integraciones**

- **Detector de ECO**: Asignar un SerializerMethodField que asigne un ECO según los primeros movimientos de la partida.

- **Tipo de partida**: Parámetro para diferenciar entre Partidas Clásicas, Rápidas o Blitz.

---

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/Mega-Barto/Chess-Games-Api.git
   cd Chess-Games-Api
   ```

2. **Crear y activar un entorno virtual**
   Es recomendable usar un entorno virtual para evitar conflictos entre dependencias de diferentes proyectos.

   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar las dependencias**
   Usa el archivo `requirements.txt` para instalar todas las dependencias necesarias.

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   Aplica las migraciones para configurar la base de datos según el modelo definido en el proyecto.

   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**
   Si necesitas acceder al panel de administración, crea un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo**
   Inicia el servidor para verificar que el proyecto funciona correctamente.

   ```bash
   python manage.py runserver
   ```

   Luego, abre un navegador y accede a `http://127.0.0.1:8000/api`.




[DRF]: https://img.shields.io/badge/django--rest--framework-3.15.2-blue?style=for-the-badge&labelColor=333333&logo=django&logoColor=white&color=red
[DRF-url]: https://www.django-rest-framework.org/
[Py]: https://img.shields.io/badge/python-3.15.2-blue?style=for-the-badge&logo=python&logoColor=ffdd54
[Py-url]: https://www.python.org/