from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)
 
students = [
    Student(1,"Suraj Soma"),
    Student(2,"Hemant Bhosale"),
    Student(3,"Rahul Pandey")
]


def to_serializable(val):
    if isinstance(val, Student):
        strStudent = {
            'sid': val.sid,
            'name': val.name
        }
        return strStudent

@app.route("/students", methods=['GET'])
def getAll():
    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)

@app.route("/students/<int:sid>", methods=['GET'])
def get(sid):
    for student in students:
        if student.sid==sid:
            return jsonify(to_serializable(student))
    return 'student not found'
 
@app.route("/students", methods=['POST'])
def add():
    students.append(Student(request.form['sid'], request.form['name']))
    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)
 
@app.route("/students/<int:sid>/", methods=['DELETE'])
def remove(sid):
    print(sid)
    for student in students:
        if student.sid==sid:
            students.remove(student)
    
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)
 
if __name__ == "__main__":
    app.run(port=5050)