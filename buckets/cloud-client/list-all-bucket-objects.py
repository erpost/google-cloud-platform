projectname = input('Project name: ')
bucketname = input('Bucket name: ')


def list_objects(bucket_name, project_name):
    from google.cloud import storage

    storage_client = storage.Client(project=project_name)

    bucket = storage_client.get_bucket(bucket_name)

    for blob in bucket.list_blobs():
        print(blob.name)


list_objects(bucketname, projectname)
