from classes.DbMongo import DbMongo
from pymongo import MongoClient

class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self,nombre,id):
        return nombre, id
    def create_courses(self,nombre,id):
        return nombre,id
    def create_students(self,nombre,edad, carrera,cursos,id):
        return nombre,edad, carrera,cursos,id
    def create_enrollments(self,alumno,curso,estado):
        return alumno,curso,estado