from ipwhois import IPWhois
import whois,socket

class Information:
    def __init__(self,domain) :
        self.domain = domain

    def Get_ip(self,domain):
        ip = socket.gethostbyname(domain)
        return ip


    def Domain_info(self,domain):
        return whois.whois(self.domain)

    def Server_info(self,domain):
        ip = Information.Get_ip(self=None,domain=domain)
        info = IPWhois(ip)
        info = info.lookup_whois()
        return info    



