# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relational_gui/survey.ui'
#
# Created: Sun Oct  9 00:27:00 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(422, 313)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QGridLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.txtSystem = QtGui.QLineEdit(Form)
        self.txtSystem.setObjectName(_fromUtf8("txtSystem"))
        self.formLayout.addWidget(self.txtSystem, 0, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.addWidget(self.label, 1, 0, 1, 1)
        self.txtCountry = QtGui.QLineEdit(Form)
        self.txtCountry.setObjectName(_fromUtf8("txtCountry"))
        self.formLayout.addWidget(self.txtCountry, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtSchool = QtGui.QLineEdit(Form)
        self.txtSchool.setObjectName(_fromUtf8("txtSchool"))
        self.formLayout.addWidget(self.txtSchool, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txtAge = QtGui.QLineEdit(Form)
        self.txtAge.setObjectName(_fromUtf8("txtAge"))
        self.formLayout.addWidget(self.txtAge, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txtFind = QtGui.QLineEdit(Form)
        self.txtFind.setObjectName(_fromUtf8("txtFind"))
        self.formLayout.addWidget(self.txtFind, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.txtComments = QtGui.QTextEdit(Form)
        self.txtComments.setTabChangesFocus(True)
        self.txtComments.setObjectName(_fromUtf8("txtComments"))
        self.formLayout.addWidget(self.txtComments, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.txtEmail = QtGui.QLineEdit(Form)
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.formLayout.addWidget(self.txtEmail, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdCancel = QtGui.QPushButton(Form)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.cmdClear = QtGui.QPushButton(Form)
        self.cmdClear.setObjectName(_fromUtf8("cmdClear"))
        self.horizontalLayout.addWidget(self.cmdClear)
        self.cmdSend = QtGui.QPushButton(Form)
        self.cmdSend.setDefault(True)
        self.cmdSend.setObjectName(_fromUtf8("cmdSend"))
        self.horizontalLayout.addWidget(self.cmdSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.txtCountry)
        self.label_2.setBuddy(self.txtSchool)
        self.label_3.setBuddy(self.txtAge)
        self.label_4.setBuddy(self.txtFind)
        self.label_5.setBuddy(self.txtSystem)
        self.label_6.setBuddy(self.txtComments)
        self.label_7.setBuddy(self.txtEmail)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtComments.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtFind.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtAge.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtSchool.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCountry.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtSystem.clear)
        QtCore.QObject.connect(self.txtSystem, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtCountry.setFocus)
        QtCore.QObject.connect(self.txtCountry, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtSchool.setFocus)
        QtCore.QObject.connect(self.txtSchool, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtAge.setFocus)
        QtCore.QObject.connect(self.txtAge, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtFind.setFocus)
        QtCore.QObject.connect(self.cmdSend, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.send)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtEmail.clear)
        QtCore.QObject.connect(self.txtFind, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtEmail.setFocus)
        QtCore.QObject.connect(self.txtEmail, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtComments.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txtSystem, self.txtCountry)
        Form.setTabOrder(self.txtCountry, self.txtSchool)
        Form.setTabOrder(self.txtSchool, self.txtAge)
        Form.setTabOrder(self.txtAge, self.txtFind)
        Form.setTabOrder(self.txtFind, self.txtEmail)
        Form.setTabOrder(self.txtEmail, self.txtComments)
        Form.setTabOrder(self.txtComments, self.cmdSend)
        Form.setTabOrder(self.cmdSend, self.cmdClear)
        Form.setTabOrder(self.cmdClear, self.cmdCancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "School", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "How did you find relational", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "System", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Email (only if you want a reply)", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClear.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSend.setText(QtGui.QApplication.translate("Form", "Send", None, QtGui.QApplication.UnicodeUTF8))

