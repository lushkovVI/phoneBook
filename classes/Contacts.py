#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

class Contacts(object):
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con
        pass

 

    def loadData(self):
        ls = []
        contactSelect = ("SELECT Contact.id,Contact.name,Work.post,Contact.mail,Contact.blacklist FROM Contact "
        " JOIN Work ON Contact.idwork = Work.id ")
        self.cur.execute(contactSelect)
        for (id, name, work,mail,blacklist) in self.cur:
            ls.append( (id, name, work,mail,blacklist) )
        return ls



    def updateContact(self,data,id):
        updateContact = "UPDATE Work SET idwork = %(idwork)s, name = %(name)s, mail = %(mail)s, blacklist = %(blacklist)s WHERE id = " +str(id) + " "
        try:
            self.cur.execute(updateContact,data)
            self.con.commit()
        except AttributeError:
            return None
        except TypeError:
            return None
        

    def addData(self,data):
        addContact = ("INSERT INTO Contact "
        "(idwork, name, mail, blacklist) "
        "VALUES (%(idwork)s, %(name)s, %(mail)s, %(blacklist)s)")
        self.cur.execute(addContact, data)
        self.update()


    def delete(self,id):
        deleteContact = "DELETE FROM Contact WHERE id = " + str(id) + "  "
        self.cur.execute(deleteContact)
        self.update()



    def getcontactNames(self):
        getNames = ("SELECT name FROM Contact")
        self.cur.execute(getNames)
        nameslist=[]
    
        for (name) in self.cur:
            nameslist.append( str(name[0]))
        return nameslist

    def getContactId(self,name):
        queryGetId = ( "SELECT id FROM Contact WHERE name = '"+str(name)+"' " )
        try:
            self.cur.execute(queryGetId)
            getid = -1
            for i in self.cur:
                return i[0]
        except AttributeError:
            return None

    def getcontactName(self,id):
        getName = ("SELECT name FROM Contact WHERE id = "+str(id))
        self.cur.execute(getName)
        for (name) in self.cur:
            return name[0]


    def findName(self,name):
        #,"Groups.type"
        query = ("Phone.number","Work.post")
        buf = ""
        for item in query:
            buf += item + "\n"
            self.cur.execute( self.setQueryName(item,name) )
            for i in self.cur:
                buf += str(i)
            buf += "\n"
        self.cur.execute( self.setQueryNameGroup(name) )
        buf+="Group.type\n"
        for i in self.cur:
            buf += str(i)
            buf += "\n"
        return buf

    def setQueryName(self,column , search):
        query =  ("SELECT  DISTINCT " +column+" "
        " FROM Contact "
        " JOIN Work ON Contact.idwork = Work.id "
        " JOIN Phone ON Contact.id = Phone.idcontact "
        " WHERE Contact.name = '"+search+"'")
        return query

    def setQueryNameGroup(self , search):
        query =  ("SELECT  DISTINCT  Groups.type "
        " FROM GroupsContacts "
        " JOIN Groups ON Groups.id = GroupsContacts.idgroup "
        " JOIN Contact ON Contact.id = GroupsContacts.idcontact "
        " JOIN Phone ON Contact.id = Phone.idcontact "
        " WHERE Contact.name = '"+search +"' ")
        return query


    



    def FindPhone(self,number):
        # ,"Groups.type"
        query = ("Contact.name","Work.post")
        buf = ""
        for item in query:
            buf += item + "\n"
            self.cur.execute( self.setQueryPhone(item,number) )
            for i in self.cur:
                buf += str(i)
            buf += "\n"
        self.cur.execute( self.setQueryPhoneGroup(number ))
        buf+="Group.type\n"
        for i in self.cur:
            buf += str(i)
            buf += "\n"
        return buf


    def setQueryPhone(self,column , search):
        query =  ("SELECT  DISTINCT " +column+" "
        " FROM Contact "
        " JOIN Work ON Contact.idwork = Work.id "
        " JOIN Phone ON Contact.id = Phone.idcontact "
        " WHERE Phone.number = '"+search+"'")
        return query

    def setQueryPhoneGroup(self,search):
        query =  ("SELECT  DISTINCT Groups.type "
        " FROM GroupsContacts "
        " JOIN Groups ON Groups.id = GroupsContacts.idgroup "
        " JOIN Contact ON Contact.id = GroupsContacts.idcontact "
        " JOIN Phone ON Phone.idcontact = Contact.id "
        " WHERE Phone.number = '"+search+"'")
        return query
    
    def update(self):
        self.con.commit()
