form = document.getElementById("marksEntry");

function aggregateFormData(wrapper){
    let questions = wrapper.querySelectorAll('.questionInput');
    let data = []
    for (let question of questions){
        let questionName = question.querySelector('span').textContent;
        let marks = question.querySelector('.marksInput').value;
        data.push(
            {
                questionName: questionName,
                marks: marks
            }
        );
    }
    return data;
}

// console.log(aggregateFormData(document.getElementById("Test 1")));

document.getElementById("submitMarks").addEventListener('click', () => {
    let email = document.getElementById("studentEmail").value;
    let tests = document.querySelectorAll(".test")
    let quizzes = document.querySelectorAll(".quiz")
    let el = document.querySelector(".el")

    let data = {
        tests: {},
        quizzes: {},
        el: []
    }

    for (let test of tests){
        let testName = test.id;
        let questions = aggregateFormData(test);
        data.tests[testName] = questions;
    }

    for (let quiz of quizzes){
        let quizName = quiz.id;
        let questions = aggregateFormData(quiz);
        data.quizzes[quizName] = questions;
    }

    let questions = aggregateFormData(el);
    data.el = questions;

    data["email"] = email;
    data["subjectName"] = document.getElementById("subjectName").textContent;
    console.log(data);

    fetch('/marksEntry', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
});