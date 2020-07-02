from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from Data import Data

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@auth.verify_password
def verify_password(username_or_token, password):
    #Try to see if it's a token first
    username_or_token = request.json.get('username')
    password = request.json.get('password')
    user_id = User.verify_auth_token(username_or_token)
    data = Data()
    if user_id:
        user = data.check_user(username=None, id=user_id)
    else:
        user = data.check_user(username=username_or_token, id=None)
    if user or user.verify_password(password):
        g.user = user
        return True
    return False


@app.route('/token', methods = ['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


@app.route('/users', methods = ['POST'])
def new_user():
    print('CALLEEDD')
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print("missing arguments")
        abort(400) 

    data = Data() 
    # if session.query(User).filter_by(username = username).first() is not None:
    user = data.check_user(username=username, id=None)
    if user:
        print("existing user")
        # user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'}), 200, {'Location': url_for('get_user', id = user.id, _external = True)}
        
    username, id = data.create_user(username=username, password=password)
    # user = User(username = username)
    # user.hash_password(password)
    # session.add(user)
    # session.commit()
    return jsonify({ 'username': username }), 201, {'Location': url_for('get_user', id = id, _external = True)}


@app.route('/api/users/<int:id>')
def get_user(id):
    data = Data()
    user = data.get_user(id)
    # user = session.query(User).filter_by(id=id).one()
    if not user:
        abort(400)
    return user


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })


if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='0.0.0.0', port=5000)
