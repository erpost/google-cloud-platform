#!/bin/bash

DEVSHELL_PROJECT_ID="tpat-ep-test"
KEYRING_NAME="test"
CRYPTOKEY_NAME="testkey"

mkdir /tmp/unencryptedfiles
mkdir /tmp/encryptedfiles

# Get encrypted files from bucket
echo "Downloading encrypted files from Google..."
for i in `gsutil ls gs://tpatciphertext`
do
        gsutil cp $i /tmp/encryptedfiles
done

echo "Decrypting files..."
for i in `ls /tmp/encryptedfiles`
do
        curl -s -X POST "https://cloudkms.googleapis.com/v1/projects/$DEVSHELL_PROJECT_ID/locations/global/keyRings/$KEYRING_NAME/cryptoKeys/$CRYPTOKEY_NAME:decrypt" \
        -d "{\"ciphertext\":\"`cat /tmp/encryptedfiles/$i`\"}" \
        -H "Authorization:Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type:application/json" | jq .plaintext -r | base64 -d > /tmp/unencryptedfiles/$i-unencrypted.txt
done

# Upload decrypted files to bucket
echo "Uploading decrypted files to Google..."
for i in `ls /tmp/unencryptedfiles`
do
        gsutil cp /tmp/unencryptedfiles/$i gs://tpatcleartextend
done

rm -rf /tmp/unencryptedfiles
rm -rf /tmp/encryptedfiles
