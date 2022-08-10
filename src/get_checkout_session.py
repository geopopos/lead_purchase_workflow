import json, requests, os
import stripe

stripe_api_key = os.environ.get('STRIPE_API_KEY')
ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')
    ppl_api_url = "http://localhost:2000"

if os.environ.get('STAGE') == 'dev':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def get_checkout_session(event, context):
    stripe.api_key = stripe_api_key
    checkout_session_id = event.get('id')
    expand=['line_items']

    #get stripe checkout session
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id, expand=expand)

    event['checkout_session'] = checkout_session
    return event 