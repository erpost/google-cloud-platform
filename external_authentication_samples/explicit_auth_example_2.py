from google.cloud import storage

storage_client = storage.Client.from_service_account_json('<path/to/key.json>')

buckets = list(storage_client.list_buckets())
print(buckets)
