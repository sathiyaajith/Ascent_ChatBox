from rasa_sdk import Action
from typing import Text
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import FollowupAction
import sqlite3
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import html5lib
from tabulate import tabulate

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionGetDetails(Action):
    
    def name(self) -> Text:
        return "action_get_details"
         
    def run(self, dispatcher, tracker, domain):
        training_id = next(tracker.get_latest_entity_values("trainid"), None)
        training_id = training_id.upper()
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
            
            buttons = [{"title": "Yes", "payload": "yes"},{"title": "No", "payload": "no"}]
            dispatcher.utter_button_message("Hi {}! - {} department. Would you like to continue?".format(trainee_name,trainee_department), buttons)
            #dispatcher.utter_message("Hi {}! - {} department. Would you like to continue?".format(trainee_name,trainee_department))

        return[SlotSet("trainid",training_id)]



class ActionCheckVacancy(Action):

    def name(self) -> Text:
        return "action_check_vacancy"
    
    def run(self, dispatcher, tracker, domain):
        print ("1st step==> fetching the details from site")
        vacc = "https://ascentflighttraining.com/vacancies/" 
        page = urllib.request.urlopen(vacc)
        
        
        soup = BeautifulSoup(page,"html.parser")
        print("2nd step==> fetching done")
        lst = []
        for row in soup.find_all('div',attrs={"class" : "post-title"}):
            #print (row.text)
            lst.append(row.text)
        print(lst)
            #SlotSet("href_values", row.text[0]) 
            #buttons = [{"title": "href_values", "payload": "vacancy_name"}]
            #dispatcher.utter_button_message("The vacancies are:", buttons)
        print("slot setted")
        dispatcher.utter_message("Here is the list of vacancies: {}".format('\n'.join(lst)))
        #dispatcher.utter_message(template="utter_enter_vacancy")
        return [] 



  
        
class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["useracro"]

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        user_input_acronym = tracker.get_slot('useracro')
        user_input_acronym = user_input_acronym.upper()
        print(user_input_acronym)
        try:
            sqliteConnection = sqlite3.connect("C:\\Users\\sathi\\rasa_ascent\\acro_database.sqlite")
            cursor = sqliteConnection.cursor()
            sqlite_select_Query = 'select * from acroinfo where acronym = "' + str(user_input_acronym) + '"'
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            #acro_lst=[]
            for row in record:
                #acro_lst.append(row)
                dispatcher.utter_message("Abbreviation:  {}".format(row[1]))
                dispatcher.utter_message("Description:  {}".format(row[2])) 
            #dispatcher.utter_message(tabulate(acro_lst[2],headers=['Description']))
            cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                sqliteConnection.close()
        buttons = [{"title": "Yes", "payload": "Yes"},{"title": "No", "payload": "No"}]
        dispatcher.utter_button_message("Do you want to know more about {} ?".format(user_input_acronym),buttons)
        
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="useracro", intent='acro'),
                     self.from_text()]
            
        }        


class ActionMEPSDetails(Action):

    def name(self) -> Text:
        return "action_MEPS_details"
    
    def run(self, dispatcher, tracker, domain):
        url = 'https://www.military.com/join-armed-forces/meps-process-requirements.html'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')
        cont_lst = []
        for heading in soup.find_all(["h2"]):
            cont_lst.append(heading.text.strip())
        SlotSet("meps_testing",cont_lst[1])
        SlotSet("meps_physical",cont_lst[2])
        print(cont_lst[1])
        print(cont_lst[2])
        buttons = [{"title": "MEPS Testing", "payload": "MEPS Testing"},{"title": "MEPS Physical", "payload": "MEPS Physical"}]
        dispatcher.utter_button_message("Do you want to know more about :",buttons)
        
        #Fetching the details of testing and physical
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
        
        
        return [SlotSet("testing_desc", desc_lst[4]),SlotSet("testing_desc_add", desc_lst[6]),SlotSet("physical_desc", desc_lst[9]),SlotSet("physical_desc_add",desc_lst[11])]      


class ActionTrainType(Action):
    
    def name(self) -> Text:
        return "action_train_type"
         
    def run(self, dispatcher, tracker, domain):
        train_info = next(tracker.get_latest_entity_values("traindetails"), None)
        print(train_info)
        dispatcher.utter_message(template="utter_ask_train")
        print("train slot setted")
        return[SlotSet("traindetails",train_info)]
        
class ActionVaccleaveType(Action):
    
    def name(self) -> Text:
        return "action_vaccleave_type"
         
    def run(self, dispatcher, tracker, domain):
        leave_info = next(tracker.get_latest_entity_values("human"), None)
        print(leave_info)
        dispatcher.utter_message(template="utter_confirm_vacc")
        print("vaccleave slot setted")
        return[SlotSet("human",leave_info)]        

class ActionLeaveType(Action):
    
    def name(self) -> Text:
        return "action_leave_type"
         
    def run(self, dispatcher, tracker, domain):
        leave_details = next(tracker.get_latest_entity_values("leaves"), None)
        print(leave_details)
        dispatcher.utter_message(template="utter_ask_leave")
        print("leave slot setted")
        return[SlotSet("leaves",leave_details)]  
        
class ActionGeneralType(Action):
    
    def name(self) -> Text:
        return "action_general_type"
         
    def run(self, dispatcher, tracker, domain):
        leave_details = next(tracker.get_latest_entity_values("acrodetails"), None)
        print(leave_details)
        dispatcher.utter_message(template="utter_confirm_acro")
        print("acro slot setted")
        return[SlotSet("acrodetails",leave_details)]          
        
class ActionTrainDetails(Action):
    
    def name(self) -> Text:
        return "action_train_details"
         
    def run(self, dispatcher, tracker, domain):
        tr_details = next(tracker.get_latest_entity_values("traincen"), None)
        print(tr_details)
        dispatcher.utter_message(template="utter_confirm_train")
        print("acro slot setted")
        return[SlotSet("traincen",tr_details)]  

class ActionFlightLocation(Action):
    
    def name(self) -> Text:
        return "action_flight_location"
         
    def run(self, dispatcher, tracker, domain):
        cranwell_info = next(tracker.get_latest_entity_values("fixed"), None)
        print(cranwell_info)
        dispatcher.utter_message(template="utter_ask_location")
        print("fixed slot setted")
        return[SlotSet("fixed",cranwell_info)]
        
class ActionCranwellType(Action):
    
    def name(self) -> Text:
        return "action_cranwell_type"
         
    def run(self, dispatcher, tracker, domain):
        phenom_info = next(tracker.get_latest_entity_values("pheno"), None)
        print( phenom_info)
        dispatcher.utter_message(template="utter_cranwell_types")
        print("pheno slot setted")
        return[SlotSet("pheno", phenom_info)]        
        

class ActionValleyType(Action):
    
    def name(self) -> Text:
        return "action_valley_type"
         
    def run(self, dispatcher, tracker, domain):
        haw_info = next(tracker.get_latest_entity_values("haw"), None)
        print( haw_info)
        dispatcher.utter_message(template="utter_valley_types")
        print("haw slot setted")
        return[SlotSet("haw", haw_info)]

class ActionShawburyType(Action):
    
    def name(self) -> Text:
        return "action_shawbury_type"
         
    def run(self, dispatcher, tracker, domain):
        rotat_info = next(tracker.get_latest_entity_values("rotatory"), None)
        print( rotat_info)
        dispatcher.utter_message(template="utter_rotate_location")
        print("rotat slot setted")
        return[SlotSet("rotatory", rotat_info)]        
