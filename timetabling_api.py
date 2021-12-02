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
        parser = reqparse.RequestParser()   #initialization of the parser class
        parser.add_argument('classCode', required = True)  #adding an argument to the post request
        args = parser.parse_args()  #parsing arguments to the dictionary. 

        data = pd.read_csv('studentDetails.csv')    #reading the csv file
        #an exception for when the entered value aleady exists
        if args['classCode'] in list(data['classCode']):
            return{
                'message': f"'{args['classCode']}' already exists in the database."
            }, 401
        else:
            #if the entry is not already in the list, create it and add it.
            #creating a new dataframe containing the new values
            new_data = pd.DataFrame({
                'classCode': args['classCode']
            })        
            data = data.append(new_data, ignore_index=True) #adding the newly entered data
            data.to_csv('studentDetails.csv', index=True)
            return{'data': data.to_dict()}, 200

api.add_resource(Students, '/students') 

class Lessons(Resource):
    def get(self):
        data = pd.read_csv('timetable.csv') #read from the local timetable
        data = data.to_dict()   #converting the dataframe to a dictionary
        return{'data': data}, 200 
    
api.add_resource(Lessons, '/lessons') #'/lessons' is the entry point for Lessons

class Events(Resource):
    def get(self):
        data = pd.read_csv('events.csv')
        data = data.to_dict()
        return{'data': data.to_dict()}, 200

api.add_resource(Events, '/events')


#to test the api locally by running it on the Flask app
if __name__ == '__main__':
    app.run() 