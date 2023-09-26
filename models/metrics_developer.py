from .database import db, ma

from .config import metrics_db_config as db_config

class PrivilegeEvents(db.Model):
    __tablename__ = 'privilege_events'
    __bind_key__ = db_config.bind_name
    actor_login: str = db.Column(db.String(255), primary_key=True)
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
    __tablename__ = 'developer_contrib_count_metrics'
    __bind_key__ = db_config.bind_name
    author_name: str = db.Column(db.String(255), primary_key=True)
    commit_num: int = db.Column(db.Integer)
    line_of_code: int = db.Column(db.Integer)


class CountMetricsSchema(ma.Schema):
    class Meta:
        fields = ("author_name", "commit_num", "line_of_code")


Count_metrics_schema = CountMetricsSchema(many=True)


class DeveloperNetworkMetrics(db.Model):
    __tablename__ = 'developer_role_network_metrics'
    __bind_key__ = db_config.bind_name
    author_name: str = db.Column(db.String(255), primary_key=True)
    degree_centrality: int = db.Column(db.Integer)
    eigenvector_centrality: float = db.Column(db.Float)


class DeveloperNetworkMetricsSchema(ma.Schema):
    class Meta:
        fields = ("author_name", "degree_centrality", "eigenvector_centrality")


Developer_network_metrics_schema = DeveloperNetworkMetricsSchema(many=True)