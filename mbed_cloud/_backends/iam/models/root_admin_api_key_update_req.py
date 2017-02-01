# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and API keys

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RootAdminApiKeyUpdateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, owner=None, status=None, name=None):
        """
        RootAdminApiKeyUpdateReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner': 'str',
            'status': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'owner': 'owner',
            'status': 'status',
            'name': 'name'
        }

        self._owner = owner
        self._status = status
        self._name = name

    @property
    def owner(self):
        """
        Gets the owner of this RootAdminApiKeyUpdateReq.
        The owner of this API key, who is the creator by default.

        :return: The owner of this RootAdminApiKeyUpdateReq.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this RootAdminApiKeyUpdateReq.
        The owner of this API key, who is the creator by default.

        :param owner: The owner of this RootAdminApiKeyUpdateReq.
        :type: str
        """

        self._owner = owner

    @property
    def status(self):
        """
        Gets the status of this RootAdminApiKeyUpdateReq.
        The status of the apikey.

        :return: The status of this RootAdminApiKeyUpdateReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RootAdminApiKeyUpdateReq.
        The status of the apikey.

        :param status: The status of this RootAdminApiKeyUpdateReq.
        :type: str
        """

        self._status = status

    @property
    def name(self):
        """
        Gets the name of this RootAdminApiKeyUpdateReq.
        The display name for the API key.

        :return: The name of this RootAdminApiKeyUpdateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RootAdminApiKeyUpdateReq.
        The display name for the API key.

        :param name: The name of this RootAdminApiKeyUpdateReq.
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
        if not isinstance(other, RootAdminApiKeyUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other