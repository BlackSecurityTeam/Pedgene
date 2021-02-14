import requests

def http_header(domain) :

    response = requests.get('http://'+domain)
    return response.headers
