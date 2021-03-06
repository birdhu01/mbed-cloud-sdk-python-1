# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TrustedCertificateInternalResp(object):
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
        'service': 'str',
        'status': 'str',
        'private_key': 'str',
        'name': 'str',
        'certificate': 'str',
        'enrollment_mode': 'bool',
        'issuer': 'str',
        'device_execution_mode': 'int',
        'created_at': 'datetime',
        'object': 'str',
        'subject': 'str',
        'updated_at': 'datetime',
        'account_id': 'str',
        'etag': 'str',
        'validity': 'datetime',
        'owner_id': 'str',
        'id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'service': 'service',
        'status': 'status',
        'private_key': 'private_key',
        'name': 'name',
        'certificate': 'certificate',
        'enrollment_mode': 'enrollment_mode',
        'issuer': 'issuer',
        'device_execution_mode': 'device_execution_mode',
        'created_at': 'created_at',
        'object': 'object',
        'subject': 'subject',
        'updated_at': 'updated_at',
        'account_id': 'account_id',
        'etag': 'etag',
        'validity': 'validity',
        'owner_id': 'owner_id',
        'id': 'id',
        'description': 'description'
    }

    def __init__(self, service=None, status=None, private_key=None, name=None, certificate=None, enrollment_mode=None, issuer=None, device_execution_mode=None, created_at=None, object=None, subject=None, updated_at=None, account_id=None, etag=None, validity=None, owner_id=None, id=None, description=None):
        """
        TrustedCertificateInternalResp - a model defined in Swagger
        """

        self._service = service
        self._status = status
        self._private_key = private_key
        self._name = name
        self._certificate = certificate
        self._enrollment_mode = enrollment_mode
        self._issuer = issuer
        self._device_execution_mode = device_execution_mode
        self._created_at = created_at
        self._object = object
        self._subject = subject
        self._updated_at = updated_at
        self._account_id = account_id
        self._etag = etag
        self._validity = validity
        self._owner_id = owner_id
        self._id = id
        self._description = description
        self.discriminator = None

    @property
    def service(self):
        """
        Gets the service of this TrustedCertificateInternalResp.
        Service name where the certificate is to be used.

        :return: The service of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this TrustedCertificateInternalResp.
        Service name where the certificate is to be used.

        :param service: The service of this TrustedCertificateInternalResp.
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")
        allowed_values = ["lwm2m", "bootstrap"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def status(self):
        """
        Gets the status of this TrustedCertificateInternalResp.
        Status of the certificate.

        :return: The status of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TrustedCertificateInternalResp.
        Status of the certificate.

        :param status: The status of this TrustedCertificateInternalResp.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def private_key(self):
        """
        Gets the private_key of this TrustedCertificateInternalResp.
        Private key of the certificate in PEM or base64 encoded DER format.

        :return: The private_key of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """
        Sets the private_key of this TrustedCertificateInternalResp.
        Private key of the certificate in PEM or base64 encoded DER format.

        :param private_key: The private_key of this TrustedCertificateInternalResp.
        :type: str
        """
        if private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")

        self._private_key = private_key

    @property
    def name(self):
        """
        Gets the name of this TrustedCertificateInternalResp.
        Certificate name.

        :return: The name of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TrustedCertificateInternalResp.
        Certificate name.

        :param name: The name of this TrustedCertificateInternalResp.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def certificate(self):
        """
        Gets the certificate of this TrustedCertificateInternalResp.
        X509.v3 trusted certificate in PEM format.

        :return: The certificate of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this TrustedCertificateInternalResp.
        X509.v3 trusted certificate in PEM format.

        :param certificate: The certificate of this TrustedCertificateInternalResp.
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")

        self._certificate = certificate

    @property
    def enrollment_mode(self):
        """
        Gets the enrollment_mode of this TrustedCertificateInternalResp.
        If true, signature is not required. Default value false.

        :return: The enrollment_mode of this TrustedCertificateInternalResp.
        :rtype: bool
        """
        return self._enrollment_mode

    @enrollment_mode.setter
    def enrollment_mode(self, enrollment_mode):
        """
        Sets the enrollment_mode of this TrustedCertificateInternalResp.
        If true, signature is not required. Default value false.

        :param enrollment_mode: The enrollment_mode of this TrustedCertificateInternalResp.
        :type: bool
        """

        self._enrollment_mode = enrollment_mode

    @property
    def issuer(self):
        """
        Gets the issuer of this TrustedCertificateInternalResp.
        Issuer of the certificate.

        :return: The issuer of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this TrustedCertificateInternalResp.
        Issuer of the certificate.

        :param issuer: The issuer of this TrustedCertificateInternalResp.
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def device_execution_mode(self):
        """
        Gets the device_execution_mode of this TrustedCertificateInternalResp.
        Device execution mode where 1 means a developer certificate.

        :return: The device_execution_mode of this TrustedCertificateInternalResp.
        :rtype: int
        """
        return self._device_execution_mode

    @device_execution_mode.setter
    def device_execution_mode(self, device_execution_mode):
        """
        Sets the device_execution_mode of this TrustedCertificateInternalResp.
        Device execution mode where 1 means a developer certificate.

        :param device_execution_mode: The device_execution_mode of this TrustedCertificateInternalResp.
        :type: int
        """

        self._device_execution_mode = device_execution_mode

    @property
    def created_at(self):
        """
        Gets the created_at of this TrustedCertificateInternalResp.
        Creation UTC time RFC3339.

        :return: The created_at of this TrustedCertificateInternalResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this TrustedCertificateInternalResp.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this TrustedCertificateInternalResp.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this TrustedCertificateInternalResp.
        Entity name: always 'trusted-cert'

        :return: The object of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this TrustedCertificateInternalResp.
        Entity name: always 'trusted-cert'

        :param object: The object of this TrustedCertificateInternalResp.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["trusted-cert"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def subject(self):
        """
        Gets the subject of this TrustedCertificateInternalResp.
        Subject of the certificate.

        :return: The subject of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this TrustedCertificateInternalResp.
        Subject of the certificate.

        :param subject: The subject of this TrustedCertificateInternalResp.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def updated_at(self):
        """
        Gets the updated_at of this TrustedCertificateInternalResp.
        Last update UTC time RFC3339.

        :return: The updated_at of this TrustedCertificateInternalResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this TrustedCertificateInternalResp.
        Last update UTC time RFC3339.

        :param updated_at: The updated_at of this TrustedCertificateInternalResp.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def account_id(self):
        """
        Gets the account_id of this TrustedCertificateInternalResp.
        The UUID of the account.

        :return: The account_id of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this TrustedCertificateInternalResp.
        The UUID of the account.

        :param account_id: The account_id of this TrustedCertificateInternalResp.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def etag(self):
        """
        Gets the etag of this TrustedCertificateInternalResp.
        API resource entity version.

        :return: The etag of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this TrustedCertificateInternalResp.
        API resource entity version.

        :param etag: The etag of this TrustedCertificateInternalResp.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def validity(self):
        """
        Gets the validity of this TrustedCertificateInternalResp.
        Expiration time in UTC formatted as RFC3339.

        :return: The validity of this TrustedCertificateInternalResp.
        :rtype: datetime
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this TrustedCertificateInternalResp.
        Expiration time in UTC formatted as RFC3339.

        :param validity: The validity of this TrustedCertificateInternalResp.
        :type: datetime
        """
        if validity is None:
            raise ValueError("Invalid value for `validity`, must not be `None`")

        self._validity = validity

    @property
    def owner_id(self):
        """
        Gets the owner_id of this TrustedCertificateInternalResp.
        The UUID of the owner.

        :return: The owner_id of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this TrustedCertificateInternalResp.
        The UUID of the owner.

        :param owner_id: The owner_id of this TrustedCertificateInternalResp.
        :type: str
        """

        self._owner_id = owner_id

    @property
    def id(self):
        """
        Gets the id of this TrustedCertificateInternalResp.
        Entity ID.

        :return: The id of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TrustedCertificateInternalResp.
        Entity ID.

        :param id: The id of this TrustedCertificateInternalResp.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this TrustedCertificateInternalResp.
        Human readable description of this certificate.

        :return: The description of this TrustedCertificateInternalResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TrustedCertificateInternalResp.
        Human readable description of this certificate.

        :param description: The description of this TrustedCertificateInternalResp.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, TrustedCertificateInternalResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
