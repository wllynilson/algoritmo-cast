from Crypto.Cipher import CAST

key = b'chave'
cipher = CAST.new(key, CAST.MODE_OPENPGP)
plaintext = b'wllynilson carneiro'
msg = cipher.encrypt(plaintext)
print(msg)

print('-----------------------------------')

eiv = msg[:CAST.block_size + 2]
ciphertext = msg[CAST.block_size + 2:]
cipher = CAST.new(key, CAST.MODE_OPENPGP, eiv)

print (cipher.decrypt(ciphertext))
