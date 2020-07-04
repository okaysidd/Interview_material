from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
import json

#NEW IMPORTS
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response
import requests

auth = HTTPBasicAuth()

class Data:
	def __init__(self):
		engine = create_engine('sqlite:///usersWithOAuth.db')
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()
	
	def check_user(self, username=None, id=None, email=None):
		if not username and not id:
			print('Missing both')
			abort(400)
		if username != None:
			user = self.session.query(User).filter_by(username=username).one()
		elif id != None:
			user = self.session.query(User).filter_by(id=id).one()
		elif email != None:
			user = self.session.query(User).filter_by(email=email).one()
		if user:
			return user
		return False

	def create_user(self, username, password):
		if not user or not password:
			print('missing arguments')
			abort(400)
		user = User(username=username)
		user.hash_password(password)
		self.session.add(user)
		self.session.commit()
		return user

	def get_user(self, username=None, id=None):
		if not username and not id:
			users = self.session.query(User).all()
			return users
		if username != None:
			try:
				user = self.session.query(User).filter_by(username=username).one()
			except:
				return False
		if id != None:
			try:
				user = self.session.query(User).filter_by(id=id).one()
			except:
				return False
		return user
