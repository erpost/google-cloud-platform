from google.cloud import storage

project_name = input('Project name: ')
if len(project_name) < 1:
    project_name = 'tpat-buckets'

def list_buckets(project_name):
    from google.cloud import storage

    bucketlist = []

    storage_client = storage.Client(project=project_name)

    for bucket in storage_client.list_buckets():
        bucketlist.append(bucket.name)
    return bucketlist


bucketlist = list_buckets(project_name)

print(bucketlist)


def remove_bucket_editor(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    policy = bucket.get_iam_policy()
    policy['roles/storage.legacyBucketOwner'].discard('projectEditor:tpat-buckets')
    bucket.set_iam_policy(policy)
    print('Removed Bucket Editor in the {} bucket'.format(bucket_name))


def remove_bucket_owner(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    policy = bucket.get_iam_policy()
    policy['roles/storage.legacyBucketOwner'].discard('projectOwner:tpat-buckets')
    bucket.set_iam_policy(policy)
    print('Removed Bucket Owner in the {} bucket'.format(bucket_name))


def remove_bucket_reader(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    policy = bucket.get_iam_policy()
    policy['roles/storage.legacyBucketReader'].discard('projectViewer:tpat-buckets')
    bucket.set_iam_policy(policy)
    print('Removed Bucket Reader in the {} bucket'.format(bucket_name))


for bucketname in bucketlist:
    remove_bucket_owner(bucketname)
    remove_bucket_editor(bucketname)
    # remove_bucket_reader(bucketname)

print('Done!')
