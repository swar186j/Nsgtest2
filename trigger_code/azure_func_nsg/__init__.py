import os
import logging
import json
import azure.functions as func
import requests


app = func.FunctionApp()
@app.function_name(name="BlobUpdate")
@app.blob_trigger(arg_name="myblob", path="insights-logs-networksecuritygroupflowevent/resourceId=/SUBSCRIPTIONS/{subscriptionId}/RESOURCEGROUPS/{resourceGroupName}/PROVIDERS/MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/{networkSecurityGroupName}/y={year}/m={month}/d={day}/h={hour}/m={minute}/macAddress={macAddress}/{filename}" ,
                  connection="AzureWebJobsStorage")
def main(myblob: func.InputStream):
    logging.info(f"Blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    # Get the storage account name and connection string from environment variables
    storage_account_name = os.getenv('StorageAccountName')
    storage_connection_string = os.getenv('AzureWebJobsStorage')
    if not storage_account_name or not storage_connection_string:
        logging.error("Storage account name or connection string environment variable not set.")
        return
    try:
        blob_name = myblob.name
        blob_url = f"https://{storage_account_name}.blob.core.windows.net/{blob_name}"
        records = requests.get(blob_url)
        
        # print("++++++++++++++++++",records.text)
        # Process the records
        records= json.loads(records.text)
        if 'records' in records:
            new_records = records['records']
            logging.info("\nNew added data:")
            for record in new_records:
                logging.info(record)
        else:
            logging.warning("No 'records' key found in JSON.")
    except Exception as e:
        logging.error(f"Error processing blob: {str(e)}")
