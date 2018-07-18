import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
import sys
from colorama import Fore, init
init()

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = "e_"+filename
	#outputFile = filename
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
	#outputFile = filename
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

def main():
	choice = sys.argv[1]
	fname = sys.argv[2]
	password = sys.argv[3]
	passwd = SHA256.new(password).digest()
	if choice.lower() == 'e':
		encrypt(passwd, fname)
		os.remove(fname)
	elif choice.lower() == 'd':
		decrypt(passwd, fname)
		os.remove(fname)
	else:
		sys.exit()

if __name__ == '__main__':
	main()