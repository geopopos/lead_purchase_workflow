import requests
import json
import os
import urllib.parse

ppl_api_url = "https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    ppl_api_url = "http://localhost:2000"

def get_lead(event, context):
    lead_id = event.get('product').get('metadata').get('lead_id')
    url = ppl_api_url + f"/lead/{urllib.parse.quote(lead_id)}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("GET", url, headers=headers)
    event['lead'] = response.json()
    return event