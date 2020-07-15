from flask import render_template, request, jsonify
import json

from app import app

@app.route('/ajax-2')
def ajax_2():
    return render_template("ajax-2.html")


@app.route('/ajax-user', methods=['POST'])
def multiplication_numbers_2():
    name = request.form['name']
    mail = request.form['mail']

    reply_name = name[0:].upper()
    reply_mail = mail[0:].upper()

    json_reply = json.dumps(
        {"nameUpper" : reply_name,
         "mailUpper" : reply_mail
        }
    )

    return  json_reply
