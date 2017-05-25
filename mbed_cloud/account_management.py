# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Functionality for Account Management related actions in mbed Cloud."""
from __future__ import absolute_import
from __future__ import unicode_literals
from six import iteritems

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.models import AccountUpdateReq
import mbed_cloud._backends.iam.rest as ApiException


class AccountManagementAPI(BaseAPI):
    """API reference for the AccountManagement API.

    Exposing functionality for creating and managing accounts,
    users, groups and API keys in the organisation.
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(AccountManagementAPI, self).__init__(params)

        # Set the api_key for the requests
        iam.configuration.api_key['Authorization'] = config.get("api_key")
        iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            iam.configuration.host = config.get("host")

    @catch_exceptions(ApiException)
    def list_api_keys(self, **kwargs):
        """List the API keys registered in the organisation.

        :param limit: Number of API keys to get (int)
        :param after: Entity ID after which to start fetching (str)
        :param order: Order of the records to return (asc|desc) (str)
        :returns: a list of :py:class:`ApiKey` objects
        :rtype: PaginatedResponse
        """
        api = iam.DeveloperApi()

        # Return the data array
        return PaginatedResponse(api.get_all_api_keys, lwrap_type=ApiKey, **kwargs)

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key):
        """Get API key details for key registered in organisation.

        :param api_key: The ID of the API key to be updated
        :returns: API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        return ApiKey(api.get_api_key(api_key))

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key):
        """Delete an API key registered in the organisation.

        :param api_key: The ID of the API key
        :returns: void
        """
        api = iam.DeveloperApi()
        api.delete_api_key(api_key)
        return

    @catch_exceptions(ApiException)
    def add_api_key(self, name, groups=[], owner=None):
        """Create new API key registered to organisation.

        :param str name: The name of the API key
        :param list groups: Optional list of group IDs (`str`)
        :param str owner: Optional user ID owning the API key
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyInfoReq(name=name, groups=groups, owner=owner)
        return ApiKey(api.create_api_key(body))

    @catch_exceptions(ApiException)
    def update_api_key(self, api_key, name, owner=None):
        """Update API key.

        :param str api_key: The ID of the API key to be updated.
        :param str name: The name of the API key.
        :param str owner: Optional user ID owning the API key.
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyUpdateReq(name=name, owner=owner)
        return ApiKey(api.update_api_key(api_key, body))

    @catch_exceptions(ApiException)
    def list_users(self, **kwargs):
        """List all users in organisation.

        :param int limit: The number of devices to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get devices after/starting at given user ID
        :returns: a list of :py:class:`User` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)

        api = iam.AccountAdminApi()
        return PaginatedResponse(api.get_all_users, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        """Get user details of specified user.

        :param str user_id: the ID of the user to get
        :returns: the user object with details about the user.
        :rtype: User
        """
        api = iam.AccountAdminApi()
        return User(api.get_user(user_id))

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        """Update user properties of specified user.

        Accepts same parameters as `add_user`.

        :param str user_id: the ID of the user to update
        :returns: the updated user object
        :rtype: User
        """
        api = iam.AccountAdminApi()
        body = iam.UserUpdateReq(**kwargs)
        return User(api.update_user(user_id, body))

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        """Delete user specified user.

        :param str user_id: the ID of the user to delete
        :returns: void
        """
        api = iam.AccountAdminApi()
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def add_user(self, username, email, **kwargs):
        """Create a new user with provided details.

        :param str username: Required. The unique username of the user
        :param str email: Required. The unique email of the user
        :param str full_name: Optional. The full name of the user
        :param list groups: Optional. List of group IDs (`str`) which this user belongs to
        :param str password: Optional. The password string of the user.
            Need to adhere to password policy
        :param str phone_number: Optional. Phone number of the user
        :param bool terms_accepted: Optional. Is 'General Terms & Conditions' accepted
        :param bool marketing_accepted: Optional. Is receiving marketing information accepted?
        :returns: the new user object
        :rtype: User
        """
        api = iam.AccountAdminApi()
        kwargs.update({'username': username, 'email': email})
        body = iam.UserInfoReq(**kwargs)
        return User(api.create_user(body))

    @catch_exceptions(ApiException)
    def get_account(self):
        """Get details of the current account.

        :returns: an account object.
        :rtype: Account
        """
        api = iam.DeveloperApi()
        return Account(api.get_my_account_info(include="limits, policies"))

    @catch_exceptions(ApiException)
    def update_account(self, **kwargs):
        """Update details of account associated with current API key.

        :param str address_line1: Postal address line 1.
        :param str address_line2: Postal address line 2.
        :param str city: The city part of the postal address.
        :param str display_name: The display name for the account.
        :param str country: The country part of the postal address.
        :param str company: The name of the company.
        :param str state: The state part of the postal address.
        :param str contact: The name of the contact person for this account.
        :param str postal_code: The postal code part of the postal address.
        :param str parent_id: The ID of the parent account.
        :param str phone_number: The phone number of the company.
        :param str email: Email address for this account.
        :param list[str] aliases: List of aliases
        :returns: an account object.
        :rtype: Account
        """
        api = iam.AccountAdminApi()
        body = AccountUpdateReq(**kwargs)
        return Account(api.update_my_account(body))

    @catch_exceptions(ApiException)
    def list_groups(self, **kwargs):
        """List all groups in organisation.

        :param int limit: The number of groups to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get groups after/starting at given group ID
        :returns: a list of :py:class:`Group` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)

        api = iam.DeveloperApi()
        return PaginatedResponse(api.get_all_groups, lwrap_type=Group, **kwargs)

    @catch_exceptions(ApiException)
    def get_group(self, group_id):
        """Get details of the group.

        :param str group_id: The group ID.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get groups after/starting at given group ID
        :returns: :py:class:`Group` object.
        :rtype: Group
        """
        api = iam.DeveloperApi()
        return Group(api.get_group_summary(group_id))

    @catch_exceptions(ApiException)
    def list_group_users(self, group_id, **kwargs):
        """List users of a group.

        :param str group_id: The group ID.
        :param int limit: The number of users to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc).
        :param str after: Get api keys after/starting at given user ID.
        :returns: a list of :py:class:`User` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)

        api = iam.AccountAdminApi()
        return PaginatedResponse(api.get_users_of_group, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def list_group_api_keys(self, group_id, **kwargs):
        """List API keys of a group.

        :param str group_id: The group ID.
        :param int limit: The number of api keys to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc).
        :param str after: Get api keys after/starting at given api key ID.
        :returns: a list of :py:class:`ApiKey` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)
        api = iam.DeveloperApi()
        return PaginatedResponse(api.get_api_keys_of_group, lwrap_type=ApiKey, **kwargs)


