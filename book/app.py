from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='cwW2skhDXdNDZP5DzZpWTA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(debug=True, port=5002)