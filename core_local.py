'''
This is main local core file.
This file contains all function that need to perform API-requests between your device and GreyNigma API-server.
All the functions are put together and perfectly balanced. 
By following the documentation correctly, you can create encrypted messages in seconds.
We urge you not to touch anything in this file or any other file.
Otherwise, you may damage the normal operation of the program. 
Change only if you know what you are doing.
'''
from random import seed, sample, randint
from os import system, name
import platform, time, re

coreStartLoadTime = time.time()

coreVersion = "1.1"
coreName = f"GN_localCore_Alpha_{coreVersion}"
try:
	import requests
	print("Requests...loaded!")
except ModuleNotFoundError:
	print("Can't detect the requests module!")
	print("Please, install 'requests' with pip")
	print("Just type: `pip install requests`")
	exit()
except ImportError:
	print("Cannot import the requests module!")
	print("Please, make sure you've installed it properly/check your $PYTHONPATH/module name and try again!")
	exit()
except Exception as e:
	print("Ooops, something went wrong!")
	print(f"There is an error message: {e}")
	print("If you are doing all right but still face that problem, please, contact us at:")
	print("E-Mail: greyhatfeedback@protonmail.com")
	print("Telegram: @greyhatfdbot")
	exit()

try:
	from bs4 import BeautifulSoup
	print("bs4...loaded!")
except ModuleNotFoundError:
	print("Can't detect the BeautifulSoup module!")
	print("Please, install 'bs4' with pip")
	print("Just type: `pip install bs4`")
	exit()
except ImportError:
	print("Cannot import the BeautifulSoup module!")
	print("Please, make sure you've installed it properly/check your $PYTHONPATH/module name and try again!")
	exit()
except Exception as e:
	print("Ooops, something went wrong!")
	print(f"There is an error message: {e}")
	print("If you are doing all right but still face that problem, please, contact us at:")
	print("E-Mail: greyhatfeedback@protonmail.com")
	print("Telegram: @greyhatfdbot")
	exit()

class Security():
	'''
	This is main security module
	Security module provides some security functions that improving total GreyNigma security
	Such as generating random word to string(if some string is empty)
	Re-writing clipboard to avoid buffer leaks
	'''
	def __init__(self):
		self.secureSeed = None

	def generateRandomWord(self):
		'''
		Generating random word
		'''
		seed(self.secureSeed)
		k = randint(5, 35)
		alphabetToGenerate = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^*()_+=-/.,]["
		_l = "".join(sample(alphabetToGenerate, k))
		return str(_l)

	def keyboardInterrupt(self):
		'''
		Method will try to override the clipboard content with useless text and clear screen.
		If your system haven't 'clipboard' module - just clearing screen.
		'''
		system('cls' if name == 'nt' else 'clear')
		try:
			from clipboard import copy
			seed(self.secureSeed)
			v = randint(10, 20)
			n = randint(20, 30)
			for _ in range(randint(v, n)):
				copy(self.generateRandomWord())
		except Exception:
			pass
		print('Bye!')
s = Security() #Initializing security module. 

class GreyNigmaAPI():
	def __init__(self, token=None):
		self.url2check = 'http://google.com'
		if self.isConnected2Internet():
			self.greyNigmaURL = self.getURL()
			self.token = token
		else:
			print("Can't connect to internet!")
			print("Please, check your internet connection and try again!")
			exit()

	def isConnected2Internet(self):
		try:
			CIRequest = requests.get(self.url2check, timeout=2)
			return True
		except (requests.ConnectionError, requests.Timeout) as exception:
			try:
				CIRequest = requests.get(self.url2check, timeout=5)
				return True
			except (requests.ConnectionError, requests.Timeout) as exception:
				return False
			except Exception as e:
				return False
		except Exception as e:
			return False

	def encryptSingleMessage(self, message, seedKey):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/encryptMessage', json={'message': message, 'seedKey': seedKey}, headers=headers).json()
		return r

	def encryptNormalMessage(self, firstFake, original, secondFake, seedKey):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/createMessage', json={'firstFake': firstFake, 'original': original, 'secondFake': secondFake, 'seedKey': seedKey}, headers=headers).json()
		return r

	def decryptMessage(self, message, seedKey):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/decryptMessage', json={'message': message, 'seedKey': seedKey}, headers=headers).json()
		return r

	def gipherEncrypt(self, message, seedKey):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/gipherEncrypt', json={'message': message, 'seedKey': seedKey}, headers=headers).json()
		return r

	def gipherDecrypt(self, message, seedKey):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/gipherDecrypt', json={'message': message, 'seedKey': seedKey}, headers=headers).json()
		return r
	def createSecureSeed(self):
		headers = {"authorization": f"GN_TOKEN {self.token}"}
		r = requests.post(f'{self.greyNigmaURL}/createSecureSeed').json()
		return r

	def getURL(self):
		print("Trying to get GN link...")
		try:
			r = requests.get('https://notabug.org/Grey_Hat_Cybersecurity/GreyNigma').text
			soup = BeautifulSoup(r, 'lxml')
			links = []
			for link in soup.findAll('a', text=re.compile('greynigma')):
				links.append(link.get('href'))
			return links[0][:len(links[0])-1:1]
		except Exception as e:
			print("Can't get GreyNigma API url...")
			print(e)
			print("Please, report that error to us at:")
			print("E-Mail: greyhatfeedback@protonmail.com")
			print("Telegram: @greyhatfdbot")
			exit()

coreStopLoadTime = time.time()
coreLoadTime = float(coreStopLoadTime - coreStartLoadTime)


if __name__ == '__main__':
	print(f"Hello from {coreName}")
	print(f"Loaded in {coreLoadTime:.3f}s")
	print("Now it's time to encrypt something!")
	exit()