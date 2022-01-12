import requests

print("requestons version: ", requests.__version__)

r = requests.get("http://www.google.com")

raw_url = "https://raw.githubusercontent.com/nick98anderson/CMPUT404-lab1/master/scripts.py"
script = requests.get(raw_url)
print(script.content.decode())