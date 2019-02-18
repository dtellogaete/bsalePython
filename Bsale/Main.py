
import requests

url='https://api.bsale.cl/v1/products/436.json'
token= 'insert your token here'

head= {'Content-Type':'application/json','access_token':token}

r=requests.get(url,headers=head)

print (r.json())