# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PredictionInputData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, x: List[List[float]]=None, y: List[float]=None):  # noqa: E501
        """PredictionInputData - a model defined in Swagger

        :param x: The x of this PredictionInputData.  # noqa: E501
        :type x: List[List[float]]
        :param y: The y of this PredictionInputData.  # noqa: E501
        :type y: List[float]
        """
        self.swagger_types = {
            'x': List[List[float]],
            'y': List[float]
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y'
        }
        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt) -> 'PredictionInputData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The predictionInputData of this PredictionInputData.  # noqa: E501
        :rtype: PredictionInputData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> List[List[float]]:
        """Gets the x of this PredictionInputData.


        :return: The x of this PredictionInputData.
        :rtype: List[List[float]]
        """
        return self._x

    @x.setter
    def x(self, x: List[List[float]]):
        """Sets the x of this PredictionInputData.


        :param x: The x of this PredictionInputData.
        :type x: List[List[float]]
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self) -> List[float]:
        """Gets the y of this PredictionInputData.


        :return: The y of this PredictionInputData.
        :rtype: List[float]
        """
        return self._y

    @y.setter
    def y(self, y: List[float]):
        """Sets the y of this PredictionInputData.


        :param y: The y of this PredictionInputData.
        :type y: List[float]
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y
