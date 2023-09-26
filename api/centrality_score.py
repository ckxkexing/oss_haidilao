# -*-coding:utf-8-*-
import json

from flask import Blueprint

from models.metrics import ContributedReposRole, ContributedReposRoleSchema, contributed_repos_role_schema, \
    TotalFixIntensity, TotalFixIntensitySchema, total_fix_intensity_role_schema, ContributionGraph, \
    ContributionGraphSchema, contribution_graph_data_schema, PeersAverageFixIntensity, PeersAverageFixIntensitySchema, \
    peers_average_fix_intensity_role_schema, DeveloperRolesMetrics, DeveloperRolesMetricsSchema, \
    developer_roles_metrics_schema
# from helpers.clickhouse_cli import CKClient

centrality_score_bp = Blueprint('centrality_score', __name__)


@centrality_score_bp.route('/metric/contributed_repos/')
@centrality_score_bp.route('/metric/contributed_repos/<int:page>')
def get_contributed_repos(page=1):
    per_page = 100
    # score = ContributedReposRole.query.all()
    score = ContributedReposRole.query.paginate(page=page, per_page=per_page, error_out=False)
    contributed_repos = ContributedReposRoleSchema.dump(contributed_repos_role_schema, score)
    map_list = []
    for data in contributed_repos:
        map_list.append({"email": data["author_email"], "maximum_join_in_repo": data["repo_count"]})
    return map_list


@centrality_score_bp.route('/metric/total_fix_intensity/')
@centrality_score_bp.route('/metric/total_fix_intensity/<int:page>')
def get_total_fix_intensity(page=1):
    per_page = 100
    # score = TotalFixIntensity.query.all()
    score = TotalFixIntensity.query.paginate(page=page, per_page=per_page, error_out=False)
    total_fix_intensity = TotalFixIntensitySchema.dump(total_fix_intensity_role_schema, score)
    map_list = []
    for data in total_fix_intensity:
        map_list.append({"email": data["author_email"], "total_fix_intensity": data["total_fix_intensity"]})
    return map_list


@centrality_score_bp.route('/metric/basic_graph')
def get_basic_graph():
    response = {}
    score = ContributionGraph.query.all()
    contribution_graph = ContributionGraphSchema.dump(contribution_graph_data_schema, score)
    results = []
    for data in contribution_graph:
        results.append({"repo_name": data["repo_name"], "cntrb_id": data["cntrb_login"],
                        "total_contributions": data["total_contributions"]})
    repo_node = []
    person_node = []
    edges = []
    for result in results:
        if result["total_contributions"] > 1:
            repo_node.append(result["repo_name"])
            person_node.append(result["cntrb_id"])
            edges.append(
                {"source": result["repo_name"], "target": result["cntrb_id"],
                 "value": result["total_contributions"] / 2000})
    repo_node_set = set(repo_node)
    person_node_set = set(person_node)
    nodes = []
    for node in repo_node_set:
        nodes.append({"id": node, "size": 50, "label": node})
    for node in person_node_set:
        nodes.append({"id": node, "size": 10})
    response["nodes"] = nodes
    response["edges"] = edges
    return response


@centrality_score_bp.route('/metric/peers_average_fix_intensity/')
@centrality_score_bp.route('/metric/peers_average_fix_intensity/<int:page>')
def get_peers_average_fix_intensity(page=1):
    per_page = 100
    # score = PeersAverageFixIntensity.query.all()
    score = PeersAverageFixIntensity.query.paginate(page=page, per_page=per_page, error_out=False)
    peers_average_fix_intensity = PeersAverageFixIntensitySchema.dump(peers_average_fix_intensity_role_schema, score)
    return peers_average_fix_intensity





@centrality_score_bp.route('/metric/person_metrics/')
@centrality_score_bp.route('/metric/person_metrics/<int:page>')
def get_person_metrics(page=1):
    per_page = 100
    # score = DeveloperRolesMetrics.query.all()
    score = DeveloperRolesMetrics.query.paginate(page=page, per_page=per_page, error_out=False)
    developer_roles_metrics = DeveloperRolesMetricsSchema.dump(developer_roles_metrics_schema, score)
    map_list = []
    for result in developer_roles_metrics:
        map_list.append(
            {"email": result["author_email"],
             "total_fix_commit_count": result["total_fix_commit_count"],
             "maximum_fix_commit_count": result["maximum_fix_commit_count"],
             "fist_year_joined_repo_count": result["repo_count"]})
    return map_list

# @centrality_score_bp.route('/metric/get_betweenness_centtality')
# def get_betweenness_centtality():
#     basic_graph = get_basic_graph()
#     with open('../merged_df.json', 'r') as f:
#         results = json.load(f)
#         repo_node = []
#         for result in results:
#             if result["total_contributions"] > 1:
#                 repo_node.append(result["repo_name"])
#     repo_node_set = set(repo_node)
#     with open('../betweenness_centrality.json', 'r') as f:
#         nodes = []
#         results = json.load(f)
#         for result in results:
#             if result in repo_node_set:
#                 nodes.append({"id": result, "size": results[result] * 200, "label": result})
#             else:
#                 if results[result] == 0:
#                     nodes.append({"id": result, "size": 1})
#                 else:
#
#                     nodes.append({"id": result, "size": results[result] * 5})
#     basic_graph["nodes"] = nodes
#     # print(basic_graph)
#     return basic_graph


