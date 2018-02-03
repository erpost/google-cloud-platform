projectname = input('Project name: ')


def get_bucket_acls(project_name):
    from google.cloud import storage

    client = storage.Client(project=project_name)

    for bucket in client.list_buckets():
        print('--------------------------')
        print('Bucket:\t' + bucket.name)
        print(list(bucket.acl))

        for entry in bucket.acl:
            print('{0}:\t {1}'.format(entry['role'], entry['entity']))

    print('--------------------------')


get_bucket_acls(projectname)