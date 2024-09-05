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
    

@app.route('/marksEntry', methods=['POST'])
def marksEntry():
    data = request.get_json()
    subjectName = data["subjectName"]
    email = data["email"]

    db.write(subjectName, data)
    return {"status": "success"}

if __name__ == '__main__':
    app.run()


{
  "email1": {
    "Test 1": [
      {
        "questionName": "1",
        "marks": 10
      },
      {
        "questionName": "2",
        "marks": 10
      },
      {
        "questionName": "3a",
        "marks": 5
      },
      {
        "questionName": "3b",
        "marks": 5
      },
      {
        "questionName": "4",
        "marks": 10
      },
      {
        "questionName": "5",
        "marks": 10
      }
    ],
    "Test 2": [
      {
        "questionName": "1",
        "marks": 10
      },
      {
        "questionName": "2",
        "marks": 10
      },
      {
        "questionName": "3a",
        "marks": 5
      },
      {
        "questionName": "3b",
        "marks": 5
      },
      {
        "questionName": "4",
        "marks": 10
      },
      {
        "questionName": "5",
        "marks": 10
      }
    ]
  },
  "email2": {
    "Test 1": [
      {
        "questionName": "1",
        "marks": 10
      },
      {
        "questionName": "2",
        "marks": 10
      },
      {
        "questionName": "3a",
        "marks": 5
      },
      {
        "questionName": "3b",
        "marks": 5
      },
      {
        "questionName": "4",
        "marks": 10
      },
      {
        "questionName": "5",
        "marks": 10
      }
    ],
    "Test 2": [
      {
        "questionName": "1",
        "marks": 10
      },
      {
        "questionName": "2",
        "marks": 10
      },
      {
        "questionName": "3a",
        "marks": 5
      },
      {
        "questionName": "3b",
        "marks": 5
      },
      {
        "questionName": "4",
        "marks": 10
      },
      {
        "questionName": "5",
        "marks": 10
      }
    ]
  }
}