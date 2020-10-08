import json

with open('data.json', 'r') as f:
    data=json.load(f)
    print(data,type(data))



for i in range(len(data['courses'])):
    print(data['courses'][i]['title'])

our_website=data['dashboard']['website']
print("our website is ",our_website)