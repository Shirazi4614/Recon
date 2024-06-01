
from bs4 import BeautifulSoup
import requests

def get_links(url):

    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")

        if href is not None and href.startswith("http"):
            links.append(href)
            
    return links

def crawl_site(url, depth=2):

    site_map = {}
    
    def crawl(url, current_depth):

        if current_depth > depth:
            return
        
        links = get_links(url)
        
        site_map[url] = links
        
        for link in links:
            if link not in site_map:
                crawl(link, current_depth + 1)
    
    crawl(url, 0)
    
    return site_map

site_map = crawl_site("https://www.digikala.com/", depth=2)

for url, links in site_map.items():
    print(url)
    for link in links:
        print("\t", link)

############################################################################################

import dns.resolver

domain = "digikala.com"

# باز کردن فایل
with open('wordlist.txt', 'r') as file:
    # خواندن و چاپ محتوای فایل
    for line in file:
        subdomain = line.strip()  # حذف فاصله‌های سفید اضافی مانند فضای خالی و خط جدید
        try:
            # انجام یک پرس و جو DNS برای هر زیردامنه
            answers = dns.resolver.query(subdomain + "." + domain, "A")
            for ip in answers:
              
              print(subdomain + "." + domain + " - " + str(ip))
              d=domain
              s=subdomain
              
        except:
            pass

##########################################################################################
    import requests

    url = "https://www.digikala.com/"

response = requests.get(url)
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Page not found.")
elif response.status_code == 500:
    print("Internal server error.")
else:
    print("Unknown status code:", response.status_code)

    import requests
    from bs4 import BeautifulSoup

    url = "https://www.digikala.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string

    print(title)
########################################################
import socket
domain = "digikala.com"

ip_address = socket.gethostbyname(domain)

print(f"The IP address of {domain} is {ip_address}")
###########################################################################print("Eip = input()nter ip: ") 


import socket

ip = "185.188.105.11" 


common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

for port in common_ports:  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))
    sock.close()   
####################################################################################################
import re


text = "@amir"

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


email = re.search(pattern, text)
if email:
    print(email.group())
else:
    print("No email found")

text = "023-526-98712"

pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"

phone = re.search(pattern, text)
if phone:
    print(phone.group())
else:
    print("No phone number found")
####################################################################################
# pip install python-whois
import whois

domain = "digikala.com"

w = whois.whois(domain)

print(w)
