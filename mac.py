import requests 
import json
import argparse

parser = argparse.ArgumentParser()

# Taking MAC as an input
parser.add_argument("MAC", type=str, help="MAC address")
arguments = parser.parse_args()

# 44:38:39:ff:ef:57

# Trying to get the response from server 
try: 
  response = requests.get("https://api.macaddress.io/v1?apiKey=at_pPk0FKIlnX9WXqqsTDZ7i9yQyusQe&output=json&search={}".format(arguments.MAC))
except:
  print("get request error")
  exit()

# Checking if the response was correct 
if response.status_code != 200:
  print("Response error: " + str(response.status_code))
  exit()

# convering response from json
response_json = json.loads(response.text)

# printing the vendor name
try: 
  print(response_json['vendorDetails']['companyName'])
except:
  print("Couldn't find company name or vendor details in response")