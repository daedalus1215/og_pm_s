from flask import Flask
from routes import order_blueprint
from models import db, init_app

# @TODO: Left off here
app = Flask(__name__)

app.config['SECRET_KEY'] = 'TsYeND1-eUJmO_SQa_bHLw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/order,db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint

if __name__ == '__main__':
    app.run(debug=True, ports=5003)