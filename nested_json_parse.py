import json

with open('data.json', 'r') as f:
    data = json.load(f)
    #print(data, type(data))

all_courses=[]



for i in range(len(data['courses'])):
    all_courses.append(data['courses'][i]['title'])

print(all_courses,type(all_courses))


