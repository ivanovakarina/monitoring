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

    def accept(self):  # это стандартный метод

        super().accept()
        self.__mapper.submit()           # отправляем данные в модель
        state = self.__model.submitAll() # отправить изменения в БД
        self.readyRequest.emit(state, self.__mapper.currentIndex())

    def reject(self): # это стандартный метод
        super().reject()
        self.__mapper.revert()
        self.__model.revertAll()

    def __onClickAddRequest(self, row=None, title=None):
        #
        d = RequestEditDialog(model=self.__model, row=row, parent=self)
        d.readyRequest.connect(self.on_ready)

        if title:
            d.setWindowTitle(title)

        d.exec_()


    def on_ready(self, state, row):
        self.projectsView.setCurrentIndex(
            self.__model.index(row, 0)
        )

        if state:
            self.projectsView.resizeColumnsToContents()
