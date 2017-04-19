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
import json

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from MessageBoxClass import ShowMessageBox

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Classe do gerenciador de API das imageboards
# ============================================
class Imageboard(object):
	# Inicializando objetos da classe
	# ===============================
	def __init__(self, jsonAPI, imgURL, board):
		# Propriedades da classe
        # ----------------------
		self.jsonAPI = jsonAPI
		self.posts = None
		self.postsNum = 0
		
		self.files = []
		self.filesNum = 0
		
		self.imageLinks = []
		self.imagesNum = 0
		
		self.videoLinks = []
		self.videosNum = 0
		
		self.filesSizeBytes = []
		self.imagesSizeBytes = []
		self.videosSizeBytes = []
		
		self.filesSize = []
		self.imagesSize = []
		self.videosSize = []
		
		self.isArchived = False

		self.imgURL = imgURL
		self.board = board
		self.downloadLinks = []

		self.threadName = ""

		self.imgTypes = [".jpg", ".jpeg", ".gif", ".png", ".pdf"]
		self.vidTypes = [".webm", ".mp4", ".swf"]

		self.messageBox = ShowMessageBox()
		self.getAllPosts()
		
		if self.posts != None:
			self.getThreadName()
			self.getFilesAndFileSize()
			self.convertFileSize(self.filesSizeBytes, self.filesSize)
			self.convertFileSize(self.imagesSizeBytes, self.imagesSize)
			self.convertFileSize(self.videosSizeBytes, self.videosSize)
			self.postsNum = len(self.posts)
			self.filesNum = len(self.files)
			self.formatDownloadLinks()
			self.filterFileLinks()
			self.imagesNum = len(self.imageLinks)
			self.videosNum = len(self.videoLinks)

	# Resgatando lista de posts do arquivo .json
	# ==========================================
	def getAllPosts(self):
		try:
			for p in self.jsonAPI['posts']:
				if 'archived' in p:
					self.isArchived = True
					break
			self.posts = self.jsonAPI['posts']
		except Exception as e:
			self.messageBox.show(u"Erro!", 
				QtGui.QMessageBox.Critical, 
				u"Não foi possível recuperar os posts!", 
				u"Erro: %s" % (e),
				QtGui.QMessageBox.Ok, 
				0)
			self.posts = None

	# Resgatando o nome do tópico
	# ===========================
	def getThreadName(self):
		for name in self.posts:
			if 'semantic_url' in name:
				self.threadName = name['semantic_url']
				break
			else:
				self.threadName = "Thread"

	# Resgatando lista de arquivos do tópico do arquivo .json
	# =======================================================
	def getFilesAndFileSize(self):
		for img in self.posts:
			if 'tim' in img and 'ext' in img:
				self.files.append("%s%s" % (img['tim'], img['ext']))
				if 'fsize' in img:
					self.filesSizeBytes.append("%s" % (img['fsize']))
					if img['ext'] in self.imgTypes:
						self.imagesSizeBytes.append("%s" % (img['fsize']))
					elif img['ext'] in self.vidTypes:
						self.videosSizeBytes.append("%s" % (img['fsize']))

			if 'extra_files' in img:
				for extra in img['extra_files']:
					self.files.append("%s%s" % (extra['tim'], extra['ext']))
					if 'fsize' in img:
						self.filesSizeBytes.append("%s" % (extra['fsize']))
						if img['ext'] in self.imgTypes:
							self.imagesSizeBytes.append("%s" % (img['fsize']))
						elif img['ext'] in self.vidTypes:
							self.videosSizeBytes.append("%s" % (img['fsize']))

	# Convertendo tamanho de arquivos
	# ===============================
	def convertFileSize(self, listSizesBytes, listSizes):
		for s in listSizesBytes:
			if len(str(s)) < 4:
				listSizes.append("%.02f %s" % (float(s), "B"))
			elif len(str(s)) >= 4 and len(str(s)) < 7:
				listSizes.append("%.02f %s" % (float(s) / 1024., "KB"))
			elif len(str(s)) >= 7 and len(str(s)) < 10:
				listSizes.append("%.02f %s" % (float(s) / 1024. / 1024., "MB"))
			else:
				listSizes.append("%.02f %s" % (float(s) / 1024. / 1024. / 1024., "GB"))

	# Formatando o link de download dos arquivos para serem baixados
	# ==============================================================
	def formatDownloadLinks(self):
		for f in self.files:
			if not '{1}' in self.imgURL:
				self.downloadLinks.append(self.imgURL.format(f))
			else:
				self.downloadLinks.append(self.imgURL.format(self.board, f))

	# Filtrando os links de download dos arquivos por tipo de arquivo
	# ===============================================================
	def filterFileLinks(self):
		for f in self.downloadLinks:
			if os.path.splitext(f)[1] in self.imgTypes:
				self.imageLinks.append(f)
			elif os.path.splitext(f)[1] in self.vidTypes:
				self.videoLinks.append(f)