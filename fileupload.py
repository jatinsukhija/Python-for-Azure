import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Use default Azure credentials (Azure CLI login, managed identity, etc.)
credential = DefaultAzureCredential()

# Replace with your actual storage account name
account_url = "https://sgterraformstate.blob.core.windows.net/"
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)


# Upload a file to a specific container
container_name = "files"        # Replace with your container name
blob_name = "test.txt"               # Name of the blob to create
local_file_path = "test1.txt"              # Path to the local file you want to upload

try:
    # Get client for the specific container and blob
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"\n✅ File '{local_file_path}' uploaded to container '{container_name}' as blob '{blob_name}'.")

except Exception as e:
    print(f"\n❌ Error: {e}")
