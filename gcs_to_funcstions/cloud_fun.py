from google.cloud import storage
import pandas as pd


source_bucket_name = 'qwiklabs-gcp-01-1bfd3dd7c03a-xlsx-excel'
source_blob_name = 'bankc.xlsx'
destination_bucket_name = 'qwiklabs-gcp-01-1bfd3dd7c03a-csv-cssv'
destination_blob_name = 'bankc.csv'



def convert_to_csv(source_bucket_name, source_blob_name,destination_bucket_name,destination_blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(source_bucket_name)
    #bucket.list_blobs()
    blob = bucket.blob(source_blob_name)
    contents = blob.download_as_string()
    xl = pd.read_excel(contents)
    xl.to_csv("data.csv")
    
    dest_bucket = storage_client.bucket(destination_bucket_name)
    blobb = dest_bucket.blob(destination_blob_name)

    blobb.upload_from_filename("data.csv")


    print('CSV file uploaded to bucket')


convert_to_csv(source_bucket_name, source_blob_name,destination_bucket_name,destination_blob_name)



