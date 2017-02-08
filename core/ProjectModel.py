# coding: utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ProjectModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTable('project')

        headers = [
            'ID',
            'Название',
            'Статус проекта',
            'Интервал повторения проверки',
            'Статус проверки',
            'Время последней проверки'
        ]

        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Horizontal, headers[i])
