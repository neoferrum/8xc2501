# -*- coding: utf-8 -*-

import numpy as np

from PyQt5 import QtCore


class TableModel(QtCore.QAbstractTableModel):
    """Simple table model.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        if 'data' in kwargs:
            data = kwargs['data']
            if isinstance(data, np.ndarray) and data.ndim == 2:
                self._data = data
            else:
                self._data = np.zeros((0, 0))
        else:
            self._data = np.zeros((0, 0))

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            r, c = index.row(), index.column()
            if role == QtCore.Qt.DisplayRole:
                return str(self._data[r, c])
            else:
                return None
        else:
            return None

    def headerData(self, section, orientation=QtCore.Qt.Horizontal, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(section)
            elif orientation == QtCore.Qt.Vertical:
                return str(section)

