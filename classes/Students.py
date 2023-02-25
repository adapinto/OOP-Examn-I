from classes.DbMongo import DbMongo
from classes import DATA, Dataprocess

class Students:
    
    def __init__(self,nombre,edad,carrera,id=""):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        self.__id=id
        
    def save(self,db):
        collection=db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        
    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )
    
    @staticmethod
    def get_list(db):
        collection = db["student"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Students(
                e["nombre"]
                , e["telefono"]
                , e["_id"] 
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes
    
    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db) 
            
    @staticmethod
    def insert_data(db):
        collection=db["students"]
        collection.insert_many(DATA)