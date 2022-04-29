try:
	try:
		import tkinter as tk
		from tkinter import *
		from tkinter import ttk
		print("tkinter...Loaded")
	except ImportError:
		import Tkinter as tk
		from Tkinter import *
		from Tkinet import ttk
		print("Tkinter...Loaded")
	except ModuleNotFoundError:
		print("Something went wrong while loading tkinter module")
		print("Please make sure 'tkinter' is installed")
		print("If not - install by single command")
		print("`pip install tk`")
		exit(0)
	except Exception as e:
		print("Something went wrong while module loading.")
		print(f"That is reason : {e}")
		print("If you are doing all right, please, contact us at: ")
		print("E-Mail : greyhatfeedback@protonmail.com")
		print("Telegram : @greyhatfdbot")
		exit(0)
	#Anything is possible. 
	#The module may be installed, but if it was written with a capital letter, the module would not load.
	from core_local import *
	print("Core...Loaded")
	from time import sleep
	from datetime import datetime
	import os
	print("All modules loaded succesfully!")
except Exception as e:
	print("Something went wrong while module loading.")
	print(f"That is reason : {e}")
	print("If you are doing all right, please, contact us at: ")
	print("E-Mail : greyhatfeedback@protonmail.com")
	print("Telegram : @greyhatfdbot")
	exit(0)

