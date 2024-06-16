# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import appFunctions
import os

pathDirectoryProject="C:\Work\WIP_Prod"

pathDirectoryTabs="./"

class MainWindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Synosc (On l'espère)")
        self.setMinimumSize(1200, 500)
        label = QLabel("Stronks")
       
        self.child_windows = []
        

 
        
        
        #Eléments de la page
        pagelayout = QHBoxLayout()
        vueLayout = QVBoxLayout()
        mainLayout =QVBoxLayout()
        button_layout = QHBoxLayout()
        mainLayout.addLayout(button_layout)
        tableLayout = QVBoxLayout()
        labelLayout = QVBoxLayout()
        mainLayout.addLayout(labelLayout)
        mainLayout.addLayout(tableLayout)
        pagelayout.addLayout(vueLayout)
        pagelayout.addLayout(mainLayout)
        label.setLayout(labelLayout)
        
        #TexteTemporaire
        labelViewTitle = QLabel("TitreTest")
        btnShowTab = QPushButton("testAnimation.yml")
        btnShowTab.pressed.connect(self.buttonMkTab)
        vueLayout.addWidget(labelViewTitle)
        vueLayout.addWidget(btnShowTab)
        
        btn = QPushButton("DossierPrincipal")
        btn.pressed.connect(self.buttonMainFile)
        button_layout.addWidget(btn)
                    
        btnTabs = QPushButton("DossierTabs")
        btnTabs.pressed.connect(self.buttonTabs)
        button_layout.addWidget(btnTabs)
        
       
        
        self.destroyed.connect(self.fermer_fenetres_filles)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
        
    def buttonMainFile(self):
        self.new_window =WindowAskMainFile()
        self.new_window.show()
        
    def buttonTabs(self):
        self.new_window =WindowAskTabs()
        self.new_window.show()    
        
    def buttonMkTab(self):
        self.new_window =WindowMkTab()
        self.new_window.show()    
           
        
        
    def fermer_fenetres_filles(self):
        # Fermer toutes les fenêtres filles
        for window in self.child_windows:
            window.close()
            
    def closeEvent(self, event):
        appFunctions.delete_files_in_directory("tempthumb")
        event.accept()

class WindowAskMainFile(QMainWindow):
    def __init__(self):
        super().__init__()

       # Créer un LineEdit et un bouton
        self.lineEdit = QLineEdit()
        self.setWindowTitle("DossierPrincipal")
        self.button = QPushButton("Valider")
        self.button.pressed.connect(self.buttonMainFile)
        self.label= QLabel("Entrer le chemin vers votre dossier de projet :")
        
        self.setMinimumSize(1200, 500)
        
        # Créer un layout vertical pour organiser les widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)

        # Appliquer le layout à la page
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def buttonMainFile(self):
        global pathDirectoryProject
        
        
        if os.path.isdir(self.lineEdit.text()):
            pathDirectoryProject = self.lineEdit.text()
            MainWindow.reload()
            self.close()
        else:
            QMessageBox.information(self, "Attention!", "Veillez à mettre un répertoire qui existe!")
            
class WindowAskTabs(QMainWindow):
    def __init__(self):
        super().__init__()

       # Créer un LineEdit et un bouton
        self.lineEdit = QLineEdit()
        self.setWindowTitle("Emplacement de vos tableaux")
        self.button = QPushButton("Valider")   
        self.button.pressed.connect(self.buttonMainFile)
        self.label= QLabel("Entrer le chemin vers votre dossier où sont situés vos tableaux :")
        
        self.setMinimumSize(1200, 500)
        
        # Créer un layout vertical pour organiser les widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)

        # Appliquer le layout à la page
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def buttonMainFile(self):
        global pathDirectoryTabs
        
        
        if os.path.isdir(self.lineEdit.text()):
            pathDirectoryTabs = self.lineEdit.text()
            print(pathDirectoryTabs)
            #self.close()
            QDesktopServices.openUrl(QUrl.fromLocalFile(pathDirectoryTabs))
        else:
            QMessageBox.information(self, "Attention!", "Veillez à mettre un répertoire qui existe!")
            
class WindowMkTab(QMainWindow):
    def __init__(self):
        super().__init__()
        tableLayout = QVBoxLayout()
        self.tableWidget = appFunctions.mkTab(pathDirectoryProject)        


        tableLayout.addWidget(self.tableWidget)
        widget = QWidget()
        widget.setLayout(tableLayout)
        self.setCentralWidget(widget)




app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()

        


