from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:35872/AAC' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self,data):

        if data:      
            return self.database.animals.find(data,{"_id":False})
        else: 
            return self.database.animals.find( {} , {"_id":False})
        
# The method to implement the U in CRUD.
    def update(self, animal, save):
        updates = { "$set": save }
        if save is not None:
                saveResult = self.database.animals.update_one(animal, updates)
                return saveResult
        else:
            raise Exception("Nothing to update, because save parameter is None")
            
# The method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.delete_one(remove)
                return removeResult
        else:
            raise Exception("Nothing to delete, because remove parameter is None")
