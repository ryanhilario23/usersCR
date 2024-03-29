from mysqlconnection import connectToMySQL


class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all_users(cls):
        query = """
                SELECT *
                FROM users;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save_user(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s,%(email)s,NOW(),NOW())
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results