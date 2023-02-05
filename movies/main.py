from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def movies():
    return render_template('home.html', list1=['Avatar', 'Mota', 'JenishChaks'])


@app.route('/movies')
def add():
    return render_template('add.html')


@app.route('/add', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return 'new movie ' + request.form['name']
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
