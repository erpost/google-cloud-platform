- Run install.sh

- Within the Project to be monitored, create GCP Service Account with Custom Role and create Key (permissions below)
  - storage.buckets.get
  - storage.buckets.getIamPolicy
  - storage.buckets.list

- Download Service Account Key file, copy and rename to Server (/home/YOUR USER DIRECTORY/.gcp/sa-bucket-perms.json)

- Update Python script Variables
  - storage_key = '/home/YOUR USER DIRECTORY/.gcp/sa-bucket-perms.json'
  - source_email = 'from@email.com'
  - dest_email = 'to@email.com'

- Create Sendgrid Account and configure API Key (link below)
  - https://app.sendgrid.com/guide/integrate/langs/python

- Modify '/home/YOUR USER DIRECTORY/.bash_profile' and add the following line
  - export SENDGRID_API_KEY='YOUR SENDGRID KEY'

- Run the command: source ~/.bash_profile