# coding: utf-8

"""
    Device Query Service API

    This is the API Documentation for the mbed device query service update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WriteDeviceQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, query=None, object=None, query_id=None, description=None, name=None):
        """
        WriteDeviceQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'str',
            'object': 'str',
            'query_id': 'str',
            'description': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'query': 'query',
            'object': 'object',
            'query_id': 'query_id',
            'description': 'description',
            'name': 'name'
        }

        self._query = query
        self._object = object
        self._query_id = query_id
        self._description = description
        self._name = name

    @property
    def query(self):
        """
        Gets the query of this WriteDeviceQuery.
        The device query

        :return: The query of this WriteDeviceQuery.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this WriteDeviceQuery.
        The device query

        :param query: The query of this WriteDeviceQuery.
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")

        self._query = query

    @property
    def object(self):
        """
        Gets the object of this WriteDeviceQuery.
        The API resource entity

        :return: The object of this WriteDeviceQuery.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this WriteDeviceQuery.
        The API resource entity

        :param object: The object of this WriteDeviceQuery.
        :type: str
        """

        self._object = object

    @property
    def query_id(self):
        """
        Gets the query_id of this WriteDeviceQuery.
        DEPRECATED: The ID of the query

        :return: The query_id of this WriteDeviceQuery.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this WriteDeviceQuery.
        DEPRECATED: The ID of the query

        :param query_id: The query_id of this WriteDeviceQuery.
        :type: str
        """

        self._query_id = query_id

    @property
    def description(self):
        """
        Gets the description of this WriteDeviceQuery.
        The description of the object

        :return: The description of this WriteDeviceQuery.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WriteDeviceQuery.
        The description of the object

        :param description: The description of this WriteDeviceQuery.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this WriteDeviceQuery.
        The name of the query

        :return: The name of this WriteDeviceQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WriteDeviceQuery.
        The name of the query

        :param name: The name of this WriteDeviceQuery.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WriteDeviceQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
