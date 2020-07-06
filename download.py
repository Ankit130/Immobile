
import os
import aiohttp
from aiohttp import ClientSession
import asyncio
from bs4 import BeautifulSoup as soup
import csv
import requests
import time
from function import geturl,reset
import json
import openpyxl

async def fetch(d, session):
            retries=0
            url='https://www.immobilienscout24.de/expose/'+d['@id']
    
            async with session.get(url) as response:
                delay = response.headers.get("DELAY")
                date = response.headers.get("DATE")
                print("{}:{} with delay {}".format(date, response.url, delay))
                content= await response.read()
                Soup=soup(content,'html.parser')
                uuid=d['@id']+'@immobilienscout24.de'
                title=d['resultlist.realEstate']['title']
                try:
                  description=Soup.find('pre',attrs={'class':'is24qa-objektbeschreibung'}).text.strip()
                except:
                  description=''
                try:
                  loca_des=Soup.find('pre',attrs={'class':'is24qa-lage'}).text.strip()
                except:
                  loca_des=''
                try:
                  other_des=Soup.find('pre',attrs={'class':'is24qa-sonstiges'}).text.strip()
                except:
                  other_des=''
                try:
                  price=Soup.find('div',attrs={'class':'is24qa-kaufpreis is24-value font-semibold is24-preis-value'}).text.strip()
                except:
                  price=''
                try:
                  brokerage=Soup.find('dd',attrs={'class':'is24qa-provision grid-item two-fifths'}).text.strip()
                except:
                  brokerage=''
                try:
                  area=Soup.find('div',attrs={'class':'is24qa-flaeche is24-value font-semibold'}).text.strip()
                except:
                  area=''
                add=d['resultlist.realEstate']['address']
                postcode=add['postcode']
                city=add['city']
                region=add['quarter']
                source=url
                try:
                  tapped=Soup.find('dd',attrs={'class':'is24qa-erschliessung grid-item three-fifths'}).text.strip()
                except:
                  tapped=''
                try:
                  arable=Soup.find('dd',attrs={'class':'is24qa-bebaubar-nach grid-item three-fifths'}).text.strip()
                except:
                  arable=''
                try:
                  utilisation=Soup.find('dd',attrs={'class':'is24qa-empfohlene-nutzung grid-item three-fifths'}).text.strip()
                except:
                  utilisation=''
                try:
                  available_from=Soup.find('dd',attrs={'class':'is24qa-verfuegbar-ab grid-item three-fifths'}).text.strip()
                except:
                  available_from=''
                plot_assets=[]
                try:
                    for l in d['resultlist.realEstate']['galleryAttachments']['attachment']:
                      try:
                        plot_assets.append({'file':l['@xlink.href']})
                      except:
                        pass
                except:
                    print(d["@id"])
                row=[uuid,title,description,loca_des,other_des,price,brokerage,area,postcode,city,region,source,tapped,arable,utilisation,available_from,str(plot_assets)]
                
                return row
        




async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        return await fetch(url, session)

async def run(r,locs,seed):
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(seed)
    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, locs[i], session))
            tasks.append(task)
        return await  asyncio.gather(*tasks)

def getlocs(i):
    r=requests.post('https://www.immobilienscout24.de/Suche/de/grundstueck-kaufen?pagenumber='+str(i))
    data=r.json()['searchResponseModel']
    try:
        return data['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']
    except:
        return None
def download(file,seed,sht,wb):
    url=geturl()
    print(url)
    i=int(url)
    if(i>543):
        return None
    locs=getlocs(i)
    if(locs==None):
        return None
    number=len(locs)
    print(number)
    
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number,locs,seed))
    rows=loop.run_until_complete(future)
    
    
    with open(file,'a') as f:
        for row in rows:
            if(row[0]==''):
                continue
            sht.append(row)
    wb.save(file)
    reset(str(i+1))
    return url
