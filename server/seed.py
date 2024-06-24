#!/usr/bin/env python3

import random
from faker import Faker
from app import app, db
from models import Pet

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    species = ['Dog', 'Cat', 'Fish', 'Bird']

    for _ in range(10):
        pet = Pet(name=fake.first_name(), species=random.choice(species))
        db.session.add(pet)

    db.session.commit()

    print('Database seeded successfully.')
