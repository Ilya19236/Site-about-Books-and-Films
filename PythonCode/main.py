from TitleProcedures import *
Titl = Title()

def AddValuesInTitle(name, surname):
    Titl.AddValuesInTitle(name, surname)
def UpdateTitle(id, name, surname, type):
    Titl.UpdateTitle(id, name, surname, type)
def DeleteTitle(id):
    Titl.DeleteTitle(id)
def DeleteTypeOfTitle(id):
    Titl.DeleteTypeOfTitle(id)

def GetTitle():
    return Titl.GetTitle()
def GetUnitsAndTitles():
    return Titl.GetUnitsAndTitles()
def GetUsersAndTitles():
    return Titl.GetUsersAndTitles()
def GetTitlesByUsers(typeoftitle):
    return Titl.GetTitlesByUsers(typeoftitle)
def GetTitlesByUser(id, typeoftitle):
    return Titl.GetTitlesByUser(id, typeoftitle)
def GetTitlesByUnits(types):
    return Titl.GetTitlesByUnits(types)
def GetTitlesByUnit(id, types):
    return Titl.GetTitlesByUnit(id, types)

print(GetTitlesByUnits(1))