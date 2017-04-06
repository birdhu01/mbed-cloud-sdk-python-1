# coding: utf-8

"""
    Device Catalog API

    This is the API Documentation for the mbed device catalog update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceDataWriteRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, manifest_timestamp=None, vendor_id=None, description=None, deployed_state=None, firmware_checksum=None, auto_update=None, mechanism=None, device_class=None, trust_level=None, custom_attributes=None, manifest=None, trust_class=None, device_key=None, state=None, ca_id=None, deployment=None, mechanism_url=None, serial_number=None, endpoint_name=None, name=None):
        """
        DeviceDataWriteRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'manifest_timestamp': 'datetime',
            'vendor_id': 'str',
            'description': 'str',
            'deployed_state': 'str',
            'firmware_checksum': 'str',
            'auto_update': 'bool',
            'mechanism': 'str',
            'device_class': 'str',
            'trust_level': 'int',
            'custom_attributes': 'object',
            'manifest': 'str',
            'trust_class': 'int',
            'device_key': 'str',
            'state': 'str',
            'ca_id': 'str',
            'deployment': 'str',
            'mechanism_url': 'str',
            'serial_number': 'str',
            'endpoint_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'manifest_timestamp': 'manifest_timestamp',
            'vendor_id': 'vendor_id',
            'description': 'description',
            'deployed_state': 'deployed_state',
            'firmware_checksum': 'firmware_checksum',
            'auto_update': 'auto_update',
            'mechanism': 'mechanism',
            'device_class': 'device_class',
            'trust_level': 'trust_level',
            'custom_attributes': 'custom_attributes',
            'manifest': 'manifest',
            'trust_class': 'trust_class',
            'device_key': 'device_key',
            'state': 'state',
            'ca_id': 'ca_id',
            'deployment': 'deployment',
            'mechanism_url': 'mechanism_url',
            'serial_number': 'serial_number',
            'endpoint_name': 'endpoint_name',
            'name': 'name'
        }

        self._manifest_timestamp = manifest_timestamp
        self._vendor_id = vendor_id
        self._description = description
        self._deployed_state = deployed_state
        self._firmware_checksum = firmware_checksum
        self._auto_update = auto_update
        self._mechanism = mechanism
        self._device_class = device_class
        self._trust_level = trust_level
        self._custom_attributes = custom_attributes
        self._manifest = manifest
        self._trust_class = trust_class
        self._device_key = device_key
        self._state = state
        self._ca_id = ca_id
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._serial_number = serial_number
        self._endpoint_name = endpoint_name
        self._name = name

    @property
    def manifest_timestamp(self):
        """
        Gets the manifest_timestamp of this DeviceDataWriteRequest.

        :return: The manifest_timestamp of this DeviceDataWriteRequest.
        :rtype: datetime
        """
        return self._manifest_timestamp

    @manifest_timestamp.setter
    def manifest_timestamp(self, manifest_timestamp):
        """
        Sets the manifest_timestamp of this DeviceDataWriteRequest.

        :param manifest_timestamp: The manifest_timestamp of this DeviceDataWriteRequest.
        :type: datetime
        """
        if manifest_timestamp is None:
            raise ValueError("Invalid value for `manifest_timestamp`, must not be `None`")

        self._manifest_timestamp = manifest_timestamp

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceDataWriteRequest.

        :return: The vendor_id of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceDataWriteRequest.

        :param vendor_id: The vendor_id of this DeviceDataWriteRequest.
        :type: str
        """
        if vendor_id is None:
            raise ValueError("Invalid value for `vendor_id`, must not be `None`")

        self._vendor_id = vendor_id

    @property
    def description(self):
        """
        Gets the description of this DeviceDataWriteRequest.

        :return: The description of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceDataWriteRequest.

        :param description: The description of this DeviceDataWriteRequest.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceDataWriteRequest.

        :return: The deployed_state of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceDataWriteRequest.

        :param deployed_state: The deployed_state of this DeviceDataWriteRequest.
        :type: str
        """
        allowed_values = ["development", "production"]
        if deployed_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployed_state` ({0}), must be one of {1}"
                .format(deployed_state, allowed_values)
            )

        self._deployed_state = deployed_state

    @property
    def firmware_checksum(self):
        """
        Gets the firmware_checksum of this DeviceDataWriteRequest.

        :return: The firmware_checksum of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._firmware_checksum

    @firmware_checksum.setter
    def firmware_checksum(self, firmware_checksum):
        """
        Sets the firmware_checksum of this DeviceDataWriteRequest.

        :param firmware_checksum: The firmware_checksum of this DeviceDataWriteRequest.
        :type: str
        """
        if firmware_checksum is None:
            raise ValueError("Invalid value for `firmware_checksum`, must not be `None`")

        self._firmware_checksum = firmware_checksum

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceDataWriteRequest.

        :return: The auto_update of this DeviceDataWriteRequest.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceDataWriteRequest.

        :param auto_update: The auto_update of this DeviceDataWriteRequest.
        :type: bool
        """
        if auto_update is None:
            raise ValueError("Invalid value for `auto_update`, must not be `None`")

        self._auto_update = auto_update

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceDataWriteRequest.

        :return: The mechanism of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceDataWriteRequest.

        :param mechanism: The mechanism of this DeviceDataWriteRequest.
        :type: str
        """
        if mechanism is None:
            raise ValueError("Invalid value for `mechanism`, must not be `None`")

        self._mechanism = mechanism

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceDataWriteRequest.

        :return: The device_class of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceDataWriteRequest.

        :param device_class: The device_class of this DeviceDataWriteRequest.
        :type: str
        """
        if device_class is None:
            raise ValueError("Invalid value for `device_class`, must not be `None`")

        self._device_class = device_class

    @property
    def trust_level(self):
        """
        Gets the trust_level of this DeviceDataWriteRequest.

        :return: The trust_level of this DeviceDataWriteRequest.
        :rtype: int
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """
        Sets the trust_level of this DeviceDataWriteRequest.

        :param trust_level: The trust_level of this DeviceDataWriteRequest.
        :type: int
        """
        if trust_level is None:
            raise ValueError("Invalid value for `trust_level`, must not be `None`")

        self._trust_level = trust_level

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceDataWriteRequest.

        :return: The custom_attributes of this DeviceDataWriteRequest.
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceDataWriteRequest.

        :param custom_attributes: The custom_attributes of this DeviceDataWriteRequest.
        :type: object
        """
        if custom_attributes is None:
            raise ValueError("Invalid value for `custom_attributes`, must not be `None`")

        self._custom_attributes = custom_attributes

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceDataWriteRequest.

        :return: The manifest of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceDataWriteRequest.

        :param manifest: The manifest of this DeviceDataWriteRequest.
        :type: str
        """
        if manifest is None:
            raise ValueError("Invalid value for `manifest`, must not be `None`")

        self._manifest = manifest

    @property
    def trust_class(self):
        """
        Gets the trust_class of this DeviceDataWriteRequest.

        :return: The trust_class of this DeviceDataWriteRequest.
        :rtype: int
        """
        return self._trust_class

    @trust_class.setter
    def trust_class(self, trust_class):
        """
        Sets the trust_class of this DeviceDataWriteRequest.

        :param trust_class: The trust_class of this DeviceDataWriteRequest.
        :type: int
        """
        if trust_class is None:
            raise ValueError("Invalid value for `trust_class`, must not be `None`")

        self._trust_class = trust_class

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceDataWriteRequest.

        :return: The device_key of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceDataWriteRequest.

        :param device_key: The device_key of this DeviceDataWriteRequest.
        :type: str
        """
        if device_key is None:
            raise ValueError("Invalid value for `device_key`, must not be `None`")

        self._device_key = device_key

    @property
    def state(self):
        """
        Gets the state of this DeviceDataWriteRequest.

        :return: The state of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceDataWriteRequest.

        :param state: The state of this DeviceDataWriteRequest.
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")

        self._state = state

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceDataWriteRequest.

        :return: The ca_id of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceDataWriteRequest.

        :param ca_id: The ca_id of this DeviceDataWriteRequest.
        :type: str
        """
        if ca_id is None:
            raise ValueError("Invalid value for `ca_id`, must not be `None`")

        self._ca_id = ca_id

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceDataWriteRequest.

        :return: The deployment of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceDataWriteRequest.

        :param deployment: The deployment of this DeviceDataWriteRequest.
        :type: str
        """
        if deployment is None:
            raise ValueError("Invalid value for `deployment`, must not be `None`")

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceDataWriteRequest.

        :return: The mechanism_url of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceDataWriteRequest.

        :param mechanism_url: The mechanism_url of this DeviceDataWriteRequest.
        :type: str
        """
        if mechanism_url is None:
            raise ValueError("Invalid value for `mechanism_url`, must not be `None`")

        self._mechanism_url = mechanism_url

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceDataWriteRequest.

        :return: The serial_number of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceDataWriteRequest.

        :param serial_number: The serial_number of this DeviceDataWriteRequest.
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")

        self._serial_number = serial_number

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceDataWriteRequest.

        :return: The endpoint_name of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceDataWriteRequest.

        :param endpoint_name: The endpoint_name of this DeviceDataWriteRequest.
        :type: str
        """
        if endpoint_name is None:
            raise ValueError("Invalid value for `endpoint_name`, must not be `None`")

        self._endpoint_name = endpoint_name

    @property
    def name(self):
        """
        Gets the name of this DeviceDataWriteRequest.

        :return: The name of this DeviceDataWriteRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDataWriteRequest.

        :param name: The name of this DeviceDataWriteRequest.
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
        if not isinstance(other, DeviceDataWriteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other