import sqlite3
import os

# PATH to the database folder where our database is saved
PATH = 'database/database.db'

def create_db():
    '''
    Create the database located at the above PATH with
    2 tables: users and messages. If the database is allready
    created it will print an appropiate message.

    The user table contains: id of type int which autoincrements,
    name of type string max 255 characters, password of type string
    max 255 characters, is_admin of type boolean.

    The message table contains: id of type int which autoincrements,
    user_id of type int which corresponds with an id from the users table,
    content of type string max 1023 characters.
    '''

    if os.path.exists(PATH):
        print("Database exists. Skipping...")
    else:
        dbConnection = sqlite3.connect(PATH)
        cursor = dbConnection.cursor()

        SQL_CREATE_USER_TABLE = """
            CREATE TABLE users(
                id INTEGER PRIMARY KEY NOT NULL,
                name varchar(255) NOT NULL,
                password varchar(255) NOT NULL,
                is_admin BOOL
            );
        """

        SQL_CREATE_MSG_TABLE = """
            CREATE TABLE messages(
                id INTEGER PRIMARY KEY NOT NULL,
                user_id INTEGER NOT NULL,
                content varchar(1023)
            );
        """

        # Create the users table
        cursor.execute(SQL_CREATE_USER_TABLE)
        dbConnection.commit()

        # Create the messages table
        cursor.execute(SQL_CREATE_MSG_TABLE)
        dbConnection.commit()

        # Close the conection
        dbConnection.close()

def get_connection():
    return sqlite3.connect(PATH)

def insert_user(user_name:str, password:str, is_admin:bool) -> bool:
    '''
    This function inserts into the users table an user with the given
    parameters.

    @param user_name the corresponding username
    @param password the corresponding password
    @param is_admin if the user is an admin or not
    '''
    dbConnection = sqlite3.connect(PATH)
    cursor = dbConnection.cursor()
    
    # Verify if the user exists
    user = get_user(user_name, password)
    if user != None:
        return False

    # Insert the user
    INSERT_QUERRY = f"""
        INSERT INTO users (name, password, is_admin)
        VALUES ("{user_name}", "{password}", {is_admin});
    """

    cursor.execute(INSERT_QUERRY)
    dbConnection.commit()

    dbConnection.close()
    return True

def get_user(user_name:str, password:str) -> tuple:
    '''
    This function returns the user with the given name and
    password. If no name was matched in the database it returns
    None.

    @param user_name a string for the user you want to get
    @param password a string for the user's password
    @return a tuple with the user's data (id:int, name:str, password:str, is_admin:bool)
    '''
    dbConnection = sqlite3.connect(PATH)
    cursor = dbConnection.cursor()

    SELECT_QUERRY = f'''
        SELECT * FROM users WHERE name="{user_name}" AND password="{password}";
    '''

    cursor.execute(SELECT_QUERRY)
    answer = cursor.fetchone()
    dbConnection.commit()

    dbConnection.close()
    
    return answer

def insert_msg(user_id:int, content:str):
    '''
    Insert a message of the user with the given id into the database.

    @param user_id: the id of the user that sent the message
    @param content: the content of the message
    '''
    dbConnection = sqlite3.connect(PATH)
    cursor = dbConnection.cursor()

    INSERT_QUERRY = f'''
        INSERT INTO messages (user_id, content)
        VALUES ({user_id}, "{content}");
    '''

    cursor.execute(INSERT_QUERRY)
    dbConnection.commit()

    dbConnection.close()

def get_msg(user_id:int, content:str) -> list:
    '''
    Get the messages with the given user_id and content.

    @param user_id: the user that sent the message
    @param content: the content of the message
    @return: a list with all the messages that match the user_id
    and the content
    '''
    dbConnection = sqlite3.connect()
    cursor = dbConnection.cursor()

    SELECT_QUERRY = f'''
        SELECT * FROM messages
        WHERE user_id={user_id} AND content="{content}";
    '''
    cursor.execute(SELECT_QUERRY)
    dbConnection.commit()
    answer = cursor.fetchall()

    dbConnection.close()

    return answer
