#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


class Phones(object):
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con
        pass

    def loadData(self):
        ls = []
        workSelect = "SELECT * FROM Phone"
        self.cur.execute(workSelect)
        for (id, number, idcontact) in self.cur:
            ls.append( (id, number, idcontact) )
        return ls

    def addData(self,data):
        addPhone = ("INSERT INTO Phone "
        "(number, idcontact)"
        "VALUES (%(number)s, %(idcontact)s)")
        self.cur.execute(addPhone, data)
        self.con.commit()

    def getContactName(self,id):
        getContact = ( " SELECT name FROM Contact WHERE id = " +str(id) )
        try:
            self.cur.execute(getContact)
            contactName = 0
            for name in self.cur:
                return name[0]
        except AttributeError:
            return None
        except Exception as e: 
            print(e) 
            return None


    def updateData(self,data,id):
        updatePhone = ("UPDATE Phone SET number = %(number)s WHERE id = " +str(id) + " " )
        self.cur.execute(updatePhone, data)
        self.con.commit()

    def delete(self,id):
        deleteWork = "DELETE FROM Phone WHERE id = " + str(id) + "  "
        self.cur.execute(deleteWork)
        self.con.commit()




        