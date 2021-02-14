import requests
import time as t
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def Discover_Subdomains(domain,WHITE,BLUE,RESET,RED,GREEN) :

    file =open("modules/subdomains.txt")
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)


    content = file.read()

    subdomains = content.splitlines()
    count = content.count("\n") + 1
    i = 0
    discoverd_subdomains_list = []
    for subdomain in subdomains :

        url = f"http://{subdomain}.{domain}"
        # http://subdomain.blacksec.ir

        try :

            session.get(url)
            i += 1
            t.sleep(1)


        except requests.ConnectionError   :
            
            i += 1  
        else :

            print(f" {GREEN} [{i}/{count}] [+] {BLUE} Discoverd Subdomain : {RESET} {url}")   
            discoverd_subdomains_list.append(url)


            with open(f"results/subdomains/{domain}.txt","w") as f  :
                for subdomain in discoverd_subdomains_list :
                    print(subdomain,file=f)