import requests
import json
from payload import *

added_book={}

addbook_response=requests.post('http://216.10.245.166/Library/Addbook.php',
              json=addbook_payload('book ','bk','222','babbi_1'),headers={'Content-Type':'application/json'},)

res=addbook_response.json()

print(addbook_response.status_code)
book_id =res['ID']
print('book id is : ',book_id)
print('book is',res['Msg'])

deletebook_response=requests.post('http://216.10.245.166/Library/DeleteBook.php',json=deletebook_payload(book_id))
res_1=deletebook_response.json()
assert deletebook_response.status_code==200
print(res_1['msg'])
assert res_1['msg']=='book is successfully deleted'

