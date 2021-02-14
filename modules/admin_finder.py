import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def admin_finder(domain,GREEN,RED,RESET):

    url = "http://"+domain
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    pages = open('modules/admins.txt','r').read().splitlines()
   
    
    for page in pages :
        full_address = url+"/"+page

        if session.get(full_address).status_code == 200:
            print(f" {GREEN} {full_address} is Exsists ====> 200 {RESET}")
        else :
            print(f" {RED} {full_address} is Not Exsists ====> 404 {RESET} ")    
