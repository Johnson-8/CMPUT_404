
My source code: 
import requests

# virtualevn.4
print("Requests version: " + requests.__version__ + "\n")

# for curl.5
r = requests.get("http://www.google.com")
print("cURL response: " + str(r))
#print("response: " + str(r) + "\n" + "text: " + str(r.text))


# download itself
fileURL = "https://raw.githubusercontent.com/Johnson-8/CMPUT_404/master/getAnswer.py"
r = requests.get(fileURL)
file = open("downloadMyself.py", "w")
file.write("\nMy source code: \n" + str(r.text))
file.close()

# print out source code
file = open("downloadMyself.py", "r")
print(file.read())
file.close()