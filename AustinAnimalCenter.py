client = MongoClient('mongodb://localhost:47368') #use to get the database cursor

# To get data from a collection i.e to read data from a collection of this database

animal_data = client.animals.find( { } )