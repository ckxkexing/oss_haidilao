from flask import Flask

from api.centrality_score import centrality_score_bp
from models.database import db, ma
from models.config import metrics_db_config

# from api.developers import developers_bp
from api.repos import repos_bp
# from api.pulls import pulls_bp
from api.network_metrics import network_metrics_bp
from api.developer_metrics import developer_metrics_bp

app = Flask(__name__)


SQLALCHEMY_BINDS = {
    metrics_db_config.bind_name : metrics_db_config.SQLALCHEMY_DATABASE_URI
}
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS


db.init_app(app)
ma.init_app(app)

# # app.register_blueprint(developers_bp, url_prefix='/developers')
app.register_blueprint(repos_bp, url_prefix='/repos')
app.register_blueprint(centrality_score_bp,url_prefix='/centrality_score')
# app.register_blueprint(pulls_bp, url_prefix='/pulls')
app.register_blueprint(network_metrics_bp,url_prefix='/network_metrics')
app.register_blueprint(developer_metrics_bp,url_prefix='/developer_metrics')

