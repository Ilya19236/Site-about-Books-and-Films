import pyodbc

def GetUnits():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('GetUnits')
    result = cursor.fetchall()
    return result

def GetUnitsByUser(Id, Type):
    Id = Id
    Type = Type
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(f"GetUnitsByUser {Id}, {Type}")
    result = cursor.fetchone()
    return result

def GetUnitsByUsers(Type):
    Type = Type
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(f"GetUnitsByUsers {Type}")
    result = cursor.fetchall()
    return result

def GetUnitsAndTitles():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('GetUnitsAndTitles')
    result = cursor.fetchall()
    return result

def GetPopularityOfUnit(Id):
    Id = Id
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(f"GetPopularityOfUnit {Id}")
    result = cursor.fetchall()
    return result

def GetPopularityOfUnits():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('GetUsers')
    result = cursor.fetchall()
    return result

def FullInformationAboutUnits():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('FullInformationAboutUnits')
    result = cursor.fetchall()
    return result

def FullInformationAboutUnit(Id):
    Id = Id
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(f"FullInformationAboutUnit {Id}")
    result = cursor.fetchall()
    return result

def AddValuesInUnit(Name,AgeRate,Description,TypeId):
    Name = Name
    AgeRate = AgeRate
    Description = Description
    TypeId = TypeId
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"AddValuesInUnit {Name}, {AgeRate}, {Description}, {TypeId}"
    cursor.execute(query)
    connection.commit()
    connection.close()

def UpdateUnit(Id,Name,AgeRate,Description,TypeId):
    Id = Id
    Name = Name
    AgeRate = AgeRate
    Description = Description
    TypeId = TypeId
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"UpdateUnit {Id},{Name},{AgeRate},{Description},{TypeId}"
    cursor.execute(query)
    connection.commit()
    connection.close()

def DeleteUnit(Id):
    Id = Id
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"DeleteUnit {Id}"
    cursor.execute(query)
    connection.commit()
    connection.close()

def DeleteTypeOfUnit(Id):
    Id = Id
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"DeleteTypeOfUnit {Id}"
    cursor.execute(query)
    connection.commit()
    connection.close()