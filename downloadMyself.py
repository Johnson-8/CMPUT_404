import requests

# virtualevn.4
print("Requests version: " + requests.__version__)

# for curl.5
r = requests.get("http://www.google.com")
print("cURL response: " + str(r))
#print("response: " + str(r) + "\n" + "text: " + str(r.text))

# download itself
fileURL = "https://raw.githubusercontent.com/Johnson-8/CMPUT_404/master/getAnswer.py"
r = requests.get(fileURL)
file = open("downloadMyself.py", "w")
file.write(r.text)
file.close()

# print out source code
file = open("downloadMyself.py", "r")
print("My source code:\n" + str(file.read()))
file.close()