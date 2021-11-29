from pipeline_tools import gcs_to_local_file, geopandas_to_gbq
import geopandas as gpd
import os

credential_path = "final-509-409489d51842.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def main(ds):
    local_path = gcs_to_local_file(
        gcs_bucket_name='1126_data',
        gcs_blob_name=f'facilitydata_2021-11-27.geojson'
    )

    print(f'Loading file {local_path} into a GeoDataFrame...')
    gdf = gpd.read_file(local_path)

    geopandas_to_gbq(
        geodataframe=gdf,
        dataset_name='musa_vegas_BQ',
        table_name='facilitydata'
    )

    print('Done.')

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())
