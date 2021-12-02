

# Load process environment variables from file named ".env". Environment vars
# will be available in the os.environ dictionary.
from dotenv import load_dotenv
load_dotenv()

# Import additional required packages
import datetime as dt
import os
import requests
from google.cloud import storage

credential_path = "final-509-409489d51842.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Retrieve data from URL
print('Downloading the addresses data...')
response = requests.get('https://opendata.arcgis.com/datasets/a1a48acba1af422e8351161655982d5a_0.geojson')

# Save retrieved data to a local file
print('Saving addresses data to a file...')

outfile_path = f'data/crimedata.geojson'
with open(outfile_path, mode='wb') as outfile:
    outfile.write(response.content)

# Upload local file of data to Google Cloud Storage
print('Uploading crime data to GCS...')
bucket_name = '1126_data'
blob_name = f'crimedata.geojson'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path)

print('Done')
