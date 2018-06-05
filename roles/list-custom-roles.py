from googleapiclient import discovery
from pprint import pprint


service = discovery.build('iam', 'v1')
request = service.roles().list(parent='projects/allofus-securitysupport')
response = request.execute()
roles = response['roles']

pprint(roles)
print('*' * 75)

service = discovery.build('iam', 'v1')
request = service.projects().roles().list(parent='projects/allofus-securitysupport')
response = request.execute()
roles = response['roles']

pprint(roles)
