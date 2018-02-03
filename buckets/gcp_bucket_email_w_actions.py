from google.cloud import storage
import os
from ses_email import send_email_default
from gcp_projects import get_projects
from gcp_authentication import get_key

"""Removes Global Permissions from Google Cloud Platform Buckets and sends Email with Bucket and Project Names"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_key()
sendemail = False
bucket_dict = {}
bckts = []

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
                    policy = bucket.get_iam_policy()
                    policy[role].discard(member)
                    bucket.set_iam_policy(policy)
                    print(bucket.name)
                    print(policy)
                    print(member)


subject = 'Globally Accessible Buckets Found and Fixed!'
body_text = '\n'.join({'Bucket:\t{0}\nProject:\t{1}\n'.format(key, value) for (key, value) in bucket_dict.items()})

if sendemail:
    send_email_default(subject, body_text)
