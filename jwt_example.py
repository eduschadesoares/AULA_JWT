import jwt
import datetime

# Chave secreta para assinatura do JWT (normalmente, seria mantida segura e fora do código)
SECRET_KEY = "sua_chave_secreta"

# Banco de dados simples para armazenar usuários registrados
usuarios = {}

# Função para registrar um novo usuário
def registrar_usuario(username, senha):
    if username in usuarios:
        print(f"Usuário '{username}' já existe!")
    else:
        usuarios[username] = senha
        print(f"Usuário '{username}' registrado com sucesso!")

# Função para gerar um JWT para o usuário ao fazer login
def login(username, senha):
    # Verifica se o usuário existe e a senha está correta
    if usuarios.get(username) == senha:
        # Gera um token JWT com uma expiração de 5 minutos
        payload = {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "role": "admin",
            "permissions": ["read", "write"],
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS512")
        print(f"Login bem-sucedido! Aqui está seu token JWT: {token}")
        return token
    else:
        print("Nome de usuário ou senha incorretos!")
        return None

# Função para acessar um recurso protegido usando o JWT
def acessar_recurso_protegido(token):
    try:
        # Decodifica o token para verificar a autenticidade
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
        username = payload["username"]
        print(f"Acesso autorizado! Bem-vindo, {username}!")
    except jwt.ExpiredSignatureError:
        print("Token expirado! Por favor, faça login novamente.")
    except jwt.InvalidTokenError:
        print("Token inválido! Acesso negado.")

# Demonstração do fluxo completo
print("### Registro ###")
registrar_usuario("alice", "senha123")
registrar_usuario("bob", "senha456")

print("\n### Login ###")
# Login bem-sucedido
token = login("alice", "senha123")
#token = login("bob", "senha456")

# Acesso ao recurso protegido
if token:
    print("\n### Acessando Recurso Protegido ###")
    acessar_recurso_protegido(token)

# Simulação de token expirado (caso queira testar manualmente, modifique a duração ou espere alguns minutos)
print("\n### Acesso com Token Expirado ###")
acessar_recurso_protegido(token)
