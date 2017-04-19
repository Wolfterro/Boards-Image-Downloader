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
import ConfigParser

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from MessageBoxClass import ShowMessageBox

# Classe do carregador de configurações
# =====================================
class ConfigLoader(object):
	# Inicializando objetos da classe
	# ===============================
	def __init__(self, configFilePath):
		self.configFilePath = configFilePath
		self.fields = ["NAME", "APIURL", "IMGURL"]
		
		self.messageBox = ShowMessageBox()
		
		self.checkConfigFileExistence()
		self.config = ConfigParser.ConfigParser()
		self.config.read(self.configFilePath)
		self.checkConfigFileIntegrity()

	# Verificando a existência do arquivo de configurações
	# ====================================================
	def checkConfigFileExistence(self):
		if not os.path.exists(self.configFilePath):
			self.messageBox.show(u"Erro!", 
				QtGui.QMessageBox.Critical, 
				u"Arquivo de configurações '%s' não existe!" % (GlobalVars.ConfigFilename), 
				u"É necessário o arquivo de configurações para carregar os valores das imageboards!",
				QtGui.QMessageBox.Ok, 
				1)

	# Verificando a integridade do arquivo de configurações
	# =====================================================
	def checkConfigFileIntegrity(self):
		for section in self.config.sections():
			for f in self.fields:
				if self.config.has_option(section, f):
					if self.config.get(section, f) == "":
						self.messageBox.show(u"Erro!", 
						QtGui.QMessageBox.Critical, 
						u"Atributo %s está vazio em [%s] no arquivo %s!" % (f, section, self.configFilePath), 
						u"É necessário que o atributo %s exista e possua um valor válido!" % (f),
						QtGui.QMessageBox.Ok, 
						2)
				else:
					self.messageBox.show(u"Erro!", 
						QtGui.QMessageBox.Critical, 
						u"Atributo %s não existe em [%s] no arquivo %s!" % (f, section, self.configFilePath),
						u"É necessário que o atributo %s exista e possua um valor válido!" % (f),
						QtGui.QMessageBox.Ok, 
						2)

	# Resgatando nome das imageboards no arquivo de configurações
	# ===========================================================
	def getImageBoardNames(self):
		names = []
		for name in self.config.sections():
			names.append(self.config.get(name, "NAME"))
		return names

	# Resgatando o endereço da API da imageboard escolhida
	# ====================================================
	def getImageBoardAPIURL(self, selectedName):
		return self.config.get(selectedName, "APIURL")

	# Resgatando o endereço de imagem da imageboard escolhida
	# =======================================================
	def getImageBoardImgURL(self, selectedName):
		return self.config.get(selectedName, "IMGURL")