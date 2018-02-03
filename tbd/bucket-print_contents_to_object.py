# Python 2.7
# Replaces contents to object in bucket

from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('ep-test-bucket')

blob = bucket.get_blob('test.txt')

blob.upload_from_string('New contents!')