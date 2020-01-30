import connexion
import flask

from controller.query_controller import filter_prediction, search_prediction
from swagger_server.models.filter_prediction_get_body import FilterPredictionGetBody  # noqa: E501
from swagger_server.models.search_prediction_get_body import SearchPredictionGetBody  # noqa: E501


def api_v1_filter_get(body):  # noqa: E501
    """Filter predictions

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: SearchFilterPredictionResponse
    """
    if connexion.request.is_json:
        body = FilterPredictionGetBody.from_dict(connexion.request.get_json())  # noqa: E501
        return filter_prediction(body)
    return flask.Response("Invalid Data! Data is not JSON!", status=400)


def api_v1_search_get(body):  # noqa: E501
    """Search predictions

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: SearchFilterPredictionResponse
    """
    if connexion.request.is_json:
        body = SearchPredictionGetBody.from_dict(connexion.request.get_json())  # noqa: E501
        return search_prediction(body)
    return flask.Response("Invalid Data! Data is not JSON!", status=400)
