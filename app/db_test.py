from sqlalchemy import exists

from model.User import User
from model.Address import Address
from app import session


def test_db():
    # INSERT
    if not session.query(exists().where(User.email == 'test@example.net')).scalar():
        u1 = User()
        u1.name = "Test user"
        u1.email = "test@example.net"

        a1 = Address()
        a1.street = "Str 123"
        a1.city = "City WTF"

        u1.address = a1
        session.add(a1)
        session.add(u1)
        session.commit()

    # check if record exists in db:
    # print session.query(Address).filter_by(city='City WTF').count()
    # print bool( session.query(Address).filter_by(city='City WTF').count() )

    #   SELECT
    if session.query(exists().where(Address.city == 'City WTF')).scalar():
        a2 = session.query(Address).filter_by(city='City WTF').first()
        print a2.city

    if bool(session.query(Address).filter_by(city='City WTF').count()):
        a2 = session.query(Address).filter_by(city='City WTF').first()
        print a2.city


    # UPDATE
    if session.query(exists().where(User.email == 'test@example.net')).scalar():
        session.query(User).filter_by(email='test@example.net').update({"nick": "a"})
        session.commit()

    if session.query(exists().where(User.email == 'test@example.net')).scalar():
        u = session.query(User).filter_by(email='test@example.net').first()
        u.nick = "b"
        session.commit()


    # DELETE
    if session.query(exists().where(User.email == 'test@example.net')).scalar():
        session.query(User).filter_by(email='test@example.net').delete()
        session.commit()

    if session.query(exists().where(Address.city == 'City WTF')).scalar():
        session.query(Address).filter_by(city='City WTF').delete()
        session.commit()
