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


class NetworkMetrics(db.Model):
    __tablename__ = 'network_metrics'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)
    repo: str = db.Column(db.String(255))
    month: str = db.Column(db.String(255))
    num_nodes: int = db.Column(db.Integer)
    num_edges: int = db.Column(db.Integer)
    num_collaborations: int = db.Column(db.Integer)
    in_degree_centrality: float = db.Column(db.Float)
    out_degree_centrality: float = db.Column(db.Float)
    triangles: float = db.Column(db.Float)
    transitivity: float = db.Column(db.Float)
    clustering: float = db.Column(db.Float)
    reciprocity: float = db.Column(db.Float)
    density: float = db.Column(db.Float)
    components_number: int = db.Column(db.Integer)
    avg_degree: float = db.Column(db.Float)


class NetworkMetricsSchema(ma.Schema):
    class Meta:
        fields = ("id", "repo", "month", "num_nodes", "num_edges", "num_collaborations", "in_degree_centrality", "out_degree_centrality", "triangles", "transitivity",
                  "clustering", "reciprocity", "density", "components_number", "avg_degree")


Network_metrics_schema = NetworkMetricsSchema(many=True)


class PrivilegeEvents(db.Model):
    __tablename__ = 'privilege_events'
    __bind_key__ = db_config.bind_name
    actor_login: str = db.Column(db.String(255))
    added_to_project: int = db.Column(db.Integer)
    converted_note_to_issue: int = db.Column(db.Integer)
    deployed: int = db.Column(db.Integer)
    deployment_environment_changed: int = db.Column(db.Integer)
    locked: int = db.Column(db.Integer)
    merged: int = db.Column(db.Integer)
    moved_columns_in_project: int = db.Column(db.Integer)
    pinned: int = db.Column(db.Integer)
    removed_from_project: int = db.Column(db.Integer)
    review_dismissed: int = db.Column(db.Integer)
    transferred: int = db.Column(db.Integer)
    unlocked: int = db.Column(db.Integer)
    unpinned: int = db.Column(db.Integer)
    user_blocked: int = db.Column(db.Integer)


class PrivilegeEventsSchema(ma.Schema):
    class Meta:
        fields = ("actor_login", "added_to_project", "converted_note_to_issue",
                              "deployed", "deployment_environment_changed",
                              "locked", "merged", "moved_columns_in_project",
                              "pinned", "removed_from_project",
                              "review_dismissed", "transferred",
                              "unlocked", "unpinned", "user_blocked")


Privilege_events_schema = PrivilegeEventsSchema(many=True)


class CountMetrics(db.Model):
    __tablename__ = 'count_metrics'
    __bind_key__ = db_config.bind_name
    author_name: str = db.Column(db.String(255))
    commit_num: int = db.Column(db.Integer)
    line_of_code: int = db.Column(db.Integer)


class CountMetricsSchema(ma.Schema):
    class Meta:
        fields = ("author_name", "commit_num", "line_of_code")


Count_metrics_schema = CountMetricsSchema(many=True)


class DeveloperNetworkMetrics(db.Model):
    __tablename__ = 'developer_network_metrics'
    __bind_key__ = db_config.bind_name
    author_name: str = db.Column(db.String(255))
    degree_centrality: int = db.Column(db.Integer)
    eigenvector_centrality: float = db.Column(db.Float)


class DeveloperNetworkMetricsSchema(ma.Schema):
    class Meta:
        fields = ("author_name", "degree_centrality", "eigenvector_centrality")


Developer_network_metrics_schema = DeveloperNetworkMetrics(many=True)