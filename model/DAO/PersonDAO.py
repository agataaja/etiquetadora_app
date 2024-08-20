
from pymongo import MongoClient
from connection.db import DB

class PersonDAO:

    def insert(self, person):
        try:
            self.c = DB().create_db().persons
            self.person_id = self.c.insert_one(person).inserted_id
            print(self.person_id)
            print(DB().create_db().name) # nome do banco de dados

        except:
            print('Erro em realizar insert')

        else:
            print('Inserido com sucesso!')    
            # listando as coleções disponiveis
            print(DB().create_db().list_collection_names())
            
            # utilizando List Comprehension:
            person = [p for p in self.c.find()]
            print(person) 