#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:39:41 2018

@author: diasaur
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if 1:
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Test')
    w.show
    sys.exit(app.exec_())

