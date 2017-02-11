# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from .ui.Ui_ProjectsWidget import Ui_Form

from core.ProjectModel import ProjectModel

from gui.ProjectEditDialog import ProjectEditDialog
#зачем тут следующее?
from .RequestsWidget import RequestsWidget


class ProjectsWidget(QWidget, Ui_Form):
    selection_changed = pyqtSignal(list, name='selectionChanged')

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_model(model)
        self.__init_ui()
        self.__init_signals()

    def __init_ui(self):
        self.setupUi(self)

        self.projectsView.setModel(self.__model)
        self.projectsView.resizeColumnsToContents()

    def __init_signals(self):
        self.projectsView.doubleClicked.connect(self.edit_project)
        self.projectsView.selectionModel().selectionChanged.connect(
            self.__on_selection_changed
        )

    def __on_selection_changed(self):
        self.selection_changed.emit(
            self.selected_rows()
        )

    def __init_model(self, model):
        if isinstance(model, ProjectModel):
            self.__model = model
            self.__model.select()
        else:
            raise RuntimeError('Переданная модель не ProjectModel')

    #закрытый метод
    #d - локальная переменная, уничтожится при закрытии диалога
    def __open_edit_dialog(self, row = None, title = None):
        d = ProjectEditDialog(model=self.__model, row = row, parent=self)
        d.ready.connect(self.on_ready)

        if title:
            d.setWindowTitle(title)

        d.exec_()

    def on_ready(self, state, row):
        self.projectsView.setCurrentIndex(
            self.__model.index(row, 0)
        )

        if state:
            self.projectsView.resizeColumnsToContents()

    def add_new_project(self):
        self.__open_edit_dialog()

    def edit_project(self, index):
        self.__open_edit_dialog(row=index.row(),
                                title=u'Редактирование проекта') #index - это объект, метод row() позволяет получить
                                                                # номер строки, без u будет кракозябра

    def edit_selected_project(self):
        selected = self.selected_rows()

        if len(selected) == 1:
            self.edit_project(selected.pop()) # selected[0]

    def remove_projects(self, indexes):
        indexes.sort(reverse = True)

        for index in indexes:
            self.__model.removeRow(index.row()) #qmodel index - eto ob'ekt s nomerom stroki i stolbca
                                                #есть метод isvalid - проверяет валидность

        self.__model.select()

    def remove_selected_projects(self):
        self.remove_projects(self.selected_rows())

    def selected_rows(self):
        return self.projectsView.selectionModel().selectedRows()
