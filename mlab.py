import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds141621.mlab.com:41621/bookproject

host = 'ds141621.mlab.com'
port = 41621
db_name = 'bookproject'
user_name = 'bookproject'
password = 'admin123'

def connect():
    mongoengine.connect(db_name, host=host, port=port,username=user_name, password = password)
