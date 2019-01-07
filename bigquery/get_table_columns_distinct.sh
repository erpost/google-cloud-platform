#!/bin/bash

# This script will ask for a BigQuery Dataset and return all Tables and Columns, as well as all unique data in each Row
# When the script completes, a CSV file (tables_columns_distinct.csv) is returned

rm -f tables_columns_distinct.csv
IFS=$'\n'

echo "Data set: "
read dataset

echo "Table,Column,Distinct Data" | tee -a tables_columns_distinct.csv

bq query --use_legacy_sql=false --format=json "SELECT table_id FROM \`$dataset.__TABLES_SUMMARY__\`" | jq -r '.[].table_id'  > /tmp/tables

for table in $(cat /tmp/tables);
do
        for column in $(bq show --format=json $dataset.$table | jq -r '.schema.fields[].name')
        do
                for data in $(bq query --use_legacy_sql=false --format=json "select distinct $column from $dataset.$table" | jq -r .[].$column)
                do
                        echo "\"$table\",\"$column\",\"$data\"" | tee -a tables_columns_distinct.csv

                done
        done
done

rm -f /tmp/tables
