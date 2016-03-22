#!/usr/bin/python
# xe_restapi_auth.py
import requests
import json       # External JSON encoder and decode module
import sys        # For system-specific functions

requests.packages.urllib3.disable_warnings() # Disable warning message

# config the following global parameters so when you call get_token() you don't need to pass them

#device ip
device_ip = "10.10.10.11"
#REST API local port number
port = "55443"
username = "cisco"
password = "cisco123!"


# return token_id 
def get_token(ip=device_ip,p=port, uname = username,pword = password):
    """
    This function returns a new secerety token.
    Passing ip, port number, username and password when use as a standalone function
    to overwrite the default configuration
    """
    # JSON input for the post ticket API request
    payload = {'username': uname,'password':pword}
    # url for the post token request
    post_url = "https://"+ip+":"+p+"/api/v1/auth/token-services"
    headers = {'Content-Type': 'application/json'}
    # POST token request and return response
    try:
        r = requests.post(post_url,headers=headers,auth=(uname, pword),verify=False)
        # remove '#' if need to print out response to see detail
        # print ("Response Status: ",r.status_code)
        response_json = r.json()
        # The token we need is the value of access_token attribute
        return response_json["token-id"]
    except:
        # Something wrong, cannot get token
        print ("Something wrong, cannot get token")
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()



