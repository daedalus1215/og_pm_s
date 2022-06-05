from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(255), unique=True)
    password = db.column(db.String(255), unique=True)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(255), unique=True,nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.column(db.Boolean, default=False)

    def __repr__(self):
        return f'<user {self.id} {self.username}>'

    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'is_admin':self.is_admin,
            'api_key':self.api_key,
            'is_active':self.is_active,
        }