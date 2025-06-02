from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

def upload_cs_file(source_file_name,filename):
    try:
        destination_file_name= f'generated_resume/{filename}'
        storage_client = storage.Client()
        bucket = storage_client.bucket(os.getenv('BUCKET_NAME'))
        blob = bucket.blob(destination_file_name)
        blob.upload_from_filename(source_file_name)
        url = f"https://storage.cloud.google.com/thiru_ai_fram/generated_resume/{filename}"
        return True, url
    except Exception as e:
        print(f"Error in the upload_cs_file Function: {e}")
        return False, None