#Importações Necessárias
import os
import pyaes
import random

randomkey = ""

#Abrir arquivo
file_name = input("Escreva o nome do arquivo para criptografar: ")
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#Excluir arquivo original
os.remove(file_name)


#Definir chave de Encriptação
#Gerar chave de aleatória
for i in range (16):
    c1 = chr(random.randint(ord('a'), ord('z')))
    c2 = chr(random.randint(ord('A'), ord('Z')))
    c3 = random.randint(0,9)
    c4 = chr(random.randint(ord('a'), ord('z')))
    cfinal = random.choice([c1, c2, c3, c4])
    randomkey += str(cfinal)
key = randomkey.encode('utf-8')
aes = pyaes.AESModeOfOperationCTR(key)

#Criptografando o arquivo
crypto_data = aes.encrypt(file_data)

#Salvar arquivo
new_file = file_name
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
print(f'Sua chave de criptografia é: {randomkey}')
print("Copie ela e não perca, \npois sem ela não será possível decriptografar o arquivo")
print("Arquivo criptografado")
