# main.py
import argparse
from functions.data_parser import parse_sql_instances

#Generate a description of this code
"""This script lists Cloud SQL instances for a given organization and exports the data to a CSV file.

It takes two arguments:

- org_id: The organization ID.
- csv_file: The path to the CSV file to export data to.

The script uses the `gcloud` command-line tool to retrieve the list of instances and then parses the JSON output into a CSV file.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Cloud SQL instances and export to CSV.")
    parser.add_argument("org_id", help="Pass the Organization ID to list Cloud SQL instances")
    parser.add_argument("csv_file", help="Path to the CSV file to export data to")
    args = parser.parse_args()
    print('Calling Main....')
    parse_sql_instances(args.org_id, args.csv_file)

