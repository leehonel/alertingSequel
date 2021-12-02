#modules to initialize the API
#the API will run on two endpoints: 
#   Students - to get the user's course code
#   Lessons - to access the timetable details for which the alerts will be sent
#with the two endpoints, if the API is located at www.api.com
# comm. with the Students and Lessons classes will be at 
# www.api.com/students and www.api.com/classes respectively. 

from flask import Flask, app
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
#from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

#To create an endpoint, define a Python class with the name 
#you want and connect it to the desired endpoint. 
#we pass 'Resource' with the class definition for Flask to know that this is an endpoint. 
class Students(Resource):
    #using the GET method, we return the data stored in the specified file
    def get(self):
        data = pd.read_csv('studentDetails.csv')    #reading the csv file
        data = data.to_dict()   #converting the dataframe to a dictionary
        return{'data': data}, 200   #return the data along with the HTTP OK code
    
    def post(self):
        """post student class code to the db"""
        parser = reqparse.RequestParser()
        #making required=True means that the argument is necessary in the post request
        parser.add_argument('class_code', required = True)

        args = parser.parse_args()

          #read from the saved class codes
        data = pd.read_json('classCodes.json')
        
        new_data = pd.DataFrame({
            'class_code': args['class_code']
        })
      
        #add the newly provided class code
        data = data.append(new_data, ignore_index=True)
        #save back to the file
        data.to_json('classCodes.json', index=False)
        #return the entered data
        return {'data': data.to_dict()}, 200


api.add_resource(Students, '/students') 



class Lessons(Resource):
    def get(self):
        data = pd.read_json('timetable2.json') #read from the local timetable
        data = data.to_dict()   #converting the dataframe to a dictionary
        return{'data': data}, 200 
    
api.add_resource(Lessons, '/lessons') #'/lessons' is the entry point for Lessons

class Events(Resource):
    def get(self):
        data = pd.read_json('events.json')
        data = data.to_dict()
        return{'data': data}, 200

api.add_resource(Events, '/events')


#to test the api locally by running it on the Flask app
if __name__ == '__main__':
    app.run() 