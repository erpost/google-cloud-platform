from google.cloud import bigquery


def get_tables(project_id, dataset):
    """gets a list of BigQuery Tables for a given Project/Dataset"""
    tables = []
    client = bigquery.Client(project=project_id)

    dataset_ref = client.dataset(dataset)
    dataset_tables = list(client.list_tables(dataset_ref))

    for dataset_table in dataset_tables:
        tables.append(dataset_table.table_id)

    return tables


def get_columns(project_id, dataset, table):
    """gets a list of all Columns for a particular BigQuery Table"""
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset, project_id)
    table_ref = dataset_ref.table(table)
    table = client.get_table(table_ref)
    rows = client.list_rows(table)
    field_names = [field.name for field in rows.schema]

    return field_names


if __name__ == '__main__':
    project_id = input('Project ID: ')
    if len(project_id) < 1:
        project_id = 'bigquery-public-data'
    dataset = input('Data set: ')
    if len(dataset) < 1:
        dataset = 'samples'
    table = input('Table: ')
    if len(table) < 1:
        table = 'shakespeare'

    print(get_tables(project_id, dataset))
    print(get_columns(project_id, dataset, table))
