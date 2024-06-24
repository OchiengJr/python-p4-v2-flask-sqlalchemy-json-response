#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from models import Pet  # Ensure models.py contains your Pet model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with metadata
metadata = MetaData()
db = SQLAlchemy(app, metadata=metadata)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Importing models to ensure they are registered with SQLAlchemy
import models  # Make sure models.py contains your Pet model

# Routes or views to interact with Pet model
@app.route('/')
def index():
    return '<h1>Welcome to the Pet Directory!</h1>'

@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    return jsonify([pet.to_dict() for pet in pets])

@app.route('/pet/<int:id>', methods=['GET'])
def get_pet(id):
    pet = Pet.query.get_or_404(id)
    return jsonify(pet.to_dict())

@app.route('/pet', methods=['POST'])
def create_pet():
    data = request.json
    pet = Pet(name=data['name'], species=data['species'])
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
