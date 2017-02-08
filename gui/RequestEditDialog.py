# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper


from .ui.Ui_RequestEditDialog import Ui_RequestDialog


class RequestEditDialog(QDialog, Ui_RequestDialog):
    readyRequest = pyqtSignal(bool, int, name='readyRequest')

    def __init__(self, model, row=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_model(model)

        if row is None:
            # работаем в режиме добавления
            self.__model.insertRow(self.__model.rowCount())
            self.__mapper.toLast()
        else:
            # работаем в режиме редактирования
            self.__mapper.setCurrentIndex(row)

    def init_ui(self):
        # loadUi('ui/notes_edit_dialog.ui', self)
        self.setupUi(self)

    def init_model(self, model):
        self.__model = model

        self.__mapper = QDataWidgetMapper(self)
        self.__mapper.setModel(self.__model)
        self.__mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.__mapper.addMapping(self.uRLLineEdit, 1)
        self.__mapper.addMapping(self.postCheckBox, 2)
        self.__mapper.addMapping(self.bodyPlainTextEdit, 3)
#тут нужен внешний ключ к другой таблицу        self.__mapper.addMapping(self.)