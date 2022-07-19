
def CheckUser (username : str, password : str, cursor):
    '''
        Function to check if a user is registered in the database.
    '''
    
    try:
        cursor.execute(f"SELECT name, password FROM User WHERE name = '{username}'")
        queryResult = cursor.fetchone()
        if password == queryResult[1]:
            return True     # Return true if username and password are in database
        else:
            return False    # Return false if password not match

    except:
        return False        # Return false if username isn't in database


def CreateUser (username : str, password : str, cursor, con):
    '''
        Function to insert a new user to database.
    '''

    try:
        cursor.execute(f"INSERT INTO User (name, password) VALUES ('{username}', '{password}')")
        con.commit()
        return True         # Commit changes and return True
        
    except:
        return False        # Return false if username and password are invalid values