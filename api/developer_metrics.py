import json

from flask import Blueprint

from models.metrics_developer import PrivilegeEvents, PrivilegeEventsSchema, Privilege_events_schema, \
    CountMetrics, CountMetricsSchema, Count_metrics_schema, \
    DeveloperNetworkMetrics, DeveloperNetworkMetricsSchema, Developer_network_metrics_schema

developer_metrics_bp = Blueprint('developer_metrics', __name__)

@developer_metrics_bp.route('/privilede_events')
def get_privilege_events():
    score = PrivilegeEvents.query.all()
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

# TODO Fix
@developer_metrics_bp.route('/count_metrics')
def get_count_metrics():
    score = CountMetrics.query.all()
    count_metrics = CountMetricsSchema.dump(Count_metrics_schema, score)
    map_list = []
    for data in count_metrics:
        map_list.append({
            "author_name": data["author_name"],
            "commit_num": data["commit_num"],
            "line_of_code": data["line_of_code"]
        })
    return map_list


@developer_metrics_bp.route('/developer_network_metrics')
def get_developer_network_metrics():
    score = DeveloperNetworkMetrics.query.all()
    developer_network_metrics = DeveloperNetworkMetricsSchema.dump(Developer_network_metrics_schema, score)
    map_list = []
    for data in developer_network_metrics:
        map_list.append({
            "author_name": data["author_name"],
            "degree_centrality": data["degree_centrality"],
            "eigenvector_centrality": data["eigenvector_centrality"]
        })
    return map_list