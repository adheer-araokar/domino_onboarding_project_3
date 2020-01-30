import flask
from dao.prediction_dao import find_prediction, execute_find_query
from bson import json_util
import json

from swagger_server.models.search_filter_prediction_response import SearchFilterPredictionResponse
from swagger_server.models.filter_prediction_get_body import FilterPredictionGetBody
from swagger_server.models.search_prediction_get_body import SearchPredictionGetBody


def search_prediction(body: SearchPredictionGetBody):
    records = find_prediction(body.prediction_id)
    response_body = SearchFilterPredictionResponse()
    response_body.records = []
    for record in records:
        response_body.records.append({"entry": json.loads(json_util.dumps(record))})
    return response_body


def filter_prediction(body: FilterPredictionGetBody):
    column = body.column
    operator = body.operator
    value = body.value
    if column == 'timestamp':
        value = int(value)
    query = {column: {}}
    if operator == ">":
        query[column] = {"$gt": value}
    elif operator == "<":
        query[column] = {"$lt": value}
    elif operator == "=":
        query[column] = value
    else:
        return flask.Response("Invalid Data!", status=400)
    records = execute_find_query(query)
    response_body = SearchFilterPredictionResponse()
    response_body.records = []
    for record in records:
        response_body.records.append({"entry": json.loads(json_util.dumps(record))})
    return response_body
