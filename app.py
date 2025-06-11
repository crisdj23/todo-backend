from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Task, initialize_db
import os

app = Flask(__name__)
CORS(app)  # Permitir CORS para GitHub Pages

# Inicializar la base de datos
initialize_db()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Obtener todas las tareas"""
    try:
        tasks = Task.select()
        tasks_list = []
        for task in tasks:
            tasks_list.append({
                'id': task.id,
                'title': task.title,
                'done': task.done
            })
        return jsonify(tasks_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks', methods=['POST'])
def create_task():
    """Crear una nueva tarea"""
    try:
        data = request.get_json()
        
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        task = Task.create(
            title=data['title'],
            done=data.get('done', False)
        )
        
        return jsonify({
            'id': task.id,
            'title': task.title,
            'done': task.done
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Actualizar una tarea existente"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        task = Task.get_by_id(task_id)
        
        if 'title' in data:
            task.title = data['title']
        if 'done' in data:
            task.done = data['done']
        
        task.save()
        
        return jsonify({
            'id': task.id,
            'title': task.title,
            'done': task.done
        }), 200
    except Task.DoesNotExist:
        return jsonify({'error': 'Task not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Eliminar una tarea"""
    try:
        task = Task.get_by_id(task_id)
        task.delete_instance()
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Task.DoesNotExist:
        return jsonify({'error': 'Task not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de salud para verificar que la API funciona"""
    return jsonify({'status': 'healthy', 'message': 'Todo API is running'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
