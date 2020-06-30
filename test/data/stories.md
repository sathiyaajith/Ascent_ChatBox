## Yespath
* greet
  - utter_greet
* give_trainingID
  - action_get_details{"trainid":"BA001"}
  - slot{"trainid":"BA001"}  
* confirm
  - utter_confirm
* vacancy
  - action_check_vacancy 
  

## Nopath 
* greet
  - utter_greet
* give_trainingID
  - action_get_details{"trainid":"BA001"}
  - slot{"trainid":"BA001"}  
* deny
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot