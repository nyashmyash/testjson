import os
import json
import sys
from jsonschema import validate
from jsonschema import Draft7Validator

event_dir_global = "d:\\task_folder\\event\\"
schema_dir_global = "d:\\task_folder\\schema\\"
def check_files(event_dir, schema_dir):
    data_schemas = {}
    name_schemas = []
    events = os.listdir(path=event_dir + ".")
    schemas = os.listdir(path=schema_dir + ".")
    for f in schemas:
        with open(schema_dir + f, "r") as read_file:
            name_schemas.append(f)
            data = json.load(read_file)
            data_schemas[f] = data

    for f in events:
        with open(event_dir + f, "r") as read_file:
            print('-------the following errors were found in file ' + f + ':')
            data = json.load(read_file)
            name_sch = ''
            if data != None and 'event' in data:
                name_sch = data['event'] + '.schema'
            print('-----------for schema ' + name_sch + ':')
            schema_detect = False
            for i in name_schemas:
                if i == name_sch:
                    schema_detect = True
                    v = Draft7Validator(data_schemas[i])
                    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
                    for error in errors:
                        print(error.message)
            if schema_detect == False:
               print ('schema failed')

if __name__ == "__main__":
    if len(sys.argv)>1:
        event_dir_global = sys.argv[1]
        schema_dir_global = sys.argv[2]
    check_files(event_dir_global, schema_dir_global)            
