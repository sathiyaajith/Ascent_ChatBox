##import urllib.request
##from bs4 import BeautifulSoup
##
##vacc = "https://ascentflighttraining.com/vacancies/" 
##page = urllib.request.urlopen(vacc)
##
##soup = BeautifulSoup(page,"lxml")
##lst = []
##for row in soup.find_all('div',attrs={"class" : "post-title"}):
####    print (row.text)
##    lst.append(row.text)
##print("vacancy_list",(', '.join(lst)))
##
##
##
##
##
##


##import urllib.request
##from bs4 import BeautifulSoup
##
##word = input("Enter the word: ")
##wiki = "https://abbreviations.yourdictionary.com/articles/military-acronyms.html"
##page = urllib.request.urlopen(wiki)
##
##soup = BeautifulSoup(page)
##
##for row in soup.select('table#table4 tr'):
##    cells = row.find_all('td')
##    print (row.get_text(' - ', strip=True))



##import sqlite3
##from tabulate import tabulate
##
##sqliteConnection = sqlite3.connect("C:\\Users\\sathi\\rasa_new\\acro_rasa.sqlite")
##cursor = sqliteConnection.cursor()
##sqlite_select_Query = 'select * from acronym_details'
##cursor.execute(sqlite_select_Query)
##record = cursor.fetchall()
##acro_lst=[]
##for row in record:
####   print ("acronym = ", row[0])
####   print("abbre  = ", row[1])
####   print ("link = ", row[2])
##   acro_lst.append(row)
##print(tabulate(acro_lst,headers=['acronyms','abbervation','links']))
##
##
##cursor.close()



##import requests
##from bs4 import BeautifulSoup



##from bs4 import BeautifulSoup, NavigableString, Tag
##import requests
##
##url = 'https://www.military.com/join-armed-forces/meps-process-requirements.html'
##reqs = requests.get(url)
##soup = BeautifulSoup(reqs.text, 'lxml')
##print("List of all the h1, h2, h3 :")
##cont_lst = []
##for heading in soup.find_all(["h2"]):
##   cont_lst.append(heading.text.strip())
##print(type(cont_lst[1]))
##print(cont_lst[2])
##soup = BeautifulSoup(reqs.text, 'html.parser')
##
##desc_lst = []
##for header in soup.find_all('h2'):
##    nextNode = header
##    
##    while True:
##        nextNode = nextNode.nextSibling
##        if nextNode is None:
##            break
##        if isinstance(nextNode, NavigableString):
##            desc_lst.append(nextNode.strip())
##        if isinstance(nextNode, Tag):
##            if nextNode.name == "h2":
##                break
##            desc_lst.append(nextNode.get_text(strip=True).strip())
##print(type(desc_lst[4]))
##print(desc_lst[6])

##print(desc_lst[9])
#print(desc_lst[11][0])


## vacany code##

from bs4 import BeautifulSoup, NavigableString, Tag
import requests

url = 'https://ascentflighttraining.com/operations-manager-raf-valley/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print(soup)
print("List of all the h1, h2, h3 :")
cont_lst = []
for heading in soup.find_all(["h2"]):
   cont_lst.append(heading.text.strip())
print(type(cont_lst[1]))
print(cont_lst[2])
soup = BeautifulSoup(reqs.text, 'html.parser')

desc_lst = []
for header in soup.find_all('h2'):
    nextNode = header
    
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if isinstance(nextNode, NavigableString):
            desc_lst.append(nextNode.strip())
        if isinstance(nextNode, Tag):
            if nextNode.name == "h2":
                break
            desc_lst.append(nextNode.get_text(strip=True).strip())
print(type(desc_lst[4]))





class ActionEnterVacancy(Action):

    def name(self) -> Text:
        return "action_enter_vacancy"
    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        if message == "operations manager":
          dispatcher.utter_message("Please Click on the url: https://ascentflighttraining.com/operations-manager-raf-valley/")
        elif message == "AJT QFI":
          dispatcher.utter_message("Please Click on the url: https://ascentflighttraining.com/ajt-qfi-training-innovation-sme/")
        else:
          dispatcher.utter_message("Please Click on the url: https://ascentflighttraining.com/qualified-observer-instructor-culdrose/")
        return []

