from google.cloud import storage
from googleapiclient import discovery
import os

storage_key = ''
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_key


def get_projects():
    project_list = []

    service = discovery.build('cloudresourcemanager', 'v1')
    request = service.projects().list()
    while request is not None:
        response = request.execute()
        for project in response['projects']:
            if project['lifecycleState'] == 'ACTIVE':
                project_list.append(project['projectId'])

        request = service.projects().list_next(previous_request=request, previous_response=response)

    return project_list


for project_name in get_projects():
    storage_client = storage.Client(project=project_name)
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        policy = bucket.get_iam_policy()
        for role in policy:
            members = policy[role]

            for member in members:
                if member == 'allUsers' or member == 'allAuthenticatedUsers':
                    print('Warning! The bucket "{0}" in the project "{1}" has the "{2}" group associated'\
                          .format(bucket.name, project_name, member))
