import urllib
appKey = "tfs8j951cmP5ViW0"
sessionToken =  "1lDrIyhwahzJ97leBU8L0De5xgmPo2QHOZW16XsJDnE="

import requests
import json

endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"

header = {'X-Application': appKey, 'X-Authentication': sessionToken, 'content-type': 'application/json'}

json_req = '{"filter":{ }}'

url = endpoint + "listEventTypes/"

response = requests.post(url, data=json_req, headers=header)

print(json.dumps(json.loads(response.text), indent=3))