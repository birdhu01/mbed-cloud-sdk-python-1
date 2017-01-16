# coding: utf-8

"""
    Provisioning endpoints - the factory provisioning package.

    The factory provisioning package needs to be installed in factories to enroll devices onto the mbed Cloud ecosystem.  These APIs allow downloading the most recent version of the factory provisioning package for various operating systems. 

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FactoryToolDownload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, download_path=None, os=None, filename=None, version=None, sha256=None, client_versions=None, size=None):
        """
        FactoryToolDownload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'download_path': 'str',
            'os': 'str',
            'filename': 'str',
            'version': 'str',
            'sha256': 'str',
            'client_versions': 'str',
            'size': 'str'
        }

        self.attribute_map = {
            'download_path': 'downloadPath',
            'os': 'os',
            'filename': 'filename',
            'version': 'version',
            'sha256': 'Sha256',
            'client_versions': 'clientVersions',
            'size': 'size'
        }

        self._download_path = download_path
        self._os = os
        self._filename = filename
        self._version = version
        self._sha256 = sha256
        self._client_versions = client_versions
        self._size = size

    @property
    def download_path(self):
        """
        Gets the download_path of this FactoryToolDownload.
        Download URL path for the specific archive.

        :return: The download_path of this FactoryToolDownload.
        :rtype: str
        """
        return self._download_path

    @download_path.setter
    def download_path(self, download_path):
        """
        Sets the download_path of this FactoryToolDownload.
        Download URL path for the specific archive.

        :param download_path: The download_path of this FactoryToolDownload.
        :type: str
        """

        self._download_path = download_path

    @property
    def os(self):
        """
        Gets the os of this FactoryToolDownload.
        Supported operating system.

        :return: The os of this FactoryToolDownload.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this FactoryToolDownload.
        Supported operating system.

        :param os: The os of this FactoryToolDownload.
        :type: str
        """

        self._os = os

    @property
    def filename(self):
        """
        Gets the filename of this FactoryToolDownload.
        The archive filename.

        :return: The filename of this FactoryToolDownload.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this FactoryToolDownload.
        The archive filename.

        :param filename: The filename of this FactoryToolDownload.
        :type: str
        """

        self._filename = filename

    @property
    def version(self):
        """
        Gets the version of this FactoryToolDownload.
        Factory Tool version.

        :return: The version of this FactoryToolDownload.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FactoryToolDownload.
        Factory Tool version.

        :param version: The version of this FactoryToolDownload.
        :type: str
        """

        self._version = version

    @property
    def sha256(self):
        """
        Gets the sha256 of this FactoryToolDownload.
        Generated SHA256 value of the archive file.

        :return: The sha256 of this FactoryToolDownload.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this FactoryToolDownload.
        Generated SHA256 value of the archive file.

        :param sha256: The sha256 of this FactoryToolDownload.
        :type: str
        """

        self._sha256 = sha256

    @property
    def client_versions(self):
        """
        Gets the client_versions of this FactoryToolDownload.
        Supported client versions for the tool.

        :return: The client_versions of this FactoryToolDownload.
        :rtype: str
        """
        return self._client_versions

    @client_versions.setter
    def client_versions(self, client_versions):
        """
        Sets the client_versions of this FactoryToolDownload.
        Supported client versions for the tool.

        :param client_versions: The client_versions of this FactoryToolDownload.
        :type: str
        """

        self._client_versions = client_versions

    @property
    def size(self):
        """
        Gets the size of this FactoryToolDownload.
        Size of archive file (MB).

        :return: The size of this FactoryToolDownload.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FactoryToolDownload.
        Size of archive file (MB).

        :param size: The size of this FactoryToolDownload.
        :type: str
        """

        self._size = size

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
