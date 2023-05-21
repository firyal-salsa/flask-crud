from flask import Blueprint, jsonify, request

tasks_blueprint = Blueprint('tasks', __name__)

tasks = {}
last_task_id = 0  # Variabel untuk melacak ID terakhir yang digunakan

@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    global last_task_id
    
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    
    last_task_id += 1  # Menambahkan ID terakhir
    task = {'id': last_task_id, 'title': title, 'description': description}
    tasks[last_task_id] = task
    
    return jsonify({'message': 'Tugas berhasil ditambahkan'})


@tasks_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'tasks': tasks})

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Tugas tidak ditemukan'})

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    
    task = tasks.get(task_id)
    if task:
        task['title'] = title
        task['description'] = description
        return jsonify({'message': 'Tugas berhasil diubah'})
    else:
        return jsonify({'message': 'Tugas tidak ditemukan'})

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({'message': 'Tugas berhasil dihapus'})
    else:
        return jsonify({'message': 'Tugas tidak ditemukan'})
