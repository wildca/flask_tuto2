from flask import render_template, request, jsonify

from app import app

@app.route('/ajax-1')
def ajax_1():
    return render_template("ajax-1.html")


@app.route('/ajax-multiplication-numbers')
def multiplication_numbers():
    number_a = request.args.get('a', 0, type=int) # default value=0
    number_b = request.args.get('b', 0, type=int)
    result = number_a * number_b
    return jsonify(result_from_server=result)
