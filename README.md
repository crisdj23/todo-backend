# Todo App Backend - Flask + PostgreSQL

Una API RESTful para gestionar tareas (To-Do List) construida con Flask, Peewee ORM y PostgreSQL.

## 🚀 Características

- API RESTful completa con operaciones CRUD
- Base de datos PostgreSQL con Peewee ORM
- Soporte CORS para frontend separado
- Desplegable en Render
- Endpoints de salud para monitoreo

## 📋 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/tasks` | Obtener todas las tareas |
| POST | `/tasks` | Crear una nueva tarea |
| PUT | `/tasks/<id>` | Actualizar una tarea |
| DELETE | `/tasks/<id>` | Eliminar una tarea |
| GET | `/health` | Verificar estado de la API |

## 🛠️ Instalación Local

### Prerrequisitos
- Python 3.8+
- PostgreSQL

### Pasos

1. Clonar el repositorio:
\`\`\`bash
git clone https://github.com/crisdj23/todo-backend
cd todo-backend
\`\`\`

2. Crear un entorno virtual:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate
\`\`\`

3. Instalar dependencias:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Configurar PostgreSQL local:
\`\`\`bash
# Crear base de datos
createdb todoapp
\`\`\`

5. Ejecutar la aplicación:
\`\`\`bash
python app.py
\`\`\`

La API estará disponible en `http://localhost:5000`

## ☁️ Despliegue en Render

### Pasos para desplegar:

1. Crear cuenta en [Render](https://render.com)
2. Conectar tu repositorio de GitHub
3. Crear un nuevo PostgreSQL database
4. Crear un nuevo Web Service
5. Configurar las variables de entorno

### Variables de entorno necesarias:
- `DATABASE_URL`: URL de conexión a PostgreSQL (proporcionada por Render)

**⚠️ IMPORTANTE:** Nunca expongas tu DATABASE_URL real en documentación pública.

## 📝 Ejemplos de uso

### Crear una tarea
\`\`\`bash
curl -X POST https://todo-api-jtw8.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Completar proyecto", "done": false}'
\`\`\`

### Obtener todas las tareas
\`\`\`bash
curl https://todo-api-jtw8.onrender.com/tasks
\`\`\`

### Actualizar una tarea
\`\`\`bash
curl -X PUT https://todo-api-jtw8.onrender.com/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
\`\`\`

### Eliminar una tarea
\`\`\`bash
curl -X DELETE https://todo-api-jtw8.onrender.com/tasks/1
\`\`\`

## 🔧 Estructura del proyecto

\`\`\`
todo-backend/
├── app.py              # Aplicación Flask principal
├── models.py           # Modelos de base de datos
├── requirements.txt    # Dependencias Python
└── README.md          # Documentación
\`\`\`

---

# Todo App Frontend - HTML + JavaScript + Bootstrap

Una interfaz web moderna y responsiva para gestionar tareas (To-Do List) construida con HTML, CSS, JavaScript puro y Bootstrap 5.

## 🚀 Características

- Interfaz moderna y responsiva con Bootstrap 5
- Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)
- Confirmación modal para eliminación de tareas
- Indicadores visuales de estado (completada/pendiente)
- Contador de tareas en tiempo real
- Manejo de errores y mensajes de éxito
- Animaciones suaves y efectos hover
- Compatible con dispositivos móviles

## 🛠️ Tecnologías utilizadas

- HTML5
- CSS3 (con animaciones y gradientes)
- JavaScript ES6+ (Vanilla JS)
- Bootstrap 5.3.0
- Font Awesome 6.0.0

## ✅ Funcionalidades

- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas/pendientes
- ✅ Eliminar tareas con confirmación
- ✅ Contador de tareas (total, completadas, pendientes)
- ✅ Interfaz responsiva para móviles
- ✅ Manejo de estados de carga
- ✅ Mensajes de error y éxito
- ✅ Validación de formularios

## ⚙️ Configuración

### Configurar la URL de la API

Antes de usar la aplicación, debes configurar la URL de tu API backend en el archivo `script.js`:

\`\`\`javascript
const API_BASE_URL = 'https://todo-api-jtw8.onrender.com';
\`\`\`

### Estructura de archivos

\`\`\`
todo-frontend/
├── index.html          # Página principal
├── styles.css          # Estilos personalizados
├── script.js           # Lógica de la aplicación
└── README.md          # Documentación
\`\`\`

## 🚀 Despliegue en GitHub Pages

### Pasos para desplegar:

1. **Crear un repositorio en GitHub:**
   - Ve a [GitHub](https://github.com) y crea un nuevo repositorio
   - Nómbralo `todo-frontend` o el nombre que prefieras
   - Marca la opción "Add a README file"

2. **Subir los archivos:**
\`\`\`bash
git clone https://github.com/crisdj23/todo-frontend
cd todo-frontend
# Copia todos los archivos del frontend aquí
git add .
git commit -m "Initial commit: Todo app frontend"
git push origin main
\`\`\`

3. **Activar GitHub Pages:**
   - Ve a la configuración del repositorio (Settings)
   - Busca la sección "Pages" en el menú lateral
   - En "Source", selecciona "Deploy from a branch"
   - Selecciona la rama `main` y la carpeta `/ (root)`
   - Haz clic en "Save"

4. **Acceder a tu aplicación:**
   - Tu aplicación estará disponible en: `https://crisdj23.github.io/todo-frontend`

## 🎯 URLs del proyecto

- **Backend API:** https://todo-api-jtw8.onrender.com
- **Frontend:** https://crisdj23.github.io/todo-frontend

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
\`\`\`

## 🔒 **ACCIÓN INMEDIATA REQUERIDA:**

**¡Cambia tu contraseña de la base de datos!** Ya que la expusiste públicamente:

1. Ve a tu base de datos en Render
2. Busca la opción para regenerar/cambiar la contraseña
3. Actualiza la variable `DATABASE_URL` en tu servicio web

¿Necesitas ayuda para cambiar la contraseña de la base de datos? 🔐

