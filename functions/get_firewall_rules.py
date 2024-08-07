# get_sql_instances.py
import subprocess
import json

def get_firewall_rules(org_id: str):
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
        '--asset-types', 'compute.googleapis.com/Firewall',
        '--content-type', 'resource',
        '--format', 'json'
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    print(result.stderr)
    firewall_rules = json.loads(result.stdout)
    
    return firewall_rules

fw = get_firewall_rules('806711562222') 
#print(fw)
for rule in fw:
    print(rule['resource']['data']['allowed'])
