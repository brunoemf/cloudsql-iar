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
            instance_data = {
                'ancestors': instance['ancestors'],
                'assetType': instance['assetType'],
                'name': instance['name'],
                'resource.data.backendType': instance['resource']['data']['backendType'],
                'resource.data.connectionName': instance['resource']['data']['connectionName'],
                'resource.data.createTime': instance['resource']['data']['createTime'],
                'resource.data.databaseInstalledVersion': instance['resource']['data']['databaseInstalledVersion'],
                'resource.data.databaseVersion': instance['resource']['data']['databaseVersion'],
                'resource.data.gceZone': instance['resource']['data']['gceZone'],
                'resource.data.instanceType': instance['resource']['data']['instanceType'],
                'resource.data.ipAddresses': instance['resource']['data']['ipAddresses'],
                'resource.data.kind': instance['resource']['data']['kind'],
                'resource.data.maintenanceVersion': instance['resource']['data']['maintenanceVersion'],
                'resource.data.name': instance['resource']['data']['name'],
                'resource.data.project': instance['resource']['data']['project'],
                'resource.data.region': instance['resource']['data']['region'],
                'resource.data.selfLink': instance['resource']['data']['selfLink'],
                'resource.data.serverCaCert.certSerialNumber': instance['resource']['data']['serverCaCert']['certSerialNumber'],
                'resource.data.serverCaCert.commonName': instance['resource']['data']['serverCaCert']['commonName'],
                'resource.data.serverCaCert.createTime': instance['resource']['data']['serverCaCert']['createTime'],
                'resource.data.serverCaCert.expirationTime': instance['resource']['data']['serverCaCert']['expirationTime'],
                'resource.data.serverCaCert.instance': instance['resource']['data']['serverCaCert']['instance'],
                'resource.data.serverCaCert.kind': instance['resource']['data']['serverCaCert']['kind'],
                'resource.data.serverCaCert.sha1Fingerprint': instance['resource']['data']['serverCaCert']['sha1Fingerprint'],
                'resource.data.serviceAccountEmailAddress': instance['resource']['data']['serviceAccountEmailAddress'],
                'resource.data.settings.activationPolicy': instance['resource']['data']['settings']['activationPolicy'],
                'resource.data.settings.availabilityType': instance['resource']['data']['settings']['availabilityType'],
                'resource.data.settings.backupConfiguration.backupRetentionSettings.retainedBackups': instance['resource']['data']['settings']['backupConfiguration']['backupRetentionSettings']['retainedBackups'],
                'resource.data.settings.backupConfiguration.backupRetentionSettings.retentionUnit': instance['resource']['data']['settings']['backupConfiguration']['backupRetentionSettings']['retentionUnit'],
                'resource.data.settings.backupConfiguration.enabled': instance['resource']['data']['settings']['backupConfiguration']['enabled'],
                'resource.data.settings.backupConfiguration.kind': instance['resource']['data']['settings']['backupConfiguration']['kind'],
                #'resource.data.settings.backupConfiguration.location': instance['resource']['data']['settings']['backupConfiguration']['location'],
                'resource.data.settings.backupConfiguration.pointInTimeRecoveryEnabled': instance['resource']['data']['settings']['backupConfiguration']['pointInTimeRecoveryEnabled'],
                'resource.data.settings.backupConfiguration.replicationLogArchivingEnabled': instance['resource']['data']['settings']['backupConfiguration']['replicationLogArchivingEnabled'],
                'resource.data.settings.backupConfiguration.startTime': instance['resource']['data']['settings']['backupConfiguration']['startTime'],
                'resource.data.settings.backupConfiguration.transactionLogRetentionDays': instance['resource']['data']['settings']['backupConfiguration']['transactionLogRetentionDays'],
                'resource.data.settings.backupConfiguration.transactionalLogStorageState': instance['resource']['data']['settings']['backupConfiguration']['transactionalLogStorageState'],
                'resource.data.settings.connectorEnforcement': instance['resource']['data']['settings']['connectorEnforcement'],
                'resource.data.settings.dataDiskSizeGb': instance['resource']['data']['settings']['dataDiskSizeGb'],
                'resource.data.settings.dataDiskType': instance['resource']['data']['settings']['dataDiskType'],
                'resource.data.settings.deletionProtectionEnabled': instance['resource']['data']['settings']['deletionProtectionEnabled'],
                #'resource.data.settings.edition': instance['resource']['data']['settings']['edition'],
                'resource.data.settings.insightsConfig': instance['resource']['data']['settings']['insightsConfig'],
                #'resource.data.settings.ipConfiguration.allocatedIpRange': instance['resource']['data']['settings']['ipConfiguration']['allocatedIpRange'],
                'resource.data.settings.ipConfiguration.ipv4Enabled': instance['resource']['data']['settings']['ipConfiguration']['ipv4Enabled'],
                #'resource.data.settings.ipConfiguration.privateNetwork': instance['resource']['data']['settings']['ipConfiguration']['privateNetwork'],
                'resource.data.settings.ipConfiguration.requireSsl': instance['resource']['data']['settings']['ipConfiguration']['requireSsl'],
                'resource.data.settings.ipConfiguration.sslMode': instance['resource']['data']['settings']['ipConfiguration']['sslMode'],
                'resource.data.settings.kind': instance['resource']['data']['settings']['kind'],
                'resource.data.settings.locationPreference.kind': instance['resource']['data']['settings']['locationPreference']['kind'],
                'resource.data.settings.locationPreference.zone': instance['resource']['data']['settings']['locationPreference']['zone'],
                'resource.data.settings.maintenanceWindow.day': instance['resource']['data']['settings']['maintenanceWindow']['day'],
                'resource.data.settings.maintenanceWindow.hour': instance['resource']['data']['settings']['maintenanceWindow']['hour'],
                'resource.data.settings.maintenanceWindow.kind': instance['resource']['data']['settings']['maintenanceWindow']['kind'],
                #'resource.data.settings.maintenanceWindow.updateTrack': instance['resource']['data']['settings']['maintenanceWindow']['updateTrack'],
                'resource.data.settings.pricingPlan': instance['resource']['data']['settings']['pricingPlan'],
                'resource.data.settings.replicationType': instance['resource']['data']['settings']['replicationType'],
                'resource.data.settings.settingsVersion': instance['resource']['data']['settings']['settingsVersion'],
                'resource.data.settings.storageAutoResize': instance['resource']['data']['settings']['storageAutoResize'],
                'resource.data.settings.storageAutoResizeLimit': instance['resource']['data']['settings']['storageAutoResizeLimit'],
                'resource.data.settings.tier': instance['resource']['data']['settings']['tier'],
                'resource.data.sqlNetworkArchitecture': instance['resource']['data']['sqlNetworkArchitecture'],
                'resource.data.state': instance['resource']['data']['state'],
                'resource.discoveryDocumentUri': instance['resource']['discoveryDocumentUri'],
                'resource.discoveryName': instance['resource']['discoveryName'],
                'resource.location': instance['resource']['location'],
                'resource.parent': instance['resource']['parent'],
                'resource.version': instance['resource']['version'],
                'updateTime': instance['updateTime']
            }
            writer.writerow(instance_data)

# Example usage
json_file = '/Users/brunoemf/Documents/workspace/cloudsql-iar/sql-instances.json'
csv_file = 'output.csv'
parse_sql_instances(json_file, csv_file)
