# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.filter_prediction_get_body import FilterPredictionGetBody  # noqa: E501
from swagger_server.models.search_filter_prediction_response import SearchFilterPredictionResponse  # noqa: E501
from swagger_server.models.search_prediction_get_body import SearchPredictionGetBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPredictionQueryController(BaseTestCase):
    """PredictionQueryController integration test stubs"""

    def test_api_v1_filter_get(self):
        """Test case for api_v1_filter_get

        Filter predictions
        """
        body = FilterPredictionGetBody()
        response = self.client.open(
            '/api/v1/filter',
            method='GET',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_search_get(self):
        """Test case for api_v1_search_get

        Search predictions
        """
        body = SearchPredictionGetBody()
        response = self.client.open(
            '/api/v1/search',
            method='GET',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
