import boto3
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize the boto3 clients
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
rds = boto3.client('rds')

def scan_ec2_instances():
    try:
        # Describe EC2 instances
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'State': instance['State']['Name'],
                    'PublicIP': instance.get('PublicIpAddress', 'N/A')
                })
        return instances
    except Exception as e:
        logging.error(f"Error scanning EC2 instances: {e}")
        return []

def scan_s3_buckets():
    try:
        # List S3 buckets
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets
    except Exception as e:
        logging.error(f"Error scanning S3 buckets: {e}")
        return []

def scan_rds_instances():
    try:
        # Describe RDS instances
        response = rds.describe_db_instances()
        rds_instances = [db['DBInstanceIdentifier'] for db in response['DBInstances']]
        return rds_instances
    except Exception as e:
        logging.error(f"Error scanning RDS instances: {e}")
        return []
