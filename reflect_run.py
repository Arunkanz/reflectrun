import requests
import json
import sys
import yaml
from yaml.loader import SafeLoader

data = {}
tdata = {}

# Open the file and load the file
with open('testdata.yml') as f:
    tdata = yaml.load(f, Loader=SafeLoader)
    print(tdata['MM_Testdata']['Testcase1'])


url = "https://api.reflect.run/v1/tests/" + str(tdata['MM_Testdata']['Testcase1']) + "/executions"
print(url)

payload = ""
headers = {"x-api-key": "x1OBUoR7PY4qH4RyH199pwuN1a7ofw32BxmrfSxf"}

response = requests.request("POST", url, data=payload, headers=headers)
json_data = json.loads(response.text)

url2 = "https://api.reflect.run/v1/executions/" + str(json_data['executionId'])

while True:
    response2 = requests.request("GET", url2, data=payload, headers=headers)
    data = json.loads(response2.text)
    print(data['tests'][0]['status'])
    if((data['tests'][0]['status'] != 'running') and (data['tests'][0]['status'] != 'queued')):
        break

if(data['tests'][0]['status'] == 'failed'):
    print("Test Execution Failed\n")
    sys.exit(-1)





