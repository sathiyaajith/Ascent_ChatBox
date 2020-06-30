import urllib.request
from bs4 import BeautifulSoup

vacc = "https://ascentflighttraining.com/vacancies/" 
page = urllib.request.urlopen(vacc)

soup = BeautifulSoup(page,"lxml")
for row in soup.find_all('div',attrs={"class" : "post-title"}):
    print (row.text)




