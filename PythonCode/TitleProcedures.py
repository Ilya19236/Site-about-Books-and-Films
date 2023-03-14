import pyodbc

class Title():
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=DATABASE;TRUSTED_CONNECTION=TRUE;'

    def GetTitle(self):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute("GetTitle")
        result = cursor.fetchall()
        connection.close()
        return result

    def AddValuesInTitle(self, name, surname):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor =  connection.cursor()
        cursor.execute(f"AddValuesInTitle {name}, {surname}")
        cursor.commit()
        connection.close()
        print("Changes commited")


    def UpdateTitle(self, id, name, surname, type):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"UpdateTitle {id}, {name}, {surname}, {type}")
        cursor.commit()
        connection.close()
        print("Changes applied")

    def DeleteTitle(self, id):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"DeleteTitle {id}")
        cursor.commit()
        connection.close()
        print(f"Title with id {id} removed")

    def DeleteTypeOfTitle(self, id):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"DeleteTypeOfTitle {id}")
        cursor.commit()
        connection.close()
        print("Changes applied")

    def GetUnitsAndTitles(self):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetUnitsAndTitles")
        result = cursor.fetchall()
        connection.close()
        return result

    def GetUsersAndTitles(self):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetUsersAndTitles")
        result = cursor.fetchall()
        connection.close()
        return result

    def GetTitlesByUsers(self, typeoftitle):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUsers {typeoftitle}")
        result = cursor.fetchall()
        connection.close()
        return result

    def GetTitlesByUser(self, id, typeoftitle):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUser {id}, {typeoftitle}")
        result = cursor.fetchall()
        connection.close()
        return result

    def GetTitlesByUnits(self, types):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUnits {types}")
        result = cursor.fetchall()
        connection.close()
        return result

    def GetTitlesByUnit(self, id, types):
        connection = pyodbc.connect(self.connection_string, timeout=500)
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUnit {id}, {types}")
        result = cursor.fetchall()
        connection.close()
        return result