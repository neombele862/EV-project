import boto3
from dotenv import dotenv_values


config = dotenv_values(".env")

def connect_to_s3() -> object:
    """Connect to Amazon S3."""
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY'],
            region_name=config['AWS_REGION_NAME']
        )
        return s3
    except Exception as e:
        print(f"Could not connect to S3.{e}")
        return None
    finally:
        print("S3 connection established.")

def upload_to_s3(file_name: str, bucket: str, object_name=None) -> None:
    """Upload a file to an Amazon S3 bucket."""
    s3 = connect_to_s3()
    
    if s3 is not None:
        try:
            s3.upload_file(file_name, bucket, object_name)
            print(f"File '{file_name}' uploaded to {bucket}/{object_name}")
        except FileNotFoundError:
            print(f"The file '{file_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Could not connect to S3.")        
        
def connect_to_rds() -> object:
    """Connect to Amazon RDS."""
    try:
        rds = boto3.client(
            'rds',
            aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY'],
            region_name=config['AWS_REGION_NAME']
        )
        return rds
    except:
        print("Could not connect to RDS.")
        return None
    
