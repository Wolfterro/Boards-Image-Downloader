# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports gerais
# ==============
from __future__ import print_function
from PyQt4 import QtCore, QtGui
from os.path import expanduser

import os
import sys
import ctypes
import platform
import subprocess

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from DownloaderClass import Downloader
from ImageboardClass import Imageboard
from ConfigLoaderClass import ConfigLoader
from MessageBoxClass import ShowMessageBox

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Determinando a pasta 'home' do usuário.
# =======================================
if platform.system() == "Windows":
    buf = ctypes.create_unicode_buffer(1024)
    ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
    home_dir = buf.value
else:
    home_dir = expanduser("~")

# Classe do gerenciador da janela principal
# =========================================
class WindowHandler(object):
    # Inicializando objetos da classe
    # ===============================
    def __init__(self, ui, MainWindow):
        self.ui = ui
        self.MainWindow = MainWindow
        self.messageBox = ShowMessageBox()
        self.configBoards = ConfigLoader(GlobalVars.ConfigFilename)
        
        # Propriedades da classe
        # ----------------------
        self.chosenDir = ""
        self.chosenBoard = ""
        self.apiURL = ""
        self.imgURL = ""
        self.threadID = ""
        self.boardValue = ""
        self.saveOption = ""
        self.openChosenDirAfterDownload = False
        self.replaceFiles = False
        self.createSubFolder = False
        self.cancelDownload = False

    # Cancelando processo de download dos arquivos
    # ============================================
    def setCancel(self):
        self.cancelDownload = True

    # Método para selecionar pasta de destino.
    # ========================================
    def selectOutputDir(self):
        self.chosenDir = QtGui.QFileDialog.getExistingDirectory(self.MainWindow, 
            'Selecione a pasta de destino:', home_dir, QtGui.QFileDialog.ShowDirsOnly)
        
        if platform.system() == "Windows":
            self.ui.lineEdit_3.setText(self.chosenDir.replace("/", "\\"))
        else:
            self.ui.lineEdit_3.setText(self.chosenDir)

    # Resgatando valores da janela principal
    # ======================================
    def gatherUserValues(self):
        self.chosenBoard = str(self.ui.comboBox.currentText()).split(" - ", 1)[0].replace(" ", "")
        self.apiURL = self.configBoards.getImageBoardAPIURL(self.chosenBoard)
        self.imgURL = self.configBoards.getImageBoardImgURL(self.chosenBoard)

        self.threadID = self.ui.lineEdit.text()
        self.boardValue = self.ui.lineEdit_2.text().replace("/", "")

        self.saveOption = str(self.ui.comboBox_2.currentText())
        self.openChosenDirAfterDownload = self.ui.checkBox_3.isChecked()
        self.replaceFiles = self.ui.checkBox.isChecked()
        self.createSubFolder = self.ui.checkBox_2.isChecked()

        if self.checkUserValues():
            self.beginDownloadProcess()

    # Verificando os valores do usuário
    # =================================
    def checkUserValues(self):
        if self.threadID == "":
            self.messageBox.show(u"Aviso!", 
                QtGui.QMessageBox.Warning, 
                u"Falta a ID do tópico!", 
                u"Insira a ID do tópico e tente novamente.",
                QtGui.QMessageBox.Ok, 
                0)
            return False
        elif self.boardValue == "":
            self.messageBox.show(u"Aviso!", 
                QtGui.QMessageBox.Warning, 
                u"Falta a board onde o tópico está!", 
                u"Insira a board onde o tópico está e tente novamente.",
                QtGui.QMessageBox.Ok, 
                0)
            return False
        elif self.chosenDir == "":
            self.messageBox.show(u"Aviso!", 
                QtGui.QMessageBox.Warning, 
                u"Falta o caminho para a pasta de destino!", 
                u"Insira o caminho para a pasta de destino e tente novamente.",
                QtGui.QMessageBox.Ok, 
                0)
            return False
        else:
            return True

    # Iniciando o processo de download dos arquivos do tópico
    # =======================================================
    def beginDownloadProcess(self):
        self.cancelDownload = False
        self.freezeProgramFields(True)
        self.apiURL = self.apiURL.format(self.boardValue, self.threadID)

        downloader = Downloader(self.chosenDir)
        downloader.replaceFiles = self.replaceFiles
        jsonData = downloader.getJson(self.apiURL)

        if jsonData != None:
            imgBoard = Imageboard(jsonData, self.imgURL, self.boardValue)

            if self.createSubFolder:
                downloader.createSubFolder("%s-[%s]" % (imgBoard.threadName, self.threadID))

            # Iniciando processo de download!
            # -------------------------------
            self.ui.textEdit.clear()
            self.ui.textEdit.append(u"[Downloader] Iniciando Download dos Arquivos ...")
            self.ui.textEdit.append(u"--------------------------------------------------------------")
            self.ui.textEdit.append(u"[Info] Número total de posts: %s" % (imgBoard.postsNum))
            self.ui.textEdit.append(u"[Info] Número total de arquivos: %s" % (imgBoard.filesNum))
            self.ui.textEdit.append(u"[Info] Número de imagens: %s" % (imgBoard.imagesNum))
            self.ui.textEdit.append(u"[Info] Número de vídeos: %s" % (imgBoard.videosNum))

            if imgBoard.isArchived:
                self.ui.textEdit.append(u"[Info] O tópico está arquivado!")
            self.ui.textEdit.append(u"--------------------------------------------------------------")
            self.ui.textEdit.append("\n===============================================\n")
            QtGui.QApplication.processEvents()

            if self.saveOption == "Apenas imagens":
                self.downloadProcess(downloader, imgBoard.imageLinks, imgBoard.imagesSizeBytes, 
                    imgBoard.imagesSize, imgBoard.imagesNum)
            elif self.saveOption == "Apenas vídeos":
                self.downloadProcess(downloader, imgBoard.videoLinks, imgBoard.videosSizeBytes, 
                    imgBoard.videosSize, imgBoard.videosNum)
            else:
                self.downloadProcess(downloader, imgBoard.downloadLinks, imgBoard.filesSizeBytes, 
                    imgBoard.filesSize, imgBoard.filesNum)

            self.freezeProgramFields(False)

            self.ui.textEdit.append("\n===============================================\n")
            self.ui.textEdit.append(u"[Downloader] Processo de Download Finalizado!")
            QtGui.QApplication.processEvents()
            # --------------------------------

            if self.openChosenDirAfterDownload:
                if platform.system() == "Windows":
                    os.startfile(self.chosenDir)
                else:
                    try:
                        subprocess.Popen(["xdg-open", "%s" % (self.chosenDir)])
                    except Exception:
                        pass
        else:
            self.freezeProgramFields(False)

    # Baixando arquivos
    # =================
    def downloadProcess(self, downloader, fLinksList, fSizeBytesList, fSizeList, fTotal):
        counter = 0
        for i in fLinksList:
            if self.cancelDownload:
                self.ui.textEdit.append(u"--------------------------------------------------------------")
                self.ui.textEdit.append(u"[Downloader] Processo de Download cancelado!")
                QtGui.QApplication.processEvents()
                break

            fName = os.path.basename(i)
            status = downloader.downloadFile(i, fName, fSizeBytesList[counter])
            if status == 0:
                self.ui.textEdit.append(u"[Download] Arquivo: '%s' --//-- Tamanho: %s --//-- [%d/%d]" % (fName, 
                    fSizeList[counter], counter + 1, fTotal))
                QtGui.QApplication.processEvents()
            elif status == 1:
                self.ui.textEdit.append(u"[Download] Arquivo: '%s' --//-- Erro ao baixar arquivo! Pulando... [%d/%d]" % (fName, 
                    counter + 1, fTotal))
                QtGui.QApplication.processEvents()
            elif status == 2:
                self.ui.textEdit.append(u"[Download] Arquivo: '%s' --//-- Arquivo já existe! Pulando... [%d/%d]" % (fName, 
                    counter + 1, fTotal))
                QtGui.QApplication.processEvents()
            
            counter += 1
    
    # Congelando as opções do programa durante o início do processo de cálculo
    # ========================================================================
    def freezeProgramFields(self, freeze):
        if freeze:
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.toolButton.setEnabled(False)
            self.ui.textEdit.clear()
            self.ui.progressBar.setProperty("value", 0)
            QtGui.QApplication.processEvents()
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.toolButton.setEnabled(True)
            QtGui.QApplication.processEvents()