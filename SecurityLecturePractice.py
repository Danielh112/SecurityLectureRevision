# Crude Stream Cipher
def streamCipher():
	m = "Hello Dan"
	k = int('01100001111', 2)	# Both use K 
	c = [] 
	decryptedM = ''

	print("Plain Text: ", m)

	#Encrypt each bit/byte using the key and the plaintext
	for char in m:
		mBinary = int(' '.join(format(ord(x), 'b') for x in char), 2)
		c.append(mBinary ^ k)

	print("Stream Cipher: ", c) # Stream ciphertext (would be transmitted a bit at a time not all together

	for bit in c:
		decryptedM += str(chr(bit ^ k))
	print("Decrypted plain text: ", decryptedM);

#----------------------------------------------------------------------------------------------------------
# Linear feedback Shift Register (Simplified design needs multiple stream ciphers to make this feasible e.g. xor the two)
def lFSR():
	m = "Hello Dan"
	k = int('01100001111', 2) # Choose k size
	k1 = int('01100001111', 2) # Choose k size
	c = [] 
	decryptedM = ''

	print("Plain Text: ", m)

	#Encrypt each bit/byte using the key and the plaintext
	for char in m:
		mBinary = int(' '.join(format(ord(x), 'b') for x in char), 2)
		c.append(mBinary ^ k)
		
		listK = list(bin(k))
		listK[3] = str(int(listK[len(listK)-1], 2) ^ int(listK[5], 2) ^ int(listK[3], 2))
		k = int("".join(listK), 2)

	print("Stream Cipher: ", c) # Stream ciphertext (would be transmitted a bit at a time not all together

	for bit in c:
		decryptedM += str(chr(bit ^ k1))
		listK = list(bin(k1))
		listK[3] = str(int(listK[len(listK)-1], 2) ^ int(listK[5], 2) ^ int(listK[3], 2))
		k1 = int("".join(listK), 2)

	print("Decrypted plain text: ", decryptedM);

lFSR()
	
#----------------------------------------------------------------------------------------------------------