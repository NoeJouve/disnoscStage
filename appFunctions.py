# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:26:41 2024

@author: IT_DISNOSC
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import yaml
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import imageio

def delete_files_in_directory(directory):
    # Parcours tous les fichiers du répertoire
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            # Supprime le fichier
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} a été supprimé avec succès.")
            else:
                print(f"{file_path} n'est pas un fichier.")
        except Exception as e:
            print(f"Erreur lors de la suppression de {file_path}: {e}")


def get_thumbnail(video_path, save_path, frame_num=0):
    vid = imageio.get_reader(video_path,  'ffmpeg')
    thumbnail = vid.get_data(frame_num)
    imageio.imwrite(save_path, thumbnail)
    print("Thumbnail saved successfully!")
        

'''def readYaml(fileName):
    with open(fileName, 'r') as file:
        leYamel = yaml.safe_load(file)
    return leYamel

ok=readYaml("testAnimation.yml")'''

def readFileStatus(fileName):
    # Ouvrir le fichier en mode lecture
    with open(fileName, 'r') as file:
        lines = file.readlines()

    # Initialiser un dictionnaire pour stocker les données
    status = {}

    # Parcourir chaque ligne du fichier
    
    for line in lines:
        # Séparer la clé et la valeur en utilisant le séparateur ':'
        if ':' in line:
            key, value = line.strip().split(':', 1)
            status[key.strip()] = value.strip()

    return status




def filePathListByExtension(repertoire, extension):
    fichiers = []

    # Parcours récursif de l'arborescence
    for dossier, sous_dossiers, fichiers_dans_dossier in os.walk(repertoire):
        for fichier in fichiers_dans_dossier:
            if fichier.endswith(extension):
                fichiers.append(os.path.join(dossier, fichier))

    return fichiers

def filePathListByExtension2(repertoire, extension):
    return [
        os.path.join(dossier, fichier)
        for dossier, _, fichiers_dans_dossier in os.walk(repertoire)
        for fichier in fichiers_dans_dossier
        if fichier.endswith(extension)
    ]



def detecter_liste(dictionnaire):
   for valeur in dictionnaire.values():
        if isinstance(valeur, list):
            return True
   return False
 

def fusionner_dictionnaires(d1, d2):
    result = d1.copy()  # Crée une copie du premier dictionnaire
    for cle, valeur in d2.items():
        if cle in result:  # Si la clé existe déjà dans le premier dictionnaire
            if isinstance(result[cle], list):  # Si la valeur est déjà une liste
                result[cle].append(valeur)  # Ajoute la nouvelle valeur à la liste existante
            else:
                result[cle] = [result[cle], valeur]  # Convertit la valeur en liste et ajoute la nouvelle valeur
        else:
            result[cle] = valeur  # Ajoute la nouvelle clé et sa valeur dans le résultat
    return result



def nombre_max_valeurs(dictionnaire):
    if not dictionnaire:
        return 0  # Retourne 0 si le dictionnaire est vide

    max_valeurs = max(len(valeurs) for valeurs in dictionnaire.values())
    return max_valeurs


def mkTab(repertoire):
    tab = QTableWidget()
    
    dicStat = {}
    
    # Définir le nombre de lignes et de colonnes
    listeStatus = filePathListByExtension(repertoire, "Status.md")
    
    
    for i in range(len(listeStatus)-1):
        newLine = readFileStatus(listeStatus[i])
        dicStat = fusionner_dictionnaires(dicStat, newLine)
    
    tab.setRowCount(len(listeStatus)+1)
    
    tab.setColumnCount(len(dicStat)+1)

        # Remplir les colonnes
    for i, (cle) in enumerate(dicStat.keys()):
        tab.setItem(0, i, QTableWidgetItem(cle))
        
        #remplissage des lignes
    incr = 0
    for i in range(len(listeStatus)-1):
        currentStatus =readFileStatus(listeStatus[i])
        for j, (key, values) in enumerate(currentStatus.items()):
            for cle in dicStat.keys():
                if key==cle:
                   tab.setItem(i+1, incr, QTableWidgetItem(values))
                   break
                else:
                   incr+=1
            incr=0
            
    tab.setItem(0, len(dicStat), QTableWidgetItem("Emplacement du statut.md"))
    
    for i in range(len(listeStatus)-1):
        tab.setItem(i+1, len(dicStat), QTableWidgetItem(listeStatus[i]))
    
    
    
    '''
    pixmap=QPixmap("S1-01.mp4")
    label=QLabel()
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)
     
    item = QTableWidgetItem()
    tab.setCellWidget(0, 0, label)
    '''
    return tab

def check_directories(directories_list, target_directory):
    """
    Vérifie si les répertoires de directories_list existent dans target_directory et ses sous-répertoires.
    
    Arguments :
        - directories_list : Liste de répertoires à vérifier.
        - target_directory : Répertoire cible dans lequel vérifier l'existence des répertoires.
    
    Renvoie :
        - Un dictionnaire où les clés sont les répertoires de directories_list et les valeurs sont des booléens
          indiquant si chaque répertoire existe ou non dans target_directory et ses sous-répertoires.
    """
    result = {}
    for directory in directories_list:
        full_path = os.path.join(target_directory, directory)
        exists = any(os.path.exists(os.path.join(root, directory)) and os.path.isdir(os.path.join(root, directory)) for root, dirs, files in os.walk(target_directory))
        result[directory] = exists
    return result


dicStat = {}
listeStatus = filePathListByExtension("C:\Work\WIP_Prod", "Status.md")


for i in range(len(listeStatus)-1):
    newLine = readFileStatus(listeStatus[i])
    dicStat = fusionner_dictionnaires(dicStat, newLine)


ok=readFileStatus('Status.md')

