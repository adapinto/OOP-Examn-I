import pymongo
import os
from classes import DATA, Dataprocess,

class DbMongo:
        
   @staticmethod
   def getDB():
       user = os.environ['USERMONGO']
       password = os.environ['PASSWORDMONGO']
       cluster = os.environ['CLUSTER']
       query_string = 'retryWrites=true&w=majority'
         
    ## Connection String
       uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
             user
           , password
           , cluster
           , query_string
       )
   
       student=pymongo.MongoClient(uri)
       db=student[os.environ['DB']]
       
       
       
       
       
       return student, db
     
     
@staticmethod
def insert_data(db):
   collection=db.students
   collection.insert_many(DATA)