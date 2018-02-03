#!/bin/bash

gcloud projects list | awk '{print $1}' | grep -v PROJECT_ID > list

rm -f buckets.txt

for project in $(cat list); do
        echo Listing buckets in project: $project
        echo ============================= >> buckets.txt
        echo $project >> buckets.txt
        echo ============================= >> buckets.txt
        gsutil ls -p $project >> buckets.txt
done

bucket_num=$(grep 'gs:' buckets.txt | wc -l)
echo ============================= >> buckets.txt
echo "$bucket_num bucket(s) total" | tee -a buckets.txt

rm -f list
