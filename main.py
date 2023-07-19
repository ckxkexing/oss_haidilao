from flask import Flask

from api.centrality_score import centrality_score_bp
from models.database import db, ma
from models.config import local_db_config
from models.config import metrics_db_config
from models.config import ck_db_config

from api.developers import developers_bp
from api.repos import repos_bp
from api.pulls import pulls_bp

app = Flask(__name__)


SQLALCHEMY_BINDS = {
    local_db_config.bind_name : local_db_config.SQLALCHEMY_DATABASE_URI,
    metrics_db_config.bind_name : metrics_db_config.SQLALCHEMY_DATABASE_URI,
    ck_db_config.bind_name : ck_db_config.SQLALCHEMY_DATABASE_URI
}
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS


db.init_app(app)
ma.init_app(app)

app.register_blueprint(developers_bp, url_prefix='/developers')
app.register_blueprint(repos_bp, url_prefix='/repos')
app.register_blueprint(centrality_score_bp,url_prefix='/centrality_score')
app.register_blueprint(pulls_bp, url_prefix='/pulls')

