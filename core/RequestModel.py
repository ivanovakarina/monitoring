# coding: utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class RequestModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTable('requests')

        headers = [
            'ID',
            'URL',
            'POST запрос или нет',
            'Тело запроса',
            'Что искать в ответе',
            'Статус запроса',
            'Интервал повторения проверки',
            'Запрос выполнен успешно',
            'Последний ответ на запрос',
            'ID проекта'
        ]

        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Horizontal, headers[i])