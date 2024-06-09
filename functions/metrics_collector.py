# metrics_collector.py
import subprocess
import json

def collect_instance_metrics(instance_name, instance_region):
    """Collects metrics for a given Cloud SQL instance.

    Args:
        instance_name: The name of the Cloud SQL instance.
        instance_region: The region of the Cloud SQL instance.

    Returns:
        A dictionary containing the collected metrics.
    """
    metrics = {}
    for metric_name in ['cpuUsage', 'diskUsage', 'memoryUsage', 'connections']:
        command = [
            'gcloud', 'sql', 'operations', 'list',
            '--filter', f'target.name="{instance_name}"',
            '--region', instance_region,
            '--format', 'json'
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        try:
            operations = json.loads(result.stdout)
            for operation in operations:
                if 'performance' in operation and metric_name in operation['performance']:
                    metrics[f'performance.{metric_name}'] = operation['performance'][metric_name]
                    break
        except (json.JSONDecodeError, KeyError):
            metrics[f'performance.{metric_name}'] = None
    return metrics

