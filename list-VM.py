import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Authenticate using Azure Managed Identity or Environment Variables
credential = DefaultAzureCredential()

# Azure subscription details
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

# Create Compute Client
compute_client = ComputeManagementClient(credential, subscription_id)

# List all VMs in a subscription
vm_list = compute_client.virtual_machines.list_all()

for vm in vm_list:
    print(f"VM Name: {vm.name}, Location: {vm.location}")
