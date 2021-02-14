import builtwith



def Fetch_info(domain,GREEN):


    res = builtwith.builtwith("http://"+domain)

    for i in res :
        print(f"{GREEN} {i}",res[i])