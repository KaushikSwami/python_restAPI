import json

personal_info='{"name" : ["Venkatesh S","babbi S"],"Pay"  : "00000000","exp"  : "10+","hobbies": ["always sleeping", "always eating"]}'

# loads method will help to convert the above string into python dictionary
dict_data=json.loads(personal_info)
print(dict_data,type(dict_data))
#print(type(dict_data))
#print(dict_data)
#print(dict_data['exp'])
#print(dict_data.keys())
#print(dict_data.values())
#print(dict_data.items())

#for i,j in dict_data.items():
#    print( i , j)

all_hobbies=dict_data['hobbies']
for i in range(len(all_hobbies)):
    print(all_hobbies[i])

print("=============================================")

for i in range(len(dict_data['hobbies'])):
    print(dict_data['hobbies'][i])

print('*********************************************')

all_names=dict_data['name']
for i in range(len(all_names)):
    print(all_names[i])

print("*********************************************")
for i in range(len(dict_data['name'])):
    print(dict_data['name'][i])
