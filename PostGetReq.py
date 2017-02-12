import urllib.request
import urllib.parse

data = {"s": "Веб программирование"}
enc_data = urllib.parse.urlencode(data)

# GET запрос
f = urllib.request.urlopen("http://nigma.ru/" + "?" + enc_data)
print(f.read())

# POST запрос
f = urllib.request.urlopen("http://nigma.ru/", enc_data.encode('utf-8'))
print(f.read())