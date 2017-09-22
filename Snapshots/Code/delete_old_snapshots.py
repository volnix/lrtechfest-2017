import boto3
import datetime

ec = boto3.client('ec2')

"""
This function looks at *all* snapshots that have a "DeleteOn" tag containing
the current day formatted as YYYY-MM-DD. This function should be run at least
daily.
"""

"""
To get your account id, run this snippet:
> import boto3
> iam = boto3.client('iam')
> print iam.get_user()['User']['Arn'].split(':')[4]
"""

account_ids = ['<YOUR ACCOUNT ID HERE>']

def lambda_handler(event, context):
    delete_on = datetime.date.today().strftime('%Y-%m-%d')
    filters = [
        {'Name': 'tag-key', 'Values': ['DeleteOn']},
        {'Name': 'tag-value', 'Values': [delete_on]},
    ]
    snapshot_response = ec.describe_snapshots(OwnerIds=account_ids, Filters=filters)


    for snap in snapshot_response['Snapshots']:
        print "Deleting snapshot %s" % snap['SnapshotId']
        ec.delete_snapshot(SnapshotId=snap['SnapshotId'])