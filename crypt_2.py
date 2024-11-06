from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Função para gerar uma chave AES de 256 bits
def gerar_chave():
    return os.urandom(32)  # 32 bytes para AES-256

# Função para criptografar a mensagem usando AES
def criptografar(mensagem, chave):
    # Inicializando o modo de operação AES
    iv = os.urandom(16)  # Vetor de inicialização para o modo CBC
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Adicionando padding para que a mensagem tenha um tamanho múltiplo de 16
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(mensagem.encode()) + padder.finalize()
    
    # Criptografando a mensagem
    mensagem_criptografada = encryptor.update(padded_data) + encryptor.finalize()
    return iv + mensagem_criptografada  # Retornar o IV junto com a mensagem criptografada

# Função para descriptografar a mensagem
def descriptografar(mensagem_criptografada, chave):
    # Separar o IV e a mensagem criptografada
    iv = mensagem_criptografada[:16]
    mensagem_criptografada = mensagem_criptografada[16:]
    
    # Inicializando o modo de operação AES
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Descriptografando a mensagem
    padded_data = decryptor.update(mensagem_criptografada) + decryptor.finalize()
    
    # Removendo o padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    mensagem_descriptografada = unpadder.update(padded_data) + unpadder.finalize()
    return mensagem_descriptografada.decode()

# Exemplo de uso
if __name__ == "__main__":
    chave = gerar_chave()  # Gerar uma nova chave

    mensagem = input("Digite a mensagem para criptografar: ")
    mensagem_criptografada = criptografar(mensagem, chave)
    print(f"Mensagem criptografada: {mensagem_criptografada}")

    # Descriptografando a mensagem
    mensagem_descriptografada = descriptografar(mensagem_criptografada, chave)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")
