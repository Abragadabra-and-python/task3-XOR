def XOR_cipher(str, key):
	encrypted_str = ''

	for text in str:
		encrypted_str += chr(ord(text) ^ key)
	return encrypted_str


def XOR_uncipher(encrypted_str, key):
	decrypted_str = ''

	for text in encrypted_str:
		decrypted_str += chr(ord(text) ^ key)
	return decrypted_str

print('Encrypt 1, Decrypt 2')
choise = str(input('>>>'))

match choise:
	case '1':
		print('Please, enter string for encrypt')
		string = str(input('>>>'))

		print('Please, enter key for encrypt (natural number only!)')
		key = int(input('>>>'))

		print(XOR_cipher(string, key))
	case '2':
		print('Please, enter string for decrypt')
		string = str(input('>>>'))

		print('Please, enter key for decrypt (natural number only!)')
		key = int(input('>>>'))

		print(XOR_uncipher(string, key))
	case _:
		print('You\'re fucking stupid :D')
