from models import Base, User, Product
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from Data import Data

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite:///regalTree.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


#ADD @auth.verify_password decorator here
@auth.verify_password
def verify_password(username_or_token, password):
	data = Data()
	username_or_token = request.json.get('username')
	password = request.json.get('password')
	user_id = User.verify_auth_token(username_or_token)
	if user_id:
		user = data.check_user(username=None, id=user_id)
	else:
		user = data.check_user(username=username_or_token, id=None)
	if not user or not user.verify_password(password):
		return False
	g.user = user
	return True


#add /token route here to get a token for a user with login credentials
@app.route('/token', methods=['GET'])
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token()
	return jsonify({"token":token.decode('ascii')})


@app.route('/users', methods = ['GET', 'POST'])
def new_user():
	data = Data()
	if request.method == "POST":
		username = request.json.get('username')
		password = request.json.get('password')
		if data.check_user(username=username, id=None):
			return jsonify({"error":"username already taken bitch!"})
		user = data.create_user(username=username, password=password)
		return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
	elif request.method == "GET":
		users = data.get_record(id=None, type='user')
		return jsonify(users = [u.serialize for u in users])


@app.route('/users/<int:id>')
def get_user(id):
	data = Data()
	user = data.get_record(id=id, type='user')
	# user = session.query(User).filter_by(id=id).one()
	if not user:
		abort(400)
	return jsonify({'username': user.username})


@app.route('/resource')
@auth.login_required
def get_resource():
	return jsonify({ 'data': 'Hello, %s!' % g.user.username })


@app.route('/products', methods = ['GET', 'POST'])
@auth.login_required
def showAllProducts():
	data = Data()
	if request.method == 'GET':
		products = data.get_record(id=None, type='product')
		# products = session.query(Product).all()
		return jsonify(products = [p.serialize for p in products])
	if request.method == 'POST':
		name = request.json.get('name')
		category = request.json.get('category')
		price = request.json.get('price')
		new_product = data.create_products(name=name, category=category, price=price)
		# newItem = Product(name = name, category = category, price = price)
		# session.add(newItem)
		# session.commit()
		return jsonify(new_product.serialize)


@app.route('/products/<category>')
@auth.login_required
def showCategoriedProducts(category):
	data = Data()
	products = data.get_products(category)
	return jsonify(products = [p.serialize for p in products])
	# if category == 'fruit':
	#     fruit_items = session.query(Product).filter_by(category = 'fruit').all()
	#     return jsonify(fruit_products = [f.serialize for f in fruit_items])
	# if category == 'legume':
	#     legume_items = session.query(Product).filter_by(category = 'legume').all()
	#     return jsonify(legume_products = [l.serialize for l in legume_items])
	# if category == 'vegetable':
	#     vegetable_items = session.query(Product).filter_by(category = 'vegetable').all()
	#     return jsonify(produce_products = [p.serialize for p in produce_items])


if __name__ == '__main__':
	app.debug = True
	#app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	app.run(host='0.0.0.0', port=5000)
