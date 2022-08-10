from itertools import product
import json, requests, os
import stripe

stripe_api_key = os.environ.get('STRIPE_API_KEY')
ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')
    ppl_api_url = "http://localhost:2000"

if os.environ.get('STAGE') == 'dev':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def set_payment_link_active_false(event, context):
    payment_link_id = event.get('payment_link')
    stripe.api_key = stripe_api_key

    # get stripe product
    payment_link = stripe.PaymentLink.modify(
        payment_link_id,
        active=False
    )
    event['payment_link'] = payment_link 

    return event