# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindow import Ui_MainWindow
from .ProjectsWidget import ProjectsWidget
from core.ProjectModel import ProjectModel
from .LoginWidget import LoginWidget
from .ProjectEditDialog import ProjectEditDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        self.menubar.setHidden(True)
        self.toolBar.setHidden(True)
        self.statusbar.setHidden(True)
        self.resize(390, 160)

        self.loginWidget = LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)

        self.projectsWidget = ProjectsWidget(ProjectModel(self), self)
        self.stackedWidget.addWidget(self.projectsWidget)
        self.projectsWidget.setHidden(True)

#        self.projectEditDialog = ProjectEditDialog(self)
#        self.stackedWidget.addWidget(self.projectEditDialog)
#        self.projectEditDialog.setHidden(True)


    def init_signals(self):
        self.loginWidget.loginPasswordRight.connect(
            self.closeLoginWindow
        )

    def update_menu(self): #тоже слот для сигнала
        selected = self.projectsWidget.selected_rows()
        self.actionEdit.setEnabled(len(selected) == 1)
        self.actionRemove.setEnabled(bool(selected))

    def closeLoginWindow(self):
        self.init_signals_all()

        self.stackedWidget.setCurrentWidget(self.projectsWidget)
        self.resize(900, 400)
        self.menubar.setHidden(False)
        self.toolBar.setHidden(False)
        self.statusbar.setHidden(False)

    def init_signals_all(self):
        self.actionAdd.triggered.connect(
            self.projectsWidget.add_new_project
        )
        self.actionExit.triggered.connect(self.close)

        self.actionEdit.triggered.connect(
            self.projectsWidget.edit_selected_project
        )

        self.actionRemove.triggered.connect(
            self.projectsWidget.remove_selected_projects
        )

        self.projectsWidget.selection_changed.connect(
            self.update_menu
        )
