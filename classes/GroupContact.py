#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


class GroupContact(object):
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con
        pass

    def loadData(self):
        ls = []
        loaddata = (" SELECT GroupsContacts.id,Contact.name,Groups.type FROM GroupsContacts "
        " JOIN Groups ON Groups.id = GroupsContacts.idgroup "
        " JOIN Contact ON Contact.id = GroupsContacts.idcontact ")
        self.cur.execute(loaddata)
        for ( id,contact, grouptype) in self.cur:
            ls.append( ( id,contact, grouptype) )
        return ls

    def AddData(self,data):
        addContact = ("INSERT INTO GroupsContacts "
        "(idcontact, idgroup)"
        "VALUES (%(idcontact)s, %(idgroup)s)")
        self.cur.execute(addContact, data)
        self.con.commit()

    def delete(self,id):
        deleteGroupContact = "DELETE FROM GroupsContacts WHERE id = " + str(id) + "  "
        self.cur.execute(deleteGroupContact)
        self.con.commit()

