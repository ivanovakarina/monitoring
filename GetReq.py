#работает!
import http.client

#conn = http.client.HTTPConnection("lectureswww.readthedocs.io")
#conn.request("GET", "/description.html#id2")
conn = http.client.HTTPConnection("kuznech.com")
conn.request("GET", "")
r1 = conn.getresponse()
print(r1.status)
data1 = r1.read()

#conn.request("GET", "/parrot.spam")
conn.request("GET", "/ru/")
r2 = conn.getresponse()
print(r2.status)
data2 = r2.read()

conn.close()