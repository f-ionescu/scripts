import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket("eatr-traefik-conf-test-763328378904-us-west-2")
bucket.object_versions..delete()
