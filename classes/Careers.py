
class Careers:
    
    def __init__ (self,nombre,id=""):
        self.nombre=nombre
        self.__id=id
        
    def save(self,db):
        collection=db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        