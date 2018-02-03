from google.cloud import storage

storage_client = storage.Client.from_service_account_json('<path/to/key.json>')

buckets = storage_client.list_buckets()

for bucket in buckets:
    print(bucket.name)
