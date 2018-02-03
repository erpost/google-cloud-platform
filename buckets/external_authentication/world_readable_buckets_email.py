from google.cloud import storage
from googleapiclient import discovery
import sendgrid
import os
from sendgrid.helpers.mail import *

storage_key = ''
source_email = ''
dest_email = ''
send_email = False
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
                    send_email = True

if send_email:

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(source_email)
    to_email = Email(dest_email)
    subject = "Check Bucket Permissions"
    content = Content("text/plain", "You have Buckets that are world-accessible")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
