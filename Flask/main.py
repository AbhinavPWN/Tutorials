from flask import Flask, render_template
from utils import check

app = Flask(__name__, template_folder='template')


@app.route('/')
def hello_world():
    return render_template('index.html', name='Abhinav karki',role='admin')


@app.route('/home/<int:id>')
def home_fxn(id):
    print('id', id)
    return '<h1>home call</h1>'


@app.route('/books')
def homebook():
    return 'Here is book list'


if __name__ == '__main__':
    check()
    app.run(debug=True)
