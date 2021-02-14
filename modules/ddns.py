import dns.resolver


class Dns_Checker :

    def __init__(self,domain):
        self.domain = domain


    def options(self=None) :
           print(f"""
        
        1  -   A Record
        2  -   C Name
        3  -   MX Record
        00 -   Return To Main Menu 

        """)

    def A_record (self,domain,type='A') :
        result = dns.resolver.query(self.domain,type)
        for ip in result :
            return ip


    def Mx_record(self,domain,type='MX') : 
        answers = dns.resolver.query(self.domain,type)
        for rdata in answers:
            return rdata
    def Cname(self,domain,type='CNAME') : 
         result = dns.resolver.query(self.domain,type)
         for cname in result :
             return cname.target           


