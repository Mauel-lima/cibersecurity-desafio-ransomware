#Importações Necessárias
import os
import pyaes

#Abrir arquivo
file_name = input("Escreva o nome do arquivo para descriptografar: ")
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#Definir chave para descriptografia
key = input("Cole sua chave de descriptografia: ")
key = key.encode('utf-8')
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#Excluir arquivo original
os.remove(file_name)

#Salvar arquivo
new_file = file_name
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
print("Arquivo descriptografado.")
