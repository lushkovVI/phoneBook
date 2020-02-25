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
import UI
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    db = database.DataBase()
    contacts = Contacts.Contacts(db.cursor,db.connection)
    groups = Group.Groups(db.cursor,db.connection)
    works = Works.Works(db.cursor,db.connection)
    phones = Phones.Phones(db.cursor,db.connection)
    groupcontact = GroupContact.GroupContact(db.cursor,db.connection)

    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI.Ui_Dialog(contacts,groups,phones,works,groupcontact)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
