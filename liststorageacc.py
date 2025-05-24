import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Use default Azure credentials (Azure CLI login, managed identity, etc.)
credential = DefaultAzureCredential()

# Replace with your actual account name
account_url = "https://sgterraformstate.blob.core.windows.net/"

blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Example: list containers
containers = blob_service_client.list_containers()
for container in containers:
    print(f"Container: {container['name']}")
