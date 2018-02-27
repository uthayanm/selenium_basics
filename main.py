#importing selenium webdriver and request module

from selenium import webdriver
import requests

#downloaded selenium webdriver's location path referenced here

driver = webdriver.Chrome("G:/chromedriver.exe")
driver.get('https://www.krossover.com/products/basketball/')

# xpath element of selenium webdriver allow us to find all the urls inside the main webpage

for a in driver.find_elements_by_xpath('.//a'):

     inner_urls = a.get_attribute('href')

     # eliminate the urls that has None at its reference
     if inner_urls is not None:

         if(inner_urls.startswith('tel')==True or inner_urls.startswith('mailto')==True ):# while parsing into all urls some them has tel:9287676 or mailto:kkjkjbkb@something so we eliminate those
             continue
         unique_urls = requests.get(inner_urls)# request module allow us to see the statuscode of urls like "200" or "404"

         print inner_urls # prints all the inner urls in that given link
         print unique_urls.status_code # and their respective statuscodes

         if(unique_urls.status_code=="404"):
             print "url is not  valid!"
         else:
             print "the URLS is Valid"  
