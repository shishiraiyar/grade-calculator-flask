import os
import csv
import math

FILE_PREFIX = "csv/"

class MarksEntryService:
    def __init__(self):
        pass
    
    def validateStudentMarks(self, marks, maxMarks):
        pass

    def insertStudentMarks(self, subjectName, studentEmail, marks, maxMarks):
        filename = FILE_PREFIX + subjectName + ".csv"
        if not os.path.exists(filename):
            self.createCSVFile(filename, marks)

        row = [studentEmail]

        testMarks = []
        for test in marks["tests"]:
            sum = 0
            for question in marks["tests"][test]:
                row.append(question["marks"])
                sum += int(question["marks"]) if question["marks"] else 0
            row.append(sum)
            testMarks.append(sum)

        testMarks.sort(reverse=True)
        testTotal = testMarks[0] + testMarks[1]
        row.append(testTotal)

        quizMarks = []
        for quiz in marks["quizzes"]:
            sum = 0
            for question in marks["quizzes"][quiz]:
                row.append(question["marks"])
                sum += int(question["marks"]) if question["marks"] else 0
            row.append(sum)
            quizMarks.append(sum)

        quizMarks.sort(reverse=True)
        quizTotal = quizMarks[0] + quizMarks[1]
        row.append(quizTotal)

        sum = 0
        for question in marks["el"]:
            sum += int(question["marks"]) if question["marks"] else 0
            row.append(question["marks"])
        row.append(sum)
        
        testCoefficient = int(maxMarks["testCoefficient"])
        quizCoefficient = int(maxMarks["quizCoefficient"])
        elCoefficient = int(maxMarks["elCoefficient"])

        total = testTotal*testCoefficient + quizTotal*quizCoefficient + sum*elCoefficient
        
        row.append(math.ceil(total))

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def createCSVFile(self, filename, marks):
        header = ["email"]

        for test in marks["tests"]:
            for question in marks["tests"][test]:
                header.append(test + "_" + question["questionName"])
            header.append(test + "_total")

        header.append("bestTwoTotal")

        for quiz in marks["quizzes"]:
            for question in marks["quizzes"][quiz]:
                header.append(quiz + "_" + question["questionName"])
            header.append(quiz + "_total")

        header.append("bestTwoTotal")

        for el in marks["el"]:
            header.append("el_" + el["questionName"])
        header.append("el_total")
        
        header.append("total")

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

        





if __name__ == "__main__":
    db = MarksEntryService()
    ab = {
    "tests": {
        "Test 1": [
            {
                "questionName": "1a",
                "marks": ""
            },
            {
                "questionName": "1b",
                "marks": "10"
            },
            {
                "questionName": "2",
                "marks": "10"
            },
            {
                "questionName": "3",
                "marks": "10"
            },
            {
                "questionName": "4",
                "marks": ""
            },
            {
                "questionName": "5a",
                "marks": ""
            },
            {
                "questionName": "5b",
                "marks": ""
            }
        ],
        "Test 2": [
            {
                "questionName": "1",
                "marks": ""
            },
            {
                "questionName": "2a",
                "marks": ""
            },
            {
                "questionName": "2b",
                "marks": ""
            },
            {
                "questionName": "3",
                "marks": ""
            },
            {
                "questionName": "4a",
                "marks": ""
            },
            {
                "questionName": "4b",
                "marks": ""
            },
            {
                "questionName": "5",
                "marks": ""
            }
        ],
        "Test 3": [
            {
                "questionName": "1",
                "marks": ""
            },
            {
                "questionName": "2",
                "marks": ""
            },
            {
                "questionName": "3",
                "marks": ""
            },
            {
                "questionName": "4a",
                "marks": ""
            },
            {
                "questionName": "4b",
                "marks": ""
            },
            {
                "questionName": "5a",
                "marks": ""
            },
            {
                "questionName": "5b",
                "marks": ""
            },
            {
                "questionName": "5c",
                "marks": ""
            }
        ]
    },
    "quizzes": {
        "Quiz 1": [
            {
                "questionName": "1",
                "marks": ""
            },
            {
                "questionName": "2",
                "marks": ""
            },
            {
                "questionName": "3",
                "marks": ""
            },
            {
                "questionName": "4",
                "marks": ""
            },
            {
                "questionName": "5",
                "marks": ""
            },
            {
                "questionName": "6",
                "marks": ""
            },
            {
                "questionName": "7",
                "marks": ""
            }
        ],
        "Quiz 2": [
            {
                "questionName": "1",
                "marks": ""
            },
            {
                "questionName": "2",
                "marks": ""
            },
            {
                "questionName": "3",
                "marks": ""
            },
            {
                "questionName": "4",
                "marks": ""
            },
            {
                "questionName": "5",
                "marks": ""
            },
            {
                "questionName": "6",
                "marks": ""
            },
            {
                "questionName": "7",
                "marks": ""
            },
            {
                "questionName": "8",
                "marks": ""
            }
        ],
        "Quiz 3": [
            {
                "questionName": "1",
                "marks": ""
            },
            {
                "questionName": "2",
                "marks": ""
            },
            {
                "questionName": "3",
                "marks": ""
            },
            {
                "questionName": "4",
                "marks": ""
            },
            {
                "questionName": "5",
                "marks": ""
            },
            {
                "questionName": "6",
                "marks": ""
            },
            {
                "questionName": "7",
                "marks": ""
            },
            {
                "questionName": "8",
                "marks": ""
            },
            {
                "questionName": "9",
                "marks": ""
            },
            {
                "questionName": "10",
                "marks": ""
            }
        ]
    },
    "el": [
        {
            "questionName": "Phase 1",
            "marks": ""
        },
        {
            "questionName": "Phase 2",
            "marks": ""
        }
    ],
    "email": "a",
    "subjectName": "Web Programming"
}
    
    # db.createCSVFile("Web Programming.csv", ab)

    db.insertStudentMarks("Web Programming", "a@a.com", ab)
