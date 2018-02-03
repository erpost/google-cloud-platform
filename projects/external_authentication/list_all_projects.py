from googleapiclient import discovery
import os

storage_key = ''


def get_projects(storage_key):
    project_list = []

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_key

    service = discovery.build('cloudresourcemanager', 'v1')
    request = service.projects().list()
    while request is not None:
        response = request.execute()
        for project in response['projects']:
            if project['lifecycleState'] == 'ACTIVE':
                project_list.append(project['projectId'])

        request = service.projects().list_next(previous_request=request, previous_response=response)

    return project_list


for project in (get_projects(storage_key)):
    print(project)
