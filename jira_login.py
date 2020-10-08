import requests
import json

login_res=requests.get('https://id.atlassian.com/login',auth=('venkatesh' , 'python@2020'))
print(login_res.status_code)
