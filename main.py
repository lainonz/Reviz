import requests, json 
from multiprocessing.dummy import Pool

class Domain:
    def __init__(self, domain):
        self.domain = domain
    
    def reverse(self):
        try:
            r = requests.get("http://api.webscan.cc/?action=query&ip={}".format(self.domain))
            result = json.loads(r.text)
            print("[{}] > [{} Domain]".format(self.domain, len(result)))
            for a in result:
                open('reverse.txt', 'a').write('http://' + a["domain"] + "\n")
        except:
            pass
        
    def process(self):
        website.reverse()

def asuna(list):    
    global website
    website = Domain(list)
    website.process()

def main():
    print("""
Reverse IP
Author : angga1337
    """)
    try:
        urList = open(input("weblist: "), "r").read().replace("https://", "").replace("http://", "").replace("/", "").split("\n")
        thread = int(input("thread: "))
        print("\n")
        pool = Pool(thread)
        pool.map(asuna, urList)
        pool.close()
        pool.join
    except:
        print("[!] Something wrong please try again...")

if __name__ == '__main__':
    main()

