from models import Base, User, Bagel
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from Data import Data

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth() 
app = Flask(__name__)

#ADD @auth.verify_password here
@auth.verify_password
def verify_password(username, password):
    try:
        username = request.json.get('username')
        password = request.json.get('password')
    except:
        abort(400) # no credentials provided
    data = Data()
    user = data.check_entry(username, 'user')
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

#ADD a /users route here
@app.route('/api/users', methods = ['GET', 'POST'])
def new_user():
    data = Data()
    if request.method == "POST":
        username = request.json.get('username')
        password = request.json.get('password')

        if username is None or password is None:
            abort(400) # missing arguments

        if data.check_entry(username, 'user'):
            abort(400) # user already exists
        
        username, id = data.create_user(username=username, password=password)

        return jsonify({"username":username}), 201, {"Location":url_for("get_user", id=id, _external=True)}

    elif request.method == "GET":
        return data.get_users()

#protect this route with a required login
# @auth.login_required
@app.route('/bagels', methods = ['GET','POST'])
@auth.login_required # to give access to only logged in users
def showAllBagels():
    data = Data()
    if request.method == 'GET':
        return data.get_bagels()
        # bagels = session.query(Bagel).all()
        # return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        if not data.check_entry(name, 'bagel'):
            bagel, id = data.create_bagel(name=name, description=description, picture=picture, price=price)
            return jsonify({"bagel": bagel}), 201
            # return jsonify({"bagel": bagel}), 201, {"Location": url_for("get_bagel", id=id, _external=True)}
        else:
            return jsonify({"error": f'Bagel {name} already in database.'})

@app.route('/api/users/<int:id>')
def get_user(id):
    data = Data()
    user_data = data.get_users(id)
    if not user_data:
        abort(400) # user not foun
    return user_data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
