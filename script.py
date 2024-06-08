import subprocess
import sys
import json  # Import the json module

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

# Print the output
print(result.stdout)

# Check for errors
if result.returncode != 0:
    print(f"Error: {result.stderr}")
