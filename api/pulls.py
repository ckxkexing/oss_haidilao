from flask import Blueprint
from flask import jsonify
from sqlalchemy import text

from models.ck import GithubPullRequests, github_pull_requests_schema
from models.ck import execute_raw_sql

pulls_bp = Blueprint('pulls', __name__)

########################################
### list pull requests
########################################

@pulls_bp.route('/')
@pulls_bp.route('/<int:page>')
def list_pulls(page=1):
    per_page = 10
    info = GithubPullRequests.query.paginate(page=page, per_page=per_page, error_out=False)
    return github_pull_requests_schema.dump(info)

@pulls_bp.route('/list/<owner>/<repo>')
@pulls_bp.route('/list/<owner>/<repo>/<int:page>')
def list_repo_pulls(owner, repo, page=1):
    per_page = 10
    info = GithubPullRequests.query.filter(
                GithubPullRequests.search_key__owner==owner, 
                GithubPullRequests.search_key__repo==repo
        ).paginate(page=page, per_page=per_page, error_out=False)
    return github_pull_requests_schema.dump(info)

########################################
### project pulls current state
########################################

@pulls_bp.route('/count/<owner>/<repo>')
def cnt_pull_requests(owner, repo):
    # 
    pulls_count = GithubPullRequests.query.filter(
                GithubPullRequests.search_key__owner==owner, 
                GithubPullRequests.search_key__repo==repo
            ).count()

    res = {"owner": owner, "repo" :repo, "pulls_count": pulls_count}
    return jsonify(res)

########################################
### pull_request state
########################################

@pulls_bp.route('/detail/<owner>/<repo>/<number>')
def pull_request_features_at_open(owner, repo, number):
    res = {}
    #
    # Project Dimension

    ret = execute_raw_sql(text("""
                select count(gpr.id) as open_pr_num from github_pull_requests as gpr
                where gpr.search_key__owner=:owner and gpr.search_key__repo=:repo
                    and gpr.closed_at = NULL
            """), {"owner":owner, "repo":repo})
    open_pr_num = ret.first()['open_pr_num']
    res["open_pr_num"] = open_pr_num


    #
    # Pull Request Dimension


    #
    # Owner Dimension


    return jsonify(res)
