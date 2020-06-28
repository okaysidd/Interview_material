from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask import Flask

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


class Data:
	def __init__(self):
		engine = create_engine('sqlite:///users.db')
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()
		# app = Flask(__name__)

	def check_user(self, username):
		user = self.session.query(User).filter_by(username = username).first()
		if self.session.query(User).filter_by(username = username).first() != None:
			user = self.session.query(User).filter_by(username = username).first()
			return user
		else:
			return False

	def create_user(self, username, password):
		user = User(username=username)
		user.hash_password(password)
		self.session.add(user)
		self.session.commit()
		return user.username, user.id

	def get_users(self, id=None):
		"""
		If id == None, return all users
		"""
		if id != None:
			user = self.session.query(User).filter_by(id=id).one()
			return jsonify({'username': user.username})

		else:
			users = self.session.query(User).all()
			return jsonify({'usernames': [user.username for user in users], 'passwords': [user.password_hash for user in users]})
