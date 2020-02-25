#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

class DataBase(object):
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',database='phoneBook',user='vlad',password='1234')
        self.cursor = self.connection.cursor()
        pass

    # def connectionCLose(self):
    #     self.cursor.close()
    #     self.connection.close()

    # def __del__(self):
    #     self.cursor.close()
    #     self.connection.close()


