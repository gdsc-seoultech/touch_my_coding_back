#src/database.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()