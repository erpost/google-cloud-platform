#!/bin/bash

gcloud projects list | awk '{print $1}' | grep -v PROJECT_ID > list

rm -f buckets.csv

for project in $(cat list); do
    echo Listing buckets in project: $project
        for bucket in $(gsutil ls -p $project);do
            echo $bucket
            echo "$project,$bucket" >> buckets.csv
done
done

bucket_num=$(grep 'gs:' buckets.csv | wc -l)
echo -e "\n$bucket_num bucket(s) total" | tee -a buckets.csv

rm -f list
