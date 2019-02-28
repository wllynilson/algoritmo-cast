from Crypto.Cipher import CAST

chave = b'Goku'
cipher = CAST.new(key, CAST.MODE_OPENPGP)
texto = b'Uma chance num milhão é melhor que nenhuma chance!'
msg = cipher.encrypt(texto)

...
tam = msg[:CAST.block_size+2]
ciphertext = msg[CAST.block_size+2:]
cipher = CAST.new(chave, CAST.MODE_OPENPGP, tam)
print cipher.decrypt(ciphertext)
