# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 307)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 13, 474, 267))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.titleEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.titleEdit.setObjectName("titleEdit")
        self.horizontalLayout_2.addWidget(self.titleEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.activateCheckRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.activateCheckRadioButton.setObjectName("activateCheckRadioButton")
        self.verticalLayout.addWidget(self.activateCheckRadioButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.timeLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.horizontalLayout.addWidget(self.timeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.addRequestToolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.addRequestToolButton.setObjectName("addRequestToolButton")
        self.verticalLayout.addWidget(self.addRequestToolButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.okPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_3.addWidget(self.okPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новый проект"))
        self.label.setText(_translate("Dialog", "Название проекта"))
        self.activateCheckRadioButton.setText(_translate("Dialog", "Включить проверку"))
        self.label_2.setText(_translate("Dialog", "Интервал времени повторения проверки в секундах"))
        self.addRequestToolButton.setText(_translate("Dialog", "Добавить запрос"))
        self.cancelPushButton.setText(_translate("Dialog", " Отмена"))
        self.okPushButton.setText(_translate("Dialog", "OK"))

