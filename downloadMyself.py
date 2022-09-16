
 My source code: 
import requests

# virtualevn.4
print("Requests version: " + requests.__version__ + "\n")

# for curl.5
r = requests.get("http://www.google.com")
print("response: " + str(r) + "\n" + "text: " + str(r.text))