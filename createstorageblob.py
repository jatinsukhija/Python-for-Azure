import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Use default Azure credentials (Azure CLI login, managed identity, etc.)
credential = DefaultAzureCredential()

container_name = "jatin"        # Replace with your container name

STORAGE_ACCOUNT_NAME = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")

blob_service_client = BlobServiceClient(account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=credential)

blob_service_client.create_container(container_name)        # Replace with your container name
