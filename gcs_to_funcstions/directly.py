from google.cloud import storage
import pandas as pd
import io


def convert_to_csv(data,context):


    source_bucket_name = 'qwiklabs-gcp-04-6cdba75072b5-xlsx'
    source_blob_name = 'bankc.xlsx'
    destination_bucket_name = 'qwiklabs-gcp-04-6cdba75072b5-csv'
    destination_blob_name = 'bankc.csv'


    storage_client = storage.Client()

    
    xl = pd.read_excel('gs://qwiklabs-gcp-04-6cdba75072b5-xlsx/bankc.xlsx')
    #xl.to_csv("data.csv")
    xl.to_csv('gs://qwiklabs-gcp-04-6cdba75072b5-csv/bankc.csv')
    
   

    print('CSV file uploaded to bucket')