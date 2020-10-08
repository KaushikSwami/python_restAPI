import  requests
import json

response=requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'babbi_1'},)

#print(response.text)
#print(type(response.text))

# converting the python into json using loads method
# res_dict=json.loads(response.text)
#print(type(res_dict))

# we can directly use .json() to parse json
json_res=response.json()
#print(json_res)
#print(type(json_res))
actual_book={}
for i in range(len(json_res)):
    if json_res[i]['aisle']=='111':
        actual_book=json_res[i]
        break
print('the actual book is : ',actual_book)

print(response.status_code)
assert response.status_code==200
print(response.headers)
assert response.headers['Content-Type']=='application/json;charset=UTF-8'

expected_book={
        "book_name": "book 1",
        "isbn": "bk",
        "aisle": "111"
    }

assert expected_book==actual_book




