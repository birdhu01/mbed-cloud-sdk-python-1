# connector_ca.ExternalAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_developer_certificates_id_get**](ExternalAPIApi.md#v3_developer_certificates_id_get) | **GET** /v3/developer-certificates/{id} | Fetch an existing developer certificate to connect to the bootstrap server.
[**v3_developer_certificates_post**](ExternalAPIApi.md#v3_developer_certificates_post) | **POST** /v3/developer-certificates | Create a new developer certificate to connect to the bootstrap server.
[**v3_server_credentials_bootstrap_get**](ExternalAPIApi.md#v3_server_credentials_bootstrap_get) | **GET** /v3/server-credentials/bootstrap | Fetch bootstrap server credentials.
[**v3_server_credentials_lwm2m_get**](ExternalAPIApi.md#v3_server_credentials_lwm2m_get) | **GET** /v3/server-credentials/lwm2m | Fetch LWM2M server credentials.


# **v3_developer_certificates_id_get**
> InlineResponse201 v3_developer_certificates_id_get(id, authorization)

Fetch an existing developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server). 

### Example 
```python
from __future__ import print_statement
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_ca.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_ca.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ExternalAPIApi()
id = 'id_example' # str | A unique identifier for the developer certificate. 
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch an existing developer certificate to connect to the bootstrap server.
    api_response = api_instance.v3_developer_certificates_id_get(id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_developer_certificates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the developer certificate.  | 
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_developer_certificates_post**
> InlineResponse201 v3_developer_certificates_post(authorization, body)

Create a new developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  Limitations:   - One developer certificate allows up to 100 devices to connect to bootstrap server.   - Only 10 developer certificates are allowed per account 

### Example 
```python
from __future__ import print_statement
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_ca.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_ca.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ExternalAPIApi()
authorization = 'authorization_example' # str | Bearer {Access Token}. 
body = connector_ca.Body() # Body | 

try: 
    # Create a new developer certificate to connect to the bootstrap server.
    api_response = api_instance.v3_developer_certificates_post(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_developer_certificates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_server_credentials_bootstrap_get**
> InlineResponse200 v3_server_credentials_bootstrap_get(authorization)

Fetch bootstrap server credentials.

This REST API is intended to be used by customers to fetch bootstrap server credentials that they will need to use with their clients to connect to bootstrap server. 

### Example 
```python
from __future__ import print_statement
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_ca.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_ca.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ExternalAPIApi()
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch bootstrap server credentials.
    api_response = api_instance.v3_server_credentials_bootstrap_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_server_credentials_bootstrap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_server_credentials_lwm2m_get**
> InlineResponse2001 v3_server_credentials_lwm2m_get(authorization)

Fetch LWM2M server credentials.

This REST API is intended to be used by customers to fetch LWM2M server credentials that they will need to use with their clients to connect to LWM2M server. 

### Example 
```python
from __future__ import print_statement
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_ca.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_ca.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ExternalAPIApi()
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch LWM2M server credentials.
    api_response = api_instance.v3_server_credentials_lwm2m_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_server_credentials_lwm2m_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
