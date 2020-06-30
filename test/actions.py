from rasa_sdk import Action
from typing import Text
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import FollowupAction
import sqlite3
import urllib.request
from bs4 import BeautifulSoup



class ActionGetDetails(Action):
    
    def name(self) -> Text:
        return "action_get_details"
    
    def run(self, dispatcher, tracker, domain):
        training_id = next(tracker.get_latest_entity_values("batchno"), None)
        print(training_id)
        try:
            sqliteConnection = sqlite3.connect("C:\\Users\\sathi\\rasa_new\\database_rasa.sqlite")
            cursor = sqliteConnection.cursor()

            sqlite_select_Query = 'select * from trainee_details where training_id = "' + str(training_id) + '"'
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print(record)
            
            cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
 
            
        for row in record:
            trainee_name = row[1]
            trainee_department = row[2]
            
            dispatcher.utter_message("Hi {}! - {} department. Would you like to continue?".format(trainee_name,trainee_department))

        return[SlotSet("trainid",training_id)]



class ActionCheckVacancy(Action):

    def name(self) -> Text:
        return "action_check_vacancy"
    
    def run(self, dispatcher, tracker, domain):
        print ("1st step==> fetching the details from site")
        vacc = "https://ascentflighttraining.com/vacancies/" 
        page = urllib.request.urlopen(vacc)
        
        
        soup = BeautifulSoup(page,"lxml")
        print("2nd step==> fetching done")
        for row in soup.find_all('div',attrs={"class" : "post-title"}):
            print (row.text)
            #SlotSet("href_values", row.text[0]) 
            #buttons = [{"title": "href_values", "payload": "vacancy_name"}]
            #dispatcher.utter_button_message("The vacancies are:", buttons)

         
            dispatcher.utter_message("1.{}\n,2.{}\n,3.{},4.{},5.{},6.{},7.{},8.{} and this policy status is {}".format(row.text[0],row.text[1],row.text[2],row.text[3],row.text[4],row.text[5],row.text[6],row.text[7]),"Kindly enter the vacancy title to know more details.")

        return[]

