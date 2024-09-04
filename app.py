from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/createTest')
def create_test_page():
    return render_template('createTestPage.html')



if __name__ == '__main__':
    app.run()