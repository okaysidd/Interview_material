from models import Base, User, Bagel
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()


class Data:
	def __init__(self):
		engine = create_engine('sqlite:///bagelShop.db')
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()
	
	def create_user(self, username, password):
		user = User(username=username)
		user.hash_password(password)
		self.session.add(user)
		self.session.commit()
		return user.username, user.id

	def check_entry(self, name, table):
		if table.lower() == 'user':
			user = self.session.query(User).filter_by(username=name).first()
			if user != None:
				return user
			else:
				return False
		elif table.lower() == 'bagel':
			bagel = self.session.query(Bagel).filter_by(name=name).first()
			if bagel != None:
				return bagel
			else:
				return False
		else:
			raise f'Wrong input, such table -{table}- does not exist'

	def create_bagel(self, name, description, picture, price):
		if not name or not description or not picture or not price:
			return {"error": "Missing complete data"}
		bagel = Bagel(name=name, description=description, picture=picture, price=price)
		self.session.add(bagel)
		self.session.commit()
		return bagel.name, bagel.id

	def get_bagels(self):
		bagels = self.session.query(Bagel).all()
		return jsonify({
			bagel.name : 
			[
				bagel.description,
				bagel.price,
				bagel.picture
				] for bagel in bagels})
	
	def get_users(self):
		users = self.session.query(User).all()
		return jsonify({
			user.name : 
			[
				user.username,
				user.password
				] for user in users})
