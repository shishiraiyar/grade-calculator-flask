from flask import Flask, render_template, request

from maxMarksService import MaxMarksService
from marksEntryService import MarksEntryService

app = Flask(__name__)
maxMarksService = MaxMarksService("maxMarks.json")
marksEntryService = MarksEntryService()

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
    maxMarksService.write(testName, data)

    return {"status": "success"}

@app.route('/subjects/<subjectName>')
def getSubject(subjectName):
    data = maxMarksService.read(subjectName)
    return render_template("marksEntry.html", subjectName=subjectName, data=data)
    

@app.route('/marksEntry', methods=['POST'])
def marksEntry():
    data = request.get_json()
    
    subjectName = data["subjectName"]
    email = data["email"]

    maxMarks = maxMarksService.read(subjectName)

    # marksEntryService.validate(data, maxMarks)
    marksEntryService.insertStudentMarks(subjectName, email, data)
    # validate (marks, maxmarks)
    # insert (subjectName, email, marks)


    # db.write(subjectName, data)
    return {"status": "success"}

if __name__ == '__main__':
    app.run()
