import requests
import os
import concurrent.futures
import sys
import urllib3
import socket

print('''
8888888b.                   d8b
888   Y88b                  Y8P
888    888
888   d88P .d88b.  888  888 888 88888888
8888888P" d8P  Y8b 888  888 888    d88P
888 T88b  88888888 Y88  88P 888   d88P
888  T88b Y8b.      Y8bd8P  888  d88P
888   T88b "Y8888    Y88P   888 88888888

    Reverse IP
    By : angga1337
                         ''')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://api.webscan.cc/?action=query&ip="
file_input = input("Weblist: ")
file_result = input("Result filename: ")

try:
    threads = int(input("Thread: "))
    if threads <= 0:
        raise ValueError
except ValueError:
    print("Please provide a valid number!")
    sys.exit()

if not os.path.exists(file_result):
    open(file_result, "w").close()

def get_domains(ip):
    if 'http' in ip or 'www' in ip or '/' in ip:
        urls = ip.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", "")
    else:
        urls = ip

    ips = socket.gethostbyname(urls)
    print(f"[{ip}] => [{ips}]")
    response = requests.get(url + ips, verify=False)
    data = response.json()
    domains = [item['domain'] for item in data]
    return domains

def reverse(ip):
    domains = get_domains(ip)
    total_domains = len(domains)
    print(f"[{ip}] => [{total_domains} domain]")
    with open(file_result, "a", encoding="utf-8") as f:
        for domain in domains:
            f.write(domain + "\n")

try:
    ips = []
    with open(file_input, "r") as f:
        ips = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        results = [executor.submit(reverse, ip) for ip in ips]

except KeyboardInterrupt:
    print("\nStopped!")
finally:
    print(f"Result saved to {file_result}")

