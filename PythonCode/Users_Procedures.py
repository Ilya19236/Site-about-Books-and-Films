import pyodbc

def GetUsers():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('GetUsers')
    result = cursor.fetchall()
    return result

def UpdateUser(Id, Name, Surname, Age):
    Id = Id
    Name = Name
    Surname = Surname
    Age = Age
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"UpdateUser {Id}, {Name}, {Surname}, {Age}"
    cursor.execute(query)
    connection.commit()
    connection.close()

def AddValuesInUser(Name, Surname, Age):
    Name = Name
    Surname = Surname
    Age = Age
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"AddValuesInUser {Name}, {Surname}, {Age}"
    cursor.execute(query)
    connection.commit()
    connection.close()

def DeleteUser(Id):
    Id = Id
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"DeleteUser {Id}"
    cursor.execute(query)
    connection.commit()
    connection.close()
