# coding: utf-8

"""
    Provisioning endpoints - developer certificates.

    A developer certificate is used during development to allow quick association of the device with the mbed Cloud account of the developer. It is used instead of the Factory Tool.  The developer should generate a key-pair (NIST P-256 Elliptic Curve), add the public key to the mbed Cloud account using these APIs, and use the private key on the device (typically in a file named identity_dev_security.c). This creates an association between the device and the cloud.  Only one developer certificate per account is allowed.  As an example, a developer certificate can be created using OpenSSL as follows:  ``` openssl ecparam -out key.pem -name prime256v1 -genkey openssl ec -text -in key.pem -pubout ```  The output is:  ``` read EC key Private-Key: (256 bit) priv:     4e:50:25:1c:c0:70:29:05:dc:1d:7b:58:ba:a1:27:     c3:6f:aa:92:22:ca:0f:f1:af:74:cb:15:a4:cb:36:     98:3f pub:     04:35:54:40:80:f8:fb:45:ad:8a:fc:1a:9e:8c:88:     58:fa:84:91:ca:51:d2:09:d5:7b:35:9f:72:10:31:     a2:7c:d6:18:8b:49:d9:56:91:f0:99:b7:a9:a0:c6:     c1:5b:b8:d3:24:a8:cd:0c:76:9f:f0:c8:41:b0:a3:     dd:d3:2c:88:e1 ASN1 OID: prime256v1 NIST CURVE: P-256 writing EC key -----BEGIN PUBLIC KEY----- MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENVRAgPj7Ra2K/BqejIhY+oSRylHS CdV7NZ9yEDGifNYYi0nZVpHwmbepoMbBW7jTJKjNDHaf8MhBsKPd0yyI4Q== -----END PUBLIC KEY----- ```  The bytes under \"priv\" are the 32 private key bytes. They should be placed on the device (in the identity_dev_security.c file), as a byte array.  The text starting with \"BEGIN PUBLIC KEY\" is the public key in PEM format, which should be uploaded using the POST API.  Another example, using Python:  ``` from ecdsa import SigningKey, NIST256p private_key = SigningKey.generate(curve=NIST256p) public_key = private_key.get_verifying_key() print \"Public key:\" print public_key.to_pem() bytes = bytearray(private_key.to_string()) for byte in bytes:   print hex(byte) + \",\", ``` 

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeveloperCertificate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_at=None, etag=None, pub_key=None, object=None, id=None):
        """
        DeveloperCertificate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_at': 'str',
            'etag': 'str',
            'pub_key': 'str',
            'object': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'etag': 'etag',
            'pub_key': 'pub_key',
            'object': 'object',
            'id': 'id'
        }

        self._created_at = created_at
        self._etag = etag
        self._pub_key = pub_key
        self._object = object
        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this DeveloperCertificate.
        UTC time of the entity creation.

        :return: The created_at of this DeveloperCertificate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeveloperCertificate.
        UTC time of the entity creation.

        :param created_at: The created_at of this DeveloperCertificate.
        :type: str
        """

        self._created_at = created_at

    @property
    def etag(self):
        """
        Gets the etag of this DeveloperCertificate.
        Currently not used.

        :return: The etag of this DeveloperCertificate.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeveloperCertificate.
        Currently not used.

        :param etag: The etag of this DeveloperCertificate.
        :type: str
        """

        self._etag = etag

    @property
    def pub_key(self):
        """
        Gets the pub_key of this DeveloperCertificate.
        The developer certificate public key in raw format (65 bytes), Base64 encoded, NIST P-256 curve.

        :return: The pub_key of this DeveloperCertificate.
        :rtype: str
        """
        return self._pub_key

    @pub_key.setter
    def pub_key(self, pub_key):
        """
        Sets the pub_key of this DeveloperCertificate.
        The developer certificate public key in raw format (65 bytes), Base64 encoded, NIST P-256 curve.

        :param pub_key: The pub_key of this DeveloperCertificate.
        :type: str
        """

        self._pub_key = pub_key

    @property
    def object(self):
        """
        Gets the object of this DeveloperCertificate.
        Currently not used.

        :return: The object of this DeveloperCertificate.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeveloperCertificate.
        Currently not used.

        :param object: The object of this DeveloperCertificate.
        :type: str
        """

        self._object = object

    @property
    def id(self):
        """
        Gets the id of this DeveloperCertificate.
        Entity ID.

        :return: The id of this DeveloperCertificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeveloperCertificate.
        Entity ID.

        :param id: The id of this DeveloperCertificate.
        :type: str
        """

        self._id = id

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
