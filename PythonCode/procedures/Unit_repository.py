from Connection import *

class Unit_repository:
    def __init__(self):
        self.__option = Options()

    def getUnits(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getUnits
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getUnitsByUser(self, Id, Type):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetUnitsByUser {Id}, {Type}")
        result = cursor.fetchone()
        return result

    def getUnitsByUsers(self, Type):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetUnitsByUsers {Type}")
        result = cursor.fetchall()
        return result

    def getUnitsAndTitles(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getUnitsAndTitles
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getPopularityOfUnit(self, Id):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"GetPopularityOfUnit {Id}")
        result = cursor.fetchall()
        return result

    def getPopularityOfUnits(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.getPopularityOfUnits
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def fullInformationAboutUnits(self):
        connection = getConnection()
        cursor = connection.cursor()
        query = self.__option.fullInformationAboutUnits
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def fullInformationAboutUnit(self, Id):
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"FullInformationAboutUnit {Id}")
        result = cursor.fetchall()
        return result

    def addValuesInUnit(self, Name,AgeRate,Description,TypeId):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"AddValuesInUnit {Name}, {AgeRate}, {Description}, {TypeId}"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def updateUnit(self, Id,Name,AgeRate,Description,TypeId):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"UpdateUnit {Id},{Name},{AgeRate},{Description},{TypeId}"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def deleteUnit(self, Id):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"DeleteUnit {Id}"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def deleteTypeOfUnit(self, Id):
        connection = getConnection()
        cursor = connection.cursor()
        query = f"DeleteTypeOfUnit {Id}"
        cursor.execute(query)
        connection.commit()
        connection.close()