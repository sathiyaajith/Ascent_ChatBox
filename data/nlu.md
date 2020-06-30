## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:give_trainingID
- my training ID is [BA001](trainid) 
- [MW001](trainid)
- Training ID is[RW001](trainid)
- Here is my training id [RW001](trainid)
- [MW003](trainid)
- [MW002](trainid)
- Training ID is[RW004](trainid)
- Here is my training id [BA001](trainid)
- this is my training id [MW006](trainid)
- let me give my training id [RW005](trainid)

## regex: trainid
- \b\[a-zA-Z]{2}\d{3}\b

## intent:acronyms
- [MEPS](useracro:MEPS)
- [CIA](useracro)
- [DEERS](useracro)
- [MOD](useracro:MOD)
- [FAST](useracro)
- [AAFES](useracro:AAFES)
- [CID] (useracro:CID)
- [TAM](useracro)
- [AAAV](useracro:AAAV)
- [AEF](useracro)
- [CFE](useracro)
- [ELB](useracro:ELB)

## intent:confirm
- yes
- indeed
- of course
- that sounds good
- correct
- yep
- ok
- okay
- sure
- perfect

## intent:deny  
- no
- never
- I don't think so
- don't like that
- no way
- not really 

## intent:goodbye
- bye
- goodbye
- see you around
- see you later


## intent:vacancy_details
- [vacancy](vaccde)
- [Vacancy](vaccde)
- [VACANCY](vaccde)

## intent:acronyms
- [acronyms](acrodetails)
- [Acronyms](acrodetails)
- [ACRONYMS](acrodetails)

## intent:leave_types
- [Leave](leaves)
- [leave](leaves)
- [LEAVES](leaves)

## intent:leave_information
- [](leavecat)
- [sickleave](leavecat)
- [maternityleave](leavecat)
- [annualleave](leavecat)

## intent:train_center
- [trainingcenters](traincen)
- [TrainingCenters](traincen)
- [Training centers](traincen)
- [training centers](traincen)

## intent:human_resource
- [humanresource](human)
- [Humanresource](human)
- [Human resource](human)
- [Human resource](human)

## intent:general_flow
- [general](gen)
- [General](gen)
- [GENERAL](gen)

## intent:finance_flow
- [financeandcontract](fin)
- [Financeandcontract](fin)
- [FinanceandContract](fin)
- [FinanceandContract](fin)


## intent:training
- [training](traindetails)
- [Training](traindetails)
- [train](traindetails)
- [Train](traindetails)

## intent:meps_testing
- MEPS Testing
- Meps Testing
- meps Testing

## intent:meps_physical
- MEPS Physical
- Meps Physical
- meps Physical

## intent:fixed_type
- [fixedwing](fixed)
- [Fixedwing](fixed)
- [Fixed wing](fixed)
- [fixed wing](fixed) 

## intent:rotatory_type
- [Rotatory Wing](rotatory)
- [rotatorywing](rotatory)
- [RotatoryWing](rotatory)
- [Rotatorywing](rotatory)
- [rotatoryWing](rotatory)

## intent:rafcarnwell_details
- [rafcarnwell](rafcar)
- [Rafcarnwell](rafcar)
- [raf carnwell](rafcar)
- [Raf Carnwell](rafcar)
- [Raf Carnwell](rafcar)

## intent:rafvalley_details
- [rafvalley](rafval)
- [Rafvalley](rafval)
- [Raf Valley](rafval)
- [Raf valley](rafval)
- [raf valley](rafval)

## intent:phenom_flight
- [Phenom](pheno)
- [phenom](pheno)
- [PHENOM](pheno)

## intent:grob_flight
- [Grob](gro)
- [grob](gro)
- [GROB](gro)

## intent:hawk_flight
- [Hawk](haw)
- [hawk](haw)
- [HAWK](haw)

## intent:bee_flight
- [Bee](be)
- [bee](be)
- [BEE](be)

## intent:chraft_flight
- [Chraft](chra)
- [chraft](chra)
- [CHRAFT](chra)

## intent:rafshawbury_details
- [rafshawbury](rafsha)
- [Rafshawbury](rafsha)
- [Raf Shawbury](rafsha)
- [Raf shawbury](rafsha)
- [raf shawburjunocoptery](rafsha)

## intent:juno_copter
- [Junocopter](jun)
- [junocopter](jun)

## intent:end_flow
- [mainmenu](home)
- [Mainmenu](home)
- [MainMenu](home)
- [MAINMENU](home)

## intent:end_end
- [Exit](end)
- [exit](end)
- [EXIT](end)



## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
