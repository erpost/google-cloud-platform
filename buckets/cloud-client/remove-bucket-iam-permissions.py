from google.cloud import storage

bucketname = input('Bucket name: ')
if len(bucketname) < 1:
    bucketname = 'tpat-test-5'

membername = input('Member name: ')
if len(membername) < 1:
    membername = 'projectOwner:tpat-buckets'

rolename = input('Role name: ')
if len(rolename) < 1:
    rolename = 'roles/storage.legacyBucketOwner'


def remove_bucket_iam_member(bucket_name, role, member):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    policy = bucket.get_iam_policy()

    policy[role].discard(member)

    bucket.set_iam_policy(policy)

    print('Removed {} with role {} from {}.'.format(member, role, bucket_name))


remove_bucket_iam_member(bucketname, rolename, membername)
