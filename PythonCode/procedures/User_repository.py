from Connection import *

class User_repository:
    def __init__(self):
        self.__option = Options()

    def getUsers(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getUsers
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def updateUser(self, Id, Name, Surname, Age):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"UpdateUser {Id}, {Name}, {Surname}, {Age}"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def addValuesInUser(self, Name, Surname, Age):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"AddValuesInUser {Name}, {Surname}, {Age}"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def deleteUser(self, Id):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"DeleteUser {Id}"
        cursor.execute(query)
        connection.commit()
        connection.close()