from flask import render_template

from app import app

@app.route('/url-path-params/<name>/<int:age>')
def param_2(name, age):
    message = 'User ' + name + ' is ' + str(age) +' years old.'
    return render_template("path_params.html",
                           name=name,
                           age=age,
                           msg=message)
