from flask import Flask
import models
from routes import user_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vZK7siKrV8BL46KsyAIPoQ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run()