class Account(BaseObject):
    """Describes account object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Get account owning the API key in use
        current_account = api.get_account()
        print(current_account.company)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "display_name": "display_name",
            "aliases": "aliases",
            "company": "company",
            "contact": "contact",
            "email": "email",
            "phone_number": "phone_number",
            "address_line1": "address_line1",
            "address_line2": "address_line2",
            "city": "city",
            "state": "state",
            "postcode": "postal_code",
            "country": "country",
            "id": "id",
            "status": "status",
            "tier": "tier",
            "limits": "limits",
            "policies": "policies",
            "provisioning_allowed": "is_provisioning_allowed",
            "created_at": "created_at",
            "upgraded_at": "upgraded_at",
            "reason": "reason",
            "template_id": "template_id"
        }

    @property
    def display_name(self):
        """The display name for the account.

        :rtype: str
        """
        return self._display_name

    @property
    def aliases(self):
        """An array of aliases.

        :rtype: str[]
        """
        return self._aliases

    @property
    def company(self):
        """The name of the company.

        :rtype: str
        """
        return self._company

    @property
    def contact(self):
        """The name of the contact person for this account.

        :rtype: str
        """
        return self._contact

    @property
    def email(self):
        """The company email address for this account.

        :rtype: str
        """
        return self._email

    @property
    def phone_number(self):
        """The phone number of the company.

        :rtype: str
        """
        return self._phone_number

    @property
    def address_line1(self):
        """Postal address line 1.

        :rtype: str
        """
        return self._address_line1

    @property
    def address_line2(self):
        """Postal address line 2.

        :rtype: str
        """
        return self._address_line2

    @property
    def city(self):
        """The city part of the postal address.

        :rtype: str
        """
        return self._city

    @property
    def state(self):
        """The state part of the postal address.

        :rtype: str
        """
        return self._state

    @property
    def postcode(self):
        """The postal code part of the postal address.

        :rtype: str
        """
        return self._postcode

    @property
    def country(self):
        """The country part of the postal address.

        :rtype: str
        """
        return self._country

    @property
    def id(self):
        """Account ID (readonly).

        :rtype: str
        """
        return self._id

    @property
    def status(self):
        """The status of the account.

        values: ENROLLING, ACTIVE, RESTRICTED, SUSPENDED

        :rtype: str
        """
        return self._status

    @property
    def tier(self):
        """The tier level of the account; '0': free tier, '1': commercial account.

        Other values are reserved for the future.

        :rtype: str
        """
        return self._tier

    @property
    def limits(self):
        """List of limits as key-value pairs if requested.

        :rtype: list of Limits
        """
        return self._limits

    @property
    def policies(self):
        """List of policies if requested.

        :rtype: list of Policies
        """
        return self._policies

    @property
    def provisioning_allowed(self):
        """Flag (true/false) indicating whether Factory Tool is allowed to download or not.

        :rtype: bool
        """
        return self._provisioning_allowed

    @property
    def created_at(self):
        """Creation UTC time RFC3339.

        :rtype: str
        """
        return self._created_at

    @property
    def upgraded_at(self):
        """Time when upgraded to commercial account in UTC format RFC3339.

        :rtype: str
        """
        return self._upgraded_at

    @property
    def reason(self):
        """A reason note for updating the status of the account.

        :rtype: str
        """
        return self._reason

    @property
    def template_id(self):
        """Account template ID.

        :rtype: str
        """
        return self._template_id


class User(BaseObject):
    """Describes user object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing users
        for idx, user in enumerate(api.list_users())
            print(user.full_name)

        # Creating a new user
        new_user = api.add_user("username",
                                "user@example.org",
                                full_name = "David Bowie",
                                password = "hunter2")
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "full_name": "full_name",
            "username": "username",
            "password": "password",
            "email": "email",
            "phone_number": "phone_number",
            "address": "address",
            "terms_accepted": "is_gtc_accepted",
            "marketing_accepted": "is_marketing_accepted",
            "groups": "groups",
            "id": "id",
            "status": "status",
            "account_id": "account_id",
            "email_verified": "email_verified",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "password_changed_time": "password_changed_time",
            "last_login_time": "last_login_time"
        }

    def _create_put_request(self):
        put_map = {
            "full_name": "full_name",
            "username": "username",
            "password": "password",
            "email": "email",
            "phone_number": "phone_number",
            "address": "address",
            "terms_accepted": "is_gtc_accepted",
            "marketing_accepted": "is_marketing_accepted",
        }
        map_put = {}
        for key, value in iteritems(put_map):
            val = getattr(self, key, None)
            if val is not None:
                map_put[value] = val
        return map_put

    @property
    def full_name(self):
        """The full name of the user.

        :rtype: str
        """
        return self._full_name

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.

        :rtype: str
        """
        return self._username

    @property
    def password(self):
        """The password when creating a new user. It will will generated when not present in the request.

        :rtype: str
        """
        return self._password

    @property
    def email(self):
        """The email address.

        :rtype: str
        """
        return self._email

    @property
    def phone_number(self):
        """Phone number.

        :rtype: str
        """
        return self._phone_number

    @property
    def address(self):
        """Address.

        :rtype: str
        """
        return self._address

    @property
    def terms_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.

        :rtype: bool
        """
        return self._terms_accepted

    @property
    def marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.

        :rtype: bool
        """
        return self._marketing_accepted

    @property
    def groups(self):
        """A list of group IDs this user belongs to (readonly).

        :rtype: str[]
        """
        return self._groups

    @property
    def id(self):
        """The UUID of the user (readonly).

        :rtype: str
        """
        return self._id

    @property
    def status(self):
        """The status of the user (readonly).

        INVITED means that the user has not accepted the invitation request.
        RESET means that the password must be changed immediately.
        values: ENROLLING, INVITED, ACTIVE, RESET, INACTIVE

        :rtype: str
        """
        return self._status

    @property
    def account_id(self):
        """The UUID of the account (readonly).

        :rtype: str
        """
        return self._account_id

    @property
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.

        :rtype: bool
        """
        return self._email_verified

    @property
    def created_at(self):
        """Creation UTC time RFC3339 (readonly).

        :rtype: str
        """
        return self._created_at

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds (readonly).

        :rtype: int
        """
        return self._creation_time

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds (readonly).

        :rtype: int
        """
        return self._password_changed_time

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds (readonly).

        :rtype: int
        """
        return self._last_login_time


class Group(BaseObject):
    """Describes group object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing groups
        for idx, g in enumerate(api.list_groups())
            print(g.name)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "id": "id",
            "account_id": "account_id",
            "name": "name",
            "user_count": "user_count",
            "apikey_count": "apikey_count",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "last_update_time": "last_update_time"
        }

    @property
    def id(self):
        """The UUID of the group. (readonly)

        :rtype: str
        """
        return self._id

    @property
    def account_id(self):
        """The UUID of the account this group belongs to. (readonly)

        :rtype: str
        """
        return self._account_id

    @property
    def name(self):
        """The name of the group. (readonly)

        :rtype: str
        """
        return self._name

    @property
    def user_count(self):
        """The number of users in this group. (readonly)

        :rtype: int
        """
        return self._user_count

    @property
    def apikey_count(self):
        """The number of API keys in this group. (readonly)

        :rtype: int
        """
        return self._apikey_count

    @property
    def created_at(self):
        """Creation UTC time RFC3339. (readonly)

        :rtype: str
        """
        return self._created_at

    @property
    def creation_time(self):
        """A timestamp of the group creation in the storage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._creation_time


class ApiKey(BaseObject):
    """Describes API key object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing keys
        for idx, k in enumerate(api.list_api_keys()):
            print(k.name, k.key)

        # Creating a new key
        new_k = api.add_api_key("New key name")
        print(new_k.key)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "name": "name",
            "owner": "owner",
            "groups": "groups",
            "id": "id",
            "key": "key",
            "status": "status",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "last_login_time": "last_login_time"
        }

    @property
    def name(self):
        """The display name for the API key.

        :rtype: str
        """
        return self._name

    @property
    def owner(self):
        """The owner of this API key, who is the creator by default.

        :rtype: str
        """
        return self._owner

    @property
    def groups(self):
        """A list of group IDs this API key belongs to.

        :rtype: str[]
        """
        return self._groups

    @property
    def id(self):
        """The UUID of the API key. (readonly)

        :rtype: str
        """
        return self._id

    @property
    def key(self):
        """The API key. (readonly)

        :rtype: str
        """
        return self._key

    @property
    def status(self):
        """The status of the API key. (readonly)

        values: ACTIVE, INACTIVE

        :rtype: str
        """
        return self._status

    @property
    def created_at(self):
        """Creation UTC time RFC3339. (readonly)

        :rtype: str
        """
        return self._created_at

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._creation_time

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._last_login_time