# -*- coding: utf-8 -*-

from abc import abstractmethod

class FtpCause:

	def __init__(self, ftp=None):
		self.ftp = ftp

	@abstractmethod
	def serv_login(self):
		pass

	@abstractmethod
	def serv_upload(self):
		pass

	@abstractmethod
	def serv_deleate(self):
		pass