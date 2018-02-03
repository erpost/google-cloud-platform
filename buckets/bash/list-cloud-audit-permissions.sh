#!/bin/bash

rm -f listAuditPermissions.txt

for project in $(gcloud projects list --format="table(projectId)" | grep -v PROJECT_ID)
  do
    echo ${project} | tee -a listAuditPermissions.txt
    gcloud projects get-iam-policy ${project} | egrep 'auditConfigs|auditLogConfigs|logType|service:' \
    | tee -a listAuditPermissions.txt
done
