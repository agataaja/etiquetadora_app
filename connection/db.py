
import datetime 
from pymongo import MongoClient


class DB:
    
    def create_conn(self):
        self.user = 'localhost'
        self.port = 27017
        self.conn = MongoClient(self.user, self.port)
        return self.conn

    def create_db(self):
        self.db = self.create_conn().cadastrodb # criando bd cadastrodb
        self.collection = self.db.cadastrodb
        return self.db



'''
# uma colecao é um grupo de documentos armazenados no MongoDB
# relativamente parecido com conceito de tabelas de banco de dados relacionais

collection = db.cadastrodb


person1 = {
    "nome": "Jefferson",
    "email": "jeff@test.com",
    "senha": "teste1234"
}


print(db.name) # nome do banco de dados

print(db.list_collection_names()) # listando as coleções disponiveis

# utilizando List Comprehension:
person = [p for p in collection.find()]

print(person)

print(collection.find_one({"nome": "J"}))
'''
