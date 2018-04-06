# make sure to install these packages before running:
# pip install requests
# pip install json

import requests   #requests module is used to fetch the HTML code from a webpage
import json   #json is a module used to convert the python dictionary into a JSON string that can be written into a file

crime_data=[]

#Here is creating a function that replaces the police_department_dataset_identifier for required crime data for particular city 

def url_from_api(police_department_dataset_identifier):
    
    url = 'https://moto.data.socrata.com/resource/'+police_department_dataset_identifier+'.json'
    
    # call API
    myResponse = requests.get(url)
    #The url of the API contains dataset identifier is retrieved by the get function and stored in myResponse
 
    data = myResponse.json()
    #the data stored in the variable myResponse is converted into json by ginving myResponse.json() ind stored in variable data
    
    #print(data)
    
    #NOTE: Here I have used a for loop because to itetate the data of variable data
    
    for d in data:
        new = dict()   #Creating a empty dictionary name as new for storing the data in required formate
        
        new['address'] = d['address_1']
        new['case_number'] = d['case_number']
        new['city'] = d['city']
        new['state'] = d['state']
        new['created_at'] = d['created_at']
        new['ay_of_week'] = d['day_of_week']
        new['hour_of_day'] = d['hour_of_day']
        new['incident_datetime'] = d['incident_datetime']
        new['incident_description'] = d['incident_description']
        new['incident_id'] = d['incident_id']
        new['incident_type_primary'] = d['incident_type_primary']
        new['latitude'] = d['latitude']
        new['longitude'] = d['longitude']
        new['parent_incident_type'] = d['parent_incident_type']
        new['updated_at'] = d['updated_at']
        
        
        crime_data.append(new)    #Append the new dictionary to a empty list crime_data


#Tthis is how to call function by giving the police_department_dataset_identifier of required city crime data

url_from_api('6ycu-kfnm')   #North Miami Beach Police Department dataset identifier is '6ycu-kfnm'


#file created for the purpose of storing data; North Miami Beach Police_crime_data.json stores crime data of North Miami Beach Police
file = open("North Miami Beach Police_data.json","w")

json.dump(crime_data,file)   #dumps the crime_data by using json.dumps function
file.close()  #closes the file

