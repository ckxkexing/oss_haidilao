# -*-coding:utf-8-*-
import json

from flask import Blueprint

from models.metrics import NetworkMetrics, NetworkMetricsSchema, Network_metrics_schema

network_metrics_bp = Blueprint('network_metrics', __name__)

@network_metrics_bp.route('/metric/<metric_name>/<owner>/<repo>/')
@network_metrics_bp.route('/metric/<metric_name>/<owner>/<repo>/<month>')
def get_network_metrics(metric_name, owner, repo, month=""):
    if month != "":
        score = NetworkMetrics.query.filter(NetworkMetrics.repo==f"{owner}__{repo}", NetworkMetrics.month==month)
    else:
        score = NetworkMetrics.query.filter(NetworkMetrics.repo==f"{owner}__{repo}")
    metrics_values = NetworkMetricsSchema.dump(Network_metrics_schema, score)
    map_list = []
    for data in metrics_values:
        map_list.append({"id": data["id"], metric_name: data[metric_name]})
    return map_list
