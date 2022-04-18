import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string",
               "minLength":5,
               "maxLength":8
              },
        "start_date":{"type":"string",
                      "format":"date"
                     },
        "end_date":{"type":"string",
                    "format":"date"
                     },
        "container_type":{"type":"string",
                          "enum":["Compactor","FL Dumpster","Lugger","RL Dumpster","RO Bin","SL Dumpster"]
                         },
        "volume":{"type":"string",
                  "pattern":"[0-9]YD"
                 },
        "quantity": {"type":"string",
                     "pattern":"[0-9]"},
        
    }
}

# schema = {
#      "type" : "string",
#      "properties" : {
#          "queryStringParameters" : {
#                 "type" : "string",
#                 "properties": {
#                         "user_id": {
#                                 "type": "string",
#                                 "minLength": 7,
#                         }
#                 }
#         },

#      },
#  }

def main(event, context):
    jsondump = json.dumps(event)
    jsonData = json.loads(jsondump)
    try:
        validate(instance=jsonData, schema=schema)
        
    #     u = int(event['user_id'])
    # # a = int(event['siteId'])

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
    except ValidationError as e:
        return {
            "statusCode": 404,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
                "x-amzn-ErrorType": "ValidationError",
            },
            "body": e.message,
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

