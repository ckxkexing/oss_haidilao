from .database import db, ma
from .config import ck_db_config as db_config

from sqlalchemy import String, Boolean, Integer, DateTime

### session for raw sql execute
def execute_raw_sql(query, params):
    res = db.session.execute(query, params,
                          bind=db.get_engine(db_config.bind_name))
    # return dict
    return res.mappings()

### TABLES

class GithubPullRequests(db.Model):
    __tablename__ = 'github_pull_requests'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(Integer, primary_key=True)
    number: int = db.Column(Integer)
    url: str = db.Column(String)
    html_url: str = db.Column(String)
    created_at = db.Column(DateTime)
    search_key__owner = db.Column(String)
    search_key__repo = db.Column(String)


class GithubPullRequestsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "number", "url", "html_url", "created_at", "search_key__owner", "search_key__repo")

github_pull_requests_schema = GithubPullRequestsSchema(many=True)
