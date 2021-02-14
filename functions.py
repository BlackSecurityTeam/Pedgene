from colorama import init,Fore
init() # Call Colors
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET
WHITE = Fore.WHITE

class Tools:

    def banner(self=None):
        print(f""" {BLUE}
        

.______    _______  _______    _______  _______ .__   __.  _______ 
|   _  \  |   ____||       \  /  _____||   ____||  \ |  | |   ____|
|  |_)  | |  |__   |  .--.  ||  |  __  |  |__   |   \|  | |  |__   
|   ___/  |   __|  |  |  |  ||  | |_ | |   __|  |  . `  | |   __|  
|  |      |  |____ |  '--'  ||  |__| | |  |____ |  |\   | |  |____ 
| _|      |_______||_______/  \______| |_______||__| \__| |_______|
                  {Fore.CYAN}                                                 

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                            
            ~  Coded By  : Mahdi Hassani            ~
            ~  WebSite   : BlackSecurityTeam.Com    ~
            ~  Telegram  : @Black_Security          ~
            ~  Instagram : @BlackSecurityTeam       ~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                     
        {RESET}""")
        
    def options(self=None):
            print(f"""
        OPTIONS :
        {RED}
        [ 1 ]  -  Whois
        [ 2 ]  -  Dns Checker
        [ 3 ]  -  Ip Location
        [ 4 ]  -  Sub Domains
        [ 5 ]  -  WordPress Plugins
        [ 6 ]  -  Admin Page Finder
        [ 7 ]  -  WebSite Information
        [ 8 ]  -  Port Scanner
        [ 9 ]  -  Show HTTP Header  
        
        {RESET}
        """)
    
