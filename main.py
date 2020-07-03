import argparse
import time
from function import reset
from download import download
import openpyxl

parser = argparse.ArgumentParser(description='Scraper for immobile')
parser.add_argument('-c','--check' ,type=str,required=True,
                    help='scrape from last checkpoint or start from scratch')
parser.add_argument('-s','--seed', type=int,help='Number of Seeds',nargs='?',default=20)
#parser.add_argument('-f','--file',type=str,required=True,help='Output file name')
args = parser.parse_args()
file='data.xlsx'
seed=args.seed
check=args.check



if(check!='last' and check!='new'):
    print('Argument --check/-c should be  last or new')
    print('Exiting.....')
    exit()

if(check=='new'):
    reset('1')
    wb=openpyxl.Workbook()
    sht=wb.active
    file='try1.xlsx'
    wb.save(file)

wb=openpyxl.Workbook('try1.xlsx')
sht=wb.active
while(1):
    flag=download(file,seed,sht,wb)
    if(flag==None):
        print("All sitemaps downloaded")
        print("Scraping successful")
        print("Exiting")
        break


