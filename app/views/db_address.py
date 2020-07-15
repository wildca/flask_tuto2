from flask import render_template, redirect

from sqlalchemy import exists

from app import app, session
from app.model.Address import Address


@app.route('/address', methods=['GET'])
def address():
    result = session.query(Address)
    print session.query(Address).count()
    print result
    return render_template('address.html', addresses=result)

@app.route('/address-delete/<int:id>', methods=['GET'])
def addressDelete(id):
    if session.query(exists().where(Address.id == id)).scalar():
        session.query(Address).filter_by(id=id).delete()
        session.commit()
    return redirect('/address')

