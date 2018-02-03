from google.cloud import storage
import os
from ses_email import send_email_default
from gcp_projects import get_projects
from gcp_authentication import get_key

"""Monitors Google Cloud Platform for Buckets with Global Permissions and sends Email with Bucket and Project Names"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_key()
sendemail = False
bucket_dict = {}

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
                    bucket_dict[bucket.name] = project_name

subject = 'Globally Accessible Buckets Found!'
body_text = '\n'.join({'Bucket:\t{0}\nProject:\t{1}\n'.format(key, value) for (key, value) in bucket_dict.items()})

if sendemail:
    send_email_default(subject, body_text)
