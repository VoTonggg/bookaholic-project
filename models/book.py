from mongoengine import *

# 1. Design database

class Book(Document):
    name = StringField()
    link = StringField()
    price = StringField()
    img = StringField()