# @centrality_score_bp.route('/metric/get_maximum_fix_intensity')
# def get_maximum_fix_intensity():
#     ck = CKClient(
#
#     )
#     results = ck.execute_no_params("""
#     select *
# from (select author_email, search_key__owner, search_key__repo, count() as commit_count, ln(commit_count + 1)
#       from (select search_key__owner, search_key__repo, author_email, authored_date, b.*
#             from (select *
#                   from gits
#                   where search_key__owner = 'rust-lang'
#                     and search_key__repo != 'llvm-project'
#                     and search_key__repo != 'llvm'
#                     and search_key__repo != 'rust-gha'
#                     and length(parents) == 1
#                     and author_email != '') as a global ASOF
#                      INNER JOIN (select author_email,
#                                         min(authored_date)          as start_at,
#                                         subtractYears(start_at, -1) as end_at
#                                  from gits
#                                  where search_key__owner = 'rust-lang'
#                                    and search_key__repo != 'llvm-project'
#                                    and search_key__repo != 'llvm'
#                                    and search_key__repo != 'rust-gha'
#                                    and length(parents) == 1
#                                    and author_email != ''
#                                  group by author_email) as b
#                                 on a.author_email = b.author_email and a.authored_date <= end_at)
#       group by author_email, search_key__owner, search_key__repo
#       order by commit_count desc)
# limit 1 by author_email
#
#     """)
#     map_list = []
#     for result in results:
#         # print(result)
#         if result[3] > 1:
#             map_list.append({"email": result[0], "maximum_fix_intensity": result[3]})
#     ck.close()
#     return map_list








# @centrality_score_bp.route('/metric/get_basic_graph')
# def get_basic_graph():
#     response = {}
#     with open('../merged_df.json', 'r') as f:
#         results = json.load(f)
#         repo_node = []
#         person_node = []
#         edges = []
#         for result in results:
#             if result["total_contributions"] > 1:
#                 repo_node.append(result["repo_name"])
#                 person_node.append(result["cntrb_id"])
#                 edges.append(
#                     {"source": result["repo_name"], "target": result["cntrb_id"],
#                      "value": result["total_contributions"] / 2000})
#         repo_node_set = set(repo_node)
#         person_node_set = set(person_node)
#         nodes = []
#         for node in repo_node_set:
#             nodes.append({"id": node, "size": 50, "label": node})
#         for node in person_node_set:
#             nodes.append({"id": node, "size": 10})
#         response["nodes"] = nodes
#         response["edges"] = edges
#     return response


@centrality_score_bp.route('/metric/get_page_rank_top_10')
def get_page_rank_top_10():
    with open('../pagerank10.json', 'r') as f:
        nodes = []
        results = json.load(f)
        for result in results:
            nodes.append({"id": result, "size": results[result] * 2000, "label": result})
    return {"nodes": nodes}


# @centrality_score_bp.route('/metric/get_betweenness_centtality')
# def get_betweenness_centtality():
#     basic_graph = get_basic_graph()
#
#     with open('../merged_df.json', 'r') as f:
#         results = json.load(f)
#         repo_node = []
#         for result in results:
#             if result["total_contributions"] > 1:
#                 repo_node.append(result["repo_name"])
#     repo_node_set = set(repo_node)
#     with open('../betweenness_centrality.json', 'r') as f:
#         nodes = []
#         results = json.load(f)
#         for result in results:
#             if result in repo_node_set:
#                 nodes.append({"id": result, "size": results[result] * 200, "label": result})
#             else:
#                 if results[result] == 0:
#                     nodes.append({"id": result, "size": 1})
#                 else:
#
#                     nodes.append({"id": result, "size": results[result] * 5})
#     basic_graph["nodes"] = nodes
#     # print(basic_graph)
#     return basic_graph


# @centrality_score_bp.route('/sendSql', methods=['POST'])
# def sendSql():
#     sql_ = request.data.decode("utf8")
#     results = ck.execute_no_params(sql_)
#     response = []
#     for result in results:
#         response.append({"value":result[0],"label":result[0]})
#     return response



# @centrality_score_bp.route('/metric/get_centrality_score')
# def get_centrality_score():
#     # 连接数据库
#     score = CentralityScore.query.all()
    return CentralityScoreSchema.dump(score)
    # results = db_engine.execute("select * from centrality_score").fetchall()
    # # 创建游标
    # # 执行 SQL 查询
    # key = 0
    # response = []
    # for result in results:
    #     key += 1
    #     # print(result)
    #     response.append({
    #
    #         "key": key,
    #         "repo": result[1],
    #         "page_rank": result[2],
    #         "betweenness_centrality": result[3],
    #         "closeness_centrality": result[4],
    #         "total_score": result[5]
    #
    #     })
    #
    # return response
