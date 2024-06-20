# get_sql_instances.py
import subprocess
import json

def get_sql_instances(org_id):
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
        '--asset-types', 'sqladmin.googleapis.com/Instance',
        '--content-type', 'resource',
        '--format', 'json'
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    #print(result)
    sql_instances = json.loads(result.stdout)
    
    return sql_instances 


