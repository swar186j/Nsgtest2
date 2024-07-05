# import logging
# import azure.functions as func
# import http.client

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     conn = http.client.HTTPSConnection("api.restful-api.dev")
#     payload = '''
#     {
#         "name": "Network Security",
#         "data": {
#             "time": "2024-06-18T11:04:44.6510000Z",
#             "systemId": "123456",
#             "category": "NetworkSecurityGroupEvent",
#             "resourceId": "/SUBSCRIPTIONS/ABCD/LSSVM-NSG",
#             "operationName": "NetworkSecurityGroupEvents",
#             "properties": {
#                 "vnetResourceGuid": "{E6DAB98C324D}",
#                 "subnetPrefix": "0.0.0.0/24",
#                 "macAddress": "0000000",
#                 "primaryIPv4Address": "0.0.0.4",
#                 "ruleName": "DefaultRule_AllowInternetOutBound",
#                 "direction": "Out",
#                 "priority": 65001,
#                 "type": "allow",
#                 "conditions": {
#                     "destinationPortRange": "0-65535",
#                     "sourcePortRange": "0-65535",
#                     "sourceIP": "0.0.0.0/0,0.0.0.0/0"
#                 }
#             }
#         }
#     }
#     '''
#     headers = {
#         'Content-Type': "application/json"
#     }
#     conn.request("POST", "/objects", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     response_data = data.decode("utf-8")
#     logging.info(f"Response from API: {response_data}")

#     return func.HttpResponse(response_data, status_code=res.status)
