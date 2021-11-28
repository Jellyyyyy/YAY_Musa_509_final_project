import json
import bigquery as bq

bq load --source_format NEWLINE_DELIMITED_JSON crimedata_vegas to_load.json
ObjectId:int64,Event_Number,Event_Date,Type,Type_Description,General_Location,Beat,Disposition,Map_X,Map_Y,New_Y,LAT,LONG,WARD,geometry:GEOGRAPHY
