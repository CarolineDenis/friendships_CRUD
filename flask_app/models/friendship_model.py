from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model 
from flask_app import DATABASE

class Friendship:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s,%(friend_id)s,NOW(),NOW())"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_friendships(cls):
        query = "SELECT users.first_name AS user_first_name, users.last_name AS user_last_name,  friend.first_name AS friend_first_name, friend.last_name AS friend_last_name, friendships.id, friendships.user_id, friendships.friend_id, friendships.created_at, friendships.updated_at FROM users LEFT JOIN friendships ON users.id = friendships.user_id LEFT JOIN users AS friend ON friend.id = friendships.friend_id;"
        results =  connectToMySQL(DATABASE).query_db(query)
        list_friendships =[]
        for b in results:
            one_friendship = cls(b)
            one_friendship.user = b['user_first_name']+ " " + b['user_last_name']
            one_friendship.friend_first_name = b['friend_first_name']
            one_friendship.friend_last_name = b['friend_last_name']
            list_friendships.append(one_friendship)
        return list_friendships
