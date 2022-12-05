from flask import Flask, Request, Response
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/ws'
mongo = PyMongo(app)

@app.route('/user', methods=['POST'])
def create_user():
  return ()

@app.route('/data', methods=['POST'])
def create_data():
  data = Request.get_json()
  post_data = mongo.db.data.insert_one(data)
  print(post_data)
  return "OK"

@app.route('/data', methods=['GET'])
def get_data():
  data = mongo.db.data.find()
  print(len(list(get_data)))
  return Response(json_util.dumps({'page' : data}),
    mimetype='application/json')

if __name__ == "__main__":
  app.run(debug=True)