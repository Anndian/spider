# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:23:40 2017

@author: zedian
"""

import urllib2
import json
from bs4 import BeautifulSoup
from pandas import DataFrame

def get_html(url):
    request = urllib2.Request(url)
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
    html = urllib2.urlopen(request)
    print html.getcode()
    return html.read()



urls = ['http://sme.macaugoodhands.com/zh_TW/search/?service={}'.format(str(i)) for i in range(1,18)]
category_url = []
category_name = []
start_url = 'http://sme.macaugoodhands.com'
def get_category(url):
    #url='http://tuan.ctrip.com/group/ajax/AjaxHotelComment.ashx?ctripid=385221&currentIndex=1'
    headers={'Origin':"http://sme.macaugoodhands.com",'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
    req=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(req)
    content=res.read()
    #print content
    contenthtml= BeautifulSoup(content,'lxml')
    urlcontent = contenthtml.select('#page > div.main-content > div > div > div.page-content > div > div:nth-of-type(2) > div.col-md-3 > div:nth-of-type(1) > div > a')
    urlcontent1 = contenthtml.select('#collapseFacet > a')    
    #print urlcontent1  
    for i in urlcontent:
        category_url.append(start_url + i.get('href'))
        category_name.append(i.text.strip().split('\n')[-1].replace(' ','').strip())
    for j in urlcontent1:
        category_url.append(start_url + j.get('href'))
        category_name.append(j.text.strip().split('\n')[-1].replace(' ','').strip())

for url in urls:
    get_category(url)
    
    
data = {'category_name':category_name,'category_url':category_url}
frame=DataFrame(data,columns=['category_name','category_url'])
frame.to_excel('C:\\Users\\zhchenjia\\Desktop\\macau2017.xlsx',index=False)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
names = []
phones = []
address = []
category1 = []
category2 = []
work_url = []
def get_macau(url):
    headers={'Origin':"http://sme.macaugoodhands.com",'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
    req=urllib2.Request(url,headers=headers)
    try:
        res=urllib2.urlopen(req)
        content=res.read()
        #print content
        contenthtml= BeautifulSoup(content,'lxml')
        category2s = contenthtml.find_all("a",attrs={"class": "list-group-item active"})
        name = contenthtml.select('#page > div.main-content > div > div > div.page-content > div > div > div.col-md-9 > div > div > h4 > a')
        phone = contenthtml.select('#page > div.main-content > div > div > div.page-content > div > div > div.col-md-9 > div > div > h5')        
        category1s = contenthtml.select('#dropdownMenu1')
        #print urlcontent1  
        for i in name:
            names.append(i.get_text().replace(' ','').strip())
        for j in phone:
            phones.append(j.text.strip().split('\n')[0].replace(' ','').strip())
            address.append(j.text.strip().split('\n')[-1].replace(' ','').strip())
            for z in category1s:
                category1.append(z.get_text().replace(' ','').strip())
                work_url.append(url)
            for y in category2s:
                category2.append(y.text.strip().split('\n')[-1].replace(' ','').strip())
    except urllib2.HTTPError:
        pass

for j in range(len(category_url)):
    all_url = [category_url[j] + '&page={}'.format(str(i)) for i in range(1,101)]
    for u in all_url:
        get_macau(u)
        
        
       
data = {'marks':marks,'names':names,'phones':phones,'address':address,'work_url':work_url}
frame=DataFrame(data,columns=['marks','names','phones','address','work_url'])
frame.to_excel('C:\\Users\\zhchenjia\\Desktop\\macau20170322.xlsx',index=False)