from flask import Blueprint
from flask import jsonify

from models.ck import GithubPullRequests, github_pull_requests_schema

pulls_bp = Blueprint('pulls', __name__)


@pulls_bp.route('/')
@pulls_bp.route('/<int:page>')
def list_sloc(page=1):
    per_page = 10
    info = GithubPullRequests.query.paginate(page=page, per_page=per_page, error_out=False)
    return github_pull_requests_schema.dump(info)


@pulls_bp.route('/count/<owner>/<repo>')
def cnt_pull_requests(owner, repo):
    info = GithubPullRequests.query.filter(
                GithubPullRequests.search_key__owner==owner, 
                GithubPullRequests.search_key__repo==repo
            ).count()

    res = {"owner": owner, "repo" :repo, "pulls_count": info}
    return jsonify(res)
