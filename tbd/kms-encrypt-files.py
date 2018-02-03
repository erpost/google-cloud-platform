# Python 2.7

from google.cloud import storage
import os
import base64
import glob

DEVSHELL_PROJECT_ID = 'tpat-ep-test'
KEYRING_NAME = 'test'
CRYPTOKEY_NAME = 'testkey'

GCP_START_PLAINTEXT_BUCKET = 'cleartextstart'
GCP_CIPHERTEXT_BUCKET = 'ciphertext'
GCP_END_PLAINTEXT_BUCKET = 'cleartextend'

PLAINTEXT_BUCKET = '/tmp/files/'
BASE64_BUCKET = '/tmp/base64files/'
CIPHERTEXT_BUCKET = '/tmp/encryptedfiles/'

os.mkdir(PLAINTEXT_BUCKET)
os.mkdir(BASE64_BUCKET)
os.mkdir(CIPHERTEXT_BUCKET)

# Get file(s) from bucket
print('Downloading plaintext files from Google...')
client = storage.Client()
bucket = client.get_bucket(GCP_START_PLAINTEXT_BUCKET)

for blob in bucket.list_blobs():
    blob.download_to_filename(filename=PLAINTEXT_BUCKET + blob.name)

# Base64 each file
print('Base64-ing files...')
for clear_file in glob.glob(PLAINTEXT_BUCKET + '*'):
    base64_file = base64.encodestring(open(clear_file, 'r').read())

    print(base64_file)
# file_list.append(file)
# print(file_list)






#    print(image_64_encode)

# Encrypt each file
print('Encrypting files...')

# Upload encrypted file to bucket
print('Uploading encrypted files to Google...')
