projectname = input('Project name: ')


def list_buckets(project_name):
    from google.cloud import storage

    bucketlist = []

    storage_client = storage.Client(project=project_name)

    for bucket in storage_client.list_buckets():
        bucketlist.append(bucket.name)
    return bucketlist


print(list_buckets(projectname))
