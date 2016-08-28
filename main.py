# -*- coding: utf-8 -*-

import os.path
import tkinter
import tkinter.filedialog
from ftplib import FTP
from up_sys.ftp_up import FtpCause

class FtpUp(FtpCause):

	def __init__(self, ftp=None):
		super().__init__(ftp)

	def serv_login(self, event):
		try:
			self.ftp = FTP(user.get())
			self.ftp.login(user.get(), passwd.get())
		except Exception as e:
			buff.set('接続できませんでした')
		else:
			user.destroy()
			passwd.destroy()
			login_acc.destroy()
			dec_before.destroy()
			
			buff.set('')
			up_acc.pack(padx='10', pady='10')
			dec_after.pack(pady='10')

	def serv_upload(self, event):
		try:
			file = tkinter.filedialog.askopenfilename(title='ファイル選択')
			self.ftp.storbinary('STOR up_img/'+ os.path.basename(file), open(file, 'rb'))
		except Exception as e:
			buff.set('アップロードできませんでした')
		else:
			buff.set('アップロード完了')

	def serv_delete(self, event):
		pass #未定


if __name__ == '__main__':

	serv = FtpUp()

	root = tkinter.Tk()
	root.title('ftp image uploader')

	buff = tkinter.StringVar()
	buff.set('')

	user = tkinter.Entry(root, width='60')
	user.pack(padx='10', pady='10')

	passwd = tkinter.Entry(root, width='60')
	passwd.pack(pady='10')

	login_acc = tkinter.Button(root, width='30', background='#fff', text='接続')
	up_acc = tkinter.Button(root, width='30', background='#fff', text='アップロード')
	login_acc.bind('<Button-1>', serv.serv_login)
	up_acc.bind('<Button-1>', serv.serv_upload)
	login_acc.pack(pady='10')

	dec_before = tkinter.Label(root, textvariable=buff)
	dec_after = tkinter.Label(root, textvariable=buff)
	dec_before.pack(pady='10')

	root.mainloop()