class GreyNigmaGUI(Tk):
	def __init__(self):
		system("cls" if name == 'nt' else 'clear')
		print("Do you have a GN_TOKEN? [ENTER] to skip")
		print("1. Yes, I have one")
		print("2. No, I haven't")
		print("3. Ima dunno what are you talking about")
		t = input(">>> ")
		if t != "1":
			self.GN = GreyNigmaAPI()
		else:
			print("Enter your GN_TOKEN here: ")
			token = input(">>> ")
			self.GN = GreyNigmaAPI(token)
		super().__init__()
		self.geometry('1010x900')
		self.title('GreyNigma GUI by Grey Hat')
		self.notebook = ttk.Notebook()
		self.tab1 = Frame(self.notebook)
		self.tab2 = Frame(self.notebook)
		self.tab3 = Frame(self.notebook)
		self.notebook.add(self.tab1, text='Encrypt/Decrypt')
		self.notebook.add(self.tab2, text='Gipher [NEW]')
		self.notebook.add(self.tab3, text='General & Debug info')
		self.popupMenu=Menu(self,tearoff=0,background='#1c1b1a',fg='white', activebackground='#534c5c',activeforeground='Yellow')
		self.popupMenu.add_command(label="Cut                     ",command=self.Cut, accelerator='Ctrl+V')
		self.popupMenu.add_command(label="Copy                    ",command=self.Copy,compound=LEFT, accelerator='Ctrl+C')
		self.popupMenu.add_command(label="Paste                   ",command=self.Paste,accelerator='Ctrl+V')
		self.popupMenu.add_command(label="Delete",command=self.deleteOnly,accelerator=" Delete")
		self.bind('<Button-3>',self.popUp)
		##########################################################################################
		#MAIN TAB (1ST)
		Label(self.tab1, text='  Enter the message \n to encrypt  ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=19, y=25)
		Label(self.tab1, text='                          Enter the message to decrypt                          ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=580, y=25)
		Label(self.tab1, text='                               Encrypted message                                ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=175, y=25)
		# Box for encrypted output
		self.encryptedOutput = Text(self.tab1)
		self.encryptedOutput.place(x=175, y=50, width=400,height=600)
		self.encryptedOutput.insert(INSERT, "Encrypted output")

		# Box for decrypted output
		Label(self.tab1, text='                                  Decrypted message                                  ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=580, y=350)
		self.decryptedOutput = Text(self.tab1)
		self.decryptedOutput.place(x=580, y=370, width=420,height=280)
		self.decryptedOutput.insert(INSERT, "Output decrypted")

		#Box for input your text to decrypt
		self.toDecrypt = Text(self.tab1)
		self.toDecrypt.place(x=580, y=50, width=420, height=260)
		# Firstfake input box
		self.firstFakeEntry = Text(self.tab1)
		self.firstFakeEntry.place(x=19, y=70, width=150,height=193.3)
		self.firstFakeEntry.insert(INSERT, 'First Fake')

		#Original string input box
		self.origStringEntry = Text(self.tab1)
		self.origStringEntry.place(x=19, y=263.3, width=150,height=193.3)
		self.origStringEntry.insert(INSERT, 'Original string')

		# Second fake input box
		self.secondFakeEntry = Text(self.tab1)
		self.secondFakeEntry.place(x=19, y=456.6,width=150,height=193.3)
		self.secondFakeEntry.insert(INSERT, 'Second Fake')

		# SeedKey input box
		self.seedKeyEntry = Entry(self.tab1)
		self.seedKeyEntry.place(x=19, y=675,width=980,height=30)
		self.seedKeyLabel = Label(self.tab1, text='Your SeedKey(KEEP IT STRONGLY SAFE AND TELL ONLY TO YOUR INTERLOCUTOR! BE ADVICED, SEED INPUT TYPE - STR!):  ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=19, y=650)
		self.seedKeyEntry.config(show="*")
		
		# Buttons to encrypt and decrypt + 'clear' fields button
		Button(self.tab1, text='        Encrypt         ', bg='#A9A9A9', font=('arial', 12, 'normal'), command=self.encryptGui).place(x=18, y=705)
		Button(self.tab1, text='                                          Decrypt!                                         ', bg='#A9A9A9', font=('arial', 12, 'normal'), command=self.decryptGUI).place(x=580, y=310)
		##########################################################################################
		#Gipher
		##########################################################################################
		self.GipherInput = Text(self.tab2)
		self.GipherInput.place(x=20, y=170, width=450,height=600)
		self.GipherInput.insert(INSERT, 'Here, type text you want to encrypt/decrypt')
		self.GipherOutput = Text(self.tab2)
		self.GipherOutput.place(x=540, y=170, width=450, height=600)
		self.GipherOutput.insert(INSERT, 'Here will be your crypted/decrypted text')
		self.toDecrypt.insert(INSERT, "Here you should paste encrypted text to decrypt")
		Label(self.tab2, text='Welcome to the Gipher!', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=0)
		Label(self.tab2, text='Gipher - extremely easy-to-use, simple and pretty-secure offsetting algorithm, based on Caesar Cipher', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=20)
		Label(self.tab2, text='It works by the next:', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=40)
		Label(self.tab2, text='You entering the word -> each letter shifted by number from the special list(which generated by your seedKey)', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=60)
		Label(self.tab2, text='Example: Hello -> Esabk', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=80)
		Label(self.tab2, text='Try it for free, share your experience in social media!', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=100)
		Label(self.tab2, text='INPUT YOUR TEXT(CLEAR OR CIPHERED)   ', bg='#A9A9A9', font=('arial', 16, 'normal')).place(x=20, y=140)
		Label(self.tab2, text='OUTPUT TEXT(CLEAR OR CIPHERED)          ', bg='#A9A9A9', font=('arial', 16, 'normal')).place(x=540, y=140)
		Button(self.tab2, text='     Encrypt your text with Gipher       ', bg="#A9A9A9", font=('arial', 20, 'normal'), command=lambda: self.Gipher('Encrypt')).place(x=20, y=770)
		Button(self.tab2, text='     Decrypt your text with Gipher       ', bg="#A9A9A9", font=('arial', 20, 'normal'), command=lambda: self.Gipher('Decrypt')).place(x=20, y=815)
		##########################################################################################
		#TAB 3(CONSOLE AND INFO)
		Label(self.tab3, text='Licensed by GNU GPL v3', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=10+5)
		Label(self.tab3, text='Official NotABug page : notabug.org/Grey_Hat_Cybersecurity/GreyNigma', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=30+5)
		Label(self.tab3, text='Official GitHub page : github.com/GreyHatCyberSecurity/GreyNigma', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=50+5)
		Label(self.tab3, text='Feedback : ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=70+5)
		Label(self.tab3, text='Telegram : @greyhatfdbot ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=90+5)
		Label(self.tab3, text='E-Mail : greyhatfeedback@protonmail.com ', bg='#A9A9A9', font=('arial', 12, 'normal')).place(x=20, y=110+5)
		self.logConsole = Text(self.tab3)
		self.logConsole.place(x=20, y=150, height=650, width=980)
		self.logConsole.insert(INSERT, 'GreyNigma GUI Console logger\n')
		Button(self.tab3, text='Clear console', bg="#A9A9A9", font=('arial', 20, 'normal'), command=lambda : self.consoleHandler('Clear Console')).place(x=20, y=800)
		Button(self.tab3, text='Show core info', bg="#A9A9A9", font=('arial', 20, 'normal'), command=self.showCoreInfo).place(x=798, y=800)	
		self.notebook.pack(expand=True,fill="both")
	##########################################################################################
	#CONTEXT MENU FUNCTIONS
	##########################################################################################
	def popUp(self, event):
		try:
			self.popupMenu.tk_popup(event.x_root, event.y_root, 0)
		finally:
			self.popupMenu.grab_release()

	def Copy(self):
		self.event_generate('<Control-c>')

	def Paste(self):
		self.event_generate('<Control-v>')

	def Cut(self):
		self.event_generate('<Control-x>')

	def deleteOnly(self):
		self.event_generate("<BackSpace>")
	##########################################################################################
	#CONSOLE HANDLER FUNCTIONS
	##########################################################################################
	def consoleHandler(self, event, fileName=None, cryptedMessageLen=None):
		eventTime = datetime.now()
		if event == 'Encrypt':
			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] Your message succesfully encrypted! Total message length: {cryptedMessageLen}')
#		elif event == 'Clear':
#			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] All entries cleared!')
		elif event == 'SavedCrypted':
			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] Encrypted message succesfully saved as :{fileName}!')
		elif event == 'Decrypt':
			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] Your message succesfully decrypted!')
		elif event == 'Copied encrypted':
			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] Your encrypted message succesfully copied to the clipboard!')
		elif event == 'Copied decrypted':
			self.logConsole.insert(INSERT, f'\n[{eventTime.strftime("%H:%M:%S")}] Your decrypted message succesfully copied to the clipboard!')
		elif event == 'Clear Console':
			self.logConsole.delete(1.0, END)
			self.logConsole.insert(INSERT, 'GreyNigma GUI Console logger\n')

	def showCoreInfo(self):
		self.logConsole.insert(INSERT, '\n==================================================={Core information}====================================================\n')
		self.logConsole.insert(INSERT, f'Core name: {coreName}\n')
		self.logConsole.insert(INSERT, f'Core load time: {coreLoadTime}s\n') 
		self.logConsole.insert(INSERT, '=================================================={General information}==================================================\n') 
		self.logConsole.insert(INSERT, f'Operating system : {platform.system()} {platform.release()}\n')
		self.logConsole.insert(INSERT, f'Python version : {platform.python_version()}\n')
		self.logConsole.insert(INSERT, '=========================================================================================================================')
	##########################################################################################
	#ENCRYPT FUNCTIONS
	##########################################################################################
	def encryptGui(self):
		'''
		Since you are entering your message to the 'Text' objects in the frame,
		variables goes to the function by 'get()' method, not as arguements, so dont
		need to insert them
		'''
		self.encryptedOutput.delete(1.0, END)
		firstFakeString = self.firstFakeEntry.get(1.0, tk.END+"-1c")
		secondFakeString = self.secondFakeEntry.get(1.0, tk.END+"-1c")
		originalString = self.origStringEntry.get(1.0, tk.END+"-1c")
		seedKey = self.seedKeyEntry.get()#(1.0, tk.END+"-1c")
		#########################################################################################
		encryptedNormalMessage = self.GN.encryptNormalMessage(firstFakeString, originalString, secondFakeString, str(seedKey))
		#########################################################################################
		if encryptedNormalMessage['success']:
			self.encryptedOutput.insert(INSERT, f"{encryptedNormalMessage['message']}")
			self.consoleHandler('Encrypt', None, len(encryptedNormalMessage['message']))
		else:
			self.encryptedOutput.insert(INSERT, f"Something went wrong while sending request to our server\n{encryptedNormalMessage}")
	##########################################################################################
	def Gipher(self, GipherEvent):
		if GipherEvent == "Encrypt":
			clearText = self.GipherInput.get(1.0, tk.END+"-1c")
			seedKey = self.seedKeyEntry.get()#(1.0, tk.END+"-1c")
			seedKey = str(seedKey)
			caesared = self.GN.gipherEncrypt(clearText, str(seedKey))
			if caesared['success']:
				self.GipherOutput.delete(1.0, END)
				self.GipherOutput.insert(INSERT, caesared['message'])
				self.consoleHandler('Encrypt', None, len(caesared['message']))
			else:
				self.GipherOutput.delete(1.0, END)
				self.GipherOutput.insert(INSERT, f"Something went wrong while sending request to our server\n{caesared}")
		elif GipherEvent == "Decrypt":
			cipherText = self.GipherInput.get(1.0, tk.END+"-1c")
			seedKey = self.seedKeyEntry.get()#(1.0, tk.END+"-1c")
			seedKey = str(seedKey)
			deCaesared = self.GN.gipherDecrypt(cipherText, str(seedKey))
			if deCaesared['success']:
				self.GipherOutput.delete(1.0, END)
				self.GipherOutput.insert(INSERT, deCaesared['message'])
				self.logConsole('Decrypt')
			else:
				self.GipherOutput.delete(1.0, END)
				self.GipherOutput.insert(INSERT, f"Something went wrong while sending request to our server\n{deCaesared}")
		elif GipherEvent == "Paste":
			pasteData = self.clipboard_get()
			self.GipherInput.delete(1.0, END)
			self.GipherInput.insert(INSERT, pasteData)
		elif GipherEvent == "Copy":
			self.clipboard_clear()
			copyData = self.GipherOutput.get(1.0, END)
			self.clipboard_append(copyData)
	##########################################################################################
	def decryptGUI(self):
		self.decryptedOutput.delete(1.0, END)
		stringToDecrypt = self.toDecrypt.get(1.0, END)#(1.0, tk.END+"-1c")
		seedKey = self.seedKeyEntry.get()#(1.0, tk.END+"-1c")
		decryptedMessage = self.GN.decryptMessage(stringToDecrypt, seedKey)
		if decryptedMessage['success']:
			self.decryptedOutput.insert(INSERT, f"{decryptedMessage['message']}")
			self.consoleHandler('Decrypt')
		else:
			self.decryptedOutput.delete(1.0, END)
			self.decryptedOutput.insert(INSERT, f"Something went wrong while sending request to our server\n{decryptedMessage}")

if __name__ == "__main__":
	gui = GreyNigmaGUI()
	gui.mainloop()