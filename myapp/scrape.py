import requests as rs
from bs4 import BeautifulSoup
import pandas as pd

def other_products(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for a in soup.findAll('div',attrs={'class':['_3liAhj','_3O0U0u']}):
            try:
                
                price=a.find('div',attrs={'class':['_1vC4OE','_1vC4OE _2rQ-NK']})
                pricef.append(price.string)
                name=a.find('a',attrs={'class':['_2cLu-l','_3wU53n']})
                namesf.append(name.string)
            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data1_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Name","Price"])
        #print("Products in Flipkart Site ")
        #print(data1_table.head(5))
        return data1_table.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)
    
        
def mobile_phones(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for line in soup.findAll('div',attrs={'class':'_3O0U0u'}):
            try:
                names=line.find('div',attrs={'class':'_3wU53n'})
                phone_name=names.string;
                namesf.append(phone_name)
                names2=line.find('div',attrs={'class':'_1vC4OE _2rQ-NK'})
                pricef.append(names2.string)   
            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Prices"])
        #print("Products in Flipkart Site ")
        #print(data_table.head(5))
        return data_table.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def fashion(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for line in soup.findAll('div',attrs={'class':'_3O0U0u'}):
            try:
                names=line.find('div',attrs={'class':'_2B_pmu'})
                fashion_name=names.string;
                namesf.append(phone_name)
                names2=line.find('div',attrs={'class':'_1vC4OE'})
                pricef.append(names3.string)   
            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Prices"])
        #print("Products in Flipkart Site ")
        #print(data_table.head(5))
        return data_table.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def paytm(key):
    try:
        url="https://paytmmall.com/shop/search?q="
        final=url+key
        data=rs.get(final)
        soup=BeautifulSoup(data.text,'html.parser')
        namess=[]
        prices=[]
        for line in soup.findAll('div',attrs={'class':'_1fje'}):
            try:
                names=line.find('div',attrs={'class':'UGUy'})
                namess.append(names.string)
                price=line.find('div',attrs={'class':['_1kMS','dQm2']})
                prices.append(price.span.text)
            except:
                namess.append("Name or category error")
                prices.append("Price error")
            
        #print("Items in paytm mall : ")
        #print(data1)
        data1=pd.DataFrame(list(zip(namess,prices)),columns=["Names","Prices"])
        return data1.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def snapdeal(key):
    try:
        url="https://www.shopclues.com/search?q="
        url2="&sc_z=2222&z=0&count=0"
        final=url+key+url2
        data=rs.get(final)
        prices=[]
        namess=[]
        soup=BeautifulSoup(data.text,'html.parser')
        for line in soup.findAll('div',attrs={'class':['column col3 search_blocks','column col3']}):
            try:
                price=line.find('span',attrs={'class':'p_price'})
                prices.append(price.string)
                name=line.find(['span','h2'],attrs={'class':['','prod_name']})
                namess.append(name.string)
            except:
                namess.append("Name or category error")
                prices.append("price error")
        #print('Items in Snapdeal site')
        #print(datat.head(5))
        datat=pd.DataFrame(list(zip(namess,prices)),columns=["Names","Prices"])
        return datat.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)