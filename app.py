# import csv
import json
# import io

# csvFilePath = "D:\\RA\\Q3\\ra_data_classifier.csv"
# jsonFilePath ="D:\\RA\\Q3\\converted_json.json"

# data={}
# f=open(csvFilePath, encoding ="ISO-8859-1")
# reader = csv.reader(f)
# next(f)
# for row in reader:
# 	data[row[0]] = {"chunk": row[1],"has_space":row[2]}

# j=json.dumps(data)
# with open(jsonFilePath,'w') as f:
# 	f.write(j)



from flask import Flask, jsonify, request

app = Flask(__name__)

jsonFilePath ="converted_json.json"
json_file = open(jsonFilePath)
myjson = json.load(json_file)
print(myjson["33BFF6QPI1YEFYISIWWDVQKGH8RW3Z"])

@app.route('/', methods=['GET','POST'])
def index():
	# if request.method == 'GET':
	# 	return j
	# elif request.method=="POST":
	print("************")
	data_ans = request.get_json()
	hid=data_ans["hid"]
	print("HID :",hid)
	response = myjson[hid]
		# chunk = data_ans['chunk']
		# has_space=data_ans['has_space']
	# return jsonify({"chunk":chunk,"has_space":has_space})
	return response

if __name__ == '__main__':
    app.run(debug=True)