from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from Data import Data

from flask import Flask

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)

"""
g is an object provided by Flask. It is a global namespace for holding any data you want during a single app context.
"""

@auth.verify_password
def verify_password(username, password):
    username = request.json.get('username')
    password = request.json.get('password')
    data = Data()
    user = data.check_user(username)
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@app.route('/api/users', methods = ['GET', 'POST'])
def new_user():
    data = Data()
    if request.method == "POST":
        username = request.json.get('username')
        password = request.json.get('password')

        if username is None or password is None:
            abort(400) # missing arguments

        if data.check_user(username):
            abort(400) # existing user

        username, id = data.create_user(username, password)

        return jsonify({ 'username': username }), 201, {'Location': url_for('get_user', id = id, _external = True)}

    elif request.method == "GET":
        return data.get_users()

@app.route('/api/users/<int:id>')
def get_user(id):
    data = Data()
    user_data = data.get_users(id)
    if not user_data:
        abort(400)
    return user_data

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': f'Hello, {g.user.username}'})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
	

"""
Get one user
GET - http://localhost:5000/api/users/1

Get all user
GET - http://localhost:5000/api/users

Create user
POST - http://localhost:5000/api/users - with json body
{"username":"okaysidd1",
"password":"okaysidd"
}
"""
