# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FilterPredictionGetBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, column: str=None, operator: str=None, value: str=None):  # noqa: E501
        """FilterPredictionGetBody - a model defined in Swagger

        :param column: The column of this FilterPredictionGetBody.  # noqa: E501
        :type column: str
        :param operator: The operator of this FilterPredictionGetBody.  # noqa: E501
        :type operator: str
        :param value: The value of this FilterPredictionGetBody.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'column': str,
            'operator': str,
            'value': str
        }

        self.attribute_map = {
            'column': 'column',
            'operator': 'operator',
            'value': 'value'
        }
        self._column = column
        self._operator = operator
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'FilterPredictionGetBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The filterPredictionGetBody of this FilterPredictionGetBody.  # noqa: E501
        :rtype: FilterPredictionGetBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def column(self) -> str:
        """Gets the column of this FilterPredictionGetBody.


        :return: The column of this FilterPredictionGetBody.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column: str):
        """Sets the column of this FilterPredictionGetBody.


        :param column: The column of this FilterPredictionGetBody.
        :type column: str
        """
        if column is None:
            raise ValueError("Invalid value for `column`, must not be `None`")  # noqa: E501

        self._column = column

    @property
    def operator(self) -> str:
        """Gets the operator of this FilterPredictionGetBody.


        :return: The operator of this FilterPredictionGetBody.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str):
        """Sets the operator of this FilterPredictionGetBody.


        :param operator: The operator of this FilterPredictionGetBody.
        :type operator: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def value(self) -> str:
        """Gets the value of this FilterPredictionGetBody.


        :return: The value of this FilterPredictionGetBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this FilterPredictionGetBody.


        :param value: The value of this FilterPredictionGetBody.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
