# import azure.functions as func
# import logging
# import requests

# app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# @app.route(route="http_trigger_poc")
# def http_trigger_poc(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     # You can customize the payload here
#     payload = {
#         "name": "Sample Object",
#         "data": "This is some sample data."
#     }
#     response = requests.post("https://api.restful-api.dev/objects", json=payload)
#     if response.status_code == 201:  # Assuming 201 Created is the success status code
#         return func.HttpResponse(f"Success: {response.text}", status_code=201)
#     else:
#         return func.HttpResponse(f"Failed: {response.text}", status_code=response.status_code)
