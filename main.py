#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

from PyQt5 import QtWidgets
from model import TableModel
from view import TableView

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    array_data = np.random.ranf((17, 3))
    table_model = TableModel(data=array_data)
    table = TableView()
    table.setModel(table_model)
    l = QtWidgets.QVBoxLayout()
    l.addWidget(table)
    w = QtWidgets.QWidget()
    w.setLayout(l)
    w.resize(400, 600)
    w.move(300, 300)
    w.show()
    sys.exit(app.exec_())

