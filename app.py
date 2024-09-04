from flask import Flask, render_template, request

from database import Database

app = Flask(__name__)
db = Database("data.json")

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/subjects')
def create_test_page():
    return render_template('createSubjectPage.html')

@app.route('/createSubject', methods=['POST'])
def createTests():
    data = request.get_json()

    testName = data["subjectName"]
    db.write(testName, data)

    return {"status": "success"}

@app.route('/subjects/<subjectName>')
def getSubject(subjectName):
    data = db.read(subjectName)
    return render_template("marksEntry.html", subjectName=subjectName, data=data)
    

if __name__ == '__main__':
    app.run()