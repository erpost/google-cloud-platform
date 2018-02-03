def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']


list_instances(compute, tpat-python-kms, us-east1-c)
