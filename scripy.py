#!/usr/bin/env python3
""" 
Job post crawling

"""
import requests
from lxml import html
import csv
count = 0
page_number = 1 
counter = 0
while (count != 10):
    URL = "https://www.simplyhired.com/search?q=cyber+security&l=united+states&fdb=7&pn="+str(page_number)+"&job=Ow5axgzXcn9KVaL0_HUmPQ_8MKBWl1K19Y_oEcqDIFRqydsktAkaIw"
   
    #URL = "https://www.simplyhired.com/search?q=cyber+security&l=united+states&fdb=7&fbclid=IwAR0_AFM-8RsbeLqVHLkUfGmEoKP7_kzw2WmJVBi0CdGWqUb4VfgbEPUZCG8&job=0v7ZQUn-4Z2LnAaoPsXb9qe7bgub9FHfBd0xHRdQyf9kQE-ZrdHGIQ"
    respond = requests.get(URL)
    PAGE = html.fromstring(respond.content)
    rows = PAGE.xpath('//div[@class="card js-job"]')
    path_job_title = './div[@class="jobposting-title-container"]/h2[@class="jobposting-title"]/a/text()'
    path_company_name = './h3/span[@class="jobposting-company"]/text()'
    path_location = './h3/span[@class="jobposting-location"]/span/span/text()'
    path_rating = './h3/span[@class="company-rating"]/span/text()'
    path_salary = './div[@class="SerpJob-metaInfo"]/div[@class="SerpJob-metaInfoLeft"]/span/text()'
  
    for row in rows:
        
        job_title = row.xpath(path_job_title)[0]
        company_name = row.xpath(path_company_name)[0]
        try:
            rating = row.xpath(path_rating)[0]
        except IndexError:
            rating = 'Not Given'
            
        location = row.xpath(path_location)[0]
        try:
            salary = row.xpath(path_salary)[1]
        except IndexError:
            try:
                salary = row.xpath(path_salary)[0]
            except:
                salary = "Not mentioned"
        with open('listed.csv','a',newline='') as f:
            thewriter = csv.writer(f)
        
            if counter == 0:
                header = ['Job Title','Company Name','Rating','Location','Salary']
                thewriter.writerow(header)
                counter += 1
            
            thewriter.writerow([job_title,company_name,rating,location,salary])
        
        if count == 10:
            break
    page_number +=1