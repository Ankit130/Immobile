import openpyxl
import json
import ast 
wb=openpyxl.load_workbook('try1.xlsx')
sht=wb.active

i=2

js={"data":[]}

while i:
    print(i)
    try:
        values=sht[i]
    except:
        break
    try:
        uuid=values[0].value.strip()
    except:
        break
    try:
        title=values[1].value.strip()
    except:
        title=''
    try:
        description=values[2].value.strip()
    except:
        description=''
    try:
        description_location=values[3].value.strip()
    except:
        description_location=''
    try:
        description_other=values[4].value.strip()
    except:
        description_other=''
    try:
        price=values[5].value.strip()
    except:
        price=''
    try:
        brokerage=values[6].value.strip()
    except:
        brokerage=''
    try:
        area=values[7].value.strip()
    except:
        area=''
    try:
        postcode=values[8].value.strip()
    except:
        postcode=''
    try:
        city=values[9].value.strip()
    except:
        city=''
    try:
        region=values[10].value.strip()
    except:
        region=''
    try:
        source=values[11].value.strip()
    except:
        source=''
    try:
        tapped=values[12].value.strip()
    except:
        tapped=''
    try:
        arable=values[13].value.strip()
    except:
        arable=''
    try:
        utilisation=values[14].value.strip()
    except:
        utilisation=''
    try:
        available_from=values[15].value.strip()
    except:
        available_from=''
    try:
        plot_assets=values[16].value.strip()
    except:
        plot_assests=[]
    res = ast.literal_eval(plot_assets) 
    div={"uuid":uuid,
        "title":title,
         "description":description,
         "description_location":description_location,
         "description_other":description_other,
         "price":price,
         "brokerage":brokerage,
         "area":area,
         "postcode":postcode,
         "city":city,
         "region":region,
         "source":source,
         "tapped":tapped,
         "arable":arable,
         "utilisation":utilisation,
         "available_from":available_from,
         "plot_assets":res
         }
    js["data"].append(div)
    #print(div)
    i=i+1


import requests

api_key='d8bfaa6e_860f_4bfc_b5af_776834895f7ea179bf40_98c8_4239_bc68_ee842f72f6bc'

url='https://grundstuecksboerse.maredata.de:8000/v1/import/'+api_key

r=requests.post(url,json=js)
print(r.status_code)
