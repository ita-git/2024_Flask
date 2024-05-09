from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('holiday_maintenance.config')

db = SQLAlchemy(app)

from holiday_maintenance.views import input, list, maintenance_date
