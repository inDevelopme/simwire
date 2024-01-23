from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, default='donotactivate@company.com')
    email = db.Column(db.String(120), unique=True, nullable=False,  default='donotactivate@company.com')
    # default is "password"
    password = db.Column(db.String(200), nullable=False, default='$pbkdf2-sha256$29000$cs65N8a4d25tTamVEsJY6w$ajG1MzwCeEBdsVKqwyUo7gutByshm5rC7IrPIm6CXW4')

    def __init__(self, username):
        self.username = username
        # self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

    # Implement required UserMixin methods and properties
    def is_authenticated(self):
        return True  # Assuming all users are authenticated

    def is_active(self):
        return True  # Assuming all users are active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
