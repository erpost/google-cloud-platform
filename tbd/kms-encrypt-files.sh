#!/bin/bash

DEVSHELL_PROJECT_ID="tpat-ep-test"
KEYRING_NAME="test"
CRYPTOKEY_NAME="testkey"

mkdir /tmp/files
mkdir /tmp/base64files
mkdir /tmp/encryptedfiles

# Get files from bucket
echo "Downloading plaintext files from Google..."
for i in `gsutil ls gs://tpatcleartextstart`
do
        gsutil cp $i /tmp/files
done

# Base64 each file
echo "Base64-ing files..."
for i in `ls /tmp/files`
do
        cat /tmp/files/$i | base64 > /tmp/base64files/$i-base64
done

# Encrypt each file
echo "Encrypting files..."
for i in `ls /tmp/base64files`
do
        curl -s -X POST "https://cloudkms.googleapis.com/v1/projects/$DEVSHELL_PROJECT_ID/locations/global/keyRings/$KEYRING_NAME/cryptoKeys/$CRYPTOKEY_NAME:encrypt" \
        -d "{\"plaintext\":\"`cat /tmp/base64files/$i`\"}" \
        -H "Authorization:Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type:application/json" | jq .ciphertext -r > /tmp/encryptedfiles/$i-encrypted
done

# Upload encrypted file to bucket
echo "Uploading encrypted files to Google..."
for i in `ls /tmp/encryptedfiles`
do
        gsutil cp /tmp/encryptedfiles/$i gs://tpatciphertext
done

rm -rf /tmp/files
rm -rf /tmp/base64files
rm -rf /tmp/encryptedfiles
