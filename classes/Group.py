#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


class Groups(object):
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con
        pass

    def loadData(self):
        ls = []
        groupSelect = "SELECT * FROM Groups"
        self.cur.execute(groupSelect)
        for (id, typegroup, note) in self.cur:
            ls.append( (id, typegroup, note) )
        return ls

    def addData(self,data):
        addContact = ("INSERT INTO Groups "
        "(type, note)"
        "VALUES (%(type)s, %(note)s)")
        self.cur.execute(addContact, data)
        self.con.commit()

    def delete(self,id):
        deleteGroup = "DELETE FROM Groups WHERE id = " + str(id) + "  "
        self.cur.execute(deleteGroup)
        self.con.commit()

    def updateData(self,data,id):
        updateGroup = ("UPDATE Groups SET type = %(type)s, note = %(note)s WHERE id = " +str(id) + " " )
        try:
            self.cur.execute(updateGroup, data)
            self.con.commit()
        except AttributeError:
            return None

    def getGroupTypes(self):
        types = ("SELECT DISTINCT Groups.type FROM Groups")
        self.cur.execute(types)
        ls=[]
        for item in self.cur:
            ls.append(item[0])
        return ls

    def getGroupId(self,types):
        queryGetId = ( "SELECT id FROM Groups WHERE type = '"+str(types)+"' " )
        try:
            self.cur.execute(queryGetId)
            for i in self.cur:
                return i[0]
        except AttributeError:
            return None

    def getGroupType(self,id):
        type = ("SELECT DISTINCT Groups.type FROM Groups WHERE id = " +str(id))
        try:
            self.cur.execute(type)
            for item in self.cur:
                return item[0]
        except Exception as e: 
            print(e)
            return None




