from flask import Flask
from routs import mission
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:8520@localhost:5432/missions_wwii'
app.register_blueprint(mission)


if __name__ == '__main__':
    app.run()
