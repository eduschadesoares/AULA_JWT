from cryptography.fernet import Fernet

# Gerar uma chave para o Fernet e salvá-la em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada e salva em 'chave.key'.")

# Carregar a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar a mensagem
def criptografar(mensagem):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

# Função para descriptografar a mensagem
def descriptografar(mensagem_criptografada):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada

# Exemplo de uso
if __name__ == "__main__":
    # Gerar uma nova chave (faça isso apenas uma vez)
    #gerar_chave()  # Descomente esta linha se a chave ainda não tiver sido gerada

    mensagem = input("Digite a mensagem para criptografar: ")
    mensagem_criptografada = criptografar(mensagem)
    print(f"Mensagem criptografada: {mensagem_criptografada}")

    # Descriptografando a mensagem
    mensagem_descriptografada = descriptografar(mensagem_criptografada)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")
