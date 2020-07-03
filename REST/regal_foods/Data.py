from models import Base, User, Product
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


class Data:
	def __init__(self):
		engine = create_engine('sqlite:///regalTree.db')

		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()

	def create_user(self, username, password):
		if username is None or password is None:
			print("missing arguments for creating user")
			abort(400)
		user = User(username=username)
		user.hash_password(password=password)
		self.session.add(user)
		self.session.commit()
		return user

	def get_record(self, id=None, type=None):
		if type.lower() == 'product':
			a = Product
		elif type.lower() == 'user':
			a = User
		if id == None:
			records = self.session.query(a).all()
		else:
			records = self.session.query(a).filter_by(id=id).first()
		return records

	def get_products(self, category):
		existing_categories = self.get_categories()
		print(existing_categories)

		if category.lower() not in existing_categories:
			print('Invalid category')
			abort(400)
		else:
			products = self.session.query(Product).filter_by(category=category).all()
			return products

	def get_categories(self):
		query = f'SELECT category from product'
		try:
			categories = self.session.execute(query).fetchall()
			categories = [x[0] for x in categories]
		except:
			categories = []
		return categories

	def check_user(self, username=None, id=None):
		print(f'username -- {username}, id -- {id}')
		if not username and not id:
			print('Neither username nor id provided')
			abort(400)
		if username != None:
			try:
				user = self.session.query(User).filter_by(username=username).one()
			except:
				return False
		elif id != None:
			try:
				user = self.session.query(User).filter_by(id=id).one()
			except:
				return False
		if user == None:
			return False
		return user

	def create_products(self, name, category, price):
		if None in {name, category, price}:
			print('Not all values for product provided')
			abort(400)
		if self.check_product(name):
			print('Product already in inventory')
			abort(400)
		else:
			new_id = self.get_max_id(type='product') + 1
			query = f'INSERT INTO product (name, category, price, id) VALUES ("{name}", "{category}", "{price}", "{new_id})'
			self.session.execute(query)
			self.session.commit()
			return name

	def check_product(self, name):
		product = self.session.query(Product).filter(name=name).first()
		if product == None:
			return False
		return product

	def get_max_id(self, type=None):
		if type == 'product':
			try:
				query = f'SELECT id FROM product'
				id = self.session.execute(query).fetchall()
				id = max([x[0] for x in id])
			except:
				id = 0
		elif type == 'user':
			try:
				query = f'SELECT id FROM user'
				id = self.session.execute(query).fetchall()
				id = max([x[0] for x in id])
			except:
				id = 0
		return id
		