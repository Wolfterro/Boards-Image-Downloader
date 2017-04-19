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
from PyQt4 import QtCore, QtGui
import os
import sys

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from ConfigLoaderClass import ConfigLoader
from WindowHandlerClass import WindowHandler

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Codificação dos elementos da janela principal
# =============================================
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

# Classe da janela principal do programa
# ======================================
class Ui_MainWindow(object):
	def setupUi(self, MainWindow, Handler):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(600, 780)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(GlobalVars.IconName)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout = QtGui.QGridLayout(self.groupBox)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.label = QtGui.QLabel(self.groupBox)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.comboBox = QtGui.QComboBox(self.groupBox)
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 3)
		self.label_2 = QtGui.QLabel(self.groupBox)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.lineEdit = QtGui.QLineEdit(self.groupBox)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
		self.label_3 = QtGui.QLabel(self.groupBox)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
		self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)
		self.groupBox_1 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))
		self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_1)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_1)
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.lineEdit_3.setReadOnly(True)
		self.gridLayout_2.addWidget(self.lineEdit_3, 0, 0, 1, 1)
		self.toolButton = QtGui.QToolButton(self.groupBox_1)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.gridLayout_2.addWidget(self.toolButton, 0, 1, 1, 1)
		self.checkBox_3 = QtGui.QCheckBox(self.groupBox_1)
		self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
		self.gridLayout_2.addWidget(self.checkBox_3, 1, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_1, 1, 0, 1, 1)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
		self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.gridLayout_3.addWidget(self.comboBox_2, 0, 0, 1, 1)
		self.checkBox = QtGui.QCheckBox(self.groupBox_2)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 1)
		self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.gridLayout_3.addWidget(self.checkBox_2, 2, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)
		self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
		self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		self.pushButton = QtGui.QPushButton(self.groupBox_3)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
		self.textEdit = QtGui.QTextEdit(self.groupBox_3)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.textEdit.setReadOnly(True)
		self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 1)
		self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_2.setEnabled(False)
		self.gridLayout_4.addWidget(self.pushButton_2, 2, 0, 1, 1)
		self.progressBar = QtGui.QProgressBar(self.groupBox_3)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.gridLayout_4.addWidget(self.progressBar, 3, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# Conectando os botões da janela principal do programa
		# ====================================================
		self.pushButton.clicked.connect(Handler.gatherUserValues)
		self.pushButton_2.clicked.connect(Handler.setCancel)
		self.toolButton.clicked.connect(Handler.selectOutputDir)

		# Populando lista de imageboards disponíveis
		# ==========================================
		self.configBoards = ConfigLoader(GlobalVars.ConfigFilename)
		boardsNames = self.configBoards.getImageBoardNames()
		self.populateImageBoardList(boardsNames)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Boards Image Downloader - v%s" % (GlobalVars.Version), None))
		self.groupBox.setTitle(_translate("MainWindow", "Opções de Imageboard", None))
		self.label.setText(_translate("MainWindow", "Imageboard", None))
		self.label_2.setText(_translate("MainWindow", "ID do tópico", None))
		self.label_3.setText(_translate("MainWindow", "Board", None))
		self.groupBox_1.setTitle(_translate("MainWindow", "Pasta de Destino", None))
		self.toolButton.setText(_translate("MainWindow", "...", None))
		self.checkBox_3.setText(_translate("MainWindow", "Abrir pasta de destino quando o download for concluído", None))
		self.groupBox_2.setTitle(_translate("MainWindow", "Opções de Salvamento", None))
		self.comboBox_2.setItemText(0, _translate("MainWindow", "Salvar tudo", None))
		self.comboBox_2.setItemText(1, _translate("MainWindow", "Apenas imagens", None))
		self.comboBox_2.setItemText(2, _translate("MainWindow", "Apenas vídeos", None))
		self.checkBox.setText(_translate("MainWindow", "Substituir arquivos existentes", None))
		self.checkBox_2.setText(_translate("MainWindow", "Criar subpasta", None))
		self.groupBox_3.setTitle(_translate("MainWindow", "Informações e Processos", None))
		self.pushButton.setText(_translate("MainWindow", "Download", None))
		self.pushButton_2.setText(_translate("MainWindow", "Cancelar", None))
		self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a Imageboard desejada</p></body></html>", None))
		self.comboBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha os tipos de arquivos a serem salvos</p></body></html>", None))
		self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insira a ID do tópico desejado</p></body></html>", None))
		self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a board desejada. Exemplo: /pol/</p></body></html>", None))
		self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha a pasta de destino das imagens</p></body></html>", None))
		self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolher pasta de destino...</p></body></html>", None))
		self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Iniciar download dos arquivos</p></body></html>", None))
		self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cancelar o download dos arquivos</p></body></html>", None))

	# Método de preenchimento da lista de imageboards
	# ===============================================
	def populateImageBoardList(self, boardsNames):
		counter = 0
		for b in boardsNames:
			self.comboBox.addItem(_fromUtf8(""))
			self.comboBox.setItemText(counter, _translate("MainWindow", "%s" % (b), None))
			counter += 1

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()

	# Os métodos do programa serão definidos pelo Handler
	# ---------------------------------------------------
	Handler = WindowHandler(ui, MainWindow)
	GlobalVars.Ui = ui
	GlobalVars.MainWindow = MainWindow
	GlobalVars.IconPath = os.path.abspath(GlobalVars.IconName)
	
	ui.setupUi(MainWindow, Handler)
	MainWindow.show()
	sys.exit(app.exec_())