from bson import ObjectId

#h5FUTkH8SjnZaBRH

class Login:
    def __init__(self, db):
        self.collection = db['Funcionario']

    def create_fornecedor(self, fornecedor_data):
        result = self.collection.insert_one(fornecedor_data)
        return str(result.inserted_id)