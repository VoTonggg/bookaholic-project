from mongoengine import *

# 1. Design database

class Book(Document):
    title = StringField()
    linkBuy = StringField()
    price_sale = IntField()
    image = StringField()
    retailer = StringField()
    category = StringField()
    title_no_accent = StringField()