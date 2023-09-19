from flask import Blueprint
from flask import jsonify

from models.metrics import Test, Test_schema
from models.metrics_repo import Nloc, Nloc_schema
from models.metrics_repo import execute_raw_sql
from sqlalchemy import text

repos_bp = Blueprint('repos', __name__)

@repos_bp.route('/')
def list():
    return jsonify({
        'owner':'kubernetes',
        'repo':'kubernetes',
        'lang':'go'
        })


@repos_bp.route('/test')
def remote_test():
    test = Test.query.all()
    return Test_schema.dump(test)


@repos_bp.route('/nloc/')
@repos_bp.route('/nloc/<int:page>')
def list_sloc(page=1):
    per_page = 10
    info = Nloc.query.paginate(page=page, per_page=per_page, error_out=False)
    return Nloc_schema.dump(info)


@repos_bp.route('/nloc/<owner>/<repo>')
def repo_sloc(owner, repo):
    res = {"owner": owner, "repo": repo}

    ret = execute_raw_sql(text("""
        SELECT
            nloc, average_nloc, average_cyclomatic_complexity, average_token_count
        FROM
            repo_code_metrics rcm
        WHERE
            rcm.owner = :owner AND
            rcm.repo  = :repo  
        """), {"owner":owner, "repo":repo})
    cur = ret.first()
    res.update(cur)

    return jsonify(res)
