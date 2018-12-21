#!/usr/bin/env bash

for project in $(gcloud projects list --format="value(projectId)")
    do
    echo 'Project: ' $project
    for instance in $(gcloud sql instances list --format="value(NAME)" --project=$project)
        do
        gcloud sql instances describe $instance --format="value(name,settings.databaseFlags.name,\
                                                          settings.databaseFlags.value)"
    done
done