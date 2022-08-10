import requests, json, os, urllib.parse
from datetime import datetime

ppl_api_url = "https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    ppl_api_url = "http://localhost:2000"

def create_purchase_record(event, context):
    lead_id = event.get('lead').get('pk')
    roofer_id = event.get('roofer').get('pk')
    url = ppl_api_url + "/lead_purchase"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "roofer": roofer_id,
        "lead": lead_id,
        "purchased_at": datetime.now().isoformat(),
        "purchase_amount": event.get('amount_total')
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(body))
    event['lead_purchase'] = response.json()
    return event