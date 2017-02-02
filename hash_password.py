import random
import hashlib
def hash_password(password):
	'use salt to encrypt'
	salt = str(random.randint(0, 10))
	return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' +salt

if __name__ == '__main__':
	password = input('Your password:')
	print('Encrypted:' + hash_password(password))