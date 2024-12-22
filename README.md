## Chess games API

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