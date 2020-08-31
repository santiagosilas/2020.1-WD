# exemplo
from flask import Flask, jsonify, request, abort, make_response
from api import app, db, utils
from api.models.task import Task, TaskSchema
from datetime import datetime



@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_schema = TaskSchema(many=True)
    data = tasks_schema.dump(tasks)
    return jsonify(data), 200

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    task_schema = TaskSchema()
    if task == None:
        abort(404)
    return {'task':task_schema.dump(task)}, 200

@app.route('/api/tasks', methods=['POST'])
def create_task():

    title = request.json['title']
    content = request.json['content']

    task = Task(title, content)

    db.session.add(task)
    db.session.commit()

    task_schema = TaskSchema()
    return task_schema.jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task == None:
        abort(404)
    title = request.json['title']
    content = request.json['content']
    date = request.json['date']

    task.title = title
    task.content = content
    task.date = datetime.strptime(date, '%Y-%m-%d')

    db.session.commit()

    task_schema = TaskSchema()
    return task_schema.jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task == None:
        abort(404)

    db.session.delete(task)
    #db.session.commit()
    task_schema = TaskSchema()
    return task_schema.jsonify(task)





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
