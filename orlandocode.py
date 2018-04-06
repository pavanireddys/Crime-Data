
import requests
url = 'https://moto.data.socrata.com/resource/hirq-qvex.json'
 # call API
myResponse = requests.get(url)
print (myResponse.status_code)
data = myResponse.json()
print(data)

orlando_crime_data=[]
for d in data:
        new = dict()
        new['address'] = d['address_1']
        new['case_number'] = d['case_number']
        new['city'] = d['city']
        new['state'] = d['state']
        new['created_at'] = d['created_at']
        new['day_of_week'] = d['day_of_week']
        new['hour_of_day'] = d['hour_of_day']
        new['incident_datetime'] = d['incident_datetime']
        new['incident_description'] = d['incident_description']
        new['incident_id'] = d['incident_id']
        new['incident_type_primary'] = d['incident_type_primary']
        new['latitude'] = d['latitude']
        new['longitude'] = d['longitude']
        new['parent_incident_type'] = d['parent_incident_type']
        new['updated_at'] = d['updated_at']
        new['zip_code'] = d['zip']
        orlando_crime_data.append(new)

print(orlando_crime_data)
