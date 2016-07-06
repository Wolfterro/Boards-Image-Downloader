# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

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

#===================================
# Criado por: Wolfterro
# Versão: 1.0 - Python 2.x
# Data: 04/07/2016
#===================================

from PyQt4 import QtCore, QtGui
from os.path import expanduser

import os
import sys
import ssl
import json
import urllib2
import platform
import subprocess

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Definindo Versão do Programa e determinando a pasta 'home' do usuário.
# ======================================================================
version = "1.0"
home_dir = expanduser("~")

# Codificação do programa.
# ========================
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# Classe principal do Programa gerado pelo Qt Designer.
# =====================================================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 550)
        MainWindow.setMaximumSize(QtCore.QSize(500, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("BID-Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.clicked.connect(self.selectOutputDir)
        self.gridLayout.addWidget(self.toolButton, 3, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.getUserValues)
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 3)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Boards Image Downloader - v%s" % (version), None))
        self.label.setText(_translate("MainWindow", "Imageboard Website:", None))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a Imageboard desejada</p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "4chan - http://www.4chan.org", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "8chan - https://8ch.pl", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "55chan - https://55chan.org", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "BRchan - http://www.brchan.org", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "GUROchan - https://www.gurochan.ch", None))
        self.label_2.setText(_translate("MainWindow", "Board:", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a board desejada. Exemplo: /pol/</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "ID do Tópico:", None))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insira a ID do tópico desejado</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "Pasta de Destino:", None))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a pasta de destino das imagens</p></body></html>", None))
        self.lineEdit_3.setText(_translate("MainWindow", "%s%sBoards" % (home_dir, "\\" if platform.system() == 'Windows' else '/'), None))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolher pasta de destino...</p></body></html>", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Iniciar download das imagens</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))

    #========================================================================================
    # Métodos de Download: Procedimentos de Resgate de Valores e Download das Imagens
    #
    # - Para adicionar novas boards, basta:
    # --- Adicionar uma nova entrada no método getJsonURL() e getImageURL()
    # --- Adicionar um novo ítem em 'self.comboBox' em setupUi() e retranslateUi()
    # --- Este novo ítem deve possuir o texto desta maneira: "Imageboard - Url da Imageboard"
    #
    #========================================================================================
    # - TODO:
    #
    # - Reestruturar melhor o programa, tornar os métodos e as variáveis mais simples
    # - Multithreading para que a janela não congele por muito tempo
    # - ???
    # - Profit!
    #
    #========================================================================================

    # Método para selecionar pasta de destino.
    # ========================================
    def selectOutputDir(self):
        self.chosenDir = QtGui.QFileDialog.getExistingDirectory(MainWindow, 'Selecione a pasta de destino:', home_dir, QtGui.QFileDialog.ShowDirsOnly)
        if platform.system() == "Windows":
            self.lineEdit_3.setText(self.chosenDir.replace("/", "\\"))
        else:
            self.lineEdit_3.setText(self.chosenDir)
        return

    # Método de verificação de pasta de destino, verificando se existe ou não.
    # ========================================================================
    def checkOutputDir(self, getOutputDir):
        if os.path.exists(unicode(self.getOutputDir)):
            os.chdir(unicode(self.getOutputDir))
        else:
            os.makedirs(unicode(self.getOutputDir))
            os.chdir(unicode(self.getOutputDir))
        return

    # Método para determinar a URL do arquivo .json da Imageboard escolhida.
    # ======================================================================
    def getJsonURL(self, getBoardValue, getThreadNumber):
        if str(self.getImageBoardValue) == "4chan":
            return "https://a.4cdn.org/%s/thread/%s.json" % (self.getBoardValue, self.getThreadNumber)
        elif str(self.getImageBoardValue) == "8chan":
            return "https://8ch.pl/%s/res/%s.json " % (self.getBoardValue, self.getThreadNumber)
        elif str(self.getImageBoardValue) == "55chan":
            return "https://55chan.org/%s/res/%s.json " % (self.getBoardValue, self.getThreadNumber)
        elif str(self.getImageBoardValue) == "BRchan":
            return "http://www.brchan.org/%s/res/%s.json " % (self.getBoardValue, self.getThreadNumber)
        elif str(self.getImageBoardValue) == "GUROchan":
            return "https://www.gurochan.ch/%s/res/%s.json" % (self.getBoardValue, self.getThreadNumber)
        else:
            return ""

    # Método para determinar a URL das imagens da Imageboard escolhida.
    # =================================================================
    def getImageURL(self, getBoardValue, image):
        if str(self.getImageBoardValue) == "4chan":
            return "http://i.4cdn.org/%s/%s" % (self.getBoardValue, str(self.image))
        elif str(self.getImageBoardValue) == "8chan":
            return "https://8ch.pl/%s/src/%s" % (self.getBoardValue, str(self.image))
        elif str(self.getImageBoardValue) == "55chan":
            return "https://55chan.org/%s/src/%s" % (self.getBoardValue, str(self.image))
        elif str(self.getImageBoardValue) == "BRchan":
            return "http://www.brchan.org/%s/src/%s" % (self.getBoardValue, str(self.image))
        elif str(self.getImageBoardValue) == "GUROchan":
            return "https://www.gurochan.ch/%s/src/%s" % (self.getBoardValue, str(self.image))
        else:
            return ""

    # Método para resgatar e ler o arquivo .json da Imageboard escolhida.
    # Utiliza-se o user-agent 'BID/1.0' para autenticação em algumas Imageboards, como o BRchan.
    # ==========================================================================================
    def getJson(self, url):
        global context

        self.context = ssl._create_unverified_context()
        try:
            self.request = urllib2.Request(self.url, headers={'User-agent' : 'BID/1.0'})
            self.response = urllib2.urlopen(self.request, context=self.context)
            self.data = json.loads(self.response.read())
        except Exception:
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar .json para %s!" % (self.url))
            return {}
        return self.data

    # Método de download das imagens da Imageboard, board e tópico escolhidos.
    # Para arquivos grandes, o processamento deste método pode congelar a janela até o processo terminar!
    # ===================================================================================================
    def downloadWithoutProgress(self, imageUrl, filename):
        self.imageRequest = urllib2.Request(self.imageUrl, headers={'User-agent' : 'BID/1.0'})
        self.imageResponse = urllib2.urlopen(self.imageRequest, context=self.context)
        with open(str(self.filename), 'wb') as self.file:
            while True:
                self.imageData = self.imageResponse.read()
                if not self.imageData:
                    break
                self.file.write(self.imageData)

    # Método para resgatar a quantidade de posts no tópico escolhido.
    # ===============================================================
    def getPosts(self, getBoardValue, getThreadNumber):
        self.url = self.getJsonURL(self.getBoardValue, self.getThreadNumber)
        self.data = self.getJson(self.url)
        try:
            return self.data['posts']
        except Exception:
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar posts do tópico %s em /%s/!" % (self.getThreadNumber, self.getBoardValue))
            QtGui.QApplication.processEvents()
            return []

    # Método para resgatar as imagens dos posts.
    # Para Imageboards com suporte a múltiplas imagens por post ou apenas uma imagem por post.
    # ========================================================================================
    def getImagesFromPosts(self, posts):
        self.imagesList = []
        for self.p in self.posts:
            if 'tim' in self.p and 'ext' in self.p:
                self.imagesList.append('%s%s' % (self.p['tim'], self.p['ext']))

            if 'extra_files' in self.p:
                for self.extra in self.p['extra_files']:
                    self.imagesList.append('%s%s' % (self.extra['tim'], self.extra['ext']))
        
        return self.imagesList

    # Método para resgatar a URL das imagens dos posts e seus nomes.
    # ==============================================================
    def downloadImage(self, getBoardValue, image):
        self.imageUrl = self.getImageURL(self.getBoardValue, self.image)
        self.filename = os.path.join(str(self.image))
        self.downloadWithoutProgress(self.imageUrl, self.filename)

    # Método para processar e resgatar valores do tópico escolhido.
    # =============================================================
    def processThread(self, getBoardValue, getThreadNumber):
        self.textEdit.append(u"[Downloader] Fazendo download em /%s/ do tópico %s" % (self.getBoardValue, self.getThreadNumber))
        QtGui.QApplication.processEvents()

        self.posts = self.getPosts(self.getBoardValue, self.getThreadNumber)
        self.images = self.getImagesFromPosts(self.posts)

        self.textEdit.append(u"[Downloader] Encontrada %d imagens em %d posts" % (len(self.images), len(self.posts)))
        self.textEdit.append("\n===========================================\n")
        QtGui.QApplication.processEvents()

        self.downloaded = 0

        for self.image in self.images:
            
            self.checkImagesInDir = os.path.isfile(str(self.image))
            if self.checkImagesInDir == True:
                self.downloaded += 1
                self.textEdit.append(u"Imagem '%s' %d/%d em /%s/ do tópico %s já existe! Pulando ..." % (
                    str(self.image), self.downloaded, len(self.images), self.getBoardValue, self.getThreadNumber))
                QtGui.QApplication.processEvents()
            else:
                self.downloaded += 1
                self.textEdit.append(u"Baixando %s - Imagem %d/%d em /%s/ do tópico %s ..." % (
                    str(self.image), self.downloaded, len(self.images), self.getBoardValue, self.getThreadNumber))
                QtGui.QApplication.processEvents()
                self.downloadImage(self.getBoardValue, self.image)

        return

    # Método para recuperar os valores inseridos pelo usuário.
    # Imageboard, board, ID do tópico e pasta de destino são resgatados por este método.
    # No final do processo, a pasta de destino é aberta para o usuário.
    # ==================================================================================
    def getUserValues(self):
        self.getImageBoardValue = str(self.comboBox.currentText()).split(" - ", 1)[0].replace(" ", "")
        self.getBoardValue = self.lineEdit.text().replace("/", "")
        self.getThreadNumber = self.lineEdit_2.text()
        self.getOutputDir = self.lineEdit_3.text()

        if self.getBoardValue == "":
            self.textEdit.append(u"[Downloader] Erro! Falta a board onde o tópico está!!")
            return
        elif self.getThreadNumber == "":
            self.textEdit.append(u"[Downloader] Erro! Falta a ID do tópico!!")
            return
        elif self.getOutputDir == "":
            self.textEdit.append(u"[Downloader] Erro! Falta o caminho para a pasta de destino!!")
            return
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setText(_translate("MainWindow", "Downloading...", None))
            self.pushButton.repaint()
            QtGui.QApplication.processEvents()

            self.checkOutputDir(self.getOutputDir)

            self.textEdit.clear()
            self.textEdit.append(u"[Downloader] Iniciando Download das Imagens ...")
            QtGui.QApplication.processEvents()

            self.processThread(self.getBoardValue, self.getThreadNumber)

            self.pushButton.setEnabled(True)
            self.pushButton.setText(_translate("MainWindow", "Download", None))
            self.pushButton.repaint()
            QtGui.QApplication.processEvents()

            self.textEdit.append(u"[Downloader] Concluído!!")
            QtGui.QApplication.processEvents()

            if platform.system() == "Windows":
                os.startfile(self.getOutputDir)
            else:
            	try:
            		subprocess.Popen(["xdg-open", "%s" % (self.getOutputDir)])
            	except Exception:
            		pass

            return

# Executando o Programa.
# ======================
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
