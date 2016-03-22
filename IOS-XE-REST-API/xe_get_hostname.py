# xe_get_hostname.py
# Get configured hostname using IOS XE REST API

from xe_restapi_auth import *

# Token is used as part of headers for the request
# Using global parameters 'device_ip' and 'port' as default
def get_configured_hostname(device_ip=device_ip,port=port):
   
    url = "https://{h}:{p}/api/v1/global/host-name".format(h=device_ip, p=port)
    # REST API headers
    headers = {"content-type": "application/json","X-Auth-Token": get_token()}
    # this statement performs a GET on the specified url
    response = requests.get(url,headers=headers, verify=False)
    # return the json as text
    return response.text


def main():
    """Simple main method calling our function."""
    # Using global parameters 'device_ip' and 'port' as default
    hostname = get_configured_hostname()
    # print the json that is returned
    print(hostname)

if __name__ == '__main__':
    sys.exit(main())
