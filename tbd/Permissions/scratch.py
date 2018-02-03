import os

print(os.popen('gsutil iam get gs://ciphertext -p tpat-python-kms').read())
