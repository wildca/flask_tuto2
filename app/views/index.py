from flask import render_template

from app import app

@app.route('/', methods=['GET'])
@app.route('/index')
@app.route('/welcome')
def index():
    user = {'name': 'Martin'}
    posts = [ # array
        {
            'author': {'name': 'John'},
            'content': 'Hello!'
        },
        {
            'author': {'name': 'Doe'},
            'content': 'World!'
        }
    ]
    return render_template("index.html",
                           title='Home page',
                           user=user,
                           posts=posts)
