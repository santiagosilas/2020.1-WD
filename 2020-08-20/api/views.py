# exemplo
from flask import Flask, jsonify, request, abort, make_response
from api import app


books = [
    {'id': 1, 'title':'Python Fluente', 'author':'Luciano Ramalho', 'read': False},
    {'id': 2, 'title':'Pense em Python', 'author':'Luciano Ramalho', 'read': True},
    {'id': 3, 'title':'Flask Web Framework', 'author':'Luciano Ramalho', 'read': False}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

#from flask import Flask, jsonify, request, abort

@app.errorhandler(404)
def not_found(error):
    print('error', error)
    #return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/books/<int:book_id>')
def get_book(book_id):
    selected = [book for book in books if book['id'] == book_id]
    if len(selected) > 0:
        return jsonify({'book': selected[0]})
    else:
        abort(404)



















@app.route('/')
def home():
    return 'my flask api'

#@app.route('/json-example', methods=['POST'])
#def json_example():
#    data = request.get_json()
#    title  = data['title']
#    author  = data['author']
#    return jsonify({'title': title})


@app.route('/json-example', methods=['GET', 'POST'])
def json_example():
    if request.method == 'POST':
        data = request.get_json()
        title  = data['title']
        author  = data['author']
        return jsonify({'title': title})
    else:
        return 'my flask api'






# http://localhost:5000/query-example?...
@app.route('/api/books/search')
def query_example():
    keyword = request.args['keyword']
    return jsonify({'search_term': keyword})

@app.route('/api/formdata-example', methods=['POST'])
def form_data_example():
    title = request.form['title']
    category = request.form['category']
    return jsonify({'cat': category})
