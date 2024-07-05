import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_poc")
def http_trigger_poc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # You can customize the payload here
    payload = {
        "name": "Sample Object",
        "data": "This is some sample data."
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    if response.status_code == 201 or response.status_code == 201:  # Assuming 201 Created is the success status code
        logging.info('Successfully executed the function',response.text)
        return func.HttpResponse(f"Success: {response.text}", status_code=201)
    else:
        logging.info('Failed to execute')
        return func.HttpResponse(f"Failed: {response.text}", status_code=response.status_code)



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
