# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:25:34 2021

@author: User
"""

from PyQt5 import uic, QtWidgets


#from PyQt5.QtWidgets import QApplication


import sys

qtCreatorFile = "PrimeraI.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# from PyQt5.QtWidgets import QApplication, QDialog

class miApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        #self.ui=Ui_MainWindow()
        self.setupUi(self)     
        
        ## Se conecta el boton a una señal para cuando se le dé un click
        ## y se le asigna el método a realizar.
        #self.ui.ABRIR.clicked.connect(self.mostrarMensaje)
        
        
    def mostrarMensaje(self):
        ## textEdit recibe un texto enriquecido, entonces es necesario ponerle 
        ##el tipo de conversión. En este caso texto plano.
        print("hola")
        # hola=self.ui.textEdit.toPlainText()
      
        # # hola="holaa
