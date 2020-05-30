# API_Space_Availability
Created a working API that is web accessible that responds to GET or POST requests containing a JSON object requesting a piece of data with a particular “hid”  &amp; Returns a JSON object with the full record for the piece of data with that particular “hid”.


<b>ra_data_classifier :- </b>
The actual CSV Data. It contains 3 columns- hid, chunk, has_space.

<b>csv_to_json.py	:- </b>
First task was to convert the csv data into a json object 

    data[row[0]] = {"chunk": row[1],"has_space":row[2]} 

I used this line of code to convert the given CSV data to a dictionary which was in turn going to be converted into a json object.
row[0] is the "hid" on which the entire extraction is going to take place. row[1] and row[2] i.e chunk and has_space are assigned to the respective "hid"
This entire dictionary is then dumped into a json object using the following line of code :

		    j=json.dumps(data)
        
This was then written into a json file converted_json.json

<b>converted_json.json:- </b>
This file contains the json file created by csv_to_json. It has the following format :

		     {"hid":{"chunk":ABC, "has_space": XYZ}}

<b>app.py :- </b>
This is a flask file. I have loaded the json file converted_json.json from the previous step.
I have then created a route with both 'GET' and 'POST' methods.
I have made a function, that takes the input json object with "hid " and outputs the "chunk" and "has_space" of that respective "hid"

            data_ans = request.get_json()
            
This line takes the json parameter object which contains the hid given in POSTMAN
Then it searches for that "hid" in the Json object i.e the converted_json.json.
It searches for the record and sends the respective data i.e chunck and has_space in the variable "response"

<b>POSTMAN :-</b>
Postman is a popular API client that makes it easy for developers to create, share, test and document APIs. This is done by allowing users to create and save simple and complex HTTP/s requests, as well as read their responses. The result - more efficient and less tedious work.  

<b>Steps : </b>

1.	Open Postman
2.	Put the localhost (http://127.0.0.1:5000) with port number 5000 used by postman
3.	Changed the setting to ‘POST’
4.	Put the “hid” object, the parameter we need to find the result of.
5.	I also changed the format to JSON, under Body section. 
6.	Hit the Send button
<b>Output : </b>

      {
        "chunk": "Landmark Center, 8th Fl",
        "has_space": "0"
      }

<b>Screenshot: </b>

 	
