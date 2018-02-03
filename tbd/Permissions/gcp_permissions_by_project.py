import os
import json


projList = []
projListCommand = os.popen('gcloud projects list --format json').read()

data = json.loads(projListCommand)

for item in data:
    projList.append(item['projectId'])

print('Project,User or Account,Permission')

for p in projList:
    cmd = 'gcloud projects get-iam-policy {} --format json'.format(p)
    projPermCommand = os.popen(cmd).read()
    info = json.loads(projPermCommand)

    for i in range(len(info['bindings'])):
        for j in range(len(info['bindings'][i]['members'])):
            print(p + ',' + info['bindings'][i]['members'][j] + ',' + info['bindings'][i]['role'])
