from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/inicio')
def pagina_inicial():
    answer = 1/ 0
    return 'Go to home.'

if __name__ == '__main__':
    app.run(debug=True)