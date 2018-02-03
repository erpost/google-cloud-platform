from google.cloud import storage
import google.auth
import os

storage_key = '/Users/epost/Downloads/tpat-bucket-perms-check.json'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_key

credentials, project = google.auth.default()

storage_client = storage.Client(credentials=credentials)

buckets = storage_client.list_buckets()

for bucket in buckets:
    print(bucket.name)
