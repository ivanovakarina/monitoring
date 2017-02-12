# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from .ui.Ui_RequestsWidget import Ui_ReqForm

from core.RequestModel import RequestModel
from .RequestEditDialog import RequestEditDialog


class RequestsWidget(QWidget, Ui_ReqForm):
    selection_changed_req = pyqtSignal(list, name='selectionChangedReq')

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_model(model)
        self.__init_ui()
        self.__init_signals()

    def __init_ui(self):
        self.setupUi(self)

        self.requestsView.setModel(self.__model)
        self.requestsView.resizeColumnsToContents()

    def __init_signals(self):
        self.requestsView.doubleClicked.connect(self.edit_request)
        self.requestsView.selectionModel().selectionChanged.connect(
            self.__on_selection_changed_req
        )

    def __on_selection_changed_req(self):
        self.selection_changed_req.emit(
            self.selected_rows()
        )

    def __init_model(self, model):
        print(type(RequestModel), "RequestModel")
        print(type(model), "model")
        if isinstance(model, RequestModel):
            self.__model = model
            self.__model.select()
        else:
            raise RuntimeError('Переданная модель не RequestModel')

    #закрытый метод
    #d - локальная переменная, уничтожится при закрытии диалога
    def __open_edit_dialog(self, row = None, title = None):
        d = RequestEditDialog(model=self.__model, row = row, parent=self)
        d.readyRequest.connect(self.on_ready_req)

        if title:
            d.setWindowTitle(title)

        d.exec_()

    def on_ready_req(self, state, row):
        self.requestsView.setCurrentIndex(
            self.__model.index(row, 0)
        )

        if state:
            self.requestsView.resizeColumnsToContents()

    def add_new_request(self):
        self.__open_edit_dialog()

    def edit_request(self, index):
        self.__open_edit_dialog(row=index.row(),
                                title=u'Редактирование запроса') #index - это объект, метод row() позволяет получить
                                                                # номер строки, без u будет кракозябра

    def edit_selected_request(self):
        selected = self.selected_rows()

        if len(selected) == 1:
            self.edit_request(selected.pop()) # selected[0]

    def remove_requests(self, indexes):
        indexes.sort(reverse = True)

        for index in indexes:
            self.__model.removeRow(index.row()) #qmodel index - eto ob'ekt s nomerom stroki i stolbca
                                                #есть метод isvalid - проверяет валидность

        self.__model.select()

    def remove_selected_requests(self):
        self.remove_requests(self.selected_rows())

    def selected_rows(self):
        return self.requestsView.selectionModel().selectedRows()
