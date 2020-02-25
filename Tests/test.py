#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/vlad/phoneBook/classes")
sys.path.insert(0, "/home/vlad/phoneBook/UI")
import database
import Contacts
import Group
import Works
import Phones
import GroupContact
import pytest


db = database.DataBase()
contacts = Contacts.Contacts(db.cursor,db.connection)
groups = Group.Groups(db.cursor,db.connection)
works = Works.Works(db.cursor,db.connection)
phones = Phones.Phones(db.cursor,db.connection)
groupcontact = GroupContact.GroupContact(db.cursor,db.connection)

@pytest.fixture()
def a_list():
    return 

def testContactId():
    names = ['Vlad','ivan','Andrew','dennis']
    for name in names:
        id = contacts.getContactId(name)
        from_db = contacts.getcontactName(id)
        assert equivalent(from_db, name)


#@pytest.mark.xfail()
def testGroupId():
    types = ['Work1','Work2','Educational','holydays']
    for typ in types:
        id = groups.getGroupId(typ)
        from_db = groups.getGroupType(id)
        assert equivalent(from_db, typ)


def equivalent(t1, t2):
    return ((t1 == t2))
   


def testGetGroupId():
    assert groups.getGroupId("hjhj") == None
    assert groups.getGroupId(9999999) == None
    assert groups.getGroupId(False) == None
    
def testGetName():
    assert phones.getContactName(999) == None
    assert phones.getContactName(-2) == None
    assert phones.getContactName(False) == None
    assert phones.getContactName("er3efr") == None

def testGetWorkId():
    assert works.getWorkId("ds") == None
    assert works.getWorkId(8888999) == None


def testGetContactId():
    assert contacts.getContactId("cc") == None
    assert contacts.getContactId(9999999) == None











