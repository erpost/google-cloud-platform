from google.cloud import storage
import os
from gcp_projects import get_projects
from gcp_authentication import get_key
import logging

"""Monitors Google Cloud Platform for Buckets with Global Permissions and sends Email"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_key()
sendemail = False
fname = './logs/gcp_bucket_log_basic.log'
logging.basicConfig(format='%(asctime)s\t- %(levelname)s: %(message)s', level=logging.INFO, filename=fname)

for project_name in get_projects():
    storage_client = storage.Client(project=project_name)
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        policy = bucket.get_iam_policy()
        for role in policy:
            members = policy[role]

            for member in members:
                if member == 'allUsers' or member == 'allAuthenticatedUsers':
                    sendemail = True
                    logging.warning('Bucket "{0}" in project "{1}" has "{2}" permissions'
                                    .format(bucket.name, project_name, member))
