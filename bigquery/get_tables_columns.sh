#!/bin/bash

echo Project Name?
read project

echo Dataset Name?
read dataset

bq ls --format=json $project:$dataset | jq -r '.[].id' | awk -F. '{print $2}'  > /tmp/tables

for table in $(cat /tmp/tables);
do
        echo "########" $table "#######"
        bq show --format=json $dataset.$table | jq -r '.schema.fields[].name'

done