from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship_model 
from flask_app import DATABASE

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,NOW(),NOW())"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results =  connectToMySQL(DATABASE).query_db(query)
        new_list_name =[]
        for b in results:
            new_list_name.append(cls(b))
        return new_list_name
