import pyodbc


def sendQuery(query: str) -> str:
    #  Connect to DataBase
    connection = pyodbc.connect('Driver={SQL Server};'
                      'xxxxxxxxxxxxxxx;' # Server Name
                      'Database=xxxxxxx;' # Database Name
                      'Trusted_Connection=yes;')
    #  Create Cursor Object
    cursor = connection.cursor()
    #  Does the query if there is no duplicate
    try:
        #  Execute Query
        cursor.execute(query)
        #  Commit Query
        connection.commit()
        # Close The cursor Object
        cursor.close()
        # Close The connection
        connection.close()
        return ''
    #  Check if there is a duplicate
    except pyodbc.Error as e:
        error_message = str(e)
        data = (error_message[error_message.find("(", 2) + 1:error_message.find(")")])
        # Close The cursor Object
        cursor.close()
        # Close The connection
        connection.close()
        return data


def sendQueryReturn(query: str) -> str:
    #  Connect to DataBase
    connection = pyodbc.connect('Driver={SQL Server};'
                      'xxxxxxxxxxxxxxx;' # Server Name
                      'Database=xxxxxxx;' # Database Name
                      'Trusted_Connection=yes;')
    #  Create Cursor Object
    cursor = connection.cursor()
    #  Does the query if there is no duplicate
    try:
        #  Execute Query
        cursor.execute(query)
        row = cursor.fetchall()
        count = query.find(row[0][2])
        #  Commit Query
        connection.commit()
        # Close The cursor Object
        cursor.close()
        # Close The connection
        connection.close()
        if count > 0:
            return row[0][0]
        else:
            return ''
    #  Check if there is a duplicate
    except pyodbc.Error as e:
        error_message = str(e)
        data = (error_message[error_message.find("(", 2) + 1:error_message.find(")")])
        # Close The cursor Object
        cursor.close()
        # Close The connection
        connection.close()
        return data


