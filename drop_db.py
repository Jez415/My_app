## Drop DB
from app import app, db

with app.app_context():
    db.drop_all()
