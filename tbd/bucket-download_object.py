from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('ep-test-bucket')

blob = bucket.blob('buckettest2.txt')

blob.download_to_filename(filename='/home/ep/test2.txt')
