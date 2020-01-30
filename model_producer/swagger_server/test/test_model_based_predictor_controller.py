# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.predction_post_body import PredctionPostBody  # noqa: E501
from swagger_server.models.prediction_response import PredictionResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModelBasedPredictorController(BaseTestCase):
    """ModelBasedPredictorController integration test stubs"""

    def test_api_v1_predict_post(self):
        """Test case for api_v1_predict_post

        Predicts the output basis the model.
        """
        body = PredctionPostBody()
        response = self.client.open(
            '/api/v1/predict',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
