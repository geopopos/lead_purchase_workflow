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

def get_product(event, context):
    checkout_session = event.get('checkout_session')
    line_item = checkout_session.get('line_items').get('data')[0]
    price = line_item.get('price')
    product = price.get('product')
    stripe.api_key = stripe_api_key

    # get stripe product
    product = stripe.Product.retrieve(product)
    event['product'] = product 

    return event