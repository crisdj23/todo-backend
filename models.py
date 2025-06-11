from peewee import *
import os
from urllib.parse import urlparse

# Configuración de la base de datos
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Parsear la URL de la base de datos para producción (Render)
    url = urlparse(DATABASE_URL)
    database = PostgresqlDatabase(
        url.path[1:],  # Nombre de la base de datos (sin el '/')
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    )
else:
    # Base de datos local para desarrollo
    database = PostgresqlDatabase(
        'todoapp',
        user='postgres',
        password='password',
        host='localhost',
        port=5432
    )

class BaseModel(Model):
    """Modelo base para todos los modelos"""
    class Meta:
        database = database

class Task(BaseModel):
    """Modelo para las tareas"""
    id = AutoField(primary_key=True)
    title = CharField(max_length=255)
    done = BooleanField(default=False)
    
    class Meta:
        table_name = 'tasks'

def initialize_db():
    """Inicializar la base de datos y crear las tablas"""
    try:
        database.connect()
        database.create_tables([Task], safe=True)
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if not database.is_closed():
            database.close()
