import boto3
import collections
import datetime

ec = boto3.client('ec2')

def lambda_handler(event, context):
    reservations = ec.describe_instances(
        Filters=[
            {'Name': 'tag:Backup', 'Values': ['backup', 'Backup']},
        ]
    ).get(
        'Reservations', [],
    )

    instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])

    print "Found %d instances that need backing up" % len(instances)

    to_tag = collections.defaultdict(list)
    
    for instance in instances:
        try:
            retention_days = [
                int(t.get('Value')) for t in instance['Tags']
                if t['Key'] == 'Retention'][0]
        except IndexError:
            retention_days = 14

        for dev in instance['BlockDeviceMappings']:
            if dev.get('Ebs', None) is None:
                continue
            vol_id = dev['Ebs']['VolumeId']
            print "Found EBS volume %s on instance %s" % (
                vol_id, instance['InstanceId'])

            snap = ec.create_snapshot(
                VolumeId=vol_id,
            )
            
            snap_id = snap['SnapshotId']
            
            snap_tags = []
            
            to_tag[retention_days].append(snap_id)

            for tag in instance['Tags']:
                if tag['Key'].startswith('aws:'):
                    next
                else:
                    snap_tags.append({'Key': tag['Key'], 'Value': tag['Value']})

            print "Retaining snapshot %s of volume %s from instance %s for %d days" % (
                snap_id,
                vol_id,
                instance['InstanceId'],
                retention_days,
            )

            delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
            delete_fmt = delete_date.strftime('%Y-%m-%d')
            snap_tags.append({'Key': 'DeleteOn', 'Value': delete_fmt})
            snap_tags.append({'Key': 'ForInstance' , 'Value': instance['InstanceId']})
            ec.create_tags(
                Resources=[snap_id],
                Tags=snap_tags
            )
            
    for retention_days in to_tag.keys():
        delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
        delete_fmt = delete_date.strftime('%Y-%m-%d')
        print "Will delete %d snapshots on %s" % (len(to_tag[retention_days]), delete_fmt)