from email import message
import os, json, requests, boto3, logging
from string import Template
from helpers import send_sms_to_sqs_queue, send_email_to_sqs_queue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

sqs_client = boto3.client('sqs')

ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    ppl_api_url = "http://localhost:2000"


def lead_delivery_spawner(event, context):
    # for each record, create a notification
    # for each notification, create a task in sqs
    sms_queue_url = os.environ.get('SQS_SMS_QUEUE_URL')
    email_queue_url = os.environ.get('SQS_EMAIL_QUEUE_URL')

    # for each record, create a notification
    # for each notification, create a task in sqs

    # get all lead data for notification
    lead = event.get('lead')
    roofer = event.get('roofer')

    # create lead notification message_subject
    message_subject = "✨ Your Sparkling New Lead! ✨"

    # create lead notification message_body
    message_body = Template("""✨ Your Sparkling New Lead! ✨
    Your Purchased Lead Details Can Be Found Below!
    Name: $name
    Phone: $phone
    Email: $email
    Street Address: $address
    Geocode Address: $geocode_address
    Project Scope: $project_scope
    Project Timeline: $project_timeline
    Thanks for doing business with us!""")

    sms_response = send_sms_to_sqs_queue.send_sms_to_sqs_queue(logger, sqs_client, sms_queue_url, message_body.substitute(name=lead.get('full_name'), phone=lead.get('phone'), email=lead.get('email'), address=lead.get('address'), geocode_address=lead.get('geocode_address'), project_timeline=lead.get('project_timeline'), project_scope=lead.get('project_scope')), roofing_contractor=roofer)

    email_response = send_email_to_sqs_queue.send_email_to_sqs_queue(logger, sqs_client, email_queue_url, message_subject=message_subject, message_body=message_body.substitute(name=lead.get('full_name'), phone=lead.get('phone'), email=lead.get('email'), address=lead.get('address'), geocode_address=lead.get('geocode_address'), project_timeline=lead.get('project_timeline'), project_scope=lead.get('project_scope')), roofing_contractor=roofer)

    return {"statusCode": 200, "body": json.dumps({"sms_response": sms_response, "email_response": email_response})}