# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'request_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RequestDialog(object):
    def setupUi(self, RequestDialog):
        RequestDialog.setObjectName("RequestDialog")
        RequestDialog.resize(405, 256)
        self.verticalLayout = QtWidgets.QVBoxLayout(RequestDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.uRLLabel = QtWidgets.QLabel(RequestDialog)
        self.uRLLabel.setObjectName("uRLLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uRLLabel)
        self.uRLLineEdit = QtWidgets.QLineEdit(RequestDialog)
        self.uRLLineEdit.setObjectName("uRLLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uRLLineEdit)
        self.postCheckBox = QtWidgets.QCheckBox(RequestDialog)
        self.postCheckBox.setObjectName("postCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.postCheckBox)
        self.label_3 = QtWidgets.QLabel(RequestDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.bodyPlainTextEdit = QtWidgets.QPlainTextEdit(RequestDialog)
        self.bodyPlainTextEdit.setObjectName("bodyPlainTextEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bodyPlainTextEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(RequestDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(RequestDialog)
        self.buttonBox.accepted.connect(RequestDialog.accept)
        self.buttonBox.rejected.connect(RequestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RequestDialog)

    def retranslateUi(self, RequestDialog):
        _translate = QtCore.QCoreApplication.translate
        RequestDialog.setWindowTitle(_translate("RequestDialog", "Новый запрос"))
        self.uRLLabel.setText(_translate("RequestDialog", "URL"))
        self.postCheckBox.setText(_translate("RequestDialog", "Post запрос"))
        self.label_3.setText(_translate("RequestDialog", "Тело запроса"))

