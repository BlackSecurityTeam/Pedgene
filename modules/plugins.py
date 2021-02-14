import requests
import time as t
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



def Discover_Plugins(domain,BLUE,RESET,RED,GREEN) :

    file =open("modules/plugins.txt")
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    content = file.read()

    plugins = content.splitlines()
    
    discoverd_plugins_list = []
    
    site = f"http://{domain}/wp-content/plugins/"

    response1 = session.get(site)
    if response1.status_code == 200 or response1.status_code == 403 :

        for plugin in plugins :
            url =  f"http://{domain}/wp-content/plugins/{plugin}"
            response2 = session.get(url)
            t.sleep(1)

            if  response2.status_code == 200 or response2.status_code == 403 :
                print(f" {GREEN} [+] Discovered Plugin : {BLUE} {plugin} {RESET}")
                discoverd_plugins_list.append(url)
            else :
                print(f" {RED} [-] Not Found Plugin : {plugin} {RESET}")
        with open(f"results/plugins/{domain}.txt", "w") as f :
            for plugin in discoverd_plugins_list :
                print(plugin,file=f)            
    else :   
        print(f" {RED} [-] This Site is Not With WordPress CMS {RESET}")        


  



                

