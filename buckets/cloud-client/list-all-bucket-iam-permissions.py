from google.cloud import storage

project_name = input('Project name: ')
if len(project_name) < 1:
    project_name = 'tpat-buckets'

client = storage.Client(project=project_name)

for bucket in client.list_buckets():

    policy = bucket.get_iam_policy()
    for role in policy:
        members = policy[role]
        print('{0}:\t {1}\t {2}'.format(bucket.name, role, members))
    