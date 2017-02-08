# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
# from PyQt5.uic import loadUi

from .ui.Ui_ProjectEditDialog import Ui_Dialog
from .ui.Ui_RequestEditDialog import Ui_RequestDialog
from gui.RequestEditDialog import RequestEditDialog
from core.RequestModel import RequestModel



class ProjectEditDialog(QDialog, Ui_Dialog):
    ready = pyqtSignal(bool, int, name='ready')

    def __init__(self, model, row=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_model(model)
        self.init_signals()

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

        #self.plannedDateTimeEdit.setMinimumDate(
        #    QDateTime.currentDateTime().date()
        #)
        #self.plannedDateTimeEdit.setDateTime(
        #    QDateTime.currentDateTime()
        #)

    def init_model(self, model):
        self.__model = model

        self.__mapper = QDataWidgetMapper(self)
        self.__mapper.setModel(self.__model)
        self.__mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.__mapper.addMapping(self.titleEdit, 1)
        self.__mapper.addMapping(self.activateCheckRadioButton, 2)
        self.__mapper.addMapping(self.timeLineEdit, 3)


#    def accept(self): # это стандартный метод
#        super().accept()
#        self.__mapper.submit()           # отправляем данные в модель
#        state = self.__model.submitAll() # отправить изменения в БД
#        self.ready.emit(state, self.__mapper.currentIndex())

#    def reject(self): # это стандартный метод
#        super().reject()
#        self.__mapper.revert()
#        self.__model.revertAll()

    def init_signals(self):
        self.addRequestToolButton.clicked.connect(self.__onClickAddRequest)
        self.cancelPushButton.clicked.connect(self.onClickCancel)
        self.okPushButton.clicked.connect(self.onClickOk)

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

    def onClickCancel(self):
        self.__mapper.revert()
        self.__model.revertAll()

    def onClickOk(self):
        self.__mapper.submit()  # отправляем данные в модель
        state = self.__model.submitAll()  # отправить изменения в БД
        self.ready.emit(state, self.__mapper.currentIndex())
