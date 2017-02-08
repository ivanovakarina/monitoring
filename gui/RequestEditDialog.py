# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper


from .ui.Ui_RequestEditDialog import Ui_RequestDialog


class ProjectEditDialog(QDialog, Ui_RequestDialog):
    readyRequest = pyqtSignal(bool, int, name='readyRequest')

    def __init__(self, model, row=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_model(model)