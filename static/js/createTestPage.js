window.onload = function(){
    createForm("Test 1", "test")
    createForm("Test 2", "test")
    createForm("Test 3", "test")
    createForm("Quiz 1", "quiz")
    createForm("Quiz 2", "quiz")
    createForm("Quiz 3", "quiz")
    createForm("EL", "el")
}

function createQuestion(){
    let question = document.createElement('div');
    question.classList.add('questionInput')
    question.innerHTML = `
        <input type="text" class="questionNameInput"/>
        <input type="number" class="maxMarksInput"/>
        <button class="questionDeleteButton" tabindex="-1">❌</button>
    `;
    let deleteButton = question.querySelector('.questionDeleteButton');
    deleteButton.addEventListener('click', () => {
        question.remove();
    });
    return question
}

function createForm(name, type){
    let wrapper = document.createElement('div');
    wrapper.id = name;
    wrapper.classList.add(type)

    let header = document.createElement('h1');
    header.innerHTML = name;
    wrapper.appendChild(header);

    let form = document.createElement('form');

    let addQuestionButton = document.createElement('button');
    addQuestionButton.innerHTML = "Add Question";

    addQuestionButton.addEventListener('click', () => {
        let question = createQuestion();
        
        form.appendChild(question);
        question.querySelector('.questionNameInput').focus();
    });

    wrapper.appendChild(form);
    wrapper.appendChild(addQuestionButton);

    document.body.appendChild(wrapper);
    
}


function aggregateFormData(wrapper){
    let questions = wrapper.querySelectorAll('.questionInput');
    let data = []
    for (let question of questions){
        let questionName = question.querySelector('.questionNameInput').value;
        let maxMarks = question.querySelector('.maxMarksInput').value;
        data.push(
            {
                question: questionName,
                maxMarks: maxMarks
            }   
        )
    }
    return data

}


let submitButton = document.getElementById('submit');

submitButton.addEventListener('click', () => {
    console.log("submit clicked");
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

    console.log(data);
    
 

});
