# AccountInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_market** | **str** | Account end market. | 
**status** | **str** | The status of the account. | 
**password_policy** | [**PasswordPolicy**](PasswordPolicy.md) | The password policy for this account. | [optional] 
**sales_contact** | **str** | Email address of the sales contact. | [optional] 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**postal_code** | **str** | The postal code part of the postal address. | [optional] 
**account_properties** | [**dict(str, dict(str, str))**](dict.md) | Account specific custom properties. | [optional] 
**customer_number** | **str** | Customer number of the customer. | [optional] 
**id** | **str** | Account ID. | 
**aliases** | **list[str]** | An array of aliases. | 
**address_line2** | **str** | Postal address line 2. | [optional] 
**city** | **str** | The city part of the postal address. | [optional] 
**address_line1** | **str** | Postal address line 1. | [optional] 
**display_name** | **str** | The display name for the account. | [optional] 
**mfa_status** | **str** | The enforcement status of the multi-factor authentication, either &#39;enforced&#39; or &#39;optional&#39;. | [optional] 
**parent_id** | **str** | The ID of the parent account, if it has any. | [optional] 
**state** | **str** | The state part of the postal address. | [optional] 
**etag** | **str** | API resource entity version. | 
**email** | **str** | The company email address for this account. | [optional] 
**phone_number** | **str** | The phone number of a representative of the company. | [optional] 
**reference_note** | **str** | A reference note for updating the status of the account | [optional] 
**company** | **str** | The name of the company. | [optional] 
**object** | **str** | Entity name: always &#39;account&#39; | 
**reason** | **str** | A reason note for updating the status of the account | [optional] 
**upgraded_at** | **datetime** | Time when upgraded to commercial account in UTC format RFC3339. | [optional] 
**tier** | **str** | The tier level of the account; &#39;0&#39;: free tier, &#39;1&#39;: commercial account, &#39;2&#39;: partner tier. Other values are reserved for the future. | 
**sub_accounts** | [**list[AccountInfo]**](AccountInfo.md) | List of sub accounts. | [optional] 
**limits** | **dict(str, str)** | List of limits as key-value pairs if requested. | [optional] 
**country** | **str** | The country part of the postal address. | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**idle_timeout** | **str** | The reference token expiration time in minutes for this account. | [optional] 
**contract_number** | **str** | Contract number of the customer. | [optional] 
**expiration_warning_threshold** | **str** | Indicates how many days (1-180) before account expiration a notification email should be sent. | [optional] 
**contact** | **str** | The name of the contact person for this account. | [optional] 
**policies** | [**list[FeaturePolicy]**](FeaturePolicy.md) | List of policies if requested. | [optional] 
**notification_emails** | **list[str]** | A list of notification email addresses. | [optional] 
**template_id** | **str** | Account template ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


