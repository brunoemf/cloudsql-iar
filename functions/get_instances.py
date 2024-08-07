import subprocess
import json
import argparse
from collections.abc import Iterable 

def get_compute_instances(org_id):
    #generate a description of this funcion
    """Retrieves a list of Cloud SQL instances for a given organization.

    Args:
        org_id: The organization ID.

    Returns:
        A list of Cloud SQL instance objects.
    """
    
    command = [
        'gcloud', 'asset', 'list', 
        '--organization', org_id,
        '--asset-types', 'compute.googleapis.com/Instance',
        '--content-type', 'resource',
        '--format', 'json'
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    print(result.stderr)
    compute_instances = json.loads(result.stdout)
    
    return compute_instances 

parser = argparse.ArgumentParser(description="List GCE Instances with Local SSD disks.")
parser.add_argument("org_id", help="Pass the Organization ID to list instances")
args = parser.parse_args()

instances = get_compute_instances(args.org_id)
#print(instances)

for instance in instances:
    try:
        disks = instance['resource']['data']['disks']
    except:
        break
    if isinstance(disks, Iterable):
        for disk in disks:            
            if disk['type'] == "SCRATCH":
                print(instance['name'])                
                break
    else:
        break