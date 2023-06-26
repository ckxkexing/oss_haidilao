from flask import Flask

from developers import developers_bp
from repos import repos_bp

app = Flask(__name__)

app.register_blueprint(developers_bp, url_prefix='/developers')
app.register_blueprint(repos_bp, url_prefix='/repos')

