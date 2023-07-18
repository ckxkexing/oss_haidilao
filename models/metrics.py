from .database import db, ma

from .config import metrics_db_config as db_config

###
#   metric table
###
class Test(db.Model):
    __tablename__ = 'test_tb'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)

class TestSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id",)

Test_schema = TestSchema(many=True)

class CentralityScore(db.Model):
    __tablename__ = 'centrality_score'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    repo: str = db.Column(db.String(255))
    page_rank: float = db.Column(db.Float)
    betweenness_centrality: float = db.Column(db.Float)
    closeness_centrality: float = db.Column(db.Float)
    total_score: float = db.Column(db.Float)


class CentralityScoreSchema(ma.Schema):
    class Meta:
        fields = ("id", "repo", "page_rank", "betweenness_centrality", "closeness_centrality", "total_score")


centrality_score_schema = CentralityScoreSchema(many=True)


class ContributedReposRole(db.Model):
    __tablename__ = 'contributed_repos_role'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    author_email: str = db.Column(db.String(255))
    repo_count: int = db.Column(db.Integer)


class ContributedReposRoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "author_email", "repo_count")


contributed_repos_role_schema = ContributedReposRoleSchema(many=True)


class TotalFixIntensity(db.Model):
    __tablename__ = 'total_fix_intensity'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    author_email: str = db.Column(db.String(255))
    total_fix_intensity: int = db.Column(db.Integer)


class TotalFixIntensitySchema(ma.Schema):
    class Meta:
        fields = ("id", "author_email", "total_fix_intensity")


total_fix_intensity_role_schema = TotalFixIntensitySchema(many=True)


class ContributionGraph(db.Model):
    __tablename__ = 'contribution_graph_data'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    cntrb_login: str = db.Column(db.String(255))
    repo_name: str = db.Column(db.String(255))
    total_contributions: int = db.Column(db.Integer)


class ContributionGraphSchema(ma.Schema):
    class Meta:
        fields = ("cntrb_login", "repo_name", "total_contributions")


contribution_graph_data_schema = ContributionGraphSchema(many=True)


class PeersAverageFixIntensity(db.Model):
    __tablename__ = 'peers_average_fix_intensity_role'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    repo: str = db.Column(db.String(255))
    author_email: str = db.Column(db.String(255))
    average_fix_intensity: float = db.Column(db.Float)


class PeersAverageFixIntensitySchema(ma.Schema):
    class Meta:
        fields = ("repo", "author_email", "average_fix_intensity")


peers_average_fix_intensity_role_schema = PeersAverageFixIntensitySchema(many=True)


class DeveloperRolesMetrics(db.Model):
    __tablename__ = 'developer_roles_metrics'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    author_email: str = db.Column(db.String(255))
    total_fix_commit_count: int = db.Column(db.Integer)
    maximum_fix_commit_count: int = db.Column(db.Integer)
    repo_count: int = db.Column(db.Integer)


class DeveloperRolesMetricsSchema(ma.Schema):
    class Meta:
        fields = ("author_email", "total_fix_commit_count", "maximum_fix_commit_count", "repo_count")


developer_roles_metrics_schema = DeveloperRolesMetricsSchema(many=True)
