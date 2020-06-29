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

#ADD a /users route here

#protect this route with a required login
@app.route('/bagels', methods = ['GET','POST'])
# @auth.login_required
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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)