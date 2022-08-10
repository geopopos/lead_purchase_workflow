{
    "Comment": "Workflow execute when new lead purchase is made",
    "StartAt": "GetLeadCheckoutSession",
    "States": {
        "GetLeadCheckoutSession": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-get_checkout_session",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "GetLeadProduct"
        },
        "GetLeadProduct": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-get_product",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "SetPaymentLinkInactive"
        }, 
        "SetPaymentLinkInactive": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-set_link_inactive",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "GetRooferByEmail"
        }, 
        "GetRooferByEmail": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-get_roofer_email",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "GetLead"
        },
        "GetLead": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-get_lead",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "CreateBuyRecord"
        },
        "CreateBuyRecord": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-create_buy_record",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "LeadDeliverySpawner"
        },
        "LeadDeliverySpawner": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:lead-purchase-workflow-dev-lead_d_spawner",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "End": true
        }
    }
}
