from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__,instance_relative_config=True)
app.config['SECRET_KEY']='LongAndRandomSecretKey'
app.config.from_pyfile('config.py')
csrf = CSRFProtect(app)
#db = SQLAlchemy(app)
#migrate=Migrate(app,db)

from apyts.guest.routes import guests

app.register_blueprint(guests)
