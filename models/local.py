from .database import db, ma
from .config import local_db_config as db_config


###
#    developers table
###
class Developers(db.Model):
    __tablename__ = 'developers'
    __bind_key__ = db_config.bind_name
    login:str = db.Column(db.String(255), nullable=False, primary_key=True)
    core:int = db.Column(db.Boolean)

class DevelopersSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("login", "core")

Developers_schema = DevelopersSchema(many=True)


###
#   repos table
###

# sloc
class Sloc(db.Model):
    __tablename__ = 'sloc'
    __bind_key__ = db_config.bind_name
    owner:str = db.Column(db.String(255))
    repo:str = db.Column(db.String(255))
    commit:str = db.Column(db.String(255), primary_key=True)
    sloc:int = db.Column(db.Integer)


class SlocSchema(ma.Schema):
    class Meta:
        fields = ("owner", "repo", "commit", "sloc")


Sloc_schema = SlocSchema(many=True)


