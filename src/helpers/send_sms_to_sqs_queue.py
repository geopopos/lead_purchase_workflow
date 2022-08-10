import os, requests, json
from string import Template

def send_sms_to_sqs_queue(logger, sqs_client, sms_queue_url, message_body, roofing_contractor):
    # create notification for sms
    notification = {
        "notification_type": "lead",
        "message_body": message_body,
        "to_number": roofing_contractor.get('Phone')
    }
    # create task in sqs sms
    try:
        task = sqs_client.send_message(
            QueueUrl=sms_queue_url, 
            MessageBody=json.dumps(notification)
            )
        logger.info(f"task: {task}")
        message = f"task: {task}"
        status_code = 200
    except Exception as e:
        logger.exception('Sending message to SQS queue failed!')
        message = str(e)
        status_code = 500
    

    return {"statusCode": status_code, "body": message}