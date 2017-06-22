# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableView


class TableView(QTableView):
    """Simple table view.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

    def wheelEvent(self, event):
        if event.modifiers() == QtCore.Qt.ShiftModifier:
            self.horizontalScrollBar().event(event)
        else:
            super().wheelEvent(event)

