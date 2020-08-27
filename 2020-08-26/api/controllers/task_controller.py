# exemplo
from flask import Flask, jsonify, request, abort, make_response
from api import app, utils
from api.models.task import Task, TaskSchema



@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_schema = TaskSchema(many=True)
    return {'tasks':tasks_schema.dump(tasks)}, 200

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    task_schema = TaskSchema()
    if task == None:
        abort(404)
    return {'task':task_schema.dump(task)}, 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    pass
    return {
        'task_id': None,
        'task_title': '???' 
    }, 201

@app.route('/api/tasks/<int:book_id>', methods=['PUT'])
def update_task(book_id):
    pass

@app.route('/api/tasks/<int:book_id>', methods=['DELETE'])
def delete_task(book_id):
    pass

# Exemplo
@app.route('/json-example', methods=['GET', 'POST'])
def json_example():
    if request.method == 'POST':
        data = request.get_json()
        title  = data['title']
        author  = data['author']
        return jsonify({'title': title})
    else:
        return 'my flask api'

# Exemplo
# http://localhost:5000/query-example?...
@app.route('/query-example')
def query_example():
    keyword = request.args['keyword']
    return jsonify({'search_term': keyword})

# Exemplo
@app.route('/api/formdata-example', methods=['POST'])
def form_data_example():
    title = request.form['title']
    category = request.form['category']
    return jsonify({'cat': category})
