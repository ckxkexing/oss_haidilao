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
    pr_id = GithubPullRequests.query.filter(
                GithubPullRequests.search_key__owner==owner, 
                GithubPullRequests.search_key__repo==repo,
                GithubPullRequests.number==number
        ).first().id

    res = {"owner": owner, "repo": repo, "number": number, "id": pr_id}

    #
    # Project Dimension

    ret = execute_raw_sql(text("""--sql
        SELECT
            count(distinct (CASE WHEN gpr.created_at < (SELECT created_at FROM github_pull_requests WHERE id = :id limit 1) THEN gpr.id ELSE 0 END)) AS opened_num,
            count(distinct (CASE WHEN gpr.closed_at is not NULL and gpr.closed_at > 1970 and gpr.closed_at < (SELECT created_at FROM github_pull_requests WHERE id = :id limit 1) THEN gpr.id ELSE 0 END)) AS closed_num
        FROM
            github_pull_requests gpr
        WHERE
            gpr.search_key__owner = :owner AND
            gpr.search_key__repo  = :repo  ;
            """), {"owner":owner, "repo":repo, "id":pr_id})
    if cur := ret.first():
        open_pr_num = cur['opened_num'] - cur['closed_num']
    else:
        open_pr_num = -1
    res["open_pr_num"] = open_pr_num

    #
    # Pull Request Dimension


    #
    # Owner Dimension


    return jsonify(res)
