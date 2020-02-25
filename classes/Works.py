#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


class Works(object):
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con
        pass


    def loadData(self):
        ls = []
        workSelect = "SELECT * FROM Work"
        self.cur.execute(workSelect)
        for (id, post, companyname) in self.cur:
            ls.append( (id, post, companyname) )
        return ls
    

    def addData(self,data):
        addContact = ("INSERT INTO Work "
        "(post, companyname)"
        "VALUES (%(post)s, %(companyname)s)")
        self.cur.execute(addContact, data)
        self.con.commit()

    def getWorkPost(self):
        getPost = "SELECT DISTINCT post FROM Work"
        self.cur.execute(getPost)
        ls=[]
        for (item) in self.cur:
            ls.append(item[0])
        return ls

    def getWorkId(self,post):
        getId = "SELECT id FROM Work WHERE post = '" +str(post)+"'"
        try:
            self.cur.execute(getId)
            for (item) in self.cur:
                return item[0]
        except AttributeError:
            return None


    def delete(self,id):
        deleteWork = "DELETE FROM Work WHERE id = " + str(id) + "  "
        self.cur.execute(deleteWork)
        self.con.commit()

    def updateData(self,data,id):
        updateGroup = ("UPDATE Work SET post = %(post)s, companyname = %(companyname)s WHERE id = " +str(id) + " " )
        try:
            self.cur.execute(updateGroup, data)
            self.con.commit()
        except AttributeError:
            return None

        