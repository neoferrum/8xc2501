# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableView


class TableView(QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__()

