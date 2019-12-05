
import flask
import os
import pymongo
#####################################################
#       API
#####################################################

client = pymongo.MongoClient()
db = client.users

app = flask.Flask(__name__)
@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/users', methods=[ 'GET' ])
def get_users():

    def filtrar_usuario(u, n):
        return {
            'id': n + 1,
            'nome': u['nome'],
            'email': u['email']
        }
    users = db.users.find().sort('_id', pymongo.ASCENDING)
    users = list(filtrar_usuario(u, n) for n, u in enumerate(users))
    return flask.jsonify(users)

@app.route('/users/auth', methods=[ 'GET' ])
def get_auth():
    return 'autenticar usuario'

@app.route('/users/<int:userid>', methods=[ 'PUT' ])
def update_user_by_id(userid):
    return 'Update usuario por id {}'.format(userid)

@app.route('/users/<int:userid>', methods=[ 'DELETE' ])
def delete_user_by_id(userid):
    return 'Deletar usuario por id {}'.format(userid)

@app.route('/users', methods=[ 'POST' ])
def post_users():
    form = flask.request.get_json()

    nome = form['nome']
    email = form['email']
    senha = form['senha']

    db.users.insert({
        'nome': nome,
        'email': email,
        'senha': senha
    })

    return 'Add user'

@app.route('/users/<int:userid>', methods=[ 'GET' ])
def get_users_by_id(userid):
    return 'Usuario ID {0}'.format(userid)

@app.route('/', methods=[ 'GET' ])
def index():
    return flask.render_template('index.html', contexto={
        'nome':'',
        'mensagem':''
    })

@app.route('/', methods=[ 'POST' ])
def post_index():
    form = flask.request.form
    return flask.render_template('index.html', contexto={
        'nome':form['nome'],
        'mensagem': 'Eae, fmz ?'
    })

if __name__ == '__main__':
    app.run(debug=True)

