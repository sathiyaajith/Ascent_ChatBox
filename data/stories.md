##greet path
* greet
  - utter_greet

##training path_cranwell_phneom_end_home
* give_trainingID{"trainid": "BA001"}
  - action_get_details 
  - slot{"trainid": "BA001"}
* confirm
  - utter_confirm 
  
##Hr dept
* human_resource{"human" :"humanresource"}
  - action_vaccleave_type 
  - slot{"human" :"humanresource"}
* leave_types{"leaves" :"leaves"}
  - action_leave_type 
  - slot{"leaves" :"leaves"}
* leave_information{"leavecat" : "casualleave"}  
  - utter_end_flow
  
  

## Story_remain
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafcarnwell_details{"rafcar": "rafcarnwell"} 
  - action_cranwell_type
  - slot{"rafcar": "rafcarnwell"}
* phenom_flight{"pheno" :"phenom"}  
  - utter_phenom_flights
  - slot{"pheno" :"phenom"} 
  - utter_end_flow

  
  
##training path_cranwell_phneom_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafcarnwell_details{"rafcar": "rafcarnwell"} 
  - action_cranwell_type
  - slot{"rafcar": "rafcarnwell"}
* phenom_flight{"pheno" :"phenom"}  
  - utter_phenom_flights
  - slot{"pheno" :"phenom"} 
  - utter_end_flow
 
  

##training path_cranwell_grob_end_home
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafcarnwell_details{"rafcar": "rafcarnwell"} 
  - action_cranwell_type
  - slot{"rafcar": "rafcarnwell"}
* grob_flight{"gro" :"grob"}  
  - utter_grob_flights
  - slot{"gro" :"grob"}
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  
 
##training path_cranwell_grob_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafcarnwell_details{"rafcar": "rafcarnwell"} 
  - action_cranwell_type
  - slot{"rafcar": "rafcarnwell"}
* grob_flight{"gro" :"grob"}  
  - utter_grob_flights
  - slot{"gro" :"grob"}
  - utter_end_flow 
* end_end{"end" :"exit"}  
  - utter_goodbye   

##training path_valley_hawk t1_end_home
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* hawk_flight{"haw" : "hawk"}
  - utter_hawk_flights  
  - slot{"haw": "hawk"}
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  


##training path_valley_hawk t1_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* hawk_flight{"haw" : "hawk"}
  - utter_hawk_flights  
  - slot{"haw": "hawk"}
  - utter_end_flow  
* end_end{"end" :"exit"}  
  - utter_goodbye    
* end_end{"end" :"exit"}  
  - utter_goodbye

  
##training path_valley_BEE hawk t2_end_home
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* bee_flight{"be" : "bee"}
  - utter_bee_flights  
  - slot{"be": "bee"}  
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  
  
  
##training path_valley_BEE hawk t2_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* bee_flight{"be" : "bee"}
  - utter_bee_flights  
  - slot{"be": "bee"}  
  - utter_end_flow
* end_end{"end" :"exit"}  
  - utter_goodbye

  
##training path_valley_chraft t1_end_home
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* bee_flight{"chra" : "chraft"}
  - utter_chraft_flights  
  - slot{"chra": "chraft"} 
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm

##training path_valley_chraft t1_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}
* fixed_type{"fixed": "fixedwing"}  
  - action_flight_location
  - slot{"fixed": "fixedwing"}
* rafvalley_details{"rafval": "rafvalley"} 
  - action_valley_type
  - slot{"rafval": "rafvalley"}
* bee_flight{"chra" : "chraft"}
  - utter_chraft_flights  
  - slot{"chra": "chraft"} 
  - utter_end_flow
* end_end{"end" :"exit"}  
  - utter_goodbye
  
##training path_rotate_end_home
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}  
* rotatory_type{"rotatory": "rotatorywing"}  
  - action_shawbury_type
  - slot{"rotatory": "rotatorywing"} 
* juno_copter{"jun": "junocopter"}
  - utter_juno_copter
  - slot{"jun": "junocopter"}
  - utter_end_flow 
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  

##training path_rotate_end_home_end_exit
* train_center{"traincen" :"trainingcenters"} 
  - action_train_details
  - slot{"traincen" :"trainingcenters"}
* training{"traindetails": "training"}
  - action_train_type
  - slot{"traindetails": "training"}  
* rotatory_type{"rotatory": "rotatorywing"}  
  - action_shawbury_type
  - slot{"rotatory": "rotatorywing"} 
* juno_copter{"jun": "junocopter"}
  - utter_juno_copter
  - slot{"jun": "junocopter"}
  - utter_end_flow   
* end_end{"end" :"exit"}  
  - utter_goodbye  
  
##vacancy path_end_home
* vacancy_details{"vaccde" :"vacancy"}
  - action_check_vacancy
  - slot{"vaccde" :"vacancy"}
  - utter_enter_vacancy
  - utter_end_flow  
* end_flow{"home" :"mainmenu"}  
  - utter_confirm

##vacancy path_end_home
* vacancy_details{"vaccde" :"vacancy"}
  - action_check_vacancy
  - slot{"vaccde" :"vacancy"}
  - utter_enter_vacancy
  - utter_end_flow  
* end_end{"end" :"exit"}  
  - utter_goodbye    
  
##Acropath_meps_testing_end_home
* general_flow{"gen" :"general"}
  - action_general_type
  - slot{"gen" :"general"}
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* confirm {"meps_testing": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
  - action_MEPS_details
  - slot{"meps_testing": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
* meps_testing
  - utter_testing
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  


##Acropath_meps_testing_end_exit
* general_flow{"gen" :"general"}
  - action_general_type
  - slot{"gen" :"general"}
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* confirm {"meps_testing": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
  - action_MEPS_details
  - slot{"meps_testing": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
* meps_testing
  - utter_testing
  - utter_end_flow 
* end_end{"end" :"exit"}  
  - utter_goodbye   
  
##Acropath_meps_physical_yes_end_home
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* confirm {"meps_physical": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
  - action_MEPS_details
  - slot{"meps_physical": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
* meps_physical
  - utter_physical
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm    


##Acropath_meps_physical_yes_end_exit
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* confirm {"meps_physical": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
  - action_MEPS_details
  - slot{"meps_physical": "Physical examinations are vitally important because everyone entering the armed forces must be in good health to endure the challenges of basic training and military service"}
* meps_physical
  - utter_physical
  - utter_end_flow
* end_end{"end" :"exit"}  
  - utter_goodbye   
  
##Acropath_meps_physical_no_end_home
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* deny
  - utter_goodbye
  - utter_end_flow
* end_flow{"home" :"mainmenu"}  
  - utter_confirm  
  
##Acropath_meps_physical_no_end_exit
* acronyms
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* deny
  - utter_goodbye
  - utter_end_flow
* end_end{"end" :"exit"}  
  - utter_goodbye    
  
  
  
## Nopath 
* deny
  - utter_goodbye


 
  

## botchallenge
* bot_challenge
  - utter_iamabot
  
## Goodbye
* goodbye
  - utter_goodbye