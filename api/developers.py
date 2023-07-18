from flask import Blueprint
from flask import jsonify

from models.local import Developers, Developers_schema

developers_bp = Blueprint('developers', __name__)

@developers_bp.route('/')
def list():
    return jsonify({
        'login':'chenkx',
        'name':'Jimit',
        'address':'china'
        })

@developers_bp.route('/core/')
@developers_bp.route('/core/<int:page>')
def list_deveplopers(page=1):
    per_page = 10
    users = Developers.query.paginate(page=page, per_page=per_page, error_out=False)
    return Developers_schema.dump(users)

