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
import os
import sys
import ssl
import json
import urllib2

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from MessageBoxClass import ShowMessageBox

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Classe de downloads do programa
# ===============================
class Downloader(object):
	# Inicializando objetos da classe
	# ===============================
	def __init__(self, chosenDir):
		self.chosenDir = chosenDir
		self.replaceFiles = False
		self.messageBox = ShowMessageBox()
		self.changeDir()
		self.context = ssl._create_unverified_context()

	# Alterando pasta local para armazenar os arquivos do tópico
	# ==========================================================
	def changeDir(self):
		if os.path.exists(unicode(self.chosenDir)):
			os.chdir(unicode(self.chosenDir))
		else:
			os.makedirs(unicode(self.chosenDir))
			os.chdir(unicode(self.chosenDir))

	# Criando subpasta
	# ================
	def createSubFolder(self, name):
		if os.path.exists(unicode(name)):
			os.chdir(unicode(name))
		else:
			os.makedirs(unicode(name))
			os.chdir(unicode(name))

	# Resgatando os valores da API em JSON
	# ====================================
	def getJson(self, apiURL):
		try:
			request = urllib2.Request(apiURL, headers={'User-agent' : GlobalVars.UserAgent})
			response = urllib2.urlopen(request, context=self.context)
			data = json.loads(response.read())
		except Exception as e:
			self.messageBox.show(u"Erro!", 
				QtGui.QMessageBox.Critical, 
				u"Não foi possível recuperar .json em %s!" % (apiURL), 
				u"Erro: %s" % (e),
				QtGui.QMessageBox.Ok, 
				0)
			return None
		return data 

	# Baixando arquivos selecionados na pasta indicada pelo usuário
	# Valores de retorno:
	# 0 - Download realizado com sucesso!
	# 1 - Não foi possível baixar arquivo!
	# 2 - Arquivo já existe na pasta!
	# =============================================================
	def downloadFile(self, fileAddr, filename, fSize):
		if os.path.exists(filename):
			if self.replaceFiles:
				return self.downloading(fileAddr, filename, fSize)
			else:
				return 2
		else:
			return self.downloading(fileAddr, filename, fSize)

	# Processo de download dos arquivos
	# =================================
	def downloading(self, fileAddr, filename, fSize):
		try:
			request = urllib2.Request(fileAddr, headers={'User-agent' : GlobalVars.UserAgent})
			response = urllib2.urlopen(request, context=self.context)
			downloadedSoFar = 0
			with open(filename, 'wb') as f:
				while True:
					fData = response.read(4096)
					downloadedSoFar += len(fData)
					if not fData:
						break
					f.write(fData)
					self.setProgress(fSize, downloadedSoFar)
			return 0
		except Exception as e:
			return 1

	# Método para calcular o progresso do download dos arquivos.
	# O método resgata o valor da barra e incrementa com o valor de cada progresso.
	# =============================================================================
	def setProgress(self, fsizefile, downloadedSoFar):
		progress = float(downloadedSoFar) / float(fsizefile)
		percent = progress * 100.0
		GlobalVars.Ui.progressBar.setProperty("value", percent)
		QtGui.QApplication.processEvents()