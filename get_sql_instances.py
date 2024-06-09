# get_sql_instances.py
import subprocess
import json

def get_sql_instances(org_id):
    
    id = org_id
    #sql_instances = {}
    
    command = [
        'gcloud', 'asset', 'list', 
        f'--organization="{id}"',
        '--asset-types=', 'sqladmin.googleapis.com/Instance',
        '--content-type=', 'resource',
        '--format=json'
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    """    
    try:
        operations = json.loads(result.stdout)
        for operation in operations:
            if 'performance' in operation and metric_name in operation['performance']:
                metrics[f'performance.{metric_name}'] = operation['performance'][metric_name]
                break
    except (json.JSONDecodeError, KeyError):
        metrics[f'performance.{metric_name}'] = None
    """
    print(result.stdout)
    #sql_instances = json.loads(result.stdout)
    
    #return sql_instances 
# Teste
teste = get_sql_instances('677188344232')  
print(teste)
