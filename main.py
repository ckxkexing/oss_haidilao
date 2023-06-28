from flask import Flask
from models import db, ma

from blueprints.developers import developers_bp
from blueprints.repos import repos_bp

app = Flask(__name__)
app.config.from_object('setting.db_config') #载入配置文件
db.init_app(app)
ma.init_app(app)

app.register_blueprint(developers_bp, url_prefix='/developers')
app.register_blueprint(repos_bp, url_prefix='/repos')

