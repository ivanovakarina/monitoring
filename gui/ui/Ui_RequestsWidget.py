# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requests_widget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReqForm(object):
    def setupUi(self, ReqForm):
        ReqForm.setObjectName("ReqForm")
        ReqForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReqForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ReqForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.requestsView = QtWidgets.QTableView(ReqForm)
        self.requestsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.requestsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.requestsView.setObjectName("requestsView")
        self.verticalLayout.addWidget(self.requestsView)

        self.retranslateUi(ReqForm)
        QtCore.QMetaObject.connectSlotsByName(ReqForm)

    def retranslateUi(self, ReqForm):
        _translate = QtCore.QCoreApplication.translate
        ReqForm.setWindowTitle(_translate("ReqForm", "Form"))
        self.label.setText(_translate("ReqForm", "Список запросов:"))

