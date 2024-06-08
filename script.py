import subprocess
import sys
import json  # Import the json module
import csv
import re

# Check if the user provided an organization ID as a command-line argument
if len(sys.argv) > 1:
    org_id = sys.argv[1]
else:
    # If no argument is provided, prompt the user for the organization ID
    org_id = input("Enter your organization ID: ")

# Construct the command list
command = [
    'gcloud', 'asset', 'list',
    '--organization', org_id,
    '--asset-types', 'sqladmin.googleapis.com/Instance',
    '--content-type', 'resource',
    '--format=json'
]

# Run the command using subprocess.run()
result = subprocess.run(command, capture_output=True, text=True)

# Create a CSV file
csv_file = open('sql_instances.csv', 'w', newline='')
csv_writer = csv.writer(csv_file) 

# Write the header row
csv_writer.writerow(['Project ID', 'Instance Name'])


# Parse the JSON output
sql_instances = json.loads(result.stdout)

# Extract and print instance names
for asset in sql_instances:
    project_id = asset['resource']['data']['project']
    instance_name = asset['resource']['data']['name']
    tier = asset['resource']['data']['settings']['tier']
    availabilityType = asset['resource']['data']['settings']['availabilityType']
    storage_auto_resize = asset['resource']['data']['settings']['storageAutoResize']
    backup_configuration =

    csv_writer.writerow([project_id, instance_name])

# Close the CSV file
csv_file.close()

print("SQL instances extracted and saved to sql_instances.csv")


