# coding: utf-8

"""
    mbed Cloud Connect REST API

    mbed Cloud Connect REST API allows web applications to communicate with devices.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class NotificationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v2_notification_callback_put(self, webhook, **kwargs):
        """
        Register a callback URL
        Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed you need to also place the subscriptions.  Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message. The given URL should be accessible and respond to the PUT request with response code of 200 or 204. mbed Cloud Connect tests the callback URL with empty payload when the URL is registered. For more information on callback notification, see NotificationData.  **Note**: Only one callback URL per access-key can be active. If you register a new URL when another one is already active, the old URL is replaced by the new. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_callback_put(webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Webhook webhook: A json object that contains the URL to which notifications need to be sent, and the optional headers.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_notification_callback_put_with_http_info(webhook, **kwargs)
        else:
            (data) = self.v2_notification_callback_put_with_http_info(webhook, **kwargs)
            return data

    def v2_notification_callback_put_with_http_info(self, webhook, **kwargs):
        """
        Register a callback URL
        Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed you need to also place the subscriptions.  Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message. The given URL should be accessible and respond to the PUT request with response code of 200 or 204. mbed Cloud Connect tests the callback URL with empty payload when the URL is registered. For more information on callback notification, see NotificationData.  **Note**: Only one callback URL per access-key can be active. If you register a new URL when another one is already active, the old URL is replaced by the new. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_callback_put_with_http_info(webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Webhook webhook: A json object that contains the URL to which notifications need to be sent, and the optional headers.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_notification_callback_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook' is set
        if ('webhook' not in params) or (params['webhook'] is None):
            raise ValueError("Missing the required parameter `webhook` when calling `v2_notification_callback_put`")

        resource_path = '/v2/notification/callback'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook' in params:
            body_params = params['webhook']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_notification_pull_get(self, **kwargs):
        """
        Get notifications using Long Poll
        In this case, notifications are delivered through HTTP long-poll requests. The HTTP request is kept open until an event notification or a batch of event notifications are delivered to the client or the request times out (response code 204). In both cases, the client should open a new polling connection after the previous one closes. You must have a persistent connection (Connection keep-alive header in the request) to avoid excess TLS handshakes.  **Note:** If it is not possible to have a public facing callback URL, for example when developing on your local machine, you can use long polling to check for new messages. However, to reduce network traffic and to increase performance we recommend that you use callback URLs (webhooks) whenever possible. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: NotificationMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_notification_pull_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_notification_pull_get_with_http_info(**kwargs)
            return data

    def v2_notification_pull_get_with_http_info(self, **kwargs):
        """
        Get notifications using Long Poll
        In this case, notifications are delivered through HTTP long-poll requests. The HTTP request is kept open until an event notification or a batch of event notifications are delivered to the client or the request times out (response code 204). In both cases, the client should open a new polling connection after the previous one closes. You must have a persistent connection (Connection keep-alive header in the request) to avoid excess TLS handshakes.  **Note:** If it is not possible to have a public facing callback URL, for example when developing on your local machine, you can use long polling to check for new messages. However, to reduce network traffic and to increase performance we recommend that you use callback URLs (webhooks) whenever possible. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: NotificationMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_notification_pull_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/notification/pull'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='NotificationMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))