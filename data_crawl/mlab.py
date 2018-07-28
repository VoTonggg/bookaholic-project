import mongoengine

# mongodb://<admin>:<admin1>@ds141671.mlab.com:41671/bookcompare-project

host = 'ds141671.mlab.com'
port = 41671
db_name = 'bookcompare-project'
user_name = 'admin'
password = 'admin1'

def connect():
    mongoengine.connect(db_name, host=host, port=port,username=user_name, password = password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())