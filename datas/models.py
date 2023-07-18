from .database import db, ma
from .metrics_config import db_config


# class db_config(object):
#     bind_name = "models"
#
#     account = 'root'  # 账号
#     password = 'root'  # 填入密码
#     proname = 'core_developers'  # 填入数据库名
#     ip = ''  # 填入服务器网址
#     port = '3306'  # 端口
#     SECRET_KEY = "hahahaha"  # session密钥hhhhhhhh
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(account, password, ip, port, proname)
#     # print(SQLALCHEMY_DATABASE_URI)
#     SQLALCHEMY_TRACK_MODIFICATIONS = True


###
#    developers table
###
class Developers(db.Model):
    __tablename__ = 'developers'
    __bind_key__ = db_config.bind_name
    login:str = db.Column(db.String(255), nullable=False, primary_key=True)
    core:int = db.Column(db.Boolean)

class DevelopersSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("login", "core")

Developers_schema = DevelopersSchema(many=True)


###
#   repos table
###

# sloc
class Sloc(db.Model):
    __tablename__ = 'sloc'
    __bind_key__ = db_config.bind_name
    owner:str = db.Column(db.String(255))
    repo:str = db.Column(db.String(255))
    commit:str = db.Column(db.String(255), primary_key=True)
    sloc:int = db.Column(db.Integer)


class SlocSchema(ma.Schema):
    class Meta:
        fields = ("owner", "repo", "commit", "sloc")


Sloc_schema = SlocSchema(many=True)


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
