from google.cloud import storage
import pandas as pd
import io



'''
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    '''




'''
source_bucket_name = 'qwiklabs-gcp-01-1bfd3dd7c03a-xlsx-excel'
source_blob_name = 'bankc.xlsx'
destination_bucket_name = 'qwiklabs-gcp-01-1bfd3dd7c03a-csv-cssv'
destination_blob_name = 'bankc.csv'

'''

def convert_to_csv(data,context):


    source_bucket_name = 'qwiklabs-gcp-04-6cdba75072b5-xlsx'
    source_blob_name = 'bankc.xlsx'
    destination_bucket_name = 'qwiklabs-gcp-04-6cdba75072b5-csv'
    destination_blob_name = 'bankc.csv'


    storage_client = storage.Client()

    bucket = storage_client.bucket(source_bucket_name)
    #bucket.list_blobs()
    blob = bucket.blob(source_blob_name)
    contents = blob.download_as_string()
    fil = io.StringIO(str(contents))
    xl = pd.read_excel(fil)
    #xl.to_csv("data.csv")
    
    dest_bucket = storage_client.bucket(destination_bucket_name)
    blobb = dest_bucket.blob(destination_blob_name)

    blobb.upload_from_string(xl)


    print('CSV file uploaded to bucket')


#convert_to_csv()



