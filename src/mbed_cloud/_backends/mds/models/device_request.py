# coding: utf-8

"""
    Connect API

    Mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payload_b64': 'str',
        'content_type': 'str',
        'method': 'str',
        'accept': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'payload_b64': 'payload-b64',
        'content_type': 'content-type',
        'method': 'method',
        'accept': 'accept',
        'uri': 'uri'
    }

    def __init__(self, payload_b64=None, content_type=None, method=None, accept=None, uri=None):
        """
        DeviceRequest - a model defined in Swagger
        """

        self._payload_b64 = payload_b64
        self._content_type = content_type
        self._method = method
        self._accept = accept
        self._uri = uri
        self.discriminator = None

    @property
    def payload_b64(self):
        """
        Gets the payload_b64 of this DeviceRequest.
        The base64 encoded payload to be sent to the device.

        :return: The payload_b64 of this DeviceRequest.
        :rtype: str
        """
        return self._payload_b64

    @payload_b64.setter
    def payload_b64(self, payload_b64):
        """
        Sets the payload_b64 of this DeviceRequest.
        The base64 encoded payload to be sent to the device.

        :param payload_b64: The payload_b64 of this DeviceRequest.
        :type: str
        """

        self._payload_b64 = payload_b64

    @property
    def content_type(self):
        """
        Gets the content_type of this DeviceRequest.
        The content type of the payload.

        :return: The content_type of this DeviceRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this DeviceRequest.
        The content type of the payload.

        :param content_type: The content_type of this DeviceRequest.
        :type: str
        """

        self._content_type = content_type

    @property
    def method(self):
        """
        Gets the method of this DeviceRequest.
        The CoAP request method. Allowed values are GET, POST, PUT and DELETE.

        :return: The method of this DeviceRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this DeviceRequest.
        The CoAP request method. Allowed values are GET, POST, PUT and DELETE.

        :param method: The method of this DeviceRequest.
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")

        self._method = method

    @property
    def accept(self):
        """
        Gets the accept of this DeviceRequest.
        The content type of an accepted response.

        :return: The accept of this DeviceRequest.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        """
        Sets the accept of this DeviceRequest.
        The content type of an accepted response.

        :param accept: The accept of this DeviceRequest.
        :type: str
        """

        self._accept = accept

    @property
    def uri(self):
        """
        Gets the uri of this DeviceRequest.
        The URI path of the requested resource.

        :return: The uri of this DeviceRequest.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this DeviceRequest.
        The URI path of the requested resource.

        :param uri: The uri of this DeviceRequest.
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri

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
        if not isinstance(other, DeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other