from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_kanji.config')
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

from flask_kanji.views import views