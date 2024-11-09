from flask import jsonify, request
from models.Login import Login
from models.db_model import db_connection

db = db_connection.connect()
Login_model = Login(db)

def login_user():
    isLogin = request.get_json()
    login_id = Login_model.create_fornecedor(isLogin)
    return jsonify({"message": "Funcionario criado", "id": login_id}), 201
        
