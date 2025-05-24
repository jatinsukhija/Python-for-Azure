import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Use default Azure credentials (Azure CLI login, managed identity, etc.)
credential = DefaultAzureCredential()

STORAGE_ACCOUNT_NAME = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")

blob_service_client = BlobServiceClient(account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=credential)

container_client = blob_service_client.get_container_client("files")

acl = container_client.get_container_access_policy()

print(acl)  
