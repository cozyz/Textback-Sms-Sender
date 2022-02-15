import requests
import json
import ctypes
from os import system

print("""


            @riksouleclown
            https://github.com/cozyz


""")

system("title " + "cozyz")
file = open("num.txt", "r")
lines = file.readlines()
for line in lines:
    r = requests.get('https://api.textback.ai/send?action=sendText&apiKey=YOURAPIKEY&from=SENDERID&to=33'+line+'&text=test')
    print(r.content)
file.close
print("Task is finish")
print("")
print("")
system("pause")