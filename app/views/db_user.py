from flask import render_template, redirect, request, url_for

from sqlalchemy import exists
from sqlalchemy.orm import joinedload, lazyload

from app import app, session
from app.model.User import User
from app.model.Address import Address


@app.route('/user', methods=['GET'])
def users():

    result_users = session.query(User)#.join(User.address).all()
    result_addresses = session.query(Address)

    print session.query(User).count()
    return render_template('user.html',
                           users=result_users,
                           addresses=result_addresses)


@app.route('/user-add', methods=['POST'])
def add_user():
    name = request.form['name']
    mail = request.form['email']
    nick = request.form['nick']
    address_id = request.form['address']

    address = session.query(Address).filter_by(id=address_id).scalar()

    u = User()
    u.name = name
    u.email = mail
    u.nick = nick
    u.address = address
    session.commit()

    return redirect(url_for('users'))



@app.route('/user-delete/<int:id>', methods=['GET'])
def userDelete(id):
    if session.query(exists().where(User.id == id)).scalar():
        session.query(User).filter_by(id=id).delete()
        session.commit()
    return redirect('/user')

