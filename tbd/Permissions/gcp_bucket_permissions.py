import os
import json


def main():
    """print CSV Headers"""
    print('Level or Tier,Project,User or Account,Permission')
    get_bucket_permissions(get_projects())

def get_projects():
    """query projects and load json elements"""
    projList = []
    projListCommand = os.popen('gcloud projects list --format json').read()
    projListData = json.loads(projListCommand)

    """load all projects in list"""
    for item in projListData:
        projList.append(item['projectId'])

    return projList

def get_bucket_permissions(projList):
    """query project and load bucket list(s)"""
    for p in projList:
        bucketListCommand = os.popen('gsutil ls -p {}'.format(p))
        bucketList = bucketListCommand.read().strip().split('\n')

        """query buckets and load json elements"""
        for b in bucketList:
            if len(b) < 1:
                continue
            else:
                bucketPermCommand = os.popen('gsutil iam get {0} -p {1}'.format(b, p)).read()
                bucketInfo = json.loads(bucketPermCommand)

                """print bucket permissions"""
                if 'bindings' in bucketInfo:
                    for i in range(len(bucketInfo['bindings'])):
                        for j in range(len(bucketInfo['bindings'][i]['members'])):
                            print(p + ',Bucket: ' + b + ',' + bucketInfo['bindings'][i]['members'][j] +
                                  ',' + bucketInfo['bindings'][i]['role'])
                else:
                    print(p + ',Bucket: ' + b)


if __name__ == "__main__":
    main()
