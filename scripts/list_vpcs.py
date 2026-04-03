
from google.cloud import compute_v1

def list_vpcs(project_id: str):
    client = compute_v1.NetworksClient()
    print(f"Listing VPC networks in project: {project_id}\n")

    for network in client.list(project=project_id):
        print(f"- Name: {network.name}")
        print(f"  Auto-create subnetworks: {network.auto_create_subnetworks}")
        print(f"  Self link: {network.self_link}")
        print()


if __name__ == "__main__":
    project_id = "project-d6bb013c-47e4-497a-9f1"
    list_vpcs(project_id)
