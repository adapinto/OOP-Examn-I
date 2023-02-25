class Enrollments:
    
    def __init__(self,curso,alumno,estado,id=""):
        self.curso=curso
        self.alumno=alumno
        self.estado=estado
        self.__id=id
        
    def save(self,db):
        collection=db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id