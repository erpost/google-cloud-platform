# Python 2.7
# Prints contents of object to the console

from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('ep-test-bucket')

blob = bucket.get_blob('test.txt')

print(blob.download_as_string())