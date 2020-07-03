import requests
from bs4 import BeautifulSoup as soup
import os
import gzip
import io
import wget
import os

path=os.getcwd()

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}

headers={'Host': 'www.revealname.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.2.671757240.1589188445; __gads=ID=261e7af86ebc5416:T=1589188453:S=ALNI_MYa9BwKnofpfyUxz-wfSBpYy73S-w; pop_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22a2f0ee0bf5a45657a20e83549453785e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22157.47.200.180%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A76%3A%22Mozilla%2F5.0+%28X11%3B+Ubuntu%3B+Linux+x86_64%3B+rv%3A73.0%29+Gecko%2F20100101+Firefox%2F73.0%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1589282585%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D3ff204ecf866a76b4468b4fe34fa7333d12903bd; __stripe_mid=8b7d6260-76ef-455e-b555-a2daec5208e5; _gid=GA1.2.2006880808.1589280754',
'Upgrade-Insecure-Requests': '1'
}

def getlocs(ur):
    r=requests.get(ur,headers=headers)
    Soup=soup(r.text,'html.parser')
    return Soup.findAll('loc')

def reset(i):
    #Soup=getcontent('https://www.revealname.com/sitemap.xml','1')
    with open('cache.txt','w') as f:
        f.write(i)
            
def geturl():
    with open('cache.txt','r') as f:
        data=f.read()
        return data

