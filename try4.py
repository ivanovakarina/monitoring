# Работает!!!
import requests


r = requests.get('http://kuznech.com')

print(r.status_code)
print(r.headers['content-type'])