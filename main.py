import functions
import os
from modules import whoiis,ddns,googlemap,subdomain,plugins,admin_finder,site_info,port_scanner,http_header
from pprint import pprint

GREEN = functions.GREEN
RED = functions.RED
BLUE = functions.BLUE
RESET = functions.RESET
WHITE = functions.WHITE

while True :
    os.system('cls' or 'clear')
    functions.Tools.banner(None)
    functions.Tools.options(None)

    try:
        
        num = input(f" {RED} [+] {WHITE} Enter a number from the list : {RESET}")
        if num == '1' : ######################### whois
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            whois = whoiis.Information(domain)
            res_domain = whois.Domain_info(domain)
            res_Server = whois.Server_info(domain)
            print(f" {RED} Result of Domain : {GREEN}")
            pprint(res_domain)
            print(f" {RED} \n Result of Server : {GREEN}  ")
            pprint(res_Server)
            input()
        elif num == '2' : ########################## Dns
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            Dns = ddns.Dns_Checker(domain)
            Dns.options()
            num = input(f" {RED} [**] {WHITE} Enter a number from list :  {RESET}")
            if num == '1' :
                res = Dns.A_record(domain)
                print(f" {GREEN} [+] ip ==> {WHITE} {res}")
                input()

            elif num == '2' :
                res = Dns.Cname(domain)
                print(f" {GREEN} [+] ip ==> {WHITE} {res}")
                input()

            elif num == '3' : 
                res = Dns.Mx_record(domain)
                print(f'{GREEN} Host {res.exchange}  has preference {res.preference} {RESET}') 
                input()
            elif num == '00' :
                continue  
        elif num == '3' : ############ Ip location
            googlemap.generate()
        elif num == '4' : ############# Subdomains
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            subdomain.Discover_Subdomains(domain,WHITE,BLUE,RESET,RED,GREEN)
            print(f" {BLUE} Discover Ended ... {RESET}")
            input()
        elif num == '5' : ############ WordPrss Plugins
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            plugins.Discover_Plugins(domain,BLUE,RESET,RED,GREEN)
            print(f" {BLUE} Discover Ended ... {RESET}")
            input()
        elif num == '6' : ########### Admin Finder  
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            admin_finder.admin_finder(domain,GREEN,RED,RESET)
            print(f" {BLUE} Discover Ended ... {RESET}")
            input()
        elif num == '7' : ############ Web Site Info
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            site_info.Fetch_info(domain,GREEN)
            input()
        elif num == '8' : ############ Port scanner
            os.system('cls' or 'clear')
            ip = input(f" {RED} [**] {WHITE} Enter a ip :  {RESET}")
            rrange = input(f" {RED} [**] {WHITE} Enter a Range of port :  {RESET}")
            port_scanner = port_scanner.Portscanner(ip,rrange,GREEN,RED,RESET)
            port_scanner.Scan()
            print(f" {BLUE} Discover Ended ... {RESET}")
            input()  
        elif num == '9' : ############ Http Header
            os.system('cls' or 'clear')
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            res = http_header.http_header(domain)
            print(f"{RED} Results : \n")
            print(f"{WHITE} {res}")
            input()    
     

        
    


       

        




        

       




                        





            
    except Exception as e:
        print(f" {RED} Error : {e}")
        input()
        continue