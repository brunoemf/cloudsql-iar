# get_sql_instances.py
import subprocess
import json

def get_sql_instances(org_id):
    
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

# Teste
#teste = get_sql_instances('677188344232')  
#print(teste)
