# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import sys


class Ui_Dialog(object):
    def __init__(self,contactClass,groupClass,phoneClass,workClass,groupcontactClass):
        self.contactClass = contactClass
        self.groupClass = groupClass
        self.phoneClass = phoneClass
        self.workClass = workClass
        self.groupcontactClass = groupcontactClass

        self.pickedIdGroup = None
        self.pickedRowGroup = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(926, 843)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 901, 751))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        #contact
        self.tableWidget_contact = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_contact.setGeometry(QtCore.QRect(20, 10, 861, 421))
        self.tableWidget_contact.setRowCount(0)
        self.tableWidget_contact.setColumnCount(6)
        self.tableWidget_contact.setObjectName("tableWidget_contact")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_contact.setHorizontalHeaderItem(5, item)
        self.tableWidget_contact.horizontalHeader().setDefaultSectionSize(141)
        self.lineEdit_name_contact = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_name_contact.setGeometry(QtCore.QRect(20, 480, 161, 25))
        self.lineEdit_name_contact.setObjectName("lineEdit_name_contact")
        self.label_name_contact = QtWidgets.QLabel(self.tab_2)
        self.label_name_contact.setGeometry(QtCore.QRect(60, 450, 67, 17))
        self.label_name_contact.setObjectName("label_name_contact")
        self.label_work_contact = QtWidgets.QLabel(self.tab_2)
        self.label_work_contact.setGeometry(QtCore.QRect(270, 450, 67, 17))
        self.label_work_contact.setObjectName("label_work_contact")
        self.lineEdit_mail_contact = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_mail_contact.setGeometry(QtCore.QRect(420, 480, 161, 25))
        self.lineEdit_mail_contact.setObjectName("lineEdit_mail_contact")
        self.label_mail_contact = QtWidgets.QLabel(self.tab_2)
        self.label_mail_contact.setGeometry(QtCore.QRect(460, 450, 67, 17))
        self.label_mail_contact.setObjectName("label_mail_contact")
        self.lineEdit_blacklist_contact = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_blacklist_contact.setGeometry(QtCore.QRect(620, 480, 161, 25))
        self.lineEdit_blacklist_contact.setObjectName("lineEdit_blacklist_contact")
        self.label_blacklist_contact = QtWidgets.QLabel(self.tab_2)
        self.label_blacklist_contact.setGeometry(QtCore.QRect(660, 450, 67, 17))
        self.label_blacklist_contact.setObjectName("label_blacklist_contact")
        self.comboBox_work_contact = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_work_contact.setGeometry(QtCore.QRect(220, 480, 161, 25))
        self.comboBox_work_contact.setObjectName("comboBox_work_contact")
        self.pushButton_save_contact = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_save_contact.setGeometry(QtCore.QRect(20, 530, 89, 25))
        self.pushButton_save_contact.setObjectName("pushButton_save_contact")
        self.pushButton_delete_contact = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_delete_contact.setGeometry(QtCore.QRect(130, 530, 89, 25))
        self.pushButton_delete_contact.setObjectName("pushButton_delete_contact")
        self.pushButton_update_contact = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_update_contact.setGeometry(QtCore.QRect(20, 580, 89, 25))
        self.pushButton_update_contact.setObjectName("pushButton_update_contact")
        self.pushButton_loaddata_contact = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_loaddata_contact.setGeometry(QtCore.QRect(20, 630, 141, 25))
        self.pushButton_loaddata_contact.setObjectName("pushButton_loaddata_contact")

        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(250, 530, 300, 110))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(560, 530, 300, 110))
        self.textEdit_2.setObjectName("textEdit_2")


        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")



        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFindName = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonFindName.setGeometry(QtCore.QRect(250, 670, 121, 41))
        self.pushButtonFindName.setFont(font)
        self.pushButtonFindName.setObjectName("pushButtonFindName")

        self.lineEditFindName = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditFindName.setGeometry(QtCore.QRect(250, 640, 151, 25))
        self.lineEditFindName.setObjectName("lineEditFindName")
        self.pushButtonFindNumber = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonFindNumber.setGeometry(QtCore.QRect(530, 670, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFindNumber.setFont(font)
        self.pushButtonFindNumber.setObjectName("pushButtonFindNumber")
        self.lineEditFindNumber = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditFindNumber.setGeometry(QtCore.QRect(520, 640, 151, 25))
        self.lineEditFindNumber.setObjectName("lineEditFindNumber")












        ## work
        self.tableWidget_work = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_work.setGeometry(QtCore.QRect(20, 10, 441, 431))
        self.tableWidget_work.setRowCount(0)
        self.tableWidget_work.setColumnCount(3)
        self.tableWidget_work.setObjectName("tableWidget_work")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_work.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_work.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_work.setHorizontalHeaderItem(2, item)
        self.tableWidget_work.horizontalHeader().setDefaultSectionSize(141)
        self.lineEdit_post_work = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_post_work.setGeometry(QtCore.QRect(480, 40, 181, 25))
        self.lineEdit_post_work.setObjectName("lineEdit_post_work")
        self.lineEdit_companyname_work = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_companyname_work.setGeometry(QtCore.QRect(480, 90, 181, 25))
        self.lineEdit_companyname_work.setObjectName("lineEdit_companyname_work")
        self.label_post_work = QtWidgets.QLabel(self.tab_4)
        self.label_post_work.setGeometry(QtCore.QRect(480, 10, 67, 17))
        self.label_post_work.setObjectName("label_post_work")
        self.label__companyname_work = QtWidgets.QLabel(self.tab_4)
        self.label__companyname_work.setGeometry(QtCore.QRect(480, 70, 111, 17))
        self.label__companyname_work.setObjectName("label__companyname_work")
        self.pushButton_save_work = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_save_work.setGeometry(QtCore.QRect(480, 140, 89, 25))
        self.pushButton_save_work.setObjectName("pushButton_save_work")
        self.pushButton_delete_work = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_delete_work.setGeometry(QtCore.QRect(480, 180, 89, 25))
        self.pushButton_delete_work.setObjectName("pushButton_delete_work")
        self.pushButton_update_work = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_update_work.setGeometry(QtCore.QRect(480, 220, 89, 25))
        self.pushButton_update_work.setObjectName("pushButton_update_work")
        self.pushButton_loaddata_work = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_loaddata_work.setGeometry(QtCore.QRect(480, 260, 141, 25))
        self.pushButton_loaddata_work.setObjectName("pushButton_loaddata_work")
        ## work


        # groups
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_groups = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_groups.setGeometry(QtCore.QRect(20, 10, 441, 431))
        self.tableWidget_groups.setRowCount(0)
        self.tableWidget_groups.setColumnCount(3)
        self.tableWidget_groups.setObjectName("tableWidget_groups")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groups.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groups.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groups.setHorizontalHeaderItem(2, item)
        self.tableWidget_groups.horizontalHeader().setDefaultSectionSize(141)
        self.pushButton_save_groups = QtWidgets.QPushButton(self.tab)
        self.pushButton_save_groups.setGeometry(QtCore.QRect(480, 140, 89, 25))
        self.pushButton_save_groups.setObjectName("pushButton_save_groups")
        self.pushButton_delete_groups = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete_groups.setGeometry(QtCore.QRect(480, 180, 89, 25))
        self.pushButton_delete_groups.setObjectName("pushButton_delete_groups")
        self.lineEdit_type_groups = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_type_groups.setGeometry(QtCore.QRect(480, 40, 181, 25))
        self.lineEdit_type_groups.setObjectName("lineEdit_type_groups")
        self.pushButton_update_groups = QtWidgets.QPushButton(self.tab)
        self.pushButton_update_groups.setGeometry(QtCore.QRect(480, 220, 89, 25))
        self.pushButton_update_groups.setObjectName("pushButton_update_groups")
        self.label_type_groups = QtWidgets.QLabel(self.tab)
        self.label_type_groups.setGeometry(QtCore.QRect(480, 10, 67, 17))
        self.label_type_groups.setObjectName("label_type_groups")
        self.pushButton_loaddata_groups = QtWidgets.QPushButton(self.tab)
        self.pushButton_loaddata_groups.setGeometry(QtCore.QRect(480, 260, 141, 25))
        self.pushButton_loaddata_groups.setObjectName("pushButton_loaddata_groups")
        self.label__note_groups = QtWidgets.QLabel(self.tab)
        self.label__note_groups.setGeometry(QtCore.QRect(480, 70, 111, 17))
        self.label__note_groups.setObjectName("label__note_groups")
        self.lineEdit_note_groups = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_note_groups.setGeometry(QtCore.QRect(480, 90, 181, 25))
        self.lineEdit_note_groups.setObjectName("lineEdit_note_groups")
        # groups

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        # phone
        self.pushButton_loaddata_phone = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_loaddata_phone.setGeometry(QtCore.QRect(480, 260, 141, 25))
        self.pushButton_loaddata_phone.setObjectName("pushButton_loaddata_phone")
        self.pushButton_save_phone = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_save_phone.setGeometry(QtCore.QRect(480, 140, 89, 25))
        self.pushButton_save_phone.setObjectName("pushButton_save_phone")
        self.label__note_groups_2 = QtWidgets.QLabel(self.tab_3)
        self.label__note_groups_2.setGeometry(QtCore.QRect(480, 70, 111, 17))
        self.label__note_groups_2.setObjectName("label__note_groups_2")
        self.pushButton_delete_phone = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_delete_phone.setGeometry(QtCore.QRect(480, 180, 89, 25))
        self.pushButton_delete_phone.setObjectName("pushButton_delete_phone")
        self.tableWidget_phone = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_phone.setGeometry(QtCore.QRect(20, 10, 441, 431))
        self.tableWidget_phone.setRowCount(0)
        self.tableWidget_phone.setColumnCount(3)
        self.tableWidget_phone.setObjectName("tableWidget_phone")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_phone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_phone.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_phone.setHorizontalHeaderItem(2, item)
        self.tableWidget_phone.horizontalHeader().setDefaultSectionSize(141)
        self.label_number_phone = QtWidgets.QLabel(self.tab_3)
        self.label_number_phone.setGeometry(QtCore.QRect(480, 10, 67, 17))
        self.label_number_phone.setObjectName("label_number_phone")
        self.lineEdit_number_phone = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_number_phone.setGeometry(QtCore.QRect(480, 40, 181, 25))
        self.lineEdit_number_phone.setObjectName("lineEdit_number_phone")
        self.pushButton_update_phone = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_update_phone.setGeometry(QtCore.QRect(480, 220, 89, 25))
        self.pushButton_update_phone.setObjectName("pushButton_update_phone")
        self.comboBox_contactid_phone = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_contactid_phone.setGeometry(QtCore.QRect(480, 90, 181, 25))
        self.comboBox_contactid_phone.setObjectName("comboBox_contactid_phone")
        self.tabWidget.addTab(self.tab_3, "")


        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_groupcontact = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_groupcontact.setGeometry(QtCore.QRect(20, 20, 441, 431))
        self.tableWidget_groupcontact.setRowCount(0)
        self.tableWidget_groupcontact.setColumnCount(3)
        self.tableWidget_groupcontact.setObjectName("tableWidget_groupcontact")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groupcontact.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groupcontact.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_groupcontact.setHorizontalHeaderItem(2, item)
        self.tableWidget_groupcontact.horizontalHeader().setDefaultSectionSize(141)
        self.comboBox_group_groupcontact = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_group_groupcontact.setGeometry(QtCore.QRect(500, 50, 181, 25))
        self.comboBox_group_groupcontact.setObjectName("comboBox_group_groupcontact")
        self.label__group_groupcontact = QtWidgets.QLabel(self.tab_5)
        self.label__group_groupcontact.setGeometry(QtCore.QRect(500, 30, 111, 17))
        self.label__group_groupcontact.setObjectName("label__group_groupcontact")
        self.comboBox_contact_groupcontact = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_contact_groupcontact.setGeometry(QtCore.QRect(500, 200, 181, 25))
        self.comboBox_contact_groupcontact.setObjectName("comboBox_contact_groupcontact")
        self.label__contact_groupcontact = QtWidgets.QLabel(self.tab_5)
        self.label__contact_groupcontact.setGeometry(QtCore.QRect(500, 180, 111, 17))
        self.label__contact_groupcontact.setObjectName("label__contact_groupcontact")
        self.pushButton_save_groupcontact = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_save_groupcontact.setGeometry(QtCore.QRect(500, 280, 89, 25))
        self.pushButton_save_groupcontact.setObjectName("pushButton_save_groupcontact")
        self.pushButton_delete_groupcontact = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_delete_groupcontact.setGeometry(QtCore.QRect(500, 340, 89, 25))
        self.pushButton_delete_groupcontact.setObjectName("pushButton_delete_groupcontact")
        self.pushButton_load_groupcontact = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_load_groupcontact.setGeometry(QtCore.QRect(500, 400, 89, 25))
        self.pushButton_load_groupcontact.setObjectName("pushButton_load_groupcontact")
        self.tabWidget.addTab(self.tab_5, "")




        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Phonebook"))

        ## Contanct
        item = self.tableWidget_contact.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "idcontact"))
        item = self.tableWidget_contact.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "name"))
        item = self.tableWidget_contact.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "work"))
        item = self.tableWidget_contact.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "mail"))
        item = self.tableWidget_contact.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "blacklist"))
        self.label_name_contact.setText(_translate("Dialog", "Name"))
        self.label_work_contact.setText(_translate("Dialog", "Work"))
        self.label_mail_contact.setText(_translate("Dialog", "Mail"))
        self.label_blacklist_contact.setText(_translate("Dialog", "Blacklist"))
        self.pushButton_save_contact.setText(_translate("Dialog", "Save"))
        self.pushButton_delete_contact.setText(_translate("Dialog", "Delete"))
        self.pushButton_update_contact.setText(_translate("Dialog", "Update"))
        self.pushButton_loaddata_contact.setText(_translate("Dialog", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Contact"))


        self.pushButtonFindName.setText(_translate("Dialog", "Find name"))
        self.pushButtonFindNumber.setText(_translate("Dialog", "Find number"))

        ### WORK
        item = self.tableWidget_work.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "idwork"))
        item = self.tableWidget_work.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "post"))
        item = self.tableWidget_work.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "company name"))

        
        self.label_post_work.setText(_translate("Dialog", "Post"))
        self.label__companyname_work.setText(_translate("Dialog", "Company name"))
        self.pushButton_save_work.setText(_translate("Dialog", "Save"))
        self.pushButton_delete_work.setText(_translate("Dialog", "Delete"))
        self.pushButton_update_work.setText(_translate("Dialog", "Update"))
        self.pushButton_loaddata_work.setText(_translate("Dialog", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Work"))

        ### Groups
        item = self.tableWidget_groups.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "idgroup"))
        item = self.tableWidget_groups.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "type"))
        item = self.tableWidget_groups.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "note"))
        self.pushButton_save_groups.setText(_translate("Dialog", "Save"))
        self.pushButton_delete_groups.setText(_translate("Dialog", "Delete"))
        self.pushButton_update_groups.setText(_translate("Dialog", "Update"))
        self.label_type_groups.setText(_translate("Dialog", "Type"))
        self.pushButton_loaddata_groups.setText(_translate("Dialog", "Load Data"))

        self.label__note_groups.setText(_translate("Dialog", "Note"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Groups"))
        self.pushButton_loaddata_phone.setText(_translate("Dialog", "Load Data"))
        self.pushButton_save_phone.setText(_translate("Dialog", "Save"))
        self.label__note_groups_2.setText(_translate("Dialog", "Contact"))
        self.pushButton_delete_phone.setText(_translate("Dialog", "Delete"))
        item = self.tableWidget_phone.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "idphone"))
        item = self.tableWidget_phone.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "number"))
        item = self.tableWidget_phone.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Contact"))
        self.label_number_phone.setText(_translate("Dialog", "Number"))
        self.pushButton_update_phone.setText(_translate("Dialog", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Phone"))

        item = self.tableWidget_groupcontact.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.tableWidget_groupcontact.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "idcontact"))
        item = self.tableWidget_groupcontact.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "idgroup"))
        self.label__group_groupcontact.setText(_translate("Dialog", "group"))
        self.label__contact_groupcontact.setText(_translate("Dialog", "Contact"))
        self.pushButton_save_groupcontact.setText(_translate("Dialog", "Save"))
        self.pushButton_delete_groupcontact.setText(_translate("Dialog", "delete"))
        self.pushButton_load_groupcontact.setText(_translate("Dialog", "Load data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "groupcontact"))

        ## init events
        self.initEvents()
        



    def initEvents(self):
        #group
        self.pushButton_loaddata_groups.clicked.connect(self.buttonClickedLoadDataGroups)
        self.pushButton_delete_groups.clicked.connect(self.buttonClickedDeleteDataGroups)
        self.pushButton_save_groups.clicked.connect(self.buttonClickedAddDataGroups)
        self.pushButton_update_groups.clicked.connect(self.buttonClickedUpdateDataGroups)

        # work
        self.pushButton_loaddata_work.clicked.connect(self.buttonClickedLoadDataWork)
        self.pushButton_delete_work.clicked.connect(self.buttonClickedDeleteDataWork)
        self.pushButton_save_work.clicked.connect(self.buttonClickedAddDataWork)
        self.pushButton_update_work.clicked.connect(self.buttonClickedUpdateDataWork)

        # phone
        self.pushButton_loaddata_phone.clicked.connect(self.buttonClickedLoadDataPhone)
        self.pushButton_update_phone.clicked.connect(self.buttonClickedUpdateDataPhone)
        self.pushButton_save_phone.clicked.connect(self.buttonClickedSaveDataPhone)
        self.pushButton_delete_phone.clicked.connect(self.buttonClickedDeleteDataPhone)

        # contact
        self.pushButtonFindName.clicked.connect(self.buttonClickedFindName)
        self.pushButtonFindNumber.clicked.connect(self.buttonClickedFindNumber)

        self.pushButton_loaddata_contact.clicked.connect(self.buttonClickedLoadDataContact)
        self.pushButton_save_contact.clicked.connect(self.buttonClickedSaveDataContact)
        self.pushButton_delete_contact.clicked.connect(self.buttonClickedDeleteContact)
        self.pushButton_update_contact.clicked.connect(self.buttonClickedUpdateContact)

        # groupcontact
        self.pushButton_load_groupcontact.clicked.connect(self.buttonClickedLoadGroupContact)
        self.pushButton_save_groupcontact.clicked.connect(self.buttonClickedSaveDataGroupContact)

        self.pushButton_delete_groupcontact.clicked.connect(self.buttonClickedDeleteDataGroupContact)


    def buttonClickedLoadGroupContact(self):
        self.loadGroupContact()

    def loadGroupContact(self):
        ls = self.groupcontactClass.loadData()
        self.tableWidget_groupcontact.setRowCount(len(ls)+1)
        for i in range(0,len(ls)):
            for j in range(0,3):
                self.tableWidget_groupcontact.setItem(i, j, QtWidgets.QTableWidgetItem( str ( ls[i][j]) ))

        contactnames = self.contactClass.getcontactNames()
        self.comboBox_contact_groupcontact.clear()
        self.comboBox_contact_groupcontact.addItems(contactnames)

        grouptypes = self.groupClass.getGroupTypes()
        self.comboBox_group_groupcontact.clear()
        self.comboBox_group_groupcontact.addItems(grouptypes)

        self.tableWidget_groupcontact.cellClicked.connect(self.getGroupContactIdFromCellClick)

        ## set editlane group_contact
    def getGroupContactIdFromCellClick(self, row,_):
        try:
            self.pickedRowGroup = row
            self.pickedIdGroup = self.tableWidget_groupcontact.item(row, 0).text()
            self.comboBox_contact_groupcontact.setCurrentText(self.tableWidget_groupcontact.item(row, 1).text())
            self.comboBox_group_groupcontact.setCurrentText(self.tableWidget_groupcontact.item(row, 2).text())
        except AttributeError:
            self.pickedRowGroup = None
            self.pickedIdGroup = None


        ## add groupcontact
    def buttonClickedSaveDataGroupContact(self):
        name = self.comboBox_contact_groupcontact.currentText()
        idcontact = self.contactClass.getContactId(name)

        types = self.comboBox_group_groupcontact.currentText()
        idgroup = self.groupClass.getGroupId(types)

        data = {
        'idcontact': idcontact,
        'idgroup': idgroup,
        }
        self.groupcontactClass.AddData(data)
        self.loadGroupContact()


    def buttonClickedDeleteDataGroupContact(self):
        if(self.pickedIdGroup != None):
            self.groupcontactClass.delete(self.pickedIdGroup)
            self.tableWidget_groupcontact.item(self.pickedRowGroup, 0).setText("") 
            self.tableWidget_groupcontact.item(self.pickedRowGroup, 1).setText("") 
            self.tableWidget_groupcontact.item(self.pickedRowGroup, 2).setText("") 
            self.setNone()
        else:
            print("select row")

    
        
   ## load Contact
    def buttonClickedLoadDataContact(self):
        self.loadContact()

    def loadContact(self):
        ls = self.contactClass.loadData()
        self.tableWidget_contact.setRowCount(len(ls)+1)
        for i in range(0,len(ls)):
            for j in range(0,5):
                self.tableWidget_contact.setItem(i, j, QtWidgets.QTableWidgetItem( str ( ls[i][j]) ))
        self.tableWidget_contact.cellClicked.connect(self.getContactIdFromCellClick)

        self.comboBox_work_contact.clear()
        workPosts = self.workClass.getWorkPost()
        self.comboBox_work_contact.addItems(workPosts)


    ## set editlane contact
    def getContactIdFromCellClick(self, row,_):
        try:
            self.pickedRowGroup = row
            self.pickedIdGroup = self.tableWidget_contact.item(row, 0).text()
            self.lineEdit_name_contact.setText(self.tableWidget_contact.item(row, 1).text())
            self.lineEdit_mail_contact.setText(self.tableWidget_contact.item(row, 3).text())
            self.lineEdit_blacklist_contact.setText(self.tableWidget_contact.item(row, 4).text())

        except AttributeError:
            self.pickedRowGroup = None
            self.pickedIdGroup = None

    ## add contact
    def buttonClickedSaveDataContact(self):
        name = self.lineEdit_name_contact.text()
        post = self.comboBox_work_contact.currentText()
        mail = self.lineEdit_mail_contact.text()
        blacklist = self.lineEdit_blacklist_contact.text()
        idwork = self.workClass.getWorkId(post)
        idcontact = self.contactClass.getContactId(name)
        if(blacklist == ""):
            blacklist = 0
        data = {
        'idwork' : idwork,
        'name': name,
        'mail': mail,
        'blacklist': blacklist
        }
        self.contactClass.addData(data)
        self.loadContact()

        ## delete contact
    def buttonClickedDeleteContact(self):
        if(self.pickedIdGroup != None):
            self.contactClass.delete(self.pickedIdGroup)
            self.lineEdit_name_contact.setText(self.tableWidget_contact.item(self.pickedRowGroup, 1).text())
            self.tableWidget_contact.item(self.pickedRowGroup, 0).setText("") 
            self.tableWidget_contact.item(self.pickedRowGroup, 1).setText("") 
            self.tableWidget_contact.item(self.pickedRowGroup, 2).setText("") 
            self.tableWidget_contact.item(self.pickedRowGroup, 3).setText("") 
            self.tableWidget_contact.item(self.pickedRowGroup, 4).setText("") 
            self.setNone()
        else:
            print("select row")
    
    ## update contact
    def buttonClickedUpdateContact(self):
        if(self.pickedIdGroup != None):
            name = self.lineEdit_name_contact.text()
            post = self.comboBox_work_contact.currentText()
            mail = self.lineEdit_mail_contact.text()
            blacklist = self.lineEdit_blacklist_contact.text()
            idwork = self.workClass.getWorkId(post)
            idcontact = self.contactClass.getContactId(name)
            data = {
            'idwork' : idwork,
            'name': name,
            'mail': mail,
            'blacklist': blacklist
            }
            self.contactClass.updateContact(data,self.pickedIdGroup)
            self.loadContact()
        else:
            print("select row")
            


    def buttonClickedFindName(self):
        name = self.lineEditFindName.text()
        response = self.contactClass.findName(name)
        self.textEdit.setText(response)

    def buttonClickedFindNumber(self):
        number = self.lineEditFindNumber.text()
        response = self.contactClass.FindPhone(number)
        self.textEdit_2.setText(response)

   ## load phone
    def buttonClickedLoadDataPhone(self):
        self.loadPhone()

    def loadPhone(self):
        ls = self.phoneClass.loadData()
        self.tableWidget_phone.setRowCount(len(ls)+1)
        for i in range(0,len(ls)):
            for j in range(0,3):
                self.tableWidget_phone.setItem(i, j, QtWidgets.QTableWidgetItem( str ( ls[i][j]) ))
        self.tableWidget_phone.cellClicked.connect(self.getPhoneIdFromCellClick)
        contactNames = self.contactClass.getcontactNames()

        self.comboBox_contactid_phone.clear()
        self.comboBox_contactid_phone.addItems(contactNames)


    ## set editlane phone
    def getPhoneIdFromCellClick(self, row,_):
        try:
            self.pickedRowGroup = row
            self.pickedIdGroup = self.tableWidget_phone.item(row, 0).text()
            self.lineEdit_number_phone.setText(self.tableWidget_phone.item(row, 1).text())
            self.comboBox_contactid_phone.setCurrentText(  self.phoneClass.getContactName((self.tableWidget_phone.item(row, 2).text())))
        except AttributeError:
            self.pickedRowGroup = None
            self.pickedIdGroup = None

    ## update phone
    def buttonClickedUpdateDataPhone(self):
        if(self.pickedIdGroup != None):
            number = self.lineEdit_number_phone.text()
            name = self.comboBox_contactid_phone.currentText()
            #companyname = self.lineEdit_companyname_work.text()
            idcontact = self.contactClass.getContactId(name)
            data = {
            'number': number
            }
            self.phoneClass.updateData(data,self.pickedIdGroup)
            self.tableWidget_phone.item(self.pickedRowGroup, 1).setText(number) 
        else:
            print("select row")
    ## add phone
    def buttonClickedSaveDataPhone(self):
        number = self.lineEdit_number_phone.text()
        name = self.comboBox_contactid_phone.currentText()
        idcontact = self.contactClass.getContactId(name)
        data = {
        'number': number,
        'idcontact': idcontact
        }
        self.phoneClass.addData(data)
        self.loadPhone()

    ## delete phone
    def buttonClickedDeleteDataPhone(self):
        if(self.pickedIdGroup != None):
            self.phoneClass.delete(self.pickedIdGroup)

            self.lineEdit_number_phone.setText(self.tableWidget_phone.item(self.pickedRowGroup, 1).text())
            

            self.tableWidget_phone.item(self.pickedRowGroup, 0).setText("") 
            self.tableWidget_phone.item(self.pickedRowGroup, 1).setText("") 
            self.tableWidget_phone.item(self.pickedRowGroup, 2).setText("") 
            self.setNone()
        else:
            print("select row")


    ## load work
    def buttonClickedLoadDataWork(self):
        self.loadWork()

    def loadWork(self):
        ls = self.workClass.loadData()
        self.tableWidget_work.setRowCount(len(ls)+1)
        for i in range(0,len(ls)):
            for j in range(0,3):
                self.tableWidget_work.setItem(i, j, QtWidgets.QTableWidgetItem( str ( ls[i][j]) ))
        self.tableWidget_work.cellClicked.connect(self.getWorkIdFromCellClick)
        ## set editlane work
    def getWorkIdFromCellClick(self, row,_):
        try:
            self.pickedRowGroup = row
            self.pickedIdGroup = self.tableWidget_work.item(row, 0).text()
            self.lineEdit_post_work.setText(self.tableWidget_work.item(row, 1).text())
            self.lineEdit_companyname_work.setText(self.tableWidget_work.item(row, 2).text())
        except AttributeError:
            self.pickedRowGroup = None
            self.pickedIdGroup = None

        ## update WORK
    def buttonClickedUpdateDataWork(self):
        if(self.pickedIdGroup != None):
            post = self.lineEdit_post_work.text()
            companyname = self.lineEdit_companyname_work.text()

            data = {
            'post': post,
            'companyname': companyname
            }
            self.workClass.updateData(data,self.pickedIdGroup)
            self.tableWidget_work.item(self.pickedRowGroup, 1).setText(post) 
            self.tableWidget_work.item(self.pickedRowGroup, 2).setText(companyname) 
        else:
            print("select row")

            
    ## add WORK
    def buttonClickedAddDataWork(self):
        post = self.lineEdit_post_work.text()
        companyname = self.lineEdit_companyname_work.text()
        data = {
        'post': post,
        'companyname': companyname
        }
        self.workClass.addData(data)
        self.loadWork()

    ## delete WORK
    def buttonClickedDeleteDataWork(self):
        if(self.pickedIdGroup != None):
            self.workClass.delete(self.pickedIdGroup)

            self.lineEdit_post_work.setText(self.tableWidget_work.item(self.pickedRowGroup, 1).text())
            self.lineEdit_companyname_work.setText(self.tableWidget_work.item(self.pickedRowGroup, 2).text())

            self.tableWidget_work.item(self.pickedRowGroup, 0).setText("") 
            self.tableWidget_work.item(self.pickedRowGroup, 1).setText("") 
            self.tableWidget_work.item(self.pickedRowGroup, 2).setText("")
            self.setNone()
        else:
            print("select row")



    ## update group
    def buttonClickedUpdateDataGroups(self):
        if(self.pickedIdGroup != None):
            typegroup = self.lineEdit_type_groups.text()
            note = self.lineEdit_note_groups.text()
            data = {
            'type': typegroup,
            'note': note
            }
            self.groupClass.updateData(data,self.pickedIdGroup)
            self.tableWidget_groups.item(self.pickedRowGroup, 1).setText(typegroup) 
            self.tableWidget_groups.item(self.pickedRowGroup, 2).setText(note) 
        else:
            print("select row")

            
    ## add group
    def buttonClickedAddDataGroups(self):
        typegroup = self.lineEdit_type_groups.text()
        note = self.lineEdit_note_groups.text()
        data = {
        'type': typegroup,
        'note': note
        }
        self.groupClass.addData(data)
        self.loadGroup()

    ## delete group
    def buttonClickedDeleteDataGroups(self):
        if(self.pickedIdGroup != None):
            self.groupClass.delete(self.pickedIdGroup)
            self.lineEdit_type_groups.setText(self.tableWidget_groups.item(self.pickedRowGroup, 1).text())
            self.lineEdit_note_groups.setText(self.tableWidget_groups.item(self.pickedRowGroup, 2).text())

            self.tableWidget_groups.item(self.pickedRowGroup, 0).setText("") 
            self.tableWidget_groups.item(self.pickedRowGroup, 1).setText("") 
            self.tableWidget_groups.item(self.pickedRowGroup, 2).setText("") 
            self.setNone()
        else:
            print("select row")


    ## load group
    def buttonClickedLoadDataGroups(self):
        self.loadGroup()

    def loadGroup(self):
        ls = self.groupClass.loadData()
        self.tableWidget_groups.setRowCount(len(ls)+1)
        for i in range(0,len(ls)):
            for j in range(0,3):
                self.tableWidget_groups.setItem(i, j, QtWidgets.QTableWidgetItem( str ( ls[i][j]) ))
        self.tableWidget_groups.cellClicked.connect(self.getGroupIdFromCellClick)


    ## set editlane group
    def getGroupIdFromCellClick(self, row,_):
        try:
            self.pickedRowGroup = row
            self.pickedIdGroup = self.tableWidget_groups.item(row, 0).text()

            self.lineEdit_type_groups.setText(self.tableWidget_groups.item(row, 1).text())
            self.lineEdit_note_groups.setText(self.tableWidget_groups.item(row, 2).text())
        except AttributeError:
            self.pickedRowGroup = None
            self.pickedIdGroup = None

    def setNone(self):
        self.pickedIdGroup = None
        self.pickedRowGroup = None

