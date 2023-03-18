import psycopg2


class DBConnector(object):
    host = None
    port = None
    database = None
    user = None
    password = None

    @classmethod
    def set_settings(cls, host='database', port='5432', database='production', user='user', password='password'):
        cls.host = host
        cls.port = port
        cls.database = database
        cls.user = user
        cls.password = password

    @classmethod
    def create_connection(cls):
        return psycopg2.connect(user=cls.user,
                                password=cls.password,
                                host=cls.host,
                                port=cls.port,
                                database=cls.database)


class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = DBConnector.create_connection()
        return cls.connection

    @classmethod
    def execute_query(cls, query):
        """execute query on singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

