import geoip2.database

def ip_to_address(ip_address):
    reader = geoip2.database.Reader("./db/GeoLite2-City.mmdb")
    response = reader.city(ip_address)
    return response.city.name

#print(ip_to_address('216.239.36.21'))
#print(ip_to_address('45.64.161.176'))