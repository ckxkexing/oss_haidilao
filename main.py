from flask import Flask

from sources.database import db, ma
from sources.models import db_config as models_config
from sources.metrics import db_config as metrics_config

from api.developers import developers_bp
from api.repos import repos_bp

app = Flask(__name__)


SQLALCHEMY_BINDS = {
    models_config.bind_name : models_config.SQLALCHEMY_DATABASE_URI,
    metrics_config.bind_name : metrics_config.SQLALCHEMY_DATABASE_URI
}
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS


db.init_app(app)
ma.init_app(app)

app.register_blueprint(developers_bp, url_prefix='/developers')
app.register_blueprint(repos_bp, url_prefix='/repos')

