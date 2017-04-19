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
# Versão: 1.7 - Python 2.x
# Data: 11/09/2016
#===================================

from PyQt4 import QtCore, QtGui
from os.path import expanduser

import os
import sys
import ssl
import json
import ctypes
import urllib2
import platform
import subprocess

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Definindo Versão do Programa e determinando a pasta 'home' do usuário.
# ======================================================================
version = "1.7"
if platform.system() == "Windows":
    buf = ctypes.create_unicode_buffer(1024)
    ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
    home_dir = buf.value
else:
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
        global cancel
        self.cancel = False

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(550, 600)
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
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2.clicked.connect(self.cancelDownload)
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 3)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOp_es = QtGui.QMenu(self.menubar)
        self.menuOp_es.setObjectName(_fromUtf8("menuOp_es"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCriar_Subpasta_Para_O_T_pico = QtGui.QAction(MainWindow)
        self.actionCriar_Subpasta_Para_O_T_pico.setCheckable(True)
        self.actionCriar_Subpasta_Para_O_T_pico.setObjectName(_fromUtf8("actionCriar_Subpasta_Para_O_T_pico"))
        self.menuOp_es.addAction(self.actionCriar_Subpasta_Para_O_T_pico)
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Boards Image Downloader - v%s" % (version), None))
        self.label.setText(_translate("MainWindow", "Imageboard Website:", None))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a Imageboard desejada</p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "4chan - http://www.4chan.org", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "8chan - https://8ch.net", None))
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
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cancelar o download das imagens</p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar", None))
        self.menuOp_es.setTitle(_translate("MainWindow", "Opções", None))
        self.actionCriar_Subpasta_Para_O_T_pico.setText(_translate("MainWindow", "Criar Subpasta Para o Tópico", None))

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

    # Método de criação de subpasta para o tópico desejado.
    # Este método só é executado quando a opção de subpasta está selecionada.
    # =======================================================================
    def createSubfolder(self, semantic_url, getThreadNumber):
        self.subFolderName = "%s-[%s]" % (self.semantic_url, self.getThreadNumber)
        if os.path.exists(unicode(self.subFolderName)):
            os.chdir(unicode(self.subFolderName))
        else:
            os.makedirs(unicode(self.subFolderName))
            os.chdir(unicode(self.subFolderName))
        return

    # Método para determinar a URL do arquivo .json da Imageboard escolhida.
    # ======================================================================
    def getJsonURL(self, getBoardValue, getThreadNumber):
        if str(self.getImageBoardValue) == "4chan":
            return "https://a.4cdn.org/%s/thread/%s.json" % (self.getBoardValue, self.getThreadNumber)
        elif str(self.getImageBoardValue) == "8chan":
            return "https://8ch.net/%s/res/%s.json " % (self.getBoardValue, self.getThreadNumber)
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
        # 4chan
        # =====
        if str(self.getImageBoardValue) == "4chan":
            return "http://i.4cdn.org/%s/%s" % (self.getBoardValue, str(self.image))
        # 8chan - Nova e antiga URL
        # =========================
        elif str(self.getImageBoardValue) == "8chan":
            if len(str(self.image)) >= 32:
                return "https://media.8ch.net/file_store/%s" % (str(self.image))
            else:
                return "https://media.8ch.net/%s/src/%s" % (self.getBoardValue, str(self.image))
        # 55chan
        # ======
        elif str(self.getImageBoardValue) == "55chan":
            return "https://55chan.org/%s/src/%s" % (self.getBoardValue, str(self.image))
        # BRChan
        # ======
        elif str(self.getImageBoardValue) == "BRchan":
            return "http://www.brchan.org/%s/src/%s" % (self.getBoardValue, str(self.image))
        # GUROchan
        # ========
        elif str(self.getImageBoardValue) == "GUROchan":
            return "https://www.gurochan.ch/%s/src/%s" % (self.getBoardValue, str(self.image))
        # NULL
        # ====
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
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar .json em %s!" % (self.url))
            return {}
        return self.data

    # Método para calcular o progresso do download dos arquivos.
    # O método resgata o valor da barra e incrementa com o valor de cada progresso.
    # =============================================================================
    def setProgress(self, fsizefile, downloadedSoFar):
        self.oldValue = self.progressBar.value()
        self.progress = float(self.downloadedSoFar) / float(self.fsizefile)
        self.percent = self.progress * 100.0
        self.progressBar.setProperty("value", self.percent)
        QtGui.QApplication.processEvents()

    # Método de download das imagens da Imageboard, board e tópico escolhidos.
    # Para arquivos grandes, o processamento deste método pode congelar a janela até o processo terminar!
    # ===================================================================================================
    def downloadWithoutProgress(self, imageUrl, filename, fsizefile):
        if self.cancel == True:
            self.textEdit.append(u"[Downloader] Cancelado!!")
            QtGui.QApplication.processEvents()
            return False
        else:
            self.imageRequest = urllib2.Request(self.imageUrl, headers={'User-agent' : 'BID/1.0'})
            self.imageResponse = urllib2.urlopen(self.imageRequest, context=self.context)
            self.downloadedSoFar = 0
            with open(str(self.filename), 'wb') as self.file:
                while True:
                    self.imageData = self.imageResponse.read(4096)
                    self.downloadedSoFar += len(self.imageData)
                    if not self.imageData:
                        break
                    self.file.write(self.imageData)
                    self.setProgress(self.fsizefile, self.downloadedSoFar)
            return True

    # Método para resgatar a quantidade de posts no tópico escolhido.
    # ===============================================================
    def getPosts(self, getBoardValue, getThreadNumber):
        self.url = self.getJsonURL(self.getBoardValue, self.getThreadNumber)
        self.data = self.getJson(self.url)
        try:
            for self.archived in self.data['posts']:
                if 'archived' in self.archived:
                    return [self.data['posts'], True]
                else:
                    return [self.data['posts'], False]
        except Exception:
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar posts do tópico %s em /%s/!" % (self.getThreadNumber, self.getBoardValue))
            QtGui.QApplication.processEvents()
            return []

    # Método para resgatar as imagens dos posts e o hash MD5 das imagens.
    # Para Imageboards com suporte a múltiplas imagens por post ou apenas uma imagem por post.
    # Algumas imageboards não possuem informações de hash das imagens!
    # ========================================================================================
    def getImagesFromPosts(self, posts):
        self.imagesList = []
        self.md5sumList = []
        self.fsizeList = []
        for self.p in self.posts:
            if 'tim' in self.p and 'ext' in self.p:
                self.imagesList.append('%s%s' % (self.p['tim'], self.p['ext']))
                if 'md5' in self.p:
                    self.md5sumList.append('%s' % (self.p['md5']))
                if 'fsize' in self.p:
                    self.fsizeList.append('%s' % (self.p['fsize']))

            if 'extra_files' in self.p:
                for self.extra in self.p['extra_files']:
                    self.imagesList.append('%s%s' % (self.extra['tim'], self.extra['ext']))
                    if 'md5' in self.extra:
                        self.md5sumList.append('%s' % (self.extra['md5']))
                    if 'fsize' in self.extra:
                        self.fsizeList.append('%s' % (self.extra['fsize']))
        
        return self.imagesList, self.md5sumList, self.fsizeList

    # Método para recuperar a URL semântica do tópico desejado. É apenas utilizado quando
    # a opção de subpasta para o tópico está selecionada.
    # Algumas imageboards podem não conter este valor, neste caso o método retorna o nome "Tópico".
    # =============================================================================================
    def getSemanticURL(self, posts):
        for self.sURL in self.posts:
            if 'semantic_url' in self.sURL:
                return self.sURL['semantic_url']
            else:
                return "Tópico"

    # Método para resgatar a URL das imagens dos posts e seus nomes.
    # ==============================================================
    def downloadImage(self, getBoardValue, image, fsizefile):
        self.imageUrl = self.getImageURL(self.getBoardValue, self.image)
        self.filename = os.path.join(str(self.image))
        self.downloadStatus = self.downloadWithoutProgress(self.imageUrl, self.filename, self.fsizefile)
        return self.downloadStatus

    # Método para processar e resgatar valores do tópico escolhido.
    # =============================================================
    def processThread(self, getBoardValue, getThreadNumber):
        self.textEdit.append(u"[Downloader] Fazendo download em /%s/ do tópico %s ..." % (self.getBoardValue, self.getThreadNumber))
        QtGui.QApplication.processEvents()

        try:
            self.posts, self.isArchived = self.getPosts(self.getBoardValue, self.getThreadNumber)
            self.images, self.md5hashes, self.fsizes = self.getImagesFromPosts(self.posts)
        except Exception:
            return

        if self.actionCriar_Subpasta_Para_O_T_pico.isChecked() == True:
            self.semantic_url = self.getSemanticURL(self.posts)
            self.createSubfolder(self.semantic_url, self.getThreadNumber)

        if self.isArchived == True:
            self.textEdit.append(u"[Downloader] O tópico %s está arquivado!" % (self.getThreadNumber))
            QtGui.QApplication.processEvents()

        self.textEdit.append(u"[Downloader] Encontrada %d imagens em %d posts:" % (len(self.images), len(self.posts)))
        self.textEdit.append("\n===============================================\n")
        QtGui.QApplication.processEvents()

        self.downloaded = 0
        self.hashpos = 0
        self.fsizepos = -1

        for self.image in self.images:
            
            self.checkImagesInDir = os.path.isfile(str(self.image))

            if self.checkImagesInDir == True or str(self.image) == "deleted":
                self.downloaded += 1
                if self.md5hashes == []:
                    self.textEdit.append(u"Imagem %s - [N/D] -- [%d/%d] já existe! Pulando ..." % (
                        str(self.image), self.downloaded, len(self.images)))
                    QtGui.QApplication.processEvents()
                    self.fsizepos += 1
                else:
                    self.textEdit.append(u"Imagem %s - [%s] -- [%d/%d] já existe! Pulando ..." % (
                        str(self.image), self.md5hashes[self.hashpos], self.downloaded, len(self.images)))
                    QtGui.QApplication.processEvents()
                    self.hashpos += 1
                    self.fsizepos += 1
            else:
                self.downloaded += 1
                if self.md5hashes == []:
                    self.textEdit.append(u"Baixando %s - [N/D] -- Imagem [%d/%d] ..." % (
                        str(self.image), self.downloaded, len(self.images)))
                    QtGui.QApplication.processEvents()
                    self.fsizepos += 1
                else:
                    self.textEdit.append(u"Baixando %s - [%s] -- Imagem [%d/%d] ..." % (
                        str(self.image), self.md5hashes[self.hashpos], self.downloaded, len(self.images)))
                    QtGui.QApplication.processEvents()
                    self.hashpos += 1
                    self.fsizepos += 1
                
                self.fsizefile = int(self.fsizes[self.fsizepos])
                self.status = self.downloadImage(self.getBoardValue, self.image, self.fsizefile)
                if self.status == False:
                    break

        return

    # Método para recuperar os valores inseridos pelo usuário.
    # Imageboard, board, ID do tópico e pasta de destino são resgatados por este método.
    # No final do processo, a pasta de destino é aberta para o usuário.
    # ==================================================================================
    def getUserValues(self):
        self.cancel = False
        self.getImageBoardValue = str(self.comboBox.currentText()).split(" - ", 1)[0].replace(" ", "")
        self.getBoardValue = self.lineEdit.text().replace("/", "")
        self.getThreadNumber = self.lineEdit_2.text()
        self.getOutputDir = self.lineEdit_3.text()

        if self.getBoardValue == "":
            self.textEdit.append(u"[Downloader] Erro! Falta a board onde o tópico está!")
            return
        elif self.getThreadNumber == "":
            self.textEdit.append(u"[Downloader] Erro! Falta a ID do tópico!")
            return
        elif self.getOutputDir == "":
            self.textEdit.append(u"[Downloader] Erro! Falta o caminho para a pasta de destino!")
            return
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setText(_translate("MainWindow", "Downloading...", None))
            self.pushButton.repaint()
            self.progressBar.setProperty("value", 0)
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

            self.textEdit.append("\n===============================================\n")
            self.textEdit.append(u"[Downloader] Processo de Download Finalizado!")
            QtGui.QApplication.processEvents()

            if platform.system() == "Windows":
                os.startfile(self.getOutputDir)
            else:
                try:
                    subprocess.Popen(["xdg-open", "%s" % (self.getOutputDir)])
                except Exception:
                    pass

            return

    # Método para cancelar o processo de download.
    # ============================================
    def cancelDownload(self):
        self.cancel = True
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
