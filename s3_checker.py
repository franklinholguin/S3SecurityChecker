import boto3
from botocore.exceptions import ClientError

def check_s3_bucket(bucket_name):
    s3 = boto3.client("s3")
    
    # Check public access
    try:
        public = s3.get_public_access_block(Bucket=bucket_name)["PublicAccessBlockConfiguration"]
        print("Public Access Blocked:", all(public.values()))
    except ClientError:
        print("Public Access: Unknown (check permissions)")
    
    # Check encryption
    try:
        encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        print("Encryption Enabled:", True)
    except ClientError:
        print("Encryption Enabled: False")

if __name__ == "__main__":
    bucket = input("Enter S3 bucket name: ")
    check_s3_bucket(bucket)