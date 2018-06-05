from googleapiclient import discovery
from pprint import pprint

service = discovery.build('iam', 'v1')
request = service.projects().roles().get(name='projects/allofus-securitysupport/roles/role_security_monitor_remove')
response = request.execute()

pprint(response)
