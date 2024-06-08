import json
import csv

def parse_sql_instances(json_file, csv_file):
    """Parses a JSON file containing Cloud SQL instances and writes data to a CSV file.

    Args:
        json_file: Path to the JSON file.
        csv_file: Path to the CSV file to write data to.
    """

    with open(json_file, 'r') as f:
        sql_instances = json.load(f)

    with open(csv_file, 'w', newline='') as csvfile:
        # Define the fieldnames for the CSV file
        fieldnames = [
            'ancestors',
            'assetType',
            'name',
            'resource.data.backendType',
            'resource.data.connectionName',
            'resource.data.createTime',
            'resource.data.databaseInstalledVersion',
            'resource.data.databaseVersion',
            'resource.data.gceZone',
            'resource.data.instanceType',
            'resource.data.ipAddresses',
            'resource.data.kind',
            'resource.data.maintenanceVersion',
            'resource.data.name',
            'resource.data.project',
            'resource.data.region',
            'resource.data.selfLink',
            'resource.data.serverCaCert.certSerialNumber',
            'resource.data.serverCaCert.commonName',
            'resource.data.serverCaCert.createTime',
            'resource.data.serverCaCert.expirationTime',
            'resource.data.serverCaCert.instance',
            'resource.data.serverCaCert.kind',
            'resource.data.serverCaCert.sha1Fingerprint',
            'resource.data.serviceAccountEmailAddress',
            'resource.data.settings.activationPolicy',
            'resource.data.settings.availabilityType',
            'resource.data.settings.backupConfiguration.backupRetentionSettings.retainedBackups',
            'resource.data.settings.backupConfiguration.backupRetentionSettings.retentionUnit',
            'resource.data.settings.backupConfiguration.enabled',
            'resource.data.settings.backupConfiguration.kind',
            'resource.data.settings.backupConfiguration.location',
            'resource.data.settings.backupConfiguration.pointInTimeRecoveryEnabled',
            'resource.data.settings.backupConfiguration.replicationLogArchivingEnabled',
            'resource.data.settings.backupConfiguration.startTime',
            'resource.data.settings.backupConfiguration.transactionLogRetentionDays',
            'resource.data.settings.backupConfiguration.transactionalLogStorageState',
            'resource.data.settings.connectorEnforcement',
            'resource.data.settings.dataDiskSizeGb',
            'resource.data.settings.dataDiskType',
            'resource.data.settings.deletionProtectionEnabled',
            'resource.data.settings.edition',
            'resource.data.settings.insightsConfig',
            'resource.data.settings.ipConfiguration.allocatedIpRange',
            'resource.data.settings.ipConfiguration.ipv4Enabled',
            'resource.data.settings.ipConfiguration.privateNetwork',
            'resource.data.settings.ipConfiguration.requireSsl',
            'resource.data.settings.ipConfiguration.sslMode',
            'resource.data.settings.kind',
            'resource.data.settings.locationPreference.kind',
            'resource.data.settings.locationPreference.zone',
            'resource.data.settings.maintenanceWindow.day',
            'resource.data.settings.maintenanceWindow.hour',
            'resource.data.settings.maintenanceWindow.kind',
            'resource.data.settings.maintenanceWindow.updateTrack',
            'resource.data.settings.pricingPlan',
            'resource.data.settings.replicationType',
            'resource.data.settings.settingsVersion',
            'resource.data.settings.storageAutoResize',
            'resource.data.settings.storageAutoResizeLimit',
            'resource.data.settings.tier',
            'resource.data.sqlNetworkArchitecture',
            'resource.data.state',
            'resource.discoveryDocumentUri',
            'resource.discoveryName',
            'resource.location',
            'resource.parent',
            'resource.version',
            'updateTime'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for instance in sql_instances:
            # Extract relevant data from the instance object
            instance_data = {}
            for fieldname in fieldnames:
                # Use get() to handle missing keys and return NULL
                value = get_nested_value(instance, fieldname)
                instance_data[fieldname] = value
            writer.writerow(instance_data)

def get_nested_value(data, key):
    """Retrieves a nested value from a dictionary using a dot-separated key.

    Args:
        data: The dictionary to search.
        key: The dot-separated key (e.g., 'resource.data.settings.tier').

    Returns:
        The value at the specified key, or None if the key is not found.
    """
    keys = key.split('.')
    for k in keys:
        if isinstance(data, dict) and k in data:
            data = data[k]
        else:
            return None
    return data

# Example usage
json_file = '/Users/brunoemf/Documents/workspace/cloudsql-iar/sql-instances.json'
csv_file = 'output.csv'
parse_sql_instances(json_file, csv_file)