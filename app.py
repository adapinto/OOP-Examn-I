import pymongo
from pymongo import MongoClient
from classes import DATA, Dataprocess, Students, data,DbMongo
from dotenv import load_dotenv


def main():
    store, db =DbMongo.getDB()
    
    pipeline = Dataprocess(DATA)
    
    
    Students.insert_data(db,DATA)

    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()

    return True

if __name__ == "__main__":
    main()