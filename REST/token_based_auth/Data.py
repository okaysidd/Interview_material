from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


class Data:
	def __init__(self):
		engine = create_engine('sqlite:///usersWithTokens.db')
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()

	def create_user(self, username, password):
		user = User(username=username)
		user.hash_password(password)
		self.session.add(user)
		self.session.commit()
		return user.username, user.id

	def get_user(self, id=None):
		if id == None:
			users = self.session.query(User).all()
			return jsonify({"usernames":[user.username for user in users], \
				"passwords":[user.password_hash for user in users]})
		else:
			user = self.session.query(User).filter_by(id=id).one()
			return jsonify({"username":user.username, "password":user.password_hash})

	def check_user(self, username=None, id=None):
		if not username and not id:
			abort(400)
		if username != None:
			user = self.session.query(User).filter_by(username=username).first()
			if user != None:
				return user
			else:
				return False
		elif id != None:
			user = self.session.query(User).filter_by(id=id).first()
			print(f'USER - {user}')
			if user != None:
				return user
			else:
				return False
