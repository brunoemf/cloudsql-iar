import subprocess
import json
import time

def list_time_series_aggregate(project_id: str):
    """Prints aggregated CPU utilization metric for last hour

    Args:
        project_id: Google Cloud project id

    Returns:
        Collection of time series.
        Iterating over this object will yield results and resolve additional pages automatically.
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
            "start_time": {"seconds": (seconds - 3600), "nanos": nanos},
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
            "filter": 'metric.type = "cloudsql.googleapis.com/database/cpu/utilization" AND resource.labels.database_id = "tonal-land-379520:run-lab-instance"',
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
        print(result)
    # [END monitoring_read_timeseries_align]
    return results

# Example usage
instance_name = 'run-lab-instance'
instance_region = 'us-central1'
project_id = 'tonal-land-379520'  # Replace with your project ID

metrics = list_time_series_aggregate(project_id)
#print(metrics)
