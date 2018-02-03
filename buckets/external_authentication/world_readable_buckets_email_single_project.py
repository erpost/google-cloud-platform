from google.cloud import storage
import sendgrid
import os
from sendgrid.helpers.mail import *

storage_key = ''
source_email = ''
dest_email = ''
send_email = False

storage_client = storage.Client.from_service_account_json(storage_key)

for bucket in storage_client.list_buckets():

    policy = bucket.get_iam_policy()
    for role in policy:
        members = policy[role]

        for member in members:
            if member == 'allUsers' or member == 'allAuthenticatedUsers':
                send_email = True
                print('Warning! The bucket "{0}" has the "{1}" group'.format(bucket.name, member))

if send_email:

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(source_email)
    to_email = Email(dest_email)
    subject = "Check Bucket Permissions"
    content = Content("text/plain", "You have Buckets that are world-accessible")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
