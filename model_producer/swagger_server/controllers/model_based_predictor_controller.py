import connexion
import flask
import six

from controller.model_prediction_controller import predict
from swagger_server.models.predction_get_body import PredctionGetBody  # noqa: E501
from swagger_server.models.prediction_response import PredictionResponse  # noqa: E501
from swagger_server import util


def api_v1_predict_get(body):  # noqa: E501
    """Predicts the output basis the model.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: PredictionResponse
    """
    if connexion.request.is_json:
        body = PredctionGetBody.from_dict(connexion.request.get_json())  # noqa: E501
        return predict(body)
    return flask.Response("Invalid Data! Data is not JSON!", status=400)
