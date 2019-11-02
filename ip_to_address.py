import ipinfo


def ip_to_address(ip_address):
    access_token = '469c6d5ff551e9'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details.city


# print(ip_to_address('216.239.36.21'))
# print(ip_to_address('45.64.161.176'))