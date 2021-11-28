import json
import bigquery as bq
with open('crimedata_2021-11-28.geojson', 'r') as ifp:
  with open('to_load.json', 'w') as ofp:
    features = json.load(ifp)['features']
    # new-line-separated JSON
    schema = None
    for obj in features:
        props = obj['properties']  # a dictionary
        props['geometry'] = json.dumps(obj['geometry'])  # make the geometry a string
        json.dump(props, fp=ofp)
        print('', file=ofp) # newline
        if schema is None:
            schema = []
            for key, value in props.items():
                if key == 'geometry':
                    schema.append('geometry:GEOGRAPHY')
                elif isinstance(value, str):
                    schema.append(key)
                else:
                    schema.append('{}:{}'.format(key,
                       'int64' if isinstance(value, int) else 'float64'))
            schema = ','.join(schema)
    print('Schema: ', schema)
