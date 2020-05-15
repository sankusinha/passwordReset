from pprint import pprint
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse
import base64
import os
import requests
import json

#username = os.getenv('API_USER')
#password = os.getenv('API_PASSWORD')
#job_url = os.getenv('JOB_URL')
username = 'admin'
password = 'admin'
job_url = 'http://localhost:8080'
parsed_url = urlparse(job_url)
base_url = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
#api_url = base_url + '/crumbIssuer/api/xml?xpath=concat(//crumbRequestField.":",//crumb)'
api_url = base_url + '/crumbIssuer/api/json'
print(api_url)
response = requests.get(
    api_url,
    auth=HTTPBasicAuth(str(username), str(password))
)
crumb = {}
if response.status_code == 401:
    pprint(response.text)
    raise Exception('unauthorized')
response_json = json.loads(response.text)
crumb = response_json['crumb']
pprint(crumb)

#crumb[str(response.text).split(":")[0]] = str(response.text).split(":")[1]
#pprint(crumb)
#return crumb
