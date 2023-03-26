import pyodbc
from Option import *

def getConnection():
    option = Options()
    connection = pyodbc.connect(option.connection_string)
    return connection
