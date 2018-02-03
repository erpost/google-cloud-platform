#from pprint import pprint

projectname = input('Project name: ')
if len(projectname) < 1:
    projectname = 'tpat-buckets'

def list_buckets(project_name):
    import googleapiclient.discovery

    storage_client = googleapiclient.discovery.build('storage', 'v1')

    buckets = storage_client.buckets().list(project=project_name).execute()
    # pprint(buckets)

    bucketlist = []

    for bucket in buckets['items']:
        # pprint(bucket)
        # print(bucket['name'])
        # print(bucket['location'])
        bucketlist.append(bucket['name'])
    return bucketlist


print(list_buckets(projectname))
