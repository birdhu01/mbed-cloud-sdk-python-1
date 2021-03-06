# coding: utf-8

"""
    Update Service API

    This is the API documentation for the Mbed deployment service, which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareManifestEqNeqFilter(object):
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
        'datafile': 'str',
        'description': 'str',
        'timestamp': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'etag': 'datetime',
        'device_class': 'str',
        'datafile_size': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'datafile': 'datafile',
        'description': 'description',
        'timestamp': 'timestamp',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'etag': 'etag',
        'device_class': 'device_class',
        'datafile_size': 'datafile_size',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, datafile=None, description=None, timestamp=None, created_at=None, updated_at=None, etag=None, device_class=None, datafile_size=None, id=None, name=None):
        """
        FirmwareManifestEqNeqFilter - a model defined in Swagger
        """

        self._datafile = datafile
        self._description = description
        self._timestamp = timestamp
        self._created_at = created_at
        self._updated_at = updated_at
        self._etag = etag
        self._device_class = device_class
        self._datafile_size = datafile_size
        self._id = id
        self._name = name
        self.discriminator = None

    @property
    def datafile(self):
        """
        Gets the datafile of this FirmwareManifestEqNeqFilter.

        :return: The datafile of this FirmwareManifestEqNeqFilter.
        :rtype: str
        """
        return self._datafile

    @datafile.setter
    def datafile(self, datafile):
        """
        Sets the datafile of this FirmwareManifestEqNeqFilter.

        :param datafile: The datafile of this FirmwareManifestEqNeqFilter.
        :type: str
        """

        self._datafile = datafile

    @property
    def description(self):
        """
        Gets the description of this FirmwareManifestEqNeqFilter.

        :return: The description of this FirmwareManifestEqNeqFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FirmwareManifestEqNeqFilter.

        :param description: The description of this FirmwareManifestEqNeqFilter.
        :type: str
        """

        self._description = description

    @property
    def timestamp(self):
        """
        Gets the timestamp of this FirmwareManifestEqNeqFilter.

        :return: The timestamp of this FirmwareManifestEqNeqFilter.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this FirmwareManifestEqNeqFilter.

        :param timestamp: The timestamp of this FirmwareManifestEqNeqFilter.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def created_at(self):
        """
        Gets the created_at of this FirmwareManifestEqNeqFilter.

        :return: The created_at of this FirmwareManifestEqNeqFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FirmwareManifestEqNeqFilter.

        :param created_at: The created_at of this FirmwareManifestEqNeqFilter.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this FirmwareManifestEqNeqFilter.

        :return: The updated_at of this FirmwareManifestEqNeqFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this FirmwareManifestEqNeqFilter.

        :param updated_at: The updated_at of this FirmwareManifestEqNeqFilter.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def etag(self):
        """
        Gets the etag of this FirmwareManifestEqNeqFilter.

        :return: The etag of this FirmwareManifestEqNeqFilter.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this FirmwareManifestEqNeqFilter.

        :param etag: The etag of this FirmwareManifestEqNeqFilter.
        :type: datetime
        """

        self._etag = etag

    @property
    def device_class(self):
        """
        Gets the device_class of this FirmwareManifestEqNeqFilter.

        :return: The device_class of this FirmwareManifestEqNeqFilter.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this FirmwareManifestEqNeqFilter.

        :param device_class: The device_class of this FirmwareManifestEqNeqFilter.
        :type: str
        """

        self._device_class = device_class

    @property
    def datafile_size(self):
        """
        Gets the datafile_size of this FirmwareManifestEqNeqFilter.

        :return: The datafile_size of this FirmwareManifestEqNeqFilter.
        :rtype: int
        """
        return self._datafile_size

    @datafile_size.setter
    def datafile_size(self, datafile_size):
        """
        Sets the datafile_size of this FirmwareManifestEqNeqFilter.

        :param datafile_size: The datafile_size of this FirmwareManifestEqNeqFilter.
        :type: int
        """

        self._datafile_size = datafile_size

    @property
    def id(self):
        """
        Gets the id of this FirmwareManifestEqNeqFilter.

        :return: The id of this FirmwareManifestEqNeqFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FirmwareManifestEqNeqFilter.

        :param id: The id of this FirmwareManifestEqNeqFilter.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FirmwareManifestEqNeqFilter.

        :return: The name of this FirmwareManifestEqNeqFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FirmwareManifestEqNeqFilter.

        :param name: The name of this FirmwareManifestEqNeqFilter.
        :type: str
        """

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
        if not isinstance(other, FirmwareManifestEqNeqFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
