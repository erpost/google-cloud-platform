projectname = input('Project name: ')
bucketname = input('Bucket name: ')


def make_bucket(bucket_name, project_name):
    from google.cloud import storage

    # Instantiates client
    storage_client = storage.Client(project=project_name)

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print('Bucket {} created.'.format(bucket.name))


make_bucket(bucketname, projectname)
