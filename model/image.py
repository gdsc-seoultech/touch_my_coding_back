from database import db

class Image(db.Model):

    __tablename__ = "images"

    keyword = db.Column(db.String(20, 'utf8mb4_unicode_ci'), primary_key = True, nullable=False)
    count = db.Column(db.Integer, nullable=10)

