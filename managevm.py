import csv
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Authenticate
credential = DefaultAzureCredential()

# Actions
def start_vm(compute_client, rg, vm_name):
    print(f"▶️ Starting VM: {vm_name}")
    compute_client.virtual_machines.begin_start(rg, vm_name).wait()
    print("✅ VM started.")

def stop_vm(compute_client, rg, vm_name):
    print(f"⏹️ Stopping VM: {vm_name}")
    compute_client.virtual_machines.begin_power_off(rg, vm_name).wait()
    print("✅ VM stopped.")

def restart_vm(compute_client, rg, vm_name):
    print(f"🔁 Restarting VM: {vm_name}")
    compute_client.virtual_machines.begin_restart(rg, vm_name).wait()
    print("✅ VM restarted.")

def delete_vm(compute_client, rg, vm_name):
    print(f"🗑️ Deleting VM: {vm_name}")
    compute_client.virtual_machines.begin_delete(rg, vm_name).wait()
    print("✅ VM deleted.")

# CLI-style usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python managevm.py [start|stop|restart|delete] <csv-file>")
        sys.exit(1)

    action = sys.argv[1].lower()
    csv_file = sys.argv[2]

    if action not in ["start", "stop", "restart", "delete"]:
        print("❌ Invalid action. Choose from: start, stop, restart, delete")
        sys.exit(1)

    try:
        with open(csv_file, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sub_id = row["subscription_id"]
                rg = row["resource_group"]
                vm = row["vm_name"]

                compute_client = ComputeManagementClient(credential, sub_id)

                if action == "start":
                    start_vm(compute_client, rg, vm)
                elif action == "stop":
                    stop_vm(compute_client, rg, vm)
                elif action == "restart":
                    restart_vm(compute_client, rg, vm)
                elif action == "delete":
                    delete_vm(compute_client, rg, vm)

    except Exception as e:
        print(f"❌ Error: {e}")
