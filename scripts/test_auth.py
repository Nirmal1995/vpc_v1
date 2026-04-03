from google.auth import default
from googleapiclient import discovery
credentials, project = default()

print("✅ Authentication successful")
print("Project ID:", project)
# Create Compute Engine client
compute = discovery.build('compute', 'v1', credentials=credentials)

print("✅ Connected to Compute Engine API")

request = compute.networks().list(project=project)

print(" VPC request created" )
response = request.execute()

print("✅ API response received")
print(response)
for network in response.get('items', []):
    print("VPC Name:", network['name'])
