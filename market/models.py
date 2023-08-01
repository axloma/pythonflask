from flask_sqlalchemy import SQLAlchemy
from market import db,login_manager
from market import bycrypt
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    id = db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    password = db.Column(db.String(length=30),nullable=False)
    cpass = db.Column(db.String(length=30),nullable=False)
    email = db.Column(db.String(length=30),nullable=False)
    Item = db.relationship('Item',backref='owned_user',lazy=True)

    @property
    def password_hashed(self):
        return self.password_hashed
    def check_password(self,attempted_password):
        return bycrypt.check_password_hash(self.password,attempted_password)

    @password_hashed.setter
    def password_hashed(self,plain_text_password):
        self.password = bycrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))
    def __repr__(self): #TODO user dender repr to return data in table
        return f'Item {self.name}'
