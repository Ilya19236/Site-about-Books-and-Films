from Connection import *

class Title_repository:
    def __init__(self):
        self.__option = Options()

    def getTitle(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getTitle
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def addValuesInTitle(self, name, surname):
        connection = getConnection()
        cursor =  connection.cursor()
        cursor.execute(f"AddValuesInTitle {name}, {surname}")
        cursor.commit()
        connection.close()


    def updateTitle(self, id, name, surname):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"UpdateTitle {id}, {name}, {surname}")
        cursor.commit()
        connection.close()

    def deleteTitle(self, id):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"DeleteTitle {id}")
        cursor.commit()
        connection.close()

    def deleteTypeOfTitle(self, id):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"DeleteTypeOfTitle {id}")
        cursor.commit()
        connection.close()

    def getUnitsAndTitles(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getUnitsAndTitles
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def getUsersAndTitles(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getUsersAndTitles
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def getTitlesByUsers(self, typeoftitle):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUsers {typeoftitle}")
        result = cursor.fetchall()
        connection.close()
        return result

    def getTitlesByUser(self, id, typeoftitle):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUser {id}, {typeoftitle}")
        result = cursor.fetchall()
        connection.close()
        return result

    def getTitlesByUnits(self, types):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUnits {types}")
        result = cursor.fetchall()
        connection.close()
        return result

    def getTitlesByUnit(self, id, types):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetTitlesByUnit {id}, {types}")
        result = cursor.fetchall()
        connection.close()
        return result