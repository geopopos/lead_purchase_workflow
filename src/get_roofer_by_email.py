import requests, os, json
# import url encod library
import urllib.parse


ppl_api_url = "https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    ppl_api_url = "http://localhost:2000"

def get_roofer_by_email(event, context):
    email = event.get('customer_details').get('email')
    url = ppl_api_url + f"/roofer/email/{urllib.parse.quote(email)}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("GET", url, headers=headers)
    event['roofer'] = response.json()
    return event