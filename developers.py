from flask import Blueprint
from flask import jsonify
developers_bp = Blueprint('developers', __name__)

@developers_bp.route('/')
def list():
    return jsonify({
        'login':'chenkx',
        'name':'Jimit',
        'address':'china'
        })

