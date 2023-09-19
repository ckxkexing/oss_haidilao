from .database import db, ma
from .config import metrics_db_config as db_config
from datetime import datetime

### session for raw sql execute
def execute_raw_sql(query, params):
    res = db.session.execute(query, params,
                          bind=db.get_engine(db_config.bind_name))
    return res.mappings()

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

# Nloc
class Nloc(db.Model):
    __tablename__ = 'repo_code_metrics'
    __bind_key__ = db_config.bind_name
    id:int = db.Column(db.Integer, primary_key=True)
    owner:str = db.Column(db.String(255))
    repo:str = db.Column(db.String(255))
    created_at:datetime = db.Column(db.DateTime,default=datetime.now)
    sha:str = db.Column(db.String(255))
    nloc:int = db.Column(db.Integer)
    average_nloc: float = db.Column(db.Float)
    average_cyclomatic_complexity: float = db.Column(db.Float)
    average_token_count: float = db.Column(db.Float)

class NlocSchema(ma.Schema):
    class Meta:
        fields = ("owner", "repo", "created_at", "sha", "nloc", "average_nloc", "average_cyclomatic_complexity", "average_token_count")


Nloc_schema = NlocSchema(many=True)


