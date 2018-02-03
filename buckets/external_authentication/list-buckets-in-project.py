from google.cloud import storage
import os

project_name = 'tpat-buckets'
storage_key = '/Users/epost/Downloads/tpat-bucket-perms-check.json'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_key

storage_client = storage.Client(project=project_name)

buckets = storage_client.list_buckets()

for bucket in buckets:
    print(bucket.name)
