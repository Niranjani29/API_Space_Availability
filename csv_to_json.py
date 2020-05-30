import csv
import json
from io import open

csvFilePath = "D:\\RA\\Q3\\ra_data_classifier.csv"
jsonFilePath ="D:\\RA\\Q3\\converted_json.json"

data={}
f=open(csvFilePath, encoding ="ISO-8859-1")
reader = csv.reader(f)
next(f)
for row in reader:
	data[row[0]] = {'chunk': row[1],'has_space':row[2]}

j=json.dumps(data)
with open(jsonFilePath,'w') as f:
	f.write(j)
