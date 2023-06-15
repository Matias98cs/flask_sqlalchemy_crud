from utils.db import db
# from sqlalchemy.types import Integer


class Contact(db.Model):
    # __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
