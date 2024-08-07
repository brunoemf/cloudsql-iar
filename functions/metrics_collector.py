import subprocess
import json
import time

def get_cpu_utilization(project_id: str, instance_name: str):
    """Prints aggregated CPU utilization metric for last 72 hours

    Args:
        project_id: Google Cloud project id
        instance_name: Google Cloud SQL instance id
    Returns:
        Mean of the CPU Utilization
    """

    print('collecting cpu usage')
    # [START monitoring_read_timeseries_align]
    from google.cloud import monitoring_v3

    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 259200), "nanos": nanos},
        }
    )
    aggregation = monitoring_v3.Aggregation(
        {
            "alignment_period": {"seconds": 3600}, 
            "per_series_aligner": monitoring_v3.Aggregation.Aligner.ALIGN_MEAN,
        }
    )

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": f'metric.type = "cloudsql.googleapis.com/database/cpu/utilization" AND resource.labels.database_id = "{project_id}:{instance_name}"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
            "aggregation": aggregation,
        }
    )
    # Manipulating the time series object
    for result in results:
        # Accessing the points
        for point in result.points:
            # Accessing the value
            value = point.value.double_value
            '''
            # Accessing the timestamp
            timestamp = point.interval.end_time
            # Formatting the timestamp
            formatted_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp.seconds))
            '''
            #print(f"CPU Usage: {value}")
        #print(result)
    # [END monitoring_read_timeseries_align]
    return value

def get_ram_utilization(project_id: str, instance_name: str):
    """Prints aggregated CPU utilization metric for last 72 hours

    Args:
        project_id: Google Cloud project id
        instance_name: Google Cloud SQL instance id
    Returns:
        Mean of the CPU Utilization
    """
    # [START monitoring_read_timeseries_align]
    from google.cloud import monitoring_v3

    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 259200), "nanos": nanos},
        }
    )
    aggregation = monitoring_v3.Aggregation(
        {
            "alignment_period": {"seconds": 3600}, 
            "per_series_aligner": monitoring_v3.Aggregation.Aligner.ALIGN_MEAN,
        }
    )

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": f'metric.type = "cloudsql.googleapis.com/database/memory/total_usage" AND resource.labels.database_id = "{project_id}:{instance_name}"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
            "aggregation": aggregation,
        }
    )
    # Manipulating the time series object
    for result in results:
        # Accessing the points
        for point in result.points:
            # Accessing the value
            value = point.value.double_value
            '''
            # Accessing the timestamp
            timestamp = point.interval.end_time
            # Formatting the timestamp
            formatted_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp.seconds))
            '''
            #print(f"CPU Usage: {value}")
        #print(result)
    # [END monitoring_read_timeseries_align]
    return value

def get_storage_utilization(project_id: str, instance_name: str):
    """Prints aggregated CPU utilization metric for last 72 hours

    Args:
        project_id: Google Cloud project id
        instance_name: Google Cloud SQL instance id
    Returns:
        Mean of the CPU Utilization
    """
    # [START monitoring_read_timeseries_align]
    from google.cloud import monitoring_v3

    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 259200), "nanos": nanos},
        }
    )
    aggregation = monitoring_v3.Aggregation(
        {
            "alignment_period": {"seconds": 3600}, 
            "per_series_aligner": monitoring_v3.Aggregation.Aligner.ALIGN_MEAN,
        }
    )

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": f'metric.type = "cloudsql.googleapis.com/database/disk/bytes_used" AND resource.labels.database_id = "{project_id}:{instance_name}"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
            "aggregation": aggregation,
        }
    )
    # Manipulating the time series object
    for result in results:
        # Accessing the points
        for point in result.points:
            # Accessing the value
            value = point.value.double_value
            '''
            # Accessing the timestamp
            timestamp = point.interval.end_time
            # Formatting the timestamp
            formatted_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp.seconds))
            '''
            #print(f"CPU Usage: {value}")
        #print(result)
    # [END monitoring_read_timeseries_align]
    return value



