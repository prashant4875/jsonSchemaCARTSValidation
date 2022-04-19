import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string",
               "minLength":5,
               "maxLength":8,
               "error_msg": "Hauling Site ID NOT Found"
              },
        "start_date":{"type":"string",
                      "format":"date",
                      "pattern":"^[1-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]$",
                      "error_msg": "Invalid Date provided"
                     },
        "end_date":{"type":"string",
                    "format":"date",
                    "pattern":"^[1-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]$",
                    "error_msg": "Invalid Date provided"
                     },
        "container_type":{"type":"string",
                          "enum":["Compactor","FL Dumpster","Lugger","RL Dumpster","RO Bin","SL Dumpster"],
                          "error_msg": "Container Type provided not found"
                         },
        # "volume":{"type":"string",
        #           "pattern":"[0-9]YD"
        #          },
        "quantity": {"type":"string",
                     "pattern":"[0-9]",
                     "error_msg": "Quantity given is not a number"
                    },
        
    },
    "required": ["id","start_date","end_date","container_type","quantity"],
}

def main(event, context):
    jsondump = json.dumps(event)
    jsonData = json.loads(jsondump)
    try:
        validate(instance=jsonData, schema=schema)
        
    except ValidationError as e:
        return {
            "statusCode": 404,
            "body": e.schema["error_msg"]
        }
    return {
        "title": "success"
    }

# import json


# def hello(event, context):
#     # user_id = event["params"]["querystring"]["userid"]
#     # activity_id = event["params"]["querystring"]["activityid"]
#     # print(event)
#     u = int(event['user_id'])
#     # a = int(event['siteId'])

#     if u==12345678:
#         return {
#             'name': "CARTS",
#             'company': "WM"
#         }
    
#     else: 
#         return {
#             'ui': u,
#             # 'ai': a,
#             'name': "other",
#             'company': "other1"
#         }

    # body = {
    #     "id": 1,
    #     "message": "Go Serverless v2.0! Your function executed successfully!",
    #     "input": event,
    # }

    # return {
    #         "userid": 2,
    #         "start_date": 2
            
    #         }

