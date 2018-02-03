import os
import json

# get organization
orgList = os.popen('gcloud organizations list | awk \'{print $2}\' | grep -v ID').read().strip()
print(orgList)

# query organization permissions and load json elements
orgPermCommand = os.popen('gcloud alpha organizations get-iam-policy {} --format json'.format(orgList)).read()
orgInfo = json.loads(orgPermCommand)

print(json.dumps(orgInfo, sort_keys=True, indent=4))

# print organization permissions
for i in range(len(orgInfo['bindings'])):
    for j in range(len(orgInfo['bindings'][i]['members'])):
        print(orgList + ',' + orgInfo['bindings'][i]['members'][j] + ',' + orgInfo['bindings'][i]['role'])
