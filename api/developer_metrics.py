import json

from flask import Blueprint

from models.metrics_developer import PrivilegeEvents, PrivilegeEventsSchema, Privilege_events_schema, \
    CountMetrics, CountMetricsSchema, Count_metrics_schema, \
    DeveloperNetworkMetrics, DeveloperNetworkMetricsSchema, Developer_network_metrics_schema

developer_metrics_bp = Blueprint('developer_metrics', __name__)

@developer_metrics_bp.route('/privilede_events/')
@developer_metrics_bp.route('/privilede_events/<int:page>')
def get_privilege_events(page=1):
    per_page = 100
    # score = PrivilegeEvents.query.all()
    score = PrivilegeEvents.query.paginate(page=page, per_page=per_page, error_out=False)
    privilege_events = PrivilegeEventsSchema.dump(Privilege_events_schema, score)
    map_list = []
    for data in privilege_events:
        map_list.append({"actor_login": data["actor_login"],
                        "added_to_project": data["added_to_project"],
                        "converted_note_to_issue": data["converted_note_to_issue"],
                        "deployed": data["deployed"],
                        "deployment_environment_changed": data["deployment_environment_changed"],
                        "locked": data["locked"],
                        "merged": data["merged"],
                        "moved_columns_in_project": data["moved_columns_in_project"],
                        "pinned": data["pinned"],
                        "removed_from_project": data["removed_from_project"],
                        "review_dismissed": data["review_dismissed"],
                        "transferred": data["transferred"],
                        "unlocked": data["transferred"],
                        "unpinned": data["unpinned"],
                        "user_blocked": data["user_blocked"]
                         })
    return map_list

@developer_metrics_bp.route('/count_metrics/')
@developer_metrics_bp.route('/count_metrics/<int:page>')
def get_count_metrics(page=1):
    per_page = 100
    # score = CountMetrics.query.all()
    score = CountMetrics.query.paginate(page=page, per_page=per_page, error_out=False)
    count_metrics = CountMetricsSchema.dump(Count_metrics_schema, score)
    map_list = []
    for data in count_metrics:
        map_list.append({
            "author_name": data["author_name"],
            "commit_num": data["commit_num"],
            "line_of_code": data["line_of_code"]
        })
    return map_list


@developer_metrics_bp.route('/developer_network_metrics/')
@developer_metrics_bp.route('/developer_network_metrics/<int:page>')
def get_developer_network_metrics(page=1):
    per_page = 100
    # score = DeveloperNetworkMetrics.query.all()
    score = DeveloperNetworkMetrics.query.paginate(page=page, per_page=per_page, error_out=False)
    developer_network_metrics = DeveloperNetworkMetricsSchema.dump(Developer_network_metrics_schema, score)
    map_list = []
    for data in developer_network_metrics:
        map_list.append({
            "author_name": data["author_name"],
            "degree_centrality": data["degree_centrality"],
            "eigenvector_centrality": data["eigenvector_centrality"]
        })
    return map_list
