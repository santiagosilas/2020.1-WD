# exemplo
from flask import Flask, jsonify, request, abort, make_response
from api import app

@app.route('/')
def home():
    return 'my flask api'

@app.errorhandler(404)
def not_found(error):
    print('error', error)
    #return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/books', methods=['GET'])
def get_books():
    pass

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    pass

@app.route('/api/books', methods=['POST'])
def create_book():
    pass

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    pass

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
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
