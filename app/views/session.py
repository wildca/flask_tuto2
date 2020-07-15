from flask import session, request, url_for, redirect, abort, render_template

from app import app

@app.route('/session', methods=['GET'])
def sessionGet():
    return render_template('session.html')

@app.route('/session', methods=['POST'])
def sessionPost():
    # session['key'] = 'value'
    session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message')) # python function name

@app.route('/session-message')
def message():
    if not 'username' in session:
        return abort(403)
    return render_template('session-message.html',
                            username=session['username'],
                            message=session['message']
                           )

@app.route('/session-clear')
def session_clear():
    session.clear()
    return redirect('/') # python function name
