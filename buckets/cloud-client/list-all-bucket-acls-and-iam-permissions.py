from google.cloud import storage

projectname = input('Project name: ')
if len(projectname) < 1:
    projectname = 'tpat-buckets'

client = storage.Client(project=projectname)

for bucket in client.list_buckets():
    print('Bucket:\t' + bucket.name)
    for entry in bucket.acl:
        print('{0}:\t {1}'.format(entry['role'], entry['entity']))

    policy = bucket.get_iam_policy()
    for role in policy:
        members = policy[role]
        print('{0}:\t {1}'.format(role, members))
