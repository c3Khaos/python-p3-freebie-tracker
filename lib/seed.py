#!/usr/bin/env python3
from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

c1 = Company(name="Apple", founding_year=1976)
c2 = Company(name="Google", founding_year=1998)

d1 = Dev(name="Alice")
d2 = Dev(name="Bob")

session.add_all([c1, c2, d1, d2])
session.commit()

f1 = c1.give_freebie(d1, "Sticker", 1)
f2 = c2.give_freebie(d1, "T-shirt", 10)
f3 = c2.give_freebie(d2, "Water Bottle", 5)

session.add_all([f1, f2, f3])
session.commit()

# Script goes here!
