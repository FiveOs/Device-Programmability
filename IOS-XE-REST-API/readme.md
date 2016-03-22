You can use the Cisco IOS XE REST API to manage the Cisco CSR 1000V as an alternative to configuring and managing selected features on the router using the Cisco IOS XE CLI. 
To enable REST API support on device please refer to [Cisco CSR 1000V Series Cloud Services 
Router Software Configuration Guide](http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/configuration/csr1000Vswcfg.pdf)<br>
For usage of API please refer to [Cisco IOS XE REST API Management Reference Guide] (http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi.html)


## Client Authentication

The REST API authentication works as follows:
* The authentication uses HTTPS as the transport for all the Cisco REST API access.
* Clients perform authentication with this service by invoking a POST on this resource with HTTP
Basic Auth as the authentication mechanism. The response of this request includes a token-id.
Token-ids are short-lived, opaque objects that represents client’s successful authentication with the
token service.
* Clients then access other APIs by including the token id as a custom HTTP header “X-auth-token”.
If this token is not present or expired, then API access will return an HTTP status code of “401
Unauthorized”
* Clients can also explicitly invalidate a token by performing a DELETE operation on the token
resource.
* The username/password for the HTTPS session should be configured with privilege 15.<br>

##### The function "get_token" in xe_restapi_auth.py is used to get the token-id. 
Simple add "from xe_restapi_auth import *" in the beginning of other scirpt to utilize "get_token" function.

#### 



