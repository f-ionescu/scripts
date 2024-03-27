import boto3

def delete_all_object_versions(bucket_name):
    # Create an S3 resource
    s3 = boto3.resource('s3')
    
    # Get the bucket
    bucket = s3.Bucket(bucket_name)
    
    # Iterate over all object versions and delete them
    for obj_version in bucket.object_versions.all():
        obj_version.delete()
    
    print("All object versions deleted from the bucket.")

# Get the bucket name from user input or any other source
bucket_name = input("Enter the S3 bucket name: ")

# Call the function with the dynamic bucket name
delete_all_object_versions(bucket_name)

