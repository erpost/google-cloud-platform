import os
import json

projects = os.popen('gcloud projects list --format json').read()

os.system('gcloud projects list --format=json')

info = json.loads(projects)
for item in info:
    print('Name:\t\t', item['name'])
    print('Number:\t\t', item['projectNumber'])
    print('Created:\t', item['createTime'])
    print('State:\t\t', item['lifecycleState'])
    print()

print(json.dumps(projects, sort_keys=True, indent=4))
