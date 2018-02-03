import base64

image = open('/tmp/files/testfile.txt', 'r')
image_64_encode = base64.encodestring(image.read())

print(image_64_encode)