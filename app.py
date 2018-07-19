from flask import *
import mlab
from models.book import Book
import sys

app = Flask(__name__)

# 0. Create connection
mlab.connect()

@app.route('/')
def abcxyz():
   pass