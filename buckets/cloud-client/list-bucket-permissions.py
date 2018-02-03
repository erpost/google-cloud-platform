from google.cloud import storage

bucketname = input('Bucket name: ')


def view_bucket_permissions(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    policy = bucket.get_iam_policy()

    for role in policy:
        members = policy[role]
        print('Role: {}, Members: {}'.format(role, members))


view_bucket_permissions(bucketname)
