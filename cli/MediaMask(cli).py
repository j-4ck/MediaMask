## CLI VERSION ##
import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
import sys
import random
from colorama import Fore, init
init()

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = "e_"+filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''

	for i in range(16):
		IV += chr(random.randint(0, 0xFF))

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
	chunksize = 64*1024
	outputFile = filename[2:]
	
	with open(filename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def Main():
	if len(sys.argv) < 4:
		print 'Invalid arguments!\nNeeded 3 arguments, and recieved ' + str(len(sys.argv)-1) + '!'
		print '\nHelp:\n\tArgument 1:\n\t\t"e" or "d" for encryption or decryption\n\tArgument 2:\n\t\tDesired file(name)\n\tArgument 3:\n\t\tChosen password\n'
		sys.exit()
	os.system('cls')
	b1 = '''

                                                                                            
                               ,,    ,,                                                     
`7MMM.     ,MMF'             `7MM    db           `7MMM.     ,MMF'                `7MM      
  MMMb    dPMM                 MM                   MMMb    dPMM                    MM      
  M YM   ,M MM  .gP"Ya    ,M""bMM  `7MM   ,6"Yb.    M YM   ,M MM   ,6"Yb.  ,pP"Ybd  MM  ,MP'
  M  Mb  M' MM ,M'   Yb ,AP    MM    MM  8)   MM    M  Mb  M' MM  8)   MM  8I   `"  MM ;Y   
  M  YM.P'  MM 8M"""""" 8MI    MM    MM   ,pm9MM    M  YM.P'  MM   ,pm9MM  `YMMMa.  MM;Mm   
  M  `YM'   MM YM.    , `Mb    MM    MM  8M   MM    M  `YM'   MM  8M   MM  L.   I8  MM `Mb. 
.JML. `'  .JMML.`Mbmmd'  `Wbmd"MML..JMML.`Moo9^Yo..JML. `'  .JMML.`Moo9^Yo.M9mmmP'.JMML. YA.
                                                                                            

	'''
	b2 = '''
  __  __          _ _       __  __           _    
 |  \/  |        | (_)     |  \/  |         | |   
 | \  / | ___  __| |_  __ _| \  / | __ _ ___| | __
 | |\/| |/ _ \/ _` | |/ _` | |\/| |/ _` / __| |/ /
 | |  | |  __/ (_| | | (_| | |  | | (_| \__ \   < 
 |_|  |_|\___|\__,_|_|\__,_|_|  |_|\__,_|___/_|\_\
                                                  
	'''
	b3 = '''


888b     d888               888 d8b          888b     d888                   888      
8888b   d8888               888 Y8P          8888b   d8888                   888      
88888b.d88888               888              88888b.d88888                   888      
888Y88888P888  .d88b.   .d88888 888  8888b.  888Y88888P888  8888b.  .d8888b  888  888 
888 Y888P 888 d8P  Y8b d88" 888 888     "88b 888 Y888P 888     "88b 88K      888 .88P 
888  Y8P  888 88888888 888  888 888 .d888888 888  Y8P  888 .d888888 "Y8888b. 888888K  
888   "   888 Y8b.     Y88b 888 888 888  888 888   "   888 888  888      X88 888 "88b 
888       888  "Y8888   "Y88888 888 "Y888888 888       888 "Y888888  88888P' 888  888 

	'''
	banners = [b1, b2,b3]
	banner = random.choice(banners)
	print banner
	time.sleep(0.5)
	choice = sys.argv[1]
	fname = sys.argv[2]
	password = sys.argv[3]
	passwd = SHA256.new(password).digest()
	if choice.lower() == 'e':
		encrypt(passwd, fname)
		print Fore.GREEN + "[+]" + Fore.WHITE + " Finished encrypting " + fname + "!"
		os.remove(fname)
		print Fore.GREEN + "[+]" + Fore.WHITE + " Removed original file!"
	elif choice.lower() == 'd':
		decrypt(passwd, fname)
		print Fore.GREEN + "[+]" + Fore.WHITE + " Finished decrypting " + fname + '!'
		os.remove(fname)
		print Fore.GREEN + "[+]" + Fore.WHITE + " Removed original file!"
	else:
		sys.exit()

if __name__ == '__main__':
	Main()