from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Developers(db.Model):
    __tablename__ = 'developers'
    login:str = db.Column(db.String(255), nullable=False, primary_key=True)
    core:int = db.Column(db.Boolean)

class DevelopersSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("login", "core")

Developers_schema = DevelopersSchema(many=True)

