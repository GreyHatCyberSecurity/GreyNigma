from core_local import *
from time import sleep
from datetime import datetime
from getpass import getpass
######################################################################
class GreyNigmaCLI():
	'''
	This is the main class of GreyNigma command-line version
	Console functions are stored here to improve core loading speed
	'''
	#######################################################
	def __init__(self):
		self.clearTerminal()
		print("Do you have a GN_TOKEN? [ENTER] to skip")
		print("1. Yes, I have one")
		print("2. No, I haven't")
		print("3. Ima dunno what are you talking about")
		t = int(input(">>> "))
		if t != 1:
			self.GN = GreyNigmaAPI()
			self.mainMenu()
		else:
			print("Enter your GN_TOKEN here: ")
			token = input(">>> ")
			self.GN = GreyNigmaAPI(token)
			self.mainMenu()
	#######################################################
	#Just for clear terminal
	def clearTerminal(self):
		system("cls" if name == 'nt' else 'clear')
	#######################################################
	def banner(self):
			print("+---------------------------------------------------------+")
			print("|█─▄▄▄▄█▄─▄▄▀█▄─▄▄─█▄─█─▄█▄─▀█▄─▄█▄─▄█─▄▄▄▄█▄─▀█▀─▄██▀▄─██|")
			print("|█─██▄─██─▄─▄██─▄█▀██▄─▄███─█▄▀─███─██─██▄─██─█▄█─███─▀─██|")
			print("|▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀|")
			print("|                    c0d3d_by_Gr3yH4t                     |")
			print("+---------------------------------------------------------+")
	#######################################################
	def mainMenu(self):
		self.clearTerminal()
		self.banner()
		print("+------------------------------+")
		print("|1. Encrypt single message     |")
		print("+------------------------------+")
		print("|2. Encrypt 3-string message   |")
		print("+------------------------------+")
		print("|3. Decrypt GreyNigma message  |")
		print("+------------------------------+")
		print("|4. Encrypt/Decrypt via Gipher |")
		print("+------------------------------+")
		print("|5. About                      |")
		print("+------------------------------+")
		print("|6. Exit                       |")
		print("+------------------------------+")
		menuChoice = input(">>> ")
		if menuChoice == "1":
			self.encryptSingleMessage()
		elif menuChoice == "2":
			self.encryptNormalMessage()
		elif menuChoice == "3":
			self.decryptMessage()
		elif menuChoice == "4":
			self.gipher()
		elif menuChoice == "5":
			self.aboutTab()
		elif menuChoice == "6":
			s.keyboardInterrupt()
		else:
			print("Error input, repeating...")
			sleep(1)
			self.mainMenu()

	def encryptSingleMessage(self):
		self.clearTerminal()
		self.banner()
		print("Enter your seedKey")
		seedKey = getpass(">>> ")
		self.clearTerminal()
		self.banner()
		print("Enter your message to encrypt")
		message = input(">>> ")
		encryptedSingleMessage = self.GN.encryptSingleMessage(message, seedKey)
		self.clearTerminal()
		self.banner()
		if encryptedSingleMessage['success']:
			print("Done! Your encrypted message is: \n")
			print(encryptedSingleMessage['message'])
			print("")
			print("Do you want to save your encrypted message?(y/n)")
			print("'y' - save your message")
			print("'n' or any button - return to main menu")
			saveOrNot = input(">>> ")
			if saveOrNot == "y":
				now = datetime.now()
				currentTime = now.strftime("%D_%H_%M_%S")
				cryptSavedName = f'EncryptedMessage{currentTime}'
				with open(f'{cryptSavedName}.txt', 'w') as f:
					f.write(f"{encryptedSingleMessage['message']}")
				print("Done!")
				print(f"Message : {cryptSavedName}.txt succesfully saved into GreyNigma folder!")
				print("Press [ENTER] to return to main menu!")
				asdasd = input()
				self.mainMenu()
			else:
				self.mainMenu()
		else:
			print("Something went wrong while sending request to our server")
			print()
			print("Server reply:")
			print(encryptedSingleMessage)
			print()
			print("If you are doing all right but still face that problem, please, contact us at:")
			print("E-Mail: greyhatfeedback@protonmail.com")
			print("Telegram: @greyhatfdbot")
			print("Press [ENTER] to return to main menu!")
			asdasd = input()
			self.mainMenu()

	def encryptNormalMessage(self):
		self.clearTerminal()
		self.banner()
		print("Enter your seedKey")
		seedKey = getpass(">>> ")
		self.clearTerminal()
		self.banner()
		print("Enter your first fake string:")
		firstFakeString = input(">>> ")
		self.clearTerminal()
		self.banner()
		print("Enter your original string:")
		originalString = input(">>> ")
		self.clearTerminal()
		self.banner()
		print("Enter your second fake string:")
		secondFakeString = input(">>> ")
		encryptedNormalMessage = self.GN.encryptNormalMessage(firstFakeString, originalString, secondFakeString, seedKey)
		self.clearTerminal()
		self.banner()
		if encryptedNormalMessage['success']:
			print("Done! Your encrypted message is: \n")
			print(encryptedNormalMessage['message'])
			print("")
			print("Do you want to save your encrypted message?(y/n)")
			print("'y' - save your message")
			print("'n' or any button - return to main menu")
			saveOrNot = input(">>> ")
			if saveOrNot == "y":
				now = datetime.now()
				currentTime = now.strftime("%D_%H_%M_%S")
				cryptSavedName = f'EncryptedMessage{currentTime}'
				with open(f'{cryptSavedName}.txt', 'w') as f:
					f.write(f"{encryptedNormalMessage['message']}")
				print("Done!")
				print(f"Message : {cryptSavedName}.txt succesfully saved into GreyNigma folder!")
				print("Press [ENTER] to return to main menu!")
				asdasd = input()
				self.mainMenu()
			else:
				self.mainMenu()
		else:
			print("Something went wrong while sending request to our server")
			print()
			print("Server reply:")
			print(encryptedNormalMessage)
			print()
			print("If you are doing all right but still face that problem, please, contact us at:")
			print("E-Mail: greyhatfeedback@protonmail.com")
			print("Telegram: @greyhatfdbot")
			print("Press [ENTER] to return to main menu!")
			asdasd = input()
			self.mainMenu()

	def decryptMessage(self):
		self.clearTerminal()
		self.banner()
		print("Decrypt from file or manually inputted text?")
		print("1. I have a file with encrypted text")
		print("2. I will paste my message manually")
		print("3. My bad, wanna go to main menu!")
		textOrFile = input(">>> ")
		if textOrFile == "1":
			print("Please, enter the path to your message")
			cryptedFile = input(">>> ")
			f = open(cryptedFile, 'r')
			cryptedData = f.read()
			f.close()
			print("Enter seedKey(type STRING):")
			seedKey = getpass(">>> ")
			decryptedData = self.GN.decryptMessage(cryptedData, seedKey)
			self.clearTerminal()
			self.banner()
			if decryptedData['success']:
				print("Done!")
				print("Your decrypted message is: ")
				print()
				print(decryptedData['message'])
				print()
				asdasdasd = input("Press [ENTER] to return to main menu!")
				self.mainMenu()
			else:
				print("Something went wrong while sending request to our server")
				print()
				print("Server reply:")
				print(decryptedData)
				print()
				print("If you are doing all right but still face that problem, please, contact us at:")
				print("E-Mail: greyhatfeedback@protonmail.com")
				print("Telegram: @greyhatfdbot")
				print("Press [ENTER] to return to main menu!")
				asdasd = input()
				self.mainMenu()

		elif textOrFile == "2":
			print("Enter seedKey(type STRING):")
			seedKey = getpass(">>> ")
			print("Enter your string to decrypt")
			stringToDecrypt = input(">>> ")
			decryptedData = self.GN.decryptMessage(stringToDecrypt, seedKey)
			self.clearTerminal()
			self.banner()
			if decryptedData['success']:
				print("Done!")
				print("Your decrypted message is: ")
				print()
				print(decryptedData['message'])
				print()
				asdasdasd = input("Press [ENTER] to return to main menu!")
				self.mainMenu()
			else:
				print("Something went wrong while sending request to our server")
				print()
				print("Server reply:")
				print(decryptedData)
				print()
				print("If you are doing all right but still face that problem, please, contact us at:")
				print("E-Mail: greyhatfeedback@protonmail.com")
				print("Telegram: @greyhatfdbot")
				print("Press [ENTER] to return to main menu!")
				asdasd = input()
				self.mainMenu()
		elif textOrFile == "3":
			self.mainMenu()
		else:
			print("Wrong input, returning to main menu!")
			sleep(1)
			self.mainMenu()

	def gipher(self):
		self.clearTerminal()
		self.banner()
		print("1. I want to encrypt the text")
		print("2. I want to decrypt the text")
		print("3. My bad, I want to return back to main menu!")
		gcipherChoise = input(">>> ")
		if gcipherChoise == "1":
			self.clearTerminal()
			self.banner()
			print("Enter seedKey(type STRING):")
			seedKey = getpass(">>> ")
			print("Please, enter your message to encrypt via GCipher")
			clearText = input(">>> ")
			cipherText = self.GN.gipherEncrypt(clearText, seedKey)
			self.clearTerminal()
			self.banner()
			if cipherText['success']:
				print("Done! Your encrypted message is: \n")
				print(cipherText['message'])
				print("")
				print("Do you want to save your encrypted message?(y/n)")
				print("'y' - save your message")
				print("'n' or any button - return to main menu")
				saveOrNot = input(">>> ")
				if saveOrNot == "y":
					now = datetime.now()
					currentTime = now.strftime("%D_%H_%M_%S")
					cryptSavedName = f'GCipheredMessage{currentTime}'
					with open(f'{cryptSavedName}.txt', 'w') as f:
						f.write(f"{cipherText['message']}")
					print("Done!")
					print(f"Message : {cryptSavedName}.txt succesfully saved into GreyNigma folder!")
					print("Press [ENTER] to return to main menu!")
					asdasd = input()
					self.mainMenu()
				else:
					self.mainMenu()
			else:
				print("Something went wrong while sending request to our server")
				print()
				print("Server reply:")
				print(cipherText)
				print()
				print("If you are doing all right but still face that problem, please, contact us at:")
				print("E-Mail: greyhatfeedback@protonmail.com")
				print("Telegram: @greyhatfdbot")
				print("Press [ENTER] to return to main menu!")
				asdasd = input()
				self.mainMenu()



		elif gcipherChoise == "2":
			self.clearTerminal()
			self.banner()
			print("1. I want to decrypt my message from file")
			print("2. I will paste my message manually")
			print("3. I want to return to main menu!")
			degcipherChoice = input(">>> ")
			if degcipherChoice == "1":
				self.clearTerminal()
				self.banner()
				print("Enter seedKey (STRING):")
				seedKey = getpass(">>> ")
				print("Please, enter the path to your message [TYPE 'BACK' TO MAIN MENU]")
				GCipheredMessagePath = input(">>> ")
				if GCipheredMessagePath == "BACK":
					self.mainMenu()
				cf = open(GCipheredMessagePath, 'r')
				GCipheredData = cf.read()
				cf.close()
				deCipherText = self.GN.gipherDecrypt(GCipheredData, seedKey)
				self.clearTerminal()
				self.banner()
				if deCipherText['success']:
					print("Done!")
					print("Your decrypted message is: ")
					print()
					print(deCipherText['message'])
					print()
					asdasdasd = input("Press [ENTER] to return to main menu!")
					self.mainMenu()
				else:
					print("Something went wrong while sending request to our server")
					print()
					print("Server reply:")
					print(deCipherText)
					print()
					print("If you are doing all right but still face that problem, please, contact us at:")
					print("E-Mail: greyhatfeedback@protonmail.com")
					print("Telegram: @greyhatfdbot")
					print("Press [ENTER] to return to main menu!")
					asdasd = input()
					self.mainMenu()

			elif degcipherChoice == "2":
				self.clearTerminal()
				self.banner()
				print("Enter seedKey(type STRING):")
				seedKey = getpass(">>> ")
				self.clearTerminal()
				self.banner()
				print("Please, enter your message to decrypt via GCipher")
				toDeGCipher = input(">>> ")
				deCipherText = self.GN.gipherDecrypt(toDeGCipher, seedKey)
				self.clearTerminal()
				self.banner()
				if deCipherText['success']:
					print("Done!")
					print("Your decrypted message is: ")
					print()
					print(deCipherText['message'])
					print()
					asdasdasd = input("Press [ENTER] to return to main menu!")
					self.mainMenu()
				else:
					print("Something went wrong while sending request to our server")
					print()
					print("Server reply:")
					print(deCipherText)
					print()
					print("If you are doing all right but still face that problem, please, contact us at:")
					print("E-Mail: greyhatfeedback@protonmail.com")
					print("Telegram: @greyhatfdbot")
					print("Press [ENTER] to return to main menu!")
					asdasd = input()
					self.mainMenu()
			elif degcipherChoice == "3":
				self.mainMenu()
			else:
				print("Wrong input, returning to main menu!")
				sleep(1)
				self.mainMenu()
		elif gcipherChoise == "3":
			self.mainMenu()
		else:
			print("Wrong input, returning to main menu!")
			sleep(1)
			self.mainMenu()


	def aboutTab(self):
		self.clearTerminal()
		self.banner()
		print("GreyNigma : Console version by Grey Hat")
		print("Licensed by GNU GPL v3")
		print("Oficial NotABug page : https://notabug.org/Grey_Hat_Cybersecurity/GreyNigma")
		print("Oficial GitHub page : https://github.com/GreyHatCyberSecurity/GreyNigma")
		print("Feedback : ")
		print("Telegram : @greyhatfdbot")
		print("E-Mail : greyhatfeedback@protonmail.com")
		print("")
		asdasdasd = input("Press [ENTER] to return to main menu!")
		self.mainMenu()
#######################################################
#STARTING
#######################################################
if __name__ == '__main__':
	try:
		cli = GreyNigmaCLI()
	except KeyboardInterrupt:
		s.keyboardInterrupt()