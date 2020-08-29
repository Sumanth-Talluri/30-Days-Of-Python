from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import requests
import os


app = Flask(__name__)

#
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']  # accessing the database


@app.route('/api/v1.0/students', methods=['GET'])
def students():
    return Response(json.dumps(students), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return


# this decorator create the home route
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    query = {"_id": ